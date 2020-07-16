# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_multi_sediment_trend_analysis_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 326)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuVariables = QtWidgets.QMenu(self.menubar)
        self.menuVariables.setObjectName("menuVariables")
        self.menuList = QtWidgets.QMenu(self.menuVariables)
        self.menuList.setObjectName("menuList")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.computeMSTA = QtWidgets.QMenu(self.menubar)
        self.computeMSTA.setObjectName("computeMSTA")
        self.menuProcessing = QtWidgets.QMenu(self.menubar)
        self.menuProcessing.setObjectName("menuProcessing")
        self.menuExpressions = QtWidgets.QMenu(self.menubar)
        self.menuExpressions.setObjectName("menuExpressions")
        self.menuTrends = QtWidgets.QMenu(self.menubar)
        self.menuTrends.setObjectName("menuTrends")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFileImport = QtWidgets.QAction(MainWindow)
        self.actionFileImport.setObjectName("actionFileImport")
        self.actionModifyVariablesName = QtWidgets.QAction(MainWindow)
        self.actionModifyVariablesName.setObjectName("actionModifyVariablesName")
        self.actionModifyVariablesUnits = QtWidgets.QAction(MainWindow)
        self.actionModifyVariablesUnits.setObjectName("actionModifyVariablesUnits")
        self.actionVModifyVariablesRange = QtWidgets.QAction(MainWindow)
        self.actionVModifyVariablesRange.setObjectName("actionVModifyVariablesRange")
        self.actionModifyVariableResearchArea = QtWidgets.QAction(MainWindow)
        self.actionModifyVariableResearchArea.setObjectName("actionModifyVariableResearchArea")
        self.actionDeleteAllVariables = QtWidgets.QAction(MainWindow)
        self.actionDeleteAllVariables.setObjectName("actionDeleteAllVariables")
        self.actionDeleteVariables = QtWidgets.QAction(MainWindow)
        self.actionDeleteVariables.setObjectName("actionDeleteVariables")
        self.actionAppQuit = QtWidgets.QAction(MainWindow)
        self.actionAppQuit.setObjectName("actionAppQuit")
        self.actionListAllTrends = QtWidgets.QAction(MainWindow)
        self.actionListAllTrends.setObjectName("actionListAllTrends")
        self.actionSelectAllVariables = QtWidgets.QAction(MainWindow)
        self.actionSelectAllVariables.setObjectName("actionSelectAllVariables")
        self.actionSelectOneVariable = QtWidgets.QAction(MainWindow)
        self.actionSelectOneVariable.setObjectName("actionSelectOneVariable")
        self.actionModifyTrends = QtWidgets.QAction(MainWindow)
        self.actionModifyTrends.setObjectName("actionModifyTrends")
        self.actionSetWorkingDirectory = QtWidgets.QAction(MainWindow)
        self.actionSetWorkingDirectory.setObjectName("actionSetWorkingDirectory")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setCheckable(False)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGSTA = QtWidgets.QAction(MainWindow)
        self.actionGSTA.setObjectName("actionGSTA")
        self.actionMSTA = QtWidgets.QAction(MainWindow)
        self.actionMSTA.setObjectName("actionMSTA")
        self.actionGSTALikeVariable = QtWidgets.QAction(MainWindow)
        self.actionGSTALikeVariable.setObjectName("actionGSTALikeVariable")
        self.actionTrendSet = QtWidgets.QAction(MainWindow)
        self.actionTrendSet.setObjectName("actionTrendSet")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoadViewText = QtWidgets.QAction(MainWindow)
        self.actionLoadViewText.setObjectName("actionLoadViewText")
        self.actionSaveViewText = QtWidgets.QAction(MainWindow)
        self.actionSaveViewText.setObjectName("actionSaveViewText")
        self.actionClearViewText = QtWidgets.QAction(MainWindow)
        self.actionClearViewText.setObjectName("actionClearViewText")
        self.actionTrendList = QtWidgets.QAction(MainWindow)
        self.actionTrendList.setObjectName("actionTrendList")
        self.actionModifyVariables = QtWidgets.QAction(MainWindow)
        self.actionModifyVariables.setObjectName("actionModifyVariables")
        self.actionResetInitial = QtWidgets.QAction(MainWindow)
        self.actionResetInitial.setObjectName("actionResetInitial")
        self.actionAll = QtWidgets.QAction(MainWindow)
        self.actionAll.setObjectName("actionAll")
        self.actionVariableListAll = QtWidgets.QAction(MainWindow)
        self.actionVariableListAll.setObjectName("actionVariableListAll")
        self.actionVariableListSelected = QtWidgets.QAction(MainWindow)
        self.actionVariableListSelected.setObjectName("actionVariableListSelected")
        self.actionComputeMSTA = QtWidgets.QAction(MainWindow)
        self.actionComputeMSTA.setObjectName("actionComputeMSTA")
        self.actionVariableSettings = QtWidgets.QAction(MainWindow)
        self.actionVariableSettings.setObjectName("actionVariableSettings")
        self.actionTrendSettings = QtWidgets.QAction(MainWindow)
        self.actionTrendSettings.setObjectName("actionTrendSettings")
        self.actionSelectVariables = QtWidgets.QAction(MainWindow)
        self.actionSelectVariables.setToolTip("Select")
        self.actionSelectVariables.setObjectName("actionSelectVariables")
        self.actionClearSelect = QtWidgets.QAction(MainWindow)
        self.actionClearSelect.setObjectName("actionClearSelect")
        self.actionCluster = QtWidgets.QAction(MainWindow)
        self.actionCluster.setObjectName("actionCluster")
        self.actionPCA = QtWidgets.QAction(MainWindow)
        self.actionPCA.setObjectName("actionPCA")
        self.actionCloseDataSet = QtWidgets.QAction(MainWindow)
        self.actionCloseDataSet.setObjectName("actionCloseDataSet")
        self.actionSetTrend = QtWidgets.QAction(MainWindow)
        self.actionSetTrend.setObjectName("actionSetTrend")
        self.actionBuild = QtWidgets.QAction(MainWindow)
        self.actionBuild.setObjectName("actionBuild")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionList = QtWidgets.QAction(MainWindow)
        self.actionList.setObjectName("actionList")
        self.actionDeleteTrend = QtWidgets.QAction(MainWindow)
        self.actionDeleteTrend.setObjectName("actionDeleteTrend")
        self.actionListTrend = QtWidgets.QAction(MainWindow)
        self.actionListTrend.setObjectName("actionListTrend")
        self.actionSetTrend1 = QtWidgets.QAction(MainWindow)
        self.actionSetTrend1.setObjectName("actionSetTrend1")
        self.actionSetGSTATrend = QtWidgets.QAction(MainWindow)
        self.actionSetGSTATrend.setObjectName("actionSetGSTATrend")
        self.menuFile.addAction(self.actionSetWorkingDirectory)
        self.menuFile.addAction(self.actionFileImport)
        self.menuFile.addAction(self.actionCloseDataSet)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAppQuit)
        self.menuList.addAction(self.actionVariableListAll)
        self.menuList.addAction(self.actionVariableListSelected)
        self.menuVariables.addAction(self.actionModifyVariables)
        self.menuVariables.addAction(self.menuList.menuAction())
        self.menuVariables.addAction(self.actionDeleteVariables)
        self.menuVariables.addSeparator()
        self.menuVariables.addAction(self.actionGSTALikeVariable)
        self.menuSettings.addAction(self.actionSaveViewText)
        self.menuSettings.addAction(self.actionLoadViewText)
        self.menuSettings.addAction(self.actionClearViewText)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionVariableSettings)
        self.menuHelp.addAction(self.actionTrendSettings)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.computeMSTA.addAction(self.actionComputeMSTA)
        self.menuProcessing.addAction(self.actionCluster)
        self.menuProcessing.addAction(self.actionPCA)
        self.menuExpressions.addSeparator()
        self.menuExpressions.addAction(self.actionBuild)
        self.menuExpressions.addAction(self.actionDelete)
        self.menuExpressions.addAction(self.actionList)
        self.menuTrends.addAction(self.actionSetTrend)
        self.menuTrends.addAction(self.actionDeleteTrend)
        self.menuTrends.addAction(self.actionListTrend)
        self.menuTrends.addAction(self.actionSetGSTATrend)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuVariables.menuAction())
        self.menubar.addAction(self.menuTrends.menuAction())
        self.menubar.addAction(self.menuExpressions.menuAction())
        self.menubar.addAction(self.computeMSTA.menuAction())
        self.menubar.addAction(self.menuProcessing.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuVariables.setTitle(_translate("MainWindow", "Variables"))
        self.menuList.setTitle(_translate("MainWindow", "List"))
        self.menuSettings.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.computeMSTA.setTitle(_translate("MainWindow", "Run"))
        self.menuProcessing.setTitle(_translate("MainWindow", "Analysis"))
        self.menuExpressions.setTitle(_translate("MainWindow", "Expressions"))
        self.menuTrends.setTitle(_translate("MainWindow", "Trends"))
        self.actionFileImport.setText(_translate("MainWindow", "Import dataset..."))
        self.actionModifyVariablesName.setText(_translate("MainWindow", "Name..."))
        self.actionModifyVariablesUnits.setText(_translate("MainWindow", "Units..."))
        self.actionVModifyVariablesRange.setText(_translate("MainWindow", "Range..."))
        self.actionModifyVariableResearchArea.setText(_translate("MainWindow", "Research area..."))
        self.actionDeleteAllVariables.setText(_translate("MainWindow", "All..."))
        self.actionDeleteVariables.setText(_translate("MainWindow", "Delete..."))
        self.actionAppQuit.setText(_translate("MainWindow", "Quit"))
        self.actionListAllTrends.setText(_translate("MainWindow", "All"))
        self.actionSelectAllVariables.setText(_translate("MainWindow", "All"))
        self.actionSelectOneVariable.setText(_translate("MainWindow", "One..."))
        self.actionModifyTrends.setText(_translate("MainWindow", "Modify..."))
        self.actionSetWorkingDirectory.setText(_translate("MainWindow", "Set working directory..."))
        self.actionSetWorkingDirectory.setToolTip(_translate("MainWindow", "Set working directory"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionGSTA.setText(_translate("MainWindow", "GSTA..."))
        self.actionMSTA.setText(_translate("MainWindow", "MSTA..."))
        self.actionGSTALikeVariable.setText(_translate("MainWindow", "GSTA variables..."))
        self.actionTrendSet.setText(_translate("MainWindow", "Set/modify..."))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionLoad.setText(_translate("MainWindow", "Load..."))
        self.actionLoadViewText.setText(_translate("MainWindow", "Load..."))
        self.actionSaveViewText.setText(_translate("MainWindow", "Save..."))
        self.actionClearViewText.setText(_translate("MainWindow", "Clear"))
        self.actionTrendList.setText(_translate("MainWindow", "List"))
        self.actionModifyVariables.setText(_translate("MainWindow", "Modify..."))
        self.actionResetInitial.setText(_translate("MainWindow", "Reset initial"))
        self.actionAll.setText(_translate("MainWindow", "All..."))
        self.actionVariableListAll.setText(_translate("MainWindow", "All"))
        self.actionVariableListSelected.setText(_translate("MainWindow", "Selected"))
        self.actionComputeMSTA.setText(_translate("MainWindow", "Compute..."))
        self.actionVariableSettings.setText(_translate("MainWindow", "Variable settings"))
        self.actionTrendSettings.setText(_translate("MainWindow", "Trend settings"))
        self.actionSelectVariables.setText(_translate("MainWindow", "Select"))
        self.actionClearSelect.setText(_translate("MainWindow", "Clear select..."))
        self.actionCluster.setText(_translate("MainWindow", "Cluster..."))
        self.actionPCA.setText(_translate("MainWindow", "PCA..."))
        self.actionCloseDataSet.setText(_translate("MainWindow", "Close data set..."))
        self.actionSetTrend.setText(_translate("MainWindow", "Set/modify..."))
        self.actionBuild.setText(_translate("MainWindow", "Build..."))
        self.actionDelete.setText(_translate("MainWindow", "Delete..."))
        self.actionList.setText(_translate("MainWindow", "List"))
        self.actionDeleteTrend.setText(_translate("MainWindow", "Delete..."))
        self.actionListTrend.setText(_translate("MainWindow", "List"))
        self.actionSetTrend1.setText(_translate("MainWindow", "Classical trends..."))
        self.actionSetGSTATrend.setText(_translate("MainWindow", "GSTA trends..."))

