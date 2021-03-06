# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gsdview/ui/pluginmanager.ui'
#
# Created: Sun Nov 13 21:17:57 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_pluginManagerForm(object):
    def setupUi(self, pluginManagerForm):
        pluginManagerForm.setObjectName(_fromUtf8("pluginManagerForm"))
        pluginManagerForm.resize(627, 419)
        pluginManagerForm.setWindowTitle(QtGui.QApplication.translate("pluginManagerForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_2 = QtGui.QVBoxLayout(pluginManagerForm)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pathGroupBox = QtGui.QGroupBox(pluginManagerForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pathGroupBox.sizePolicy().hasHeightForWidth())
        self.pathGroupBox.setSizePolicy(sizePolicy)
        self.pathGroupBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.pathGroupBox.setTitle(QtGui.QApplication.translate("pluginManagerForm", "Plugins Search Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.pathGroupBox.setObjectName(_fromUtf8("pathGroupBox"))
        self.pathGroupHorizontalLayout = QtGui.QHBoxLayout(self.pathGroupBox)
        self.pathGroupHorizontalLayout.setObjectName(_fromUtf8("pathGroupHorizontalLayout"))
        self.pathListWidget = QtGui.QListWidget(self.pathGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathListWidget.sizePolicy().hasHeightForWidth())
        self.pathListWidget.setSizePolicy(sizePolicy)
        self.pathListWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.pathListWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.pathListWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.pathListWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.pathListWidget.setObjectName(_fromUtf8("pathListWidget"))
        self.pathGroupHorizontalLayout.addWidget(self.pathListWidget)
        self.buttonsVerticalLayout = QtGui.QVBoxLayout()
        self.buttonsVerticalLayout.setSpacing(0)
        self.buttonsVerticalLayout.setObjectName(_fromUtf8("buttonsVerticalLayout"))
        self.addButton = QtGui.QPushButton(self.pathGroupBox)
        self.addButton.setToolTip(QtGui.QApplication.translate("pluginManagerForm", "Add a new item.", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("pluginManagerForm", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setShortcut(QtGui.QApplication.translate("pluginManagerForm", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.buttonsVerticalLayout.addWidget(self.addButton)
        self.removeButton = QtGui.QPushButton(self.pathGroupBox)
        self.removeButton.setEnabled(False)
        self.removeButton.setToolTip(QtGui.QApplication.translate("pluginManagerForm", "Remove selected items.", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(QtGui.QApplication.translate("pluginManagerForm", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setShortcut(QtGui.QApplication.translate("pluginManagerForm", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.buttonsVerticalLayout.addWidget(self.removeButton)
        self.editButton = QtGui.QPushButton(self.pathGroupBox)
        self.editButton.setEnabled(False)
        self.editButton.setToolTip(QtGui.QApplication.translate("pluginManagerForm", "Edit selected item.", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("pluginManagerForm", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.buttonsVerticalLayout.addWidget(self.editButton)
        self.upButton = QtGui.QPushButton(self.pathGroupBox)
        self.upButton.setEnabled(False)
        self.upButton.setToolTip(QtGui.QApplication.translate("pluginManagerForm", "Move selected items one position up.", None, QtGui.QApplication.UnicodeUTF8))
        self.upButton.setText(QtGui.QApplication.translate("pluginManagerForm", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.buttonsVerticalLayout.addWidget(self.upButton)
        self.downButton = QtGui.QPushButton(self.pathGroupBox)
        self.downButton.setEnabled(False)
        self.downButton.setToolTip(QtGui.QApplication.translate("pluginManagerForm", "Move selected items one position down.", None, QtGui.QApplication.UnicodeUTF8))
        self.downButton.setText(QtGui.QApplication.translate("pluginManagerForm", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.buttonsVerticalLayout.addWidget(self.downButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.buttonsVerticalLayout.addItem(spacerItem)
        self.pathGroupHorizontalLayout.addLayout(self.buttonsVerticalLayout)
        self.verticalLayout_2.addWidget(self.pathGroupBox)
        self.pluginsTableWidget = QtGui.QTableWidget(pluginManagerForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.pluginsTableWidget.sizePolicy().hasHeightForWidth())
        self.pluginsTableWidget.setSizePolicy(sizePolicy)
        self.pluginsTableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.pluginsTableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.pluginsTableWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.pluginsTableWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.pluginsTableWidget.setObjectName(_fromUtf8("pluginsTableWidget"))
        self.pluginsTableWidget.setColumnCount(5)
        self.pluginsTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("pluginManagerForm", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("pluginManagerForm", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("pluginManagerForm", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("pluginManagerForm", "Active", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginsTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("pluginManagerForm", "Load on startup", None, QtGui.QApplication.UnicodeUTF8))
        item.setToolTip(QtGui.QApplication.translate("pluginManagerForm", "Load this plagin at application startup time.", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginsTableWidget.setHorizontalHeaderItem(4, item)
        self.pluginsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.pluginsTableWidget.verticalHeader().setVisible(True)
        self.verticalLayout_2.addWidget(self.pluginsTableWidget)

        self.retranslateUi(pluginManagerForm)
        QtCore.QMetaObject.connectSlotsByName(pluginManagerForm)

    def retranslateUi(self, pluginManagerForm):
        item = self.pluginsTableWidget.horizontalHeaderItem(0)
        item = self.pluginsTableWidget.horizontalHeaderItem(1)
        item = self.pluginsTableWidget.horizontalHeaderItem(2)
        item = self.pluginsTableWidget.horizontalHeaderItem(3)
        item = self.pluginsTableWidget.horizontalHeaderItem(4)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    pluginManagerForm = QtGui.QWidget()
    ui = Ui_pluginManagerForm()
    ui.setupUi(pluginManagerForm)
    pluginManagerForm.show()
    sys.exit(app.exec_())

