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
        AboutDlg.setModal(True)
        self.aboutText = QtWidgets.QTextEdit(AboutDlg)
        self.aboutText.setEnabled(False)
        self.aboutText.setGeometry(QtCore.QRect(10, 20, 511, 211))
        self.aboutText.setObjectName("aboutText")
        self.okButton = QtWidgets.QPushButton(AboutDlg)
        self.okButton.setGeometry(QtCore.QRect(10, 240, 80, 24))
        self.okButton.setAutoDefault(True)
        self.okButton.setObjectName("okButton")

        self.retranslateUi(AboutDlg)
        self.okButton.clicked.connect(AboutDlg.close)
        QtCore.QMetaObject.connectSlotsByName(AboutDlg)

    def retranslateUi(self, AboutDlg):
        _translate = QtCore.QCoreApplication.translate
        AboutDlg.setWindowTitle(_translate("AboutDlg", "About MSTA"))
        self.aboutText.setHtml(_translate("AboutDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\'; font-size:18pt; color:#000000; background-color:#ffffff;\">MSTA</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\'; font-size:14px; font-weight:600; color:#000000;\">Multi-Sediment Trend Analysis (MSTA) is an enhancement of a previous QGIS plugin (GiSedTrend).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\'; font-size:14px; font-weight:600; color:#000000;\">MSTA still allows classical Grain Size Trend Analysis (GSTA), for which it includes particular menu entries.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\'; font-size:14px; font-weight:600; color:#000000;\">MSTA allows now to realize trend analysis of any numerical variable at point locations.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\'; font-size:14px; font-weight:600; color:#000000;\">MSTA</span><span style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\'; font-size:14px; color:#000000;\"> is realized by E. Poizot (emmanuel.poizot@lecnam.net).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\'; font-size:14px; color:#000000;\">Collaborations: Y. Mear, A. Murat, G. Gregoire and N. Baux</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.okButton.setText(_translate("AboutDlg", "Ok"))

