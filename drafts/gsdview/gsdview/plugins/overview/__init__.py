# -*- coding: utf-8 -*-

### Copyright (C) 2008-2011 Antonio Valentino <a_valentino@users.sf.net>

### This file is part of GSDView.

### GSDView is free software; you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation; either version 2 of the License, or
### (at your option) any later version.

### GSDView is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.

### You should have received a copy of the GNU General Public License
### along with GSDView; if not, write to the Free Software
### Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA.


'''Overview pannel for GDAL raster bands.'''


from .info import *
from .info import __version__, __requires__


__author__ = 'Antonio Valentino <a_valentino@users.sf.net>'
__date__ = '$Date: 2011-08-01 19:26:21 +0200 (lun, 01 ago 2011) $'
__revision__ = '$Revision: 997 $'

__all__ = ['init', 'close', 'loadSettings', 'saveSettings',
           'name', 'version', 'short_description', 'description',
           'author', 'author_email', 'copyright', 'license_type',
           'website', 'website_label',
]

_instance = None


def init(app):
    from .core import OverviewController

    global _instance
    _instance = OverviewController(app)


def close(app):
    saveSettings(app.settings)

    global _instance
    _instance = None


def loadSettings(settings):
    pass


def saveSettings(settings):
    pass