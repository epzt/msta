# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_set_gsta_variables_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        self.widget = QtWidgets.QWidget(setGSTAVariablesDialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 241, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.meanComboBox = QtWidgets.QComboBox(self.widget)
        self.meanComboBox.setObjectName("meanComboBox")
        self.horizontalLayout.addWidget(self.meanComboBox)
        self.widget1 = QtWidgets.QWidget(setGSTAVariablesDialog)
        self.widget1.setGeometry(QtCore.QRect(20, 60, 241, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sortingComboBox = QtWidgets.QComboBox(self.widget1)
        self.sortingComboBox.setObjectName("sortingComboBox")
        self.horizontalLayout_2.addWidget(self.sortingComboBox)
        self.widget2 = QtWidgets.QWidget(setGSTAVariablesDialog)
        self.widget2.setGeometry(QtCore.QRect(20, 100, 241, 25))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.skewnessComboBox = QtWidgets.QComboBox(self.widget2)
        self.skewnessComboBox.setObjectName("skewnessComboBox")
        self.horizontalLayout_3.addWidget(self.skewnessComboBox)

        self.retranslateUi(setGSTAVariablesDialog)
        self.buttonBox.accepted.connect(setGSTAVariablesDialog.accept)
        self.buttonBox.rejected.connect(setGSTAVariablesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(setGSTAVariablesDialog)

    def retranslateUi(self, setGSTAVariablesDialog):
        _translate = QtCore.QCoreApplication.translate
        setGSTAVariablesDialog.setWindowTitle(_translate("setGSTAVariablesDialog", "Set GSTA variables"))
        self.label.setText(_translate("setGSTAVariablesDialog", "MEAN"))
        self.label_2.setText(_translate("setGSTAVariablesDialog", "SORTING"))
        self.label_3.setText(_translate("setGSTAVariablesDialog", "SKEWNESS"))

