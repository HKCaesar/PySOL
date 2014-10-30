# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gsdview/ui/plugininfo.ui'
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

class Ui_pluginInfoForm(object):
    def setupUi(self, pluginInfoForm):
        pluginInfoForm.setObjectName(_fromUtf8("pluginInfoForm"))
        pluginInfoForm.resize(642, 407)
        pluginInfoForm.setWindowTitle(QtGui.QApplication.translate("pluginInfoForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(pluginInfoForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.nameValue = QtGui.QLabel(pluginInfoForm)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.nameValue.setFont(font)
        self.nameValue.setText(QtGui.QApplication.translate("pluginInfoForm", "Plugin Name", None, QtGui.QApplication.UnicodeUTF8))
        self.nameValue.setAlignment(QtCore.Qt.AlignCenter)
        self.nameValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.nameValue.setObjectName(_fromUtf8("nameValue"))
        self.verticalLayout.addWidget(self.nameValue)
        self.descriptionValue = QtGui.QLabel(pluginInfoForm)
        self.descriptionValue.setMinimumSize(QtCore.QSize(0, 80))
        self.descriptionValue.setText(QtGui.QApplication.translate("pluginInfoForm", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionValue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descriptionValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.descriptionValue.setObjectName(_fromUtf8("descriptionValue"))
        self.verticalLayout.addWidget(self.descriptionValue)
        self.infoGroupBox = QtGui.QGroupBox(pluginInfoForm)
        self.infoGroupBox.setTitle(QtGui.QApplication.translate("pluginInfoForm", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.infoGroupBox.setObjectName(_fromUtf8("infoGroupBox"))
        self.infoFormLayout = QtGui.QFormLayout(self.infoGroupBox)
        self.infoFormLayout.setObjectName(_fromUtf8("infoFormLayout"))
        self.authorLabel = QtGui.QLabel(self.infoGroupBox)
        self.authorLabel.setText(QtGui.QApplication.translate("pluginInfoForm", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.authorLabel.setObjectName(_fromUtf8("authorLabel"))
        self.infoFormLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.authorLabel)
        self.versionHorizontalLayout = QtGui.QHBoxLayout()
        self.versionHorizontalLayout.setObjectName(_fromUtf8("versionHorizontalLayout"))
        self.authorValue = QtGui.QLabel(self.infoGroupBox)
        self.authorValue.setText(QtGui.QApplication.translate("pluginInfoForm", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.authorValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.authorValue.setObjectName(_fromUtf8("authorValue"))
        self.versionHorizontalLayout.addWidget(self.authorValue)
        self.emailValue = QtGui.QLabel(self.infoGroupBox)
        self.emailValue.setText(QtGui.QApplication.translate("pluginInfoForm", "Author email", None, QtGui.QApplication.UnicodeUTF8))
        self.emailValue.setOpenExternalLinks(True)
        self.emailValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.emailValue.setObjectName(_fromUtf8("emailValue"))
        self.versionHorizontalLayout.addWidget(self.emailValue)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.versionHorizontalLayout.addItem(spacerItem)
        self.infoFormLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.versionHorizontalLayout)
        self.versionLabel = QtGui.QLabel(self.infoGroupBox)
        self.versionLabel.setText(QtGui.QApplication.translate("pluginInfoForm", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.infoFormLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.versionLabel)
        self.authorHorizontalLayout = QtGui.QHBoxLayout()
        self.authorHorizontalLayout.setObjectName(_fromUtf8("authorHorizontalLayout"))
        self.versionValue = QtGui.QLabel(self.infoGroupBox)
        self.versionValue.setText(QtGui.QApplication.translate("pluginInfoForm", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.versionValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.versionValue.setObjectName(_fromUtf8("versionValue"))
        self.authorHorizontalLayout.addWidget(self.versionValue)
        self.revisionValue = QtGui.QLabel(self.infoGroupBox)
        self.revisionValue.setText(QtGui.QApplication.translate("pluginInfoForm", "Revision", None, QtGui.QApplication.UnicodeUTF8))
        self.revisionValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.revisionValue.setObjectName(_fromUtf8("revisionValue"))
        self.authorHorizontalLayout.addWidget(self.revisionValue)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.authorHorizontalLayout.addItem(spacerItem1)
        self.infoFormLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.authorHorizontalLayout)
        self.licenseLabel = QtGui.QLabel(self.infoGroupBox)
        self.licenseLabel.setText(QtGui.QApplication.translate("pluginInfoForm", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.licenseLabel.setObjectName(_fromUtf8("licenseLabel"))
        self.infoFormLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.licenseLabel)
        self.licenseValue = QtGui.QLabel(self.infoGroupBox)
        self.licenseValue.setText(QtGui.QApplication.translate("pluginInfoForm", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.licenseValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.licenseValue.setObjectName(_fromUtf8("licenseValue"))
        self.infoFormLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.licenseValue)
        self.copyrightLabel = QtGui.QLabel(self.infoGroupBox)
        self.copyrightLabel.setText(QtGui.QApplication.translate("pluginInfoForm", "Copyright", None, QtGui.QApplication.UnicodeUTF8))
        self.copyrightLabel.setObjectName(_fromUtf8("copyrightLabel"))
        self.infoFormLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.copyrightLabel)
        self.copyrightValue = QtGui.QLabel(self.infoGroupBox)
        self.copyrightValue.setText(QtGui.QApplication.translate("pluginInfoForm", "Copyright", None, QtGui.QApplication.UnicodeUTF8))
        self.copyrightValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.copyrightValue.setObjectName(_fromUtf8("copyrightValue"))
        self.infoFormLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.copyrightValue)
        self.websiteLabel = QtGui.QLabel(self.infoGroupBox)
        self.websiteLabel.setText(QtGui.QApplication.translate("pluginInfoForm", "Web Site", None, QtGui.QApplication.UnicodeUTF8))
        self.websiteLabel.setObjectName(_fromUtf8("websiteLabel"))
        self.infoFormLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.websiteLabel)
        self.websiteValue = QtGui.QLabel(self.infoGroupBox)
        self.websiteValue.setText(QtGui.QApplication.translate("pluginInfoForm", "Web Site", None, QtGui.QApplication.UnicodeUTF8))
        self.websiteValue.setOpenExternalLinks(True)
        self.websiteValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.websiteValue.setObjectName(_fromUtf8("websiteValue"))
        self.infoFormLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.websiteValue)
        self.verticalLayout.addWidget(self.infoGroupBox)
        self.statusGroupBox = QtGui.QGroupBox(pluginInfoForm)
        self.statusGroupBox.setTitle(QtGui.QApplication.translate("pluginInfoForm", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.statusGroupBox.setObjectName(_fromUtf8("statusGroupBox"))
        self.statusFormLayout = QtGui.QFormLayout(self.statusGroupBox)
        self.statusFormLayout.setObjectName(_fromUtf8("statusFormLayout"))
        self.fullPathLabel = QtGui.QLabel(self.statusGroupBox)
        self.fullPathLabel.setText(QtGui.QApplication.translate("pluginInfoForm", "Ful Path", None, QtGui.QApplication.UnicodeUTF8))
        self.fullPathLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.fullPathLabel.setObjectName(_fromUtf8("fullPathLabel"))
        self.statusFormLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.fullPathLabel)
        self.fullPathValue = QtGui.QLabel(self.statusGroupBox)
        self.fullPathValue.setText(QtGui.QApplication.translate("pluginInfoForm", "Ful Path", None, QtGui.QApplication.UnicodeUTF8))
        self.fullPathValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.fullPathValue.setObjectName(_fromUtf8("fullPathValue"))
        self.statusFormLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.fullPathValue)
        self.loadedCheckBox = QtGui.QCheckBox(self.statusGroupBox)
        self.loadedCheckBox.setEnabled(False)
        self.loadedCheckBox.setText(QtGui.QApplication.translate("pluginInfoForm", "Loaded", None, QtGui.QApplication.UnicodeUTF8))
        self.loadedCheckBox.setObjectName(_fromUtf8("loadedCheckBox"))
        self.statusFormLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.loadedCheckBox)
        self.verticalLayout.addWidget(self.statusGroupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(pluginInfoForm)
        QtCore.QMetaObject.connectSlotsByName(pluginInfoForm)

    def retranslateUi(self, pluginInfoForm):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    pluginInfoForm = QtGui.QWidget()
    ui = Ui_pluginInfoForm()
    ui.setupUi(pluginInfoForm)
    pluginInfoForm.show()
    sys.exit(app.exec_())

