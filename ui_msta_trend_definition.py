# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_msta_trend_definition.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
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
        self.variableAComboBox = QtWidgets.QComboBox(mstaTrendDefinitionDialog)
        self.variableAComboBox.setGeometry(QtCore.QRect(231, 27, 121, 24))
        self.variableAComboBox.setObjectName("variableAComboBox")
        self.variableBComboBox = QtWidgets.QComboBox(mstaTrendDefinitionDialog)
        self.variableBComboBox.setGeometry(QtCore.QRect(231, 120, 121, 24))
        self.variableBComboBox.setObjectName("variableBComboBox")
        self.comparatorComboBox = QtWidgets.QComboBox(mstaTrendDefinitionDialog)
        self.comparatorComboBox.setGeometry(QtCore.QRect(250, 60, 40, 32))
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
        self.trendListLabel = QtWidgets.QLabel(mstaTrendDefinitionDialog)
        self.trendListLabel.setEnabled(True)
        self.trendListLabel.setGeometry(QtCore.QRect(10, 20, 131, 161))
        self.trendListLabel.setAutoFillBackground(True)
        self.trendListLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.trendListLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.trendListLabel.setLineWidth(1)
        self.trendListLabel.setMidLineWidth(0)
        self.trendListLabel.setText("")
        self.trendListLabel.setTextFormat(QtCore.Qt.AutoText)
        self.trendListLabel.setScaledContents(False)
        self.trendListLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trendListLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.trendListLabel.setObjectName("trendListLabel")
        self.label = QtWidgets.QLabel(mstaTrendDefinitionDialog)
        self.label.setGeometry(QtCore.QRect(230, 10, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(mstaTrendDefinitionDialog)
        self.label_2.setGeometry(QtCore.QRect(230, 103, 60, 16))
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(mstaTrendDefinitionDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 53, 61, 81))
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
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setObjectName("label_3")
        self.linkOperandComboBox = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linkOperandComboBox.setFont(font)
        self.linkOperandComboBox.setObjectName("linkOperandComboBox")
        self.linkOperandComboBox.addItem("")
        self.linkOperandComboBox.addItem("")
        self.linkOperandComboBox.addItem("")

        self.retranslateUi(mstaTrendDefinitionDialog)
        self.buttonBox.accepted.connect(mstaTrendDefinitionDialog.accept)
        self.buttonBox.rejected.connect(mstaTrendDefinitionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(mstaTrendDefinitionDialog)

    def retranslateUi(self, mstaTrendDefinitionDialog):
        _translate = QtCore.QCoreApplication.translate
        mstaTrendDefinitionDialog.setWindowTitle(_translate("mstaTrendDefinitionDialog", "Dialog"))
        self.comparatorComboBox.setItemText(0, _translate("mstaTrendDefinitionDialog", ">"))
        self.comparatorComboBox.setItemText(1, _translate("mstaTrendDefinitionDialog", "<"))
        self.label.setText(_translate("mstaTrendDefinitionDialog", "Variable A"))
        self.label_2.setText(_translate("mstaTrendDefinitionDialog", "Variable B"))
        self.addPushButton.setText(_translate("mstaTrendDefinitionDialog", "<<"))
        self.deletePushButton.setText(_translate("mstaTrendDefinitionDialog", ">>"))
        self.clearPushButton.setText(_translate("mstaTrendDefinitionDialog", "Clear"))
        self.label_3.setText(_translate("mstaTrendDefinitionDialog", "Link operand"))
        self.linkOperandComboBox.setItemText(0, _translate("mstaTrendDefinitionDialog", "AND"))
        self.linkOperandComboBox.setItemText(1, _translate("mstaTrendDefinitionDialog", "OR"))
        self.linkOperandComboBox.setItemText(2, _translate("mstaTrendDefinitionDialog", "XOR"))

