# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_msta_trend_definition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mstaTrendDefinitionDialog(object):
    def setupUi(self, mstaTrendDefinitionDialog):
        mstaTrendDefinitionDialog.setObjectName("mstaTrendDefinitionDialog")
        mstaTrendDefinitionDialog.resize(360, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mstaTrendDefinitionDialog.sizePolicy().hasHeightForWidth())
        mstaTrendDefinitionDialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtWidgets.QDialogButtonBox(mstaTrendDefinitionDialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 200, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comparatorComboBox = QtWidgets.QComboBox(mstaTrendDefinitionDialog)
        self.comparatorComboBox.setGeometry(QtCore.QRect(270, 80, 40, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comparatorComboBox.setFont(font)
        self.comparatorComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comparatorComboBox.setAutoFillBackground(False)
        self.comparatorComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comparatorComboBox.setObjectName("comparatorComboBox")
        self.comparatorComboBox.addItem("")
        self.comparatorComboBox.addItem("")
        self.comparatorComboBox.addItem("")
        self.layoutWidget = QtWidgets.QWidget(mstaTrendDefinitionDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 50, 82, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addPushButton.setObjectName("addPushButton")
        self.verticalLayout_2.addWidget(self.addPushButton)
        self.deletePushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deletePushButton.setObjectName("deletePushButton")
        self.verticalLayout_2.addWidget(self.deletePushButton)
        self.clearPushButton = QtWidgets.QPushButton(mstaTrendDefinitionDialog)
        self.clearPushButton.setGeometry(QtCore.QRect(10, 190, 80, 24))
        self.clearPushButton.setObjectName("clearPushButton")
        self.splitter = QtWidgets.QSplitter(mstaTrendDefinitionDialog)
        self.splitter.setGeometry(QtCore.QRect(170, 160, 181, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.trendCaseTextEdit = QtWidgets.QTextEdit(mstaTrendDefinitionDialog)
        self.trendCaseTextEdit.setEnabled(True)
        self.trendCaseTextEdit.setGeometry(QtCore.QRect(10, 10, 141, 171))
        self.trendCaseTextEdit.setAutoFillBackground(False)
        self.trendCaseTextEdit.setReadOnly(True)
        self.trendCaseTextEdit.setObjectName("trendCaseTextEdit")
        self.splitter_2 = QtWidgets.QSplitter(mstaTrendDefinitionDialog)
        self.splitter_2.setGeometry(QtCore.QRect(230, 10, 111, 44))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        self.label.setObjectName("label")
        self.variableAComboBox = QtWidgets.QComboBox(self.splitter_2)
        self.variableAComboBox.setObjectName("variableAComboBox")
        self.splitter_3 = QtWidgets.QSplitter(mstaTrendDefinitionDialog)
        self.splitter_3.setGeometry(QtCore.QRect(230, 130, 111, 44))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_2 = QtWidgets.QLabel(self.splitter_3)
        self.label_2.setObjectName("label_2")
        self.variableBComboBox = QtWidgets.QComboBox(self.splitter_3)
        self.variableBComboBox.setObjectName("variableBComboBox")

        self.retranslateUi(mstaTrendDefinitionDialog)
        self.buttonBox.accepted.connect(mstaTrendDefinitionDialog.accept)
        self.buttonBox.rejected.connect(mstaTrendDefinitionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(mstaTrendDefinitionDialog)

    def retranslateUi(self, mstaTrendDefinitionDialog):
        _translate = QtCore.QCoreApplication.translate
        mstaTrendDefinitionDialog.setWindowTitle(_translate("mstaTrendDefinitionDialog", "Dialog"))
        self.comparatorComboBox.setItemText(0, _translate("mstaTrendDefinitionDialog", ">"))
        self.comparatorComboBox.setItemText(1, _translate("mstaTrendDefinitionDialog", "<"))
        self.comparatorComboBox.setItemText(2, _translate("mstaTrendDefinitionDialog", "=="))
        self.addPushButton.setText(_translate("mstaTrendDefinitionDialog", "<<"))
        self.deletePushButton.setText(_translate("mstaTrendDefinitionDialog", ">>"))
        self.clearPushButton.setText(_translate("mstaTrendDefinitionDialog", "Clear"))
        self.label.setText(_translate("mstaTrendDefinitionDialog", "Variable A"))
        self.label_2.setText(_translate("mstaTrendDefinitionDialog", "Variable B"))

