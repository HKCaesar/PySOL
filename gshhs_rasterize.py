# coding: utf-8

import os, sys

from osgeo import gdal, ogr, osr
from numpy import asarray, floor

from pyproj import Proj

def msg(s): print (s)
def dashes(): msg(40*'-')
def msgt(s): dashes(); msg(s); dashes()
def msgx(s): dashes(); msg('ERROR'); msg(s); dashes(); sys.exit(0)

# Creates a land mask by projecting land polygons in lat/lon coordinates from
# an ESRI shapefile to coordinates of the unprojected image and rasterizing the polygons.
def gshhs_rasterize(lonlim=(1,31), latlim=(55,65), \
                    area_def=None, lakes = False, \
                    shapefile = '/media/SOLabNFS/store/auxdata/coastline/GSHHS_shp/f/GSHHS_f_L1.shp'):

    proj      = area_def.proj_
    proj_name =  area_def.proj_name
    raster_shape = area_def.shape

    # Get area extent
    # p = Proj(proj)

    # up    = max(latlim)
    # down  = min(latlim)
    # left  = min(lonlim)
    # right = max(lonlim)
    # # минимум из всех координат X, Y, максимум из всех координат X, Y
    # # Такой результат даёт правильный area_extent для 3413
    # # При этом для 4326 area_extent остаётся неизменным
    # # area_def_3413 = swath_area_def(name='Temporal SWATH EPSG Projection 3413', proj='stere', \
    # #                                lonlim=(-180,180), latlim=(30,90), ellps="WGS84", res=1500, \
    # #                                lat_ts=70, lat_0=90, lon_0=-45)
    # # Area extent: (-5050747.263141337, 0.0, 0.0, 5050747.263141336)
    # area_extent = (
    #                 min(left_ex1, left_ex2, right_ex1, right_ex2),
    #                 min(up_ex1, up_ex2, down_ex1, down_ex2),
    #                 max(left_ex1, left_ex2, right_ex1, right_ex2),
    #                 max(up_ex1, up_ex2, down_ex1, down_ex2)
    #             )

    minlon, minlat, maxlon, maxlat = area_def.area_extent_ll
    lonlim = (minlon, maxlon)
    latlim = (minlat, maxlat)
    # else:
    #     minlon,minlat,maxlon,maxlat=[min(lonlim),min(latlim),max(lonlim),max(latlim)]


    # if projection is not 4326 use manual config
    if proj!='4326':
        # if projection file alredy exists - skip
        outputShapefile = get_output_fname(shapefile, proj_name)
        if not os.path.isfile(outputShapefile):
            msgt('Projection %s file not found. Reprojecting ' % proj_name)
            reproject(shapefile, proj, proj_name)
        if lakes:
            # if projection file alredy exists - skip
            shapefile_lakes = shapefile[:-5] + "2.shp"
            outputShapefile = get_output_fname(shapefile_lakes, proj_name)
            if not os.path.isfile(outputShapefile):
                msgt('Lakes Projection %s file not found. Reprojecting ' % proj_name)
                reproject(shapefile_lakes, proj, proj_name)


    # Get the shape of the rasterized field
    nrows,ncols=raster_shape
    maskvalue = 1

    # set the geotransform
    xres=(maxlon-minlon)/float(ncols)
    yres=(maxlat-minlat)/float(nrows)
    geotransform=(minlon,xres,0,maxlat,0, -yres)

    # Open the shape file and read the layers
    if proj!='4326':
        shpfn = get_output_fname(shapefile, proj_name)
    else:
        shpfn = shapefile
    src_ds = ogr.Open(shpfn)
    src_lyr=src_ds.GetLayer()

    dst_ds = gdal.GetDriverByName('MEM').Create('', ncols, nrows, 1 ,gdal.GDT_Byte)
    dst_rb = dst_ds.GetRasterBand(1)
    dst_rb.Fill(0) #initialise raster with zeros
    dst_rb.SetNoDataValue(0)
    dst_ds.SetGeoTransform(geotransform)

    err = gdal.RasterizeLayer(dst_ds, [maskvalue], src_lyr)
    dst_ds.FlushCache()
    
    mask_arr=dst_ds.GetRasterBand(1).ReadAsArray()

    # if lakes are also specified for masking
    if lakes:
        # Open the shape file and read the layers
        if proj!='4326':
            shapefile_lakes = get_output_fname(shapefile[:-5] + "2.shp", proj_name)
        else:
            shapefile_lakes =  shapefile[:-5] + "2.shp"
        src_ds = ogr.Open(shapefile_lakes)
        src_lyr=src_ds.GetLayer()

        dst_ds = gdal.GetDriverByName('MEM').Create('', ncols, nrows, 1 ,gdal.GDT_Byte)
        dst_rb = dst_ds.GetRasterBand(1)
        dst_rb.Fill(0) #initialise raster with zeros
        dst_rb.SetNoDataValue(0)
        dst_ds.SetGeoTransform(geotransform)

        err = gdal.RasterizeLayer(dst_ds, [maskvalue], src_lyr)
        dst_ds.FlushCache()

        mask_arr_lakes=dst_ds.GetRasterBand(1).ReadAsArray()

    return (mask_arr & ~mask_arr_lakes)

def get_output_fname(fname, new_suffix):
    fparts = fname.split('.')
    if len(fparts[-1]) == 3:
        return '.'.join(fparts[:-1]) + '_' + new_suffix + '.' + fparts[-1]

    return fname + '_' + new_suffix

