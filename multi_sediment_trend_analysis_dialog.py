# -*- coding: utf-8 -*-
"""
/***************************************************************************
 mstaDialog
                                 A QGIS plugin
 Mutli-Sediment Trend Analysis
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-03-01
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Emmanuel Poizot
        email                : emmanuel.poizot@lecnam.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
#import pandas as pd
import numpy as np

from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from qgis import core, gui, utils
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from datetime import datetime

from .pyMstaTextFileAnalysisDialog import pyMstaTextFileAnalysisDialog
from .mstaCoreClass import mstaPoint as mp
from .mstaCoreClass import mstaVariable as mv
from .mstaCoreClass import mstaTrendCase, mstaComposedTrendCase, mstaOperand
from .mstaUtilsClass import *
from . import config as cfg

# Change apply 19/11/2019 to work around a problem with resources not manage by uic
#Ui_MainWindow, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'ui_multi_sediment_trend_analysis_dialog_base.ui'))
# Old way to load the dialog
from .ui_multi_sediment_trend_analysis_dialog_base  import Ui_MainWindow

class mstaDialog(QMainWindow, Ui_MainWindow):
    def __init__(self, _iface, parent=None):
        """Constructor."""
        super(mstaDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)             
        
        # Actions management
        self.actionAppQuit.triggered.connect(self.close)
        self.actionFileImport.triggered.connect(self.DataFileImport)
        self.actionAbout.triggered.connect(self.DisplayAboutMSTA)
        self.actionSetWorkingDirectory.triggered.connect(self.SetWorkingDirectory)
        self.actionComputeMSTA.triggered.connect(self.ComputeMSTA)
        self.actionBarrierLayers.triggered.connect(self.BarrierLayers)
        self.actionViewDataSet.triggered.connect(self.ViewDataSet)
        self.actionClearViewText.triggered.connect(self.SetClearText)
        self.actionCloseDataSet.triggered.connect(self.CloseCurrentDataSet)
        #
        self.actionVariableListAll.triggered.connect(self.PrintAllVariablesList)
        self.actionVariableListSelected.triggered.connect(self.PrintSelectedVariablesList)
        self.actionModifyVariables.triggered.connect(self.ModifyVariables)
        self.actionDeleteVariables.triggered.connect(self.DeleteOneVariable)
        self.actionGSTALikeVariable.triggered.connect(self.SetGSTAVariables)
        #
        self.actionSetGSTATrend.triggered.connect(self.SetGSTATrendCases)
        self.actionListTrend.triggered.connect(self.PrintTrendsList)
        self.actionSetTrend.triggered.connect(self.SetMSTATrendCases)
        self.actionDeleteTrend.triggered.connect(self.DeleteTrends)
        #
        self.actionBuild.triggered.connect(self.ExpressionBuild)
        self.actionDelete.triggered.connect(self.ExpressionDelete)
        self.actionList.triggered.connect(self.ExpressionList)

        self.setGeometry(10, 10, 500, 400)
        self.setWindowTitle('Multi Sediment Trend Analysis')

        self.menuVariables.setEnabled(False)
        self.actionSetGSTATrend.setEnabled(False)
        self.actionSetTrend.setEnabled(False)
        self.computeMSTA.setEnabled(False)
        self.actionClearSelect.setEnabled(False)
        #self.actionVariableListSelected.setEnabled(False)

        # Variables
        self.iface = _iface
        self.workingDir = os.path.expanduser("~user")
        self.points = list()
        # A list of all the variables names in the current dataset
        self.totalVariablesName = list()
        # The list of the current selected variable names, i.e. the working variables
        self.selectedVariableNames = list()
        # A list of all the variables objects of class mstaVariable
        self.theVariablesObject = list()
        # The main trend case list, contains all trend case(s), simple and/or composed
        self.theTrendsList = list()
        # The main trend object which containts the expression tout test (trends + operands)
        self.theExpressionObject = mstaComposedTrendCase()
        # "Central Widget" expands to fill all available space
        self.textwidget = QTextEdit()
        self.setCentralWidget(self.textwidget)
        self.textwidget.setEnabled(True)
        self.textwidget.setTextColor(QColor("black"))
        fontWeight = self.textwidget.currentFont().weight()
        self.textwidget.setTabStopWidth(fontWeight)
        self.temporaryLayer = ""
        self.barrierListLayers = list()

    ###############################################
    @pyqtSlot(bool)
    def DisplayAboutMSTA(self):
        dlg=aboutMSTA(self)
        dlg.exec_()
        #QMessageBox.information(self, "Information", "MSTA plugin")

    ###############################################
    @pyqtSlot(bool)
    def SetWorkingDirectory(self):
        self.workingDir = QFileDialog.getExistingDirectory(self, self.workingDir, "Select working directory...", QFileDialog.ShowDirsOnly)

    ###############################################
    @pyqtSlot(bool)
    def DataFileImport(self):
        # Check if a previous data set is loaded
        if self.theVariablesObject:
            self.CloseCurrentDataSet()
        # Choice of the file name
        fullPathFileName,_= QFileDialog.getOpenFileName(self,"Open a data file", 
                                                self.workingDir,"Text file(s) (*.txt *.csv)")
        if os.path.isfile(fullPathFileName): 
            importDlg = pyMstaTextFileAnalysisDialog(fullPathFileName)
            if importDlg.exec_() == QDialog.Rejected:
                QMessageBox.information(self, "Load data file", "No data imported.")
                return
            if not importDlg.getDataVarCoordsList():
                QMessageBox.information(self, "Load data file", "No data imported.")
                return
            try:
                # get the lists of information
                coordsids,coordsnames,varids,varnames=importDlg.getDataVarCoordsList()
                if importDlg.firstLineAsHeader:
                    dataset = np.genfromtxt(fullPathFileName,
                                            delimiter=importDlg.currentSeparator,
                                            skip_header=importDlg.getNumberOfFirstLineToSkip(),
                                            names=True,
                                            missing_values=("0", " "),
                                            filling_values=0.0,
                                            invalid_raise=True,
                                            usecols=tuple(varids),
                                            dtype=None
                                            )
                    # get the coordinates
                    coordsset = np.genfromtxt(fullPathFileName,
                                            delimiter=importDlg.currentSeparator,
                                            skip_header=importDlg.getNumberOfFirstLineToSkip(),
                                            names=True,
                                            invalid_raise=True,
                                            usecols=tuple(coordsids),
                                            dtype=None
                                            )
                else:
                    dataset = np.genfromtxt(fullPathFileName,
                                            delimiter=importDlg.currentSeparator,
                                            skip_header=importDlg.getNumberOfFirstLineToSkip(),
                                            names=tuple(varnames),
                                            missing_values=("0", " "),
                                            filling_values=0.0,
                                            invalid_raise=True,
                                            usecols=tuple(varids),
                                            dtype=None
                                            )
                    # get the coordinates
                    coordsset = np.genfromtxt(fullPathFileName,
                                            delimiter=importDlg.currentSeparator,
                                            skip_header=importDlg.getNumberOfFirstLineToSkip(),
                                            names=tuple(coordsnames),
                                            invalid_raise=True,
                                            usecols=tuple(coordsids),
                                            dtype=None
                                            )
                # QMessageBox.information(self, "Import data...", f'{dataset.shape[0]} rows have been imported.')
            except ValueError:
                QMessageBox.critical(self, "Load data file error", "An error occured while reading data file.\nNo data imported")
                return
        else:
            QMessageBox.information(self, "Load data file", "No data imported.")
            return
        # Create a temporary layer and add it to the current project
        # Create the database use for computations
        try:
            self.temporaryLayer = self.CreateTemporaryLayer(coordsset, QFileInfo(fullPathFileName).baseName())
        except:
            QMessageBox.critical(self, "Temporary layer error", "An error occured while creating temporary layer.")
            return
        try:
            self.createPointDB(dataset, varnames, coordsset, coordsnames)
        except:
            QMessageBox.critical(self, "Database initialisation error", "An error occured during database creation")
            return

        # Save information before living, just de names, variables are not created yet
        self.totalVariablesName = varnames.copy()
        self.updateLogViewPort(6, f'{len(self.points)} points created')
        self.updateLogViewPort(1, self.totalVariablesName)
        # Data set is loaded, variables and trends can be manage
        self.menuVariables.setEnabled(True)
        self.actionSetTrend.setEnabled(True)
        # Save current directory in a variable
        self.workingDir = os.path.dirname(fullPathFileName)
        return

    ###############################################
    # _coordsset: np.array of n samples lines and two coordinates
    # _filename: name of the text file (without extension) which contains the original data
    def CreateTemporaryLayer(self, _coordsset, _filename):
        # Selection of a reference system eventually different from the current project
        theProj = QgsProjectionSelectionDialog(self)
        theProj.setCrs(QgsProject.instance().crs())
        result = theProj.exec_()
        if result == QDialog.Rejected:
            QMessageBox.information(self, "Reference system", "Layer reference system is the same to the current project")
            URI=f'point?crs={QgsProject.instance().crs().authid()}'
        else:
            URI=f'point?crs={theProj.crs().authid()}'
        # create the temporary layer
        vl = QgsVectorLayer(URI, f'msta_{_filename}_Layer', "memory")
        pr = vl.dataProvider()
        
        # create fields
        # TODO: define the list of fields to create to store the results
        pr.addAttributes([QgsField("Trends", QVariant.String)])
        pr.addAttributes([QgsField("Scores", QVariant.String)])
        pr.addAttributes([QgsField("Angle", QVariant.Double)])
        pr.addAttributes([QgsField("Module", QVariant.Double)])
        pr.addAttributes([QgsField("Comments", QVariant.String)])
        vl.updateFields() # tell the vector layer to fetch changes from the provider

        # add features
        i = 0
        for coords in _coordsset:
            fet = QgsFeature()
            fet.setId(i+1)  # Set the ID doing to way to ensure id is set correctly
            fet.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(coords[0],coords[1])))
            pr.addFeatures([fet])
            i += 1
        # update layer's extent when new features have been added
        # because change of extent in provider is not propagated to the layer
        vl.updateExtents()
        # Add the temporary layer to the current project
        QgsProject.instance().addMapLayer(vl)
        return vl

    ###############################################
    # _points: np.array of n samples lines and two coordinates
    # _variables: np.array of n samples lines and m variables columns
    # _coordnames: list of the two coordinates variables
    # _varnames: list of the variables names
    # The variable names and values are stored at each point location
    def createPointDB(self, _dataset, _varnames, _coordsset, _coordnames):
        # first loop over the points
        i = 0
        for coords in _coordsset:
            # mp is mstaPoint
            newpt = mp(coords[0], coords[1])
            newpt.setID(i+1)
            j = 0
            for var in _varnames:
                # mv is mstaVariable
                newvar = mv()
                newvar.setName(var)
                newvar.setAlias(var) # Alias = name by default
                newvar.setUnit("%") # By default % unit
                newvar.setValue(_dataset[i][j])
                newvar.setDg(0.0) # By default Dg is null
                newvar.setRange(0.0) # By default, no range
                newvar.setSearch(0.0,0.0,0.0) # By default omnidirectional
                newpt.addVariable(newvar)
                j += 1
            self.points.append(newpt)
            i += 1
        # As each point has the same variable list, the object list is equal to the list of the 1st point by default
        self.theVariablesObject = self.points[0].getVariables().copy()

    ###############################################
    # Function to update the variables in the points database
    def updatePointsDB(self, _newVariables):
        for p in self.points:
            for newv in _newVariables:
                p.updateVariable(newv)
        return

    ###############################################
    # Function which erase variables of current data set
    @pyqtSlot(bool)
    def CloseCurrentDataSet(self):
        # Check if a previous data set is loaded
        if not self.theVariablesObject:
            QMessageBox.information(self, "Data set", "No data set currently load.")
            return
        if QMessageBox.question(self, "Import data set",
                                "There is a data set loaded\nDo you want to close it ?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            # Cleaning of the variables used to manage the data set
            self.theVariablesObject = list()
            self.theTrendsList = list()
            QgsProject.instance().removeMapLayer(self.temporaryLayer.id())
            self.iface.mapCanvas().refresh()
            self.temporaryLayer = ""
            self.points = list()
            self.totalVariablesName = list()
            self.selectedVariableNames = list()
        else:
            return

    ###############################################
    # Add _text information on the viewport of the application
    # base on _context (see CONTEXTINFO dict definition)
    def updateLogViewPort(self, _context, _text):
        dt = datetime.now()
        self.textwidget.append(f'\n{dt.strftime("%d %b %Y, %H:%M:%S")}: {cfg.CONTEXTINFO[_context]}')
        if not _text:
            self.textwidget.append("\t------")
        if isinstance(_text, list):
            for i in _text:
                self.textwidget.append(f'{i.__str__()}')
        else:
            self.textwidget.append(f'{_text.__str__()}')

    ###############################################
    @pyqtSlot(bool)
    def SetClearText(self):
        self.textwidget.clear()

    ###############################################
    # Print the current defined variable(s)
    @pyqtSlot(bool)
    def PrintAllVariablesList(self):
        if not self.totalVariablesName:
            QMessageBox.information(self, "Variable", "No variables defined yet.")
            return
        # Print all the current loaded variables
        self.updateLogViewPort(1, self.theVariablesObject)

    ###############################################
    # Print the current selected variable(s)
    @pyqtSlot(bool)
    def PrintSelectedVariablesList(self):
        if not self.selectedVariableNames:
            QMessageBox.information(self, "Variable", "No variables used yet.")
            return
        if len(self.theVariablesObject) == 0:
            QMessageBox.information(self, "Variable", "No variables defined yet.")
            return
        # Print the current selected variables
        self.updateLogViewPort(1, [v for v in self.theVariablesObject if v.getName() in self.selectedVariableNames])

    ###############################################
    # Print the defined trend(s)
    @pyqtSlot(bool)
    def PrintTrendsList(self):
        if not self.theTrendsList:
            QMessageBox.information(self, "Trend case", "No trend case(s) defined yet.")
            return
        self.updateLogViewPort(2, self.theTrendsList)

    ###############################################
    # Definition of the GSTA variables to use for mean, sorting and skewness
    @pyqtSlot(bool)
    def SetGSTAVariables(self):
        # Verification if previous definition of GSTA variables exist
        theVariableNumber = sum([1 for v in self.theVariablesObject if v.getAlias() in cfg.GSTAVAR])
        if theVariableNumber == 3:
            if QMessageBox.question(self, "GSTA variable definition", "There are still 3 variables defined for GSTA.\nDo you want to defined a set of GSTA variables ?", \
                                    QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
                return
            else:
                # Erase previous definition of GSTA variables
                for v in self.theVariablesObject:
                    v.setAlias(v.getName())
        # Before defined new set of GSTA variables, verify that enough variable are still available
        theVariablesList = [v for v in self.theVariablesObject if not v.getName() in self.selectedVariableNames]
        if len(theVariablesList) < 3:
            QMessageBox.information(self, "GSTA variable definition",
                                    "There are not enough variable available.\n Need "
                                    "at least 3 variables, only {} available.".format(
                                        len(theVariablesList)))
            return
        # Use to fill the variable combobox of the dialog
        tmpVarObjectsList = self.theVariablesObject.copy()
        #self.selectedVariableNames.clear()
        # Open dialog of variables settings for MEAN variable
        dlg = setMSTAVariableOptionDlg(tmpVarObjectsList)
        dlg.setVariableAlias("Mean")
        while True:
            result = dlg.exec()
            if result == QDialog.Accepted:
                newVar = dlg.getVariableDefinition()
                for i,v in enumerate(tmpVarObjectsList):
                    if v.getName() == newVar.getName():
                        del tmpVarObjectsList[i]
                        self.selectedVariableNames.append(newVar.getName())
                for i,v in enumerate(self.theVariablesObject):
                    if v.getName() == newVar.getName():
                        self.theVariablesObject[i] = newVar
                break
            elif result == QDialog.Rejected:
                if QMessageBox.question(self, "Mean variable", "No mean variable selected", \
                                        QMessageBox.Abort|QMessageBox.Retry) == QMessageBox.Abort:
                    return

        # Open dialog of variables settings for SORTING variable
        dlg = setMSTAVariableOptionDlg(tmpVarObjectsList)
        dlg.setVariableAlias("Sorting")
        while True:
            result = dlg.exec()
            if result:
                newVar = dlg.getVariableDefinition()
                for i,v in enumerate(tmpVarObjectsList):
                    if v.getName() == newVar.getName():
                        del tmpVarObjectsList[i]
                        self.selectedVariableNames.append(newVar.getName())
                for i, v in enumerate(self.theVariablesObject):
                    if v.getName() == newVar.getName():
                        self.theVariablesObject[i] = newVar
                break
            elif result == QDialog.Rejected:
                if QMessageBox.question(self, "Sorting variable", "No sorting variable selected", \
                                    QMessageBox.Abort | QMessageBox.Retry) == QMessageBox.Abort:
                    return

        # Open dialog of variables settings for SKEWNESS variable
        dlg = setMSTAVariableOptionDlg(tmpVarObjectsList)
        dlg.setVariableAlias("Skewness")
        while True:
            result = dlg.exec()
            if result:
                newVar = dlg.getVariableDefinition()
                for i,v in enumerate(tmpVarObjectsList):
                    if v.getName() == newVar.getName():
                        del tmpVarObjectsList[i]
                        self.selectedVariableNames.append(newVar.getName())
                for i, v in enumerate(self.theVariablesObject):
                    if v.getName() == newVar.getName():
                        self.theVariablesObject[i] = newVar
                break
            elif result == QDialog.Rejected:
                if QMessageBox.question(self, "Skewness variable", "No skewness variable selected", \
                                    QMessageBox.Abort | QMessageBox.Retry) == QMessageBox.Abort:
                    return

        if len(self.selectedVariableNames) == 3: # Three variables must be selected
            self.updatePointsDB(self.theVariablesObject)  # Update the corresponding variables at each points
            self.updateLogViewPort(5, self.selectedVariableNames)
            # Update menu entries
            self.actionClearSelect.setEnabled(True)
            #self.actionVariableListSelected.setEnabled(True)
            # GSTA variables are defined, trends can be manage
            self.actionSetGSTATrend.setEnabled(True)
            self.actionSetTrend.setEnabled(True)
        else:
            QMessageBox.information(self, "GSTA variable definition", "3 variables must defined for a GSTA analysis\nOnly {} actually defined".format(len(self.selectedVariableNames)))
            #self.selectedVariableNames.clear()
            self.actionClearSelect.setEnabled(False)
            #self.actionVariableListSelected.setEnabled(False)
            # GSTA variables are defined, trends can be manage
            self.actionSetGSTATrend.setEnabled(False)
            self.actionSetTrend.setEnabled(True)

    ###############################################
    @pyqtSlot(bool)
    def ModifyVariables(self):
        # Open dialog of variables settings
        dlg = setMSTAVariableOptionDlg(self.theVariablesObject)
        ok = dlg.exec()
        if ok:
            newVar = dlg.getVariableDefinition()
            # Check if this variable is used in a defined trend case
            for trend in self.theTrendsList:
                for v in trend.getVars():
                    if newVar.getName() == v.getName():
                        QMessageBox.warning(self, "Trend definition", "The variable {} is used in a trend case.\nDelete the corresponding trend case before modifying the variable.".format(v.getName()))
                        return
            # Update the list of the mstaVariable
            for i,v in enumerate(self.theVariablesObject):
                if v.getName() == newVar.getName():
                    self.theVariablesObject[i] = newVar
            self.theVariablesObject = sorted(self.theVariablesObject, key=lambda mstaVariable: mstaVariable.name)
            self.updatePointsDB(self.theVariablesObject)  # Update the corresponding variables at each points
            self.updateLogViewPort(1, "Variable {} has been modified.".format(newVar.getName()))
        return

    ###############################################
    @pyqtSlot(bool)
    def DeleteOneVariable(self):
        if len(self.selectedVariableNames) == 0:
            QMessageBox.information(self, "Selected variable", "No variables selected/used yet\nNothing to delete.")
            return
        # Get the name of the variable to delete from user
        variable, rep = QInputDialog.getItem(self, 'Delete a variable', 'Select a variable',
                                             self.selectedVariableNames,
                                             0, False)
        if rep:
            for vol in self.theVariablesObject:
                if vol.getName() == variable:
                    for tc in self.theTrendsList:
                        for var in tc.getVars():
                            if var.getName() == variable:
                                QMessageBox.information(self, "Delete variable", "variable {} is used in a trend case. Delete according trend case first before deleting {}".fomrat(variable,variable))
                                return
                    if QMessageBox.question(self, "Variable", "Are you sure you want to delete variable {} ?".format(variable)) == QMessageBox.Yes:
                        # Delete the variable name only from selected variable name list, variableObjectsList is not modified
                        del self.selectedVariableNames[self.selectedVariableNames.index(variable)]
                        self.updateLogViewPort(1, "Variable {} has been delete.".format(variable))
                    break

    ###############################################
    # Definition of the trend case(s) for a GSTA analysis
    @pyqtSlot(bool)
    def SetGSTATrendCases(self):
        # Verification that the three needed GSTA variables are sets
        theVariableNumber = sum([1 for v in self.theVariablesObject if v.getAlias() in ["Mean","Sorting","Skewness"]])
        if theVariableNumber < 3:
            QMessageBox.information(self, "GSTA trend definition", "There are not enough variable available.\n Need "
                                                                   "at least 3 variables, only {} set.".format(
                len(theVariableNumber)))
            return
        dlg = setGSTATrendCasesDlg(self.theVariablesObject, self.theTrendsList)
        result = dlg.exec()
        if result:
            if len(dlg.getTrendCases()) > 0:
                self.theTrendsList = dlg.getTrendCases()
                self.selectedVariableNames = dlg.getSelectedMSTAVarnames()
                self.computeMSTA.setEnabled(True)
                return

    ###############################################
    @pyqtSlot(bool)
    def SetMSTATrendCases(self):
        # Construction of the list of variables that are NOT used by GSTA
        theVariablesList = [v for v in self.theVariablesObject if not v.getName() in self.selectedVariableNames]
        # Construction of the list of available variables, i.e. those which are not used yet
        #theVariablesList = [v for v in self.theVariablesObject if not v.getName() in self.selectedVariableNames]
        if len(theVariablesList) == 0:
            QMessageBox.information(self, "MSTA trend definition", "All variables are used.\n \
                                                      Delete one or more trends to release variables.")
            return
        dlg = setMSTATrendCasesDlg(theVariablesList, self.theTrendsList) # Variable definition is the same for all points
        result = dlg.exec()
        if result:
            if len(dlg.getTrendCases()) > 0:
                self.theTrendsList = dlg.getTrendCases()
                self.selectedVariableNames = dlg.getSelectedMSTAVarnames()
                self.computeMSTA.setEnabled(True)
                return

    ###############################################
    @pyqtSlot(bool)
    def DeleteTrends(self):
        if len(self.theTrendsList) == 0:
            QMessageBox.information(self, "Trend case(s)", "No trend case(s) defined yet.")
            return
        delDlg = DeleteTrendCaseDlg(self.theTrendsList)
        if not delDlg.exec():
            return
        newTrendList = delDlg.GetTrendCaseList()
        deletedElementList = list()
        if len(newTrendList) > 0:
            for tc in self.theTrendsList:
                if not tc.getID() in [ntc.getID() for ntc in newTrendList]:
                    deletedElementList.append(tc) # Construction of list of deleted trend case
        else:
            self.theTrendsList = list()
            return
        if len(deletedElementList) > 0:
            if self.theExpressionObject.getTrendCount() > 0: # If an expression was previously defined
                for dtc in deletedElementList:
                    if dtc.getID() in self.theExpressionObject.getFlatTrendIDList(): # Check if one of the deleted trend case is present in the expression
                        if QMessageBox.question(self, "Delete trend",
                                                "Trend case ({}) is present in global expression to apply.\n If you continue, global expression will be erased.\n Do you want to continue ?".format(dtc.__str__())) \
                                == QMessageBox.Yes:
                            self.theExpressionObject = mstaComposedTrendCase()
                            self.theTrendsList = newTrendList
            else:
                self.theTrendsList = newTrendList
        return

    ###############################################
    @pyqtSlot(bool)
    def ExpressionBuild(self):
        if len(self.theTrendsList) == 0:
            QMessageBox.information(self, "Trend case", "No trend case(s) defined yet.")
            return
        dlg = SetMSTAExpressionDlg(self.theTrendsList, self.theExpressionObject)
        result = dlg.exec_()
        if result:
            self.theExpressionObject = dlg.GetMSTAExpressionTrendCase()

    ###############################################
    @pyqtSlot(bool)
    def ExpressionDelete(self):
        if self.theExpressionObject.getTrendCount() == 0:
            QMessageBox.information(self, "Trend case", "No expression defined yet.\nNothing to delete")
            return
        if not QMessageBox.question(self, "Delete current expression",
                                    "Do you realy want to delete current expression\n{}".format(
                                            self.theExpressionObject.__str__())):
            return
        self.theExpressionObject = mstaComposedTrendCase()

    ###############################################
    @pyqtSlot(bool)
    def ExpressionList(self):
        if self.theExpressionObject.getTrendCount() == 0:
            QMessageBox.information(self, "List expression", "No expression defined yet.\nNothing to print.")
            return
        self.updateLogViewPort(2, self.theExpressionObject.__str__())

    ###############################################
    @pyqtSlot(bool)
    def BarrierLayers(self):
        dlg = SelectBarrierLayerDlg(self.iface.mapCanvas(), self.barrierListLayers)
        result = dlg.exec_()
        if result:
            self.barrierListLayers = dlg.GetBarrierLIst()
    ###############################################
    @pyqtSlot(bool)
    def ViewDataSet(self):
        if len(self.points) == 0:
            QMessageBox.information(self, "Data set", "Load a data set before.\nNothing to view.")
            return
        dlg = ViewDataBaseDlg(self.points)
        result = dlg.exec_()

    ###############################################
    @pyqtSlot(bool)
    def ComputeMSTA(self):
        assert len(self.theTrendsList) > 0 # Must have at least one trend to study
        assert len(self.theVariablesObject) > 0 # Must have at least one variable in the current selected list
        assert self.temporaryLayer # Check the temporary layer is set

        if self.theExpressionObject.getTrendCount() == 0:
            QMessageBox.information(self, "Expression", "No expression defined yet.\nMust be set before computing any trend.")
            return

        # Get list of the unique variables used
        totalVarsList = self.theExpressionObject.getVars() # All variables in flatten list, but with multiple
        varsListName = [totalVarsList[0].getName()] # The first variable
        varsList = [totalVarsList[0]]               # and it's name
        for v in totalVarsList:
            if not v.getName() in varsListName: # If the current variable name not in the list
                varsListName.append(v.getName())
                varsList.append(v)      # Add the variable to the result list
        del totalVarsList, varsListName # No more use of temporary lists

        #outf = open("Results-MSTA.txt", 'w')

        # Definition of a progress bar to show computation progression
        progress = QProgressDialog("Computation in progress...", "Cancel", 0, len(self.points), self)
        progress.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        progress.setModal(True)
        progress.setMinimumDuration(0)
        # progress.setCancelButton(None)  # Remove the cancel button.
        pbCount = 0

        self.updateLogViewPort(999, "Start cumputation...")
        self.temporaryLayer.startEditing()
        # Declaration of the dictionary which will containt variable name as key and surrounding point IDs
        surroundingWorkingDict = dict()
        # Loop over the points of the temporary layer
        for point in self.points:
            #outf.write("\n\nPoint ID: {}".format(point.getID()))
            for v in varsList:
                nbPoints = v.GetNeiborhoodPoints(self.temporaryLayer, point, self.points)
                # Continue if no neiboring points
                if len(nbPoints) == 0:
                    continue
                pointsToRemoved = list()
                # eventually deselect points which cross barrier layer(s)
                for barrier in self.barrierListLayers:
                    # Select in the bounding box of the self.temporaryLayer to restrict the list of features to look at
                    barrier.selectByRect(self.temporaryLayer.extent())
                    for nbp in nbPoints:
                        line = QgsFeature()
                        line.setGeometry(QgsLineString([point, nbp]))
                        for f in barrier.selectedFeatures():
                            if line.geometry().crosses(f.geometry()):
                                pointsToRemoved.append(nbp.getID())
                    barrier.removeSelection()
                results = mstaResults(v.getName)
                results.SetNeighborList([rp for rp in nbPoints if not rp.getID() in pointsToRemoved])
                # store the surrounding points in a dictionnary (keys are variable names)
                surroundingWorkingDict[v.getName] = results
            # Apply expression for each central point (point) and store results
            count = 0
            for varname in surroundingWorkingDict:
                count = 0
                result = surroundingWorkingDict[varname]
                for nbp in result.GetNeighborList():
                    if self.theExpressionObject.result(point, nbp):
                        # Expression is True between central point and neighbor -> save vector components
                        # it just add the new value to a list
                        D = np.sqrt(point.distanceSquared(nbp))
                        E = np.cos(np.radians(point.azimuth(nbp))) * (1.0 / D)
                        N = np.sin(np.radians(point.azimuth(nbp))) * (1.0 / D)
                        result.SetDistance(D)
                        result.SetEasting(E)
                        result.SetNorthing(N)
                        count += 1
                # Storage of the number of neighbor points for which trend is True
                result.SetUsedNeighbor(count)
                #outf.write(result.__repr__())

            distance = 0.0
            direction = 0.0
            for varname in surroundingWorkingDict:
                distance = surroundingWorkingDict[varname].GetDistance() # Get total distance of vectors as if they were aligned
                if distance != 0:
                    N = surroundingWorkingDict[varname].GetNorthing() # Get sum of northing values
                    E = surroundingWorkingDict[varname].GetEasting()  # get sum of easting values
                    direction = np.rad2deg(np.arctan2(N, E))

            pf = self.temporaryLayer.getFeature(point.getID())
            pf["Angle"] = float(direction)
            pf["Module"] = float(distance)
            pf["Trends"] = "{}".format(self.theExpressionObject)
            pf["Comments"] = "Neighbor count : {}".format(surroundingWorkingDict[varname].GetUsedNeighbor())
            self.temporaryLayer.updateFeature(pf)

            # Update the progress bar
            pbCount += 1
            progress.setValue(pbCount)
            if progress.wasCanceled():
                break

        progress.close()
        #outf.close()
        self.temporaryLayer.commitChanges()
        self.updateLogViewPort(999, "Computation ended.\nResults are in the temporary layer attributs table")
            # TODO:
            # 1 - construction the ellipse/circle for each variable -> DONE
            # 2 - select all points inside the ellipse/circle for each variable -> DONE
            # 3 - deselect the current central point (working point) -> DONE
            # 4 - deselect eventually points which cross selected barrier layer(s) -> DONE
            # 5 - apply the expression corresponding to each trend case/variables involved -> DONE
            # 6 - compute vector component E and N taking into account computation settings -> DONE

        return

    def norm(_dataset):
        if isinstance(_dataset, list):
            norm_list = list()
            min_value = min(_dataset)
            max_value = max(_dataset)
            for value in _dataset:
                tmp = (value - min_value) / (max_value - min_value)
                norm_list.append(tmp)
        return norm_list