# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_set_gsta_variables_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setGSTAVariablesDialog(object):
    def setupUi(self, setGSTAVariablesDialog):
        setGSTAVariablesDialog.setObjectName("setGSTAVariablesDialog")
        setGSTAVariablesDialog.resize(280, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(setGSTAVariablesDialog.sizePolicy().hasHeightForWidth())
        setGSTAVariablesDialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtWidgets.QDialogButtonBox(setGSTAVariablesDialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 140, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.meanButton = QtWidgets.QPushButton(setGSTAVariablesDialog)
        self.meanButton.setGeometry(QtCore.QRect(10, 20, 80, 24))
        self.meanButton.setObjectName("meanButton")
        self.sortingButton = QtWidgets.QPushButton(setGSTAVariablesDialog)
        self.sortingButton.setGeometry(QtCore.QRect(10, 60, 80, 24))
        self.sortingButton.setObjectName("sortingButton")
        self.skewnessButton = QtWidgets.QPushButton(setGSTAVariablesDialog)
        self.skewnessButton.setGeometry(QtCore.QRect(10, 100, 80, 24))
        self.skewnessButton.setObjectName("skewnessButton")
        self.meanLineEdit = QtWidgets.QLineEdit(setGSTAVariablesDialog)
        self.meanLineEdit.setGeometry(QtCore.QRect(100, 20, 161, 24))
        self.meanLineEdit.setObjectName("meanLineEdit")
        self.sortingLineEdit = QtWidgets.QLineEdit(setGSTAVariablesDialog)
        self.sortingLineEdit.setGeometry(QtCore.QRect(100, 60, 161, 24))
        self.sortingLineEdit.setObjectName("sortingLineEdit")
        self.skewnessLineEdit = QtWidgets.QLineEdit(setGSTAVariablesDialog)
        self.skewnessLineEdit.setGeometry(QtCore.QRect(100, 100, 161, 24))
        self.skewnessLineEdit.setObjectName("skewnessLineEdit")

        self.retranslateUi(setGSTAVariablesDialog)
        self.buttonBox.accepted.connect(setGSTAVariablesDialog.accept)
        self.buttonBox.rejected.connect(setGSTAVariablesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(setGSTAVariablesDialog)

    def retranslateUi(self, setGSTAVariablesDialog):
        _translate = QtCore.QCoreApplication.translate
        setGSTAVariablesDialog.setWindowTitle(_translate("setGSTAVariablesDialog", "Set GSTA variables"))
        self.meanButton.setText(_translate("setGSTAVariablesDialog", "Mean"))
        self.sortingButton.setText(_translate("setGSTAVariablesDialog", "Sorting"))
        self.skewnessButton.setText(_translate("setGSTAVariablesDialog", "Skewness"))

