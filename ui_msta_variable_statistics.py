# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_msta_variable_statistics.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mstaVariableStatisticsDialog(object):
    def setupUi(self, mstaVariableStatisticsDialog):
        mstaVariableStatisticsDialog.setObjectName("mstaVariableStatisticsDialog")
        mstaVariableStatisticsDialog.resize(400, 208)
        self.buttonBox = QtWidgets.QDialogButtonBox(mstaVariableStatisticsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.variableListComboBox = QtWidgets.QComboBox(mstaVariableStatisticsDialog)
        self.variableListComboBox.setGeometry(QtCore.QRect(20, 30, 161, 25))
        self.variableListComboBox.setObjectName("variableListComboBox")
        self.label = QtWidgets.QLabel(mstaVariableStatisticsDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 92, 17))
        self.label.setObjectName("label")
        self.statisticsTextEdit = QtWidgets.QPlainTextEdit(mstaVariableStatisticsDialog)
        self.statisticsTextEdit.setGeometry(QtCore.QRect(20, 80, 251, 111))
        self.statisticsTextEdit.setReadOnly(True)
        self.statisticsTextEdit.setObjectName("statisticsTextEdit")

        self.retranslateUi(mstaVariableStatisticsDialog)
        self.buttonBox.accepted.connect(mstaVariableStatisticsDialog.accept)
        self.buttonBox.rejected.connect(mstaVariableStatisticsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(mstaVariableStatisticsDialog)

    def retranslateUi(self, mstaVariableStatisticsDialog):
        _translate = QtCore.QCoreApplication.translate
        mstaVariableStatisticsDialog.setWindowTitle(_translate("mstaVariableStatisticsDialog", "Dialog"))
        self.label.setText(_translate("mstaVariableStatisticsDialog", "Select a variable"))