def reproject(shape_fname, proj='+units=m +ellps=WGS84 +lon_0=-45 +proj=stere +lat_ts=70 +lat_0=90', proj_name='3413'):
    """Re-project the shapefile. From the Python GDAL/OGR Cookbook

    Source: http://pcjericks.github.io/py-gdalogr-co...

    :param shape_fname: full file path to a shapefile (.shp)
    :returns: full file path to a reprojected shapefile
    """
    if not os.path.isfile(shape_fname):
        msgx('File not found: %s' % shape_fname)

    driver = ogr.GetDriverByName('ESRI Shapefile')
    inDataSet = driver.Open(shape_fname)

    # input SpatialReference
    inLayer = inDataSet.GetLayer()
    inSpatialRef = inLayer.GetSpatialRef()

    # output SpatialReference
    outSpatialRef = osr.SpatialReference()
    outSpatialRef.ImportFromProj4(proj)
    outSpatialRef.SetProjCS(proj_name)

    # create the CoordinateTransformation
    coordTrans = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)

    # create the output layer
    outputShapefile = get_output_fname(shape_fname, proj_name)
    #msg('output file: %s' % outputShapefile)

    if os.path.exists(outputShapefile):
        driver.DeleteDataSource(outputShapefile)
    outDataSet = driver.CreateDataSource(outputShapefile)
    outLayer = outDataSet.CreateLayer("basemap_"+proj_name, geom_type=ogr.wkbMultiPolygon)

    # add fields
    inLayerDefn = inLayer.GetLayerDefn()
    for i in range(0, inLayerDefn.GetFieldCount()):
        fieldDefn = inLayerDefn.GetFieldDefn(i)
        outLayer.CreateField(fieldDefn)

    # get the output layer's feature definition
    outLayerDefn = outLayer.GetLayerDefn()

    # loop through the input features
    inFeature = inLayer.GetNextFeature()
    while inFeature:
        # get the input geometry
        geom = inFeature.GetGeometryRef()
        # reproject the geometry
        geom.Transform(coordTrans)
        # create a new feature
        outFeature = ogr.Feature(outLayerDefn)
        # set the geometry and attribute
        outFeature.SetGeometry(geom)
        for i in range(0, outLayerDefn.GetFieldCount()):
            outFeature.SetField(outLayerDefn.GetFieldDefn(i).GetNameRef(), inFeature.GetField(i))
        # add the feature to the shapefile
        outLayer.CreateFeature(outFeature)
        # destroy the features and get the next input feature
        outFeature.Destroy()
        inFeature.Destroy()
        inFeature = inLayer.GetNextFeature()

    # close the shapefiles
    inDataSet.Destroy()
    outDataSet.Destroy()


#~ from memory_profiler import profile
#~ @profile
def gshhs_rasterize_4326(lonlim=(1,31), latlim=(55,65), \
                    pxRes=(0.1,0.1), arrShape=None, lakes = True, \
                    shapefile = '/media/SOLabNFS/store/auxdata/coastline/GSHHS_shp/f/GSHHS_f_L1.shp'):

    # Get area extent
    minlon,minlat,maxlon,maxlat=[min(lonlim),min(latlim),max(lonlim),max(latlim)]

    maskvalue = 1

    # Get the shape of the rasterized field
    xres = float(pxRes[0])
    yres = float(pxRes[1])
    if arrShape is None:
        ncols = int( floor( (maxlon-minlon)/xres ) )
        nrows = int( floor( (maxlat-minlat)/yres ) )
    else:
        ncols = arrShape[1]
        nrows = arrShape[0]

    # set the geotransform
    geotransform=(minlon,xres,0,maxlat,0, -yres)

    # Open the shape file and read the layers
    src_ds = ogr.Open(shapefile)
    src_lyr=src_ds.GetLayer()

    dst_ds = gdal.GetDriverByName('MEM').Create('', ncols, nrows, 1 ,gdal.GDT_Byte)
    dst_rb = dst_ds.GetRasterBand(1)
    dst_rb.Fill(0) #initialise raster with zeros
    dst_rb.SetNoDataValue(0)
    dst_ds.SetGeoTransform(geotransform)

    err = gdal.RasterizeLayer(dst_ds, [maskvalue], src_lyr)
    dst_ds.FlushCache()
    
    mask_arr=dst_ds.GetRasterBand(1).ReadAsArray()

    # if lakes are also specified for masking
    if lakes:
        # Open the shape file and read the layers
        shapefile_lakes =  shapefile[:-5] + "2.shp"
        src_ds = ogr.Open(shapefile_lakes)
        src_lyr=src_ds.GetLayer()

        dst_ds = gdal.GetDriverByName('MEM').Create('', ncols, nrows, 1 ,gdal.GDT_Byte)
        dst_rb = dst_ds.GetRasterBand(1)
        dst_rb.Fill(0) #initialise raster with zeros
        dst_rb.SetNoDataValue(0)
        dst_ds.SetGeoTransform(geotransform)

        err = gdal.RasterizeLayer(dst_ds, [maskvalue], src_lyr)
        dst_ds.FlushCache()

        mask_arr_lakes=dst_ds.GetRasterBand(1).ReadAsArray()

    return (mask_arr & ~mask_arr_lakes)

    msg('output file: %s' % outputShapefile)
    return outputShapefile
