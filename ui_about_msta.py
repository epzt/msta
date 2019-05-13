# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about_msta.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDlg(object):
    def setupUi(self, AboutDlg):
        AboutDlg.setObjectName("AboutDlg")
        AboutDlg.resize(539, 273)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/mutli_sediment_trend_analysis/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDlg.setWindowIcon(icon)
        AboutDlg.setModal(True)
        self.okButton = QtWidgets.QPushButton(AboutDlg)
        self.okButton.setGeometry(QtCore.QRect(10, 240, 80, 24))
        self.okButton.setAutoDefault(True)
        self.okButton.setObjectName("okButton")
        self.label = QtWidgets.QLabel(AboutDlg)
        self.label.setGeometry(QtCore.QRect(40, 10, 441, 37))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AboutDlg)
        self.label_2.setGeometry(QtCore.QRect(220, 50, 83, 37))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AboutDlg)
        self.label_3.setGeometry(QtCore.QRect(240, 250, 291, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AboutDlg)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 451, 131))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/plugins/mutli_sediment_trend_analysis/logogeoceano transparent.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AboutDlg)
        self.label_5.setGeometry(QtCore.QRect(170, 210, 206, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(AboutDlg)
        self.okButton.clicked.connect(AboutDlg.close)
        QtCore.QMetaObject.connectSlotsByName(AboutDlg)

    def retranslateUi(self, AboutDlg):
        _translate = QtCore.QCoreApplication.translate
        AboutDlg.setWindowTitle(_translate("AboutDlg", "About MSTA"))
        self.okButton.setText(_translate("AboutDlg", "Ok"))
        self.label.setText(_translate("AboutDlg", "Mutli-Sediment Trend Analysis"))
        self.label_2.setText(_translate("AboutDlg", "MSTA"))
        self.label_3.setText(_translate("AboutDlg", "Author: E. Poizot (emmanuel.poizot@lecnam.net)"))
        self.label_5.setText(_translate("AboutDlg", "http://www.geoceano.fr"))

import resources
