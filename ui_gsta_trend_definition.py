# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gsta_trend_definition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setGSTATrendCaseDialog(object):
    def setupUi(self, setGSTATrendCaseDialog):
        setGSTATrendCaseDialog.setObjectName("setGSTATrendCaseDialog")
        setGSTATrendCaseDialog.setEnabled(True)
        setGSTATrendCaseDialog.resize(504, 459)
        setGSTATrendCaseDialog.setSizeGripEnabled(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(setGSTATrendCaseDialog)
        self.buttonBox.setGeometry(QtCore.QRect(310, 420, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.GSTAGroup = QtWidgets.QGroupBox(setGSTATrendCaseDialog)
        self.GSTAGroup.setEnabled(True)
        self.GSTAGroup.setGeometry(QtCore.QRect(180, 10, 311, 401))
        self.GSTAGroup.setAutoFillBackground(False)
        self.GSTAGroup.setStyleSheet("")
        self.GSTAGroup.setFlat(False)
        self.GSTAGroup.setObjectName("GSTAGroup")
        self.buttonRemoveGSTATrendCase = QtWidgets.QPushButton(self.GSTAGroup)
        self.buttonRemoveGSTATrendCase.setGeometry(QtCore.QRect(40, 159, 41, 27))
        self.buttonRemoveGSTATrendCase.setObjectName("buttonRemoveGSTATrendCase")
        self.buttonAddGSTATrendCase = QtWidgets.QPushButton(self.GSTAGroup)
        self.buttonAddGSTATrendCase.setGeometry(QtCore.QRect(40, 109, 41, 27))
        self.buttonAddGSTATrendCase.setObjectName("buttonAddGSTATrendCase")
        self.GSTATrendMeanGroup = QtWidgets.QGroupBox(self.GSTAGroup)
        self.GSTATrendMeanGroup.setGeometry(QtCore.QRect(90, 59, 181, 51))
        self.GSTATrendMeanGroup.setCheckable(False)
        self.GSTATrendMeanGroup.setObjectName("GSTATrendMeanGroup")
        self.layoutWidget = QtWidgets.QWidget(self.GSTATrendMeanGroup)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 161, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioGSTAMeanFiner = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioGSTAMeanFiner.setObjectName("radioGSTAMeanFiner")
        self.gridLayout.addWidget(self.radioGSTAMeanFiner, 0, 0, 1, 1)
        self.radioGSTAMeanCoarser = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioGSTAMeanCoarser.setObjectName("radioGSTAMeanCoarser")
        self.gridLayout.addWidget(self.radioGSTAMeanCoarser, 0, 1, 1, 1)
        self.radioGSTAMeanNone = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioGSTAMeanNone.setChecked(True)
        self.radioGSTAMeanNone.setObjectName("radioGSTAMeanNone")
        self.gridLayout.addWidget(self.radioGSTAMeanNone, 0, 2, 1, 1)
        self.GSTATrendSortingGroup = QtWidgets.QGroupBox(self.GSTAGroup)
        self.GSTATrendSortingGroup.setGeometry(QtCore.QRect(90, 120, 181, 51))
        self.GSTATrendSortingGroup.setObjectName("GSTATrendSortingGroup")
        self.layoutWidget1 = QtWidgets.QWidget(self.GSTATrendSortingGroup)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 161, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioGSTASortingBetter = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioGSTASortingBetter.setObjectName("radioGSTASortingBetter")
        self.gridLayout_2.addWidget(self.radioGSTASortingBetter, 0, 0, 1, 1)
        self.radioGSTASortingPorer = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioGSTASortingPorer.setObjectName("radioGSTASortingPorer")
        self.gridLayout_2.addWidget(self.radioGSTASortingPorer, 0, 1, 1, 1)
        self.radioGSTASortingNone = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioGSTASortingNone.setChecked(True)
        self.radioGSTASortingNone.setObjectName("radioGSTASortingNone")
        self.gridLayout_2.addWidget(self.radioGSTASortingNone, 0, 2, 1, 1)
        self.GSTATrendSkewnessGroup = QtWidgets.QGroupBox(self.GSTAGroup)
        self.GSTATrendSkewnessGroup.setGeometry(QtCore.QRect(90, 180, 181, 51))
        self.GSTATrendSkewnessGroup.setObjectName("GSTATrendSkewnessGroup")
        self.layoutWidget2 = QtWidgets.QWidget(self.GSTATrendSkewnessGroup)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 161, 24))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioGSTASkewnessPlus = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioGSTASkewnessPlus.setObjectName("radioGSTASkewnessPlus")
        self.gridLayout_3.addWidget(self.radioGSTASkewnessPlus, 0, 0, 1, 1)
        self.radioGSTASkewnessMinus = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioGSTASkewnessMinus.setObjectName("radioGSTASkewnessMinus")
        self.gridLayout_3.addWidget(self.radioGSTASkewnessMinus, 0, 1, 1, 1)
        self.radioGSTASkewnessNone = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioGSTASkewnessNone.setChecked(True)
        self.radioGSTASkewnessNone.setObjectName("radioGSTASkewnessNone")
        self.gridLayout_3.addWidget(self.radioGSTASkewnessNone, 0, 2, 1, 1)
        self.PreDefinedGroupBox = QtWidgets.QGroupBox(self.GSTAGroup)
        self.PreDefinedGroupBox.setGeometry(QtCore.QRect(20, 290, 271, 91))
        self.PreDefinedGroupBox.setCheckable(True)
        self.PreDefinedGroupBox.setChecked(False)
        self.PreDefinedGroupBox.setObjectName("PreDefinedGroupBox")
        self.GaoCollinsTrendCasesRadioButton = QtWidgets.QRadioButton(self.PreDefinedGroupBox)
        self.GaoCollinsTrendCasesRadioButton.setGeometry(QtCore.QRect(10, 30, 212, 21))
        self.GaoCollinsTrendCasesRadioButton.setObjectName("GaoCollinsTrendCasesRadioButton")
        self.XORHeightTrendCasesRadioButton = QtWidgets.QRadioButton(self.PreDefinedGroupBox)
        self.XORHeightTrendCasesRadioButton.setGeometry(QtCore.QRect(10, 60, 207, 21))
        self.XORHeightTrendCasesRadioButton.setObjectName("XORHeightTrendCasesRadioButton")
        self.UserDefinedGroupBox = QtWidgets.QGroupBox(self.GSTAGroup)
        self.UserDefinedGroupBox.setGeometry(QtCore.QRect(20, 30, 271, 251))
        self.UserDefinedGroupBox.setObjectName("UserDefinedGroupBox")
        self.label = QtWidgets.QLabel(self.UserDefinedGroupBox)
        self.label.setGeometry(QtCore.QRect(30, 210, 123, 29))
        self.label.setObjectName("label")
        self.linkOperandComboBox = QtWidgets.QComboBox(self.UserDefinedGroupBox)
        self.linkOperandComboBox.setGeometry(QtCore.QRect(180, 210, 67, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linkOperandComboBox.sizePolicy().hasHeightForWidth())
        self.linkOperandComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linkOperandComboBox.setFont(font)
        self.linkOperandComboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.linkOperandComboBox.setMaxVisibleItems(4)
        self.linkOperandComboBox.setMaxCount(5)
        self.linkOperandComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.linkOperandComboBox.setObjectName("linkOperandComboBox")
        self.linkOperandComboBox.addItem("")
        self.linkOperandComboBox.addItem("")
        self.linkOperandComboBox.addItem("")
        self.UserDefinedGroupBox.raise_()
        self.PreDefinedGroupBox.raise_()
        self.buttonAddGSTATrendCase.raise_()
        self.GSTATrendSortingGroup.raise_()
        self.GSTATrendSkewnessGroup.raise_()
        self.GSTATrendMeanGroup.raise_()
        self.buttonRemoveGSTATrendCase.raise_()
        self.TrendCaseTextEdit = QtWidgets.QTextEdit(setGSTATrendCaseDialog)
        self.TrendCaseTextEdit.setGeometry(QtCore.QRect(10, 30, 161, 381))
        self.TrendCaseTextEdit.setObjectName("TrendCaseTextEdit")

        self.retranslateUi(setGSTATrendCaseDialog)
        self.buttonBox.accepted.connect(setGSTATrendCaseDialog.accept)
        self.buttonBox.rejected.connect(setGSTATrendCaseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(setGSTATrendCaseDialog)

    def retranslateUi(self, setGSTATrendCaseDialog):
        _translate = QtCore.QCoreApplication.translate
        setGSTATrendCaseDialog.setWindowTitle(_translate("setGSTATrendCaseDialog", "GSTA trends cases"))
        self.GSTAGroup.setTitle(_translate("setGSTATrendCaseDialog", "GSTA Trend case(s) to study"))
        self.buttonRemoveGSTATrendCase.setText(_translate("setGSTATrendCaseDialog", ">>"))
        self.buttonAddGSTATrendCase.setText(_translate("setGSTATrendCaseDialog", "<<"))
        self.GSTATrendMeanGroup.setTitle(_translate("setGSTATrendCaseDialog", "Mean"))
        self.radioGSTAMeanFiner.setText(_translate("setGSTATrendCaseDialog", "F"))
        self.radioGSTAMeanCoarser.setText(_translate("setGSTATrendCaseDialog", "C"))
        self.radioGSTAMeanNone.setText(_translate("setGSTATrendCaseDialog", "None"))
        self.GSTATrendSortingGroup.setTitle(_translate("setGSTATrendCaseDialog", "Sorting"))
        self.radioGSTASortingBetter.setText(_translate("setGSTATrendCaseDialog", "B"))
        self.radioGSTASortingPorer.setText(_translate("setGSTATrendCaseDialog", "P"))
        self.radioGSTASortingNone.setText(_translate("setGSTATrendCaseDialog", "None"))
        self.GSTATrendSkewnessGroup.setTitle(_translate("setGSTATrendCaseDialog", "Skewness"))
        self.radioGSTASkewnessPlus.setText(_translate("setGSTATrendCaseDialog", "+"))
        self.radioGSTASkewnessMinus.setText(_translate("setGSTATrendCaseDialog", "-"))
        self.radioGSTASkewnessNone.setText(_translate("setGSTATrendCaseDialog", "None"))
        self.PreDefinedGroupBox.setTitle(_translate("setGSTATrendCaseDialog", "Pre-defined trend case(s)"))
        self.GaoCollinsTrendCasesRadioButton.setText(_translate("setGSTATrendCaseDialog", "Gao and Collins (FB- AND CB+)"))
        self.XORHeightTrendCasesRadioButton.setText(_translate("setGSTATrendCaseDialog", "XOR on 8 possible trend cases"))
        self.UserDefinedGroupBox.setTitle(_translate("setGSTATrendCaseDialog", "User defined"))
        self.label.setText(_translate("setGSTATrendCaseDialog", "Operand which link\n"
"multiple trend cases"))
        self.linkOperandComboBox.setItemText(0, _translate("setGSTATrendCaseDialog", "AND"))
        self.linkOperandComboBox.setItemText(1, _translate("setGSTATrendCaseDialog", "OR"))
        self.linkOperandComboBox.setItemText(2, _translate("setGSTATrendCaseDialog", "XOR"))

