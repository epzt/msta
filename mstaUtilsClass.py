# -*- coding: utf-8 -*-
"""
/***************************************************************************
 msta
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

from PyQt5.QtWidgets import  QMessageBox, QDialog, QInputDialog, QCheckBox, QGroupBox, QVBoxLayout, QGridLayout, QDialogButtonBox
from PyQt5.QtCore import QObject, pyqtSlot
import itertools as it

#from .ui_about_msta import Ui_AboutDlg
from .ui_set_gsta_variables_dialog import Ui_setGSTAVariablesDialog as setGSTAVarDlg
from .ui_gsta_trend_definition import Ui_setGSTATrendCaseDialog as setGSTATrendDlg
from .ui_msta_variable_definition import Ui_SetMSTAVarOptionsDlg as setMSTAVariableDlg
from .ui_msta_trend_definition import Ui_mstaTrendDefinitionDialog as setMSTATrendDlg
from .ui_msta_expression_builder_dialog import Ui_mstaExpressionBuilderDlg as setMSTAExpressionDlg

from .mstaCoreClass import mstaTrendCase, mstaComposedTrendCase, mstaVariable, mstaOperand

from . import config as cfg

#############################################################################
# Just a class to print About information
#############################################################################
# class aboutMSTA(QDialog, Ui_AboutDlg):
#    def __int__(self, parent=None):
#        super(aboutMSTA,self).__init__(parent)
#        self.setupUi(self)

#############################################################################
# GSTA variables definition from global variable list
#############################################################################
class setGSTAVariablesDlg(QDialog, setGSTAVarDlg):
    def __init__(self, _variablesList, parent=None):
        super(setGSTAVariablesDlg,self).__init__(parent)
        self.setupUi(self)

        self.meanComboBox.addItem('Choose a variable...')
        self.sortingComboBox.addItem('Choose a variable...')
        self.skewnessComboBox.addItem('Choose a variable...')
        # fill comboboxes with variables' names
        self.meanComboBox.addItems(_variablesList)
        self.sortingComboBox.addItems(_variablesList)
        self.skewnessComboBox.addItems(_variablesList)

        # currentTextChanged
        self.meanComboBox.activated.connect(self.getMean)
        self.sortingComboBox.activated.connect(self.getSorting)
        self.skewnessComboBox.activated.connect(self.getSkewness)

        # Initialisations
        self.items = _variablesList  # List of variable names
        self.variablesDefinition = [] # List of variable definitions (list of class mstaVariable)

    def getVariableDefinitionNames(self):
        return [v.getName() for v in self.variablesDefinition]

    def getVariableDefinitionAlias(self):
        return [v.getAlias() for v in self.variablesDefinition]

    def isVariableSet(self, _vname):
        return _vname in self.getVariableDefinitionNames()

    def isAliasSet(self, _valias):
        return _valias in self.getVariableDefinitionAlias()

    def getVariableDefinitionNameIndex(self, _vname):
        return self.getVariableDefinitionNames().index(_vname)

    def getVariableDefinitionAliasIndex(self, _vname):
        return self.getVariableDefinitionAlias().index(_vname)

    @pyqtSlot(int)
    def getMean(self, _index):
        item = self.meanComboBox.itemText(_index)
        if item == 'Choose a variable...' and self.isAliasSet('Mean'):
            varIndex = self.getVariableDefinitionAliasIndex('Mean')
            del self.variablesDefinition[varIndex]
            #return
        if self.isVariableSet(item):
            msg = "Variable {} is already used for {} parameter.\nDo you want to erase previous definition.".format(
                item, self.getVariableDefinitionAliasIndex(item))
            if QMessageBox.question(self, "GSTA Variables", msg) == QMessageBox.Yes:
                varIndex = self.getVariableDefinitionAliasIndex(item)
                del self.variablesDefinition[varIndex]

        #key = list(self.variablesDict.keys())[list(self.variablesDict.values()).index(item)]

        # Launch the dialog box of variable options definition
        variableDlg = setMSTAVariableOptionDlg(item)
        result = variableDlg.exec_()
        if not result:
            msg = "Mean variable not set."
            QMessageBox.information(self, "GSTA Variables", msg)
            return
        # Even if in variableDlg no definition is set for the mean variable, it is set to default values
        newVar = variableDlg.getVariableDefinition()
        # This is to force alias to have "Mean" value
        newVar.setAlias("Mean")
        self.variablesDefinition.append(newVar)

    @pyqtSlot(int)
    def getSorting(self, _index):
        item = self.sortingComboBox.itemText(_index)
        if item == 'Choose a variable...' and self.isAliasSet('Sorting'):
            varIndex = self.getVariableDefinitionAliasIndex('Sorting')
            del self.variablesDefinition[varIndex]
            #return
        if self.isVariableSet(item):
            msg = "Variable {} is already used for {} parameter.\nDo you want to erase previous definition.".format(
                item, self.getVariableDefinitionAliasIndex(item))
            if QMessageBox.question(self, "GSTA Variables", msg) == QMessageBox.Yes:
                varIndex = self.getVariableDefinitionAliasIndex(item)
                del self.variablesDefinition[varIndex]

        # Launch the dialog box of variable options definition
        variableDlg = setMSTAVariableOptionDlg(item)
        result = variableDlg.exec_()
        if not result:
            msg = "Sorting variable not set."
            QMessageBox.information(self, "GSTA Variables", msg)
            return
        # Even if in variableDlg no definition is set for the mean variable, it is set to default values
        newVar = variableDlg.getVariableDefinition()
        # This is to force alias to have "Sorting" value
        newVar.setAlias("Sorting")
        self.variablesDefinition.append(newVar)

    @pyqtSlot(int)
    def getSkewness(self, _index):
        item = self.skewnessComboBox.itemText(_index)
        if item == 'Choose a variable...' and self.isAliasSet('Skewness'):
            varIndex = self.getVariableDefinitionAliasIndex('Skewness')
            del self.variablesDefinition[varIndex]
            #return
        if self.isVariableSet(item):
            msg = "Variable {} is already used for {} parameter.\nDo you want to erase previous definition.".format(
                item, self.getVariableDefinitionAliasIndex(item))
            if QMessageBox.question(self, "GSTA Variables", msg) == QMessageBox.Yes:
                varIndex = self.getVariableDefinitionAliasIndex(item)
                del self.variablesDefinition[varIndex]

        # Launch the dialog box of variable options definition
        variableDlg = setMSTAVariableOptionDlg(item)
        result = variableDlg.exec_()
        if not result:
            msg = "Skewness variable not set."
            QMessageBox.information(self, "GSTA Variables", msg)
            return
        # Even if in variableDlg no definition is set for the mean variable, it is set to default values
        newVar = variableDlg.getVariableDefinition()
        # This is to force alias to have "Skewness" value
        newVar.setAlias("Skewness")
        self.variablesDefinition.append(newVar)

    def areAllGSTAVariablesSet(self):
        retValue  = False
        if self.getMeanVariableName() and self.getSortingVariableName() and self.getSkewnessVariableName():
            retValue = True
        return retValue

    def getMeanVariableName(self):
        try:
            id = self.getVariableDefinitionAliasIndex('Mean')
            return self.variablesDefinition[id]
        except:
            return ''

    def getSortingVariableName(self):
        try:
            id = self.getVariableDefinitionAliasIndex('Sorting')
            return self.variablesDefinition[id]
        except:
            return ''

    def getSkewnessVariableName(self):
        try:
            id = self.getVariableDefinitionAliasIndex('Skewness')
            return self.variablesDefinition[id]
        except:
            return ''

    def getGSTAVariablesDefinitions(self):
        return(self.variablesDefinition)

#############################################################################
# GSTA trend definition
#############################################################################
class setGSTATrendCasesDlg(QDialog, setGSTATrendDlg):
    def __init__(self, _variables, _trends, parent=None):
        super(setGSTATrendCasesDlg,self).__init__(parent)
        self.setupUi(self)
        # _variables should be a list of three mstaVariable objects
        assert isinstance(_variables, list) and len(_variables) >= 3
        assert isinstance(_variables[0], mstaVariable)
        # _trends must be of type mstaComposedTrendCase
        #assert isinstance(_trends, mstaComposedTrendCase)
        assert isinstance(_trends, list)
        # Assignements
        self.variables = _variables
        self.mainTrends = _trends  # mstaComposedTrendCase object(s)
        # Initial variables
        self.meanTrend = None
        self.sortingTrend = None
        self.skewnessTrend = None

        # In case there is/are trend(s) defined, set default operand
        #if self.mainTrends.getTrendCount() > 0:
        if len(self.mainTrends) > 0:
            self.linkOperand = cfg.OPERAND['et'] # Default operand to link multiple GSTA trend case
            self.linkOperandComboBox.setCurrentText(cfg.OPERAND['et'])
            self.linkOperandComboBox.setEnabled(True)
        else:
            self.linkOperand = cfg.OPERAND['none'] # No operand yet
            self.linkOperandComboBox.setCurrentText(cfg.OPERAND['none'])
            self.linkOperandComboBox.setEnabled(False)

        self.buttonAddGSTATrendCase.clicked.connect(self.addTrendCase)
        self.buttonRemoveGSTATrendCase.clicked.connect(self.removeGSTATrendCase)

        self.radioGSTAMeanFiner.toggled.connect(self.setMeanTrend)
        self.radioGSTAMeanCoarser.toggled.connect(self.setMeanTrend)
        self.radioGSTAMeanNone.toggled.connect(self.setMeanTrend)
        self.radioGSTASortingBetter.toggled.connect(self.setSortingTrend)
        self.radioGSTASortingPorer.toggled.connect(self.setSortingTrend)
        self.radioGSTASortingNone.toggled.connect(self.setSortingTrend)
        self.radioGSTASkewnessPlus.toggled.connect(self.setSkewnessTrend)
        self.radioGSTASkewnessMinus.toggled.connect(self.setSkewnessTrend)
        self.radioGSTASkewnessNone.toggled.connect(self.setSkewnessTrend)
        self.linkOperandComboBox.currentTextChanged.connect(self.currentTextChanged)

        self.updateGSTATrendCasesText(self.mainTrends)

    ###############################################
    @pyqtSlot(bool)
    def setMeanTrend(self):
        self.meanTrend =  mstaTrendCase(self.getNameFromVariableList(self.variables, "Mean"), "none")
        if self.radioGSTAMeanFiner.isChecked():
            if self.meanTrend.getLeftVar().isMetric():
                self.meanTrend.setComp("sup")
            else:
                self.meanTrend.setComp("inf")
        elif self.radioGSTAMeanCoarser.isChecked():
            if self.meanTrend.getLeftVar().isMetric():
                self.meanTrend.setComp("inf")
            else:
                self.meanTrend.setComp("sup")
        else:
            self.meanTrend = None

    ###############################################
    @pyqtSlot(bool)
    def setSortingTrend(self):
        self.sortingTrend = mstaTrendCase(self.getNameFromVariableList(self.variables, "Sorting"), "none")
        if self.radioGSTASortingBetter.isChecked():
            self.sortingTrend.setComp("sup")
        elif self.radioGSTASortingPorer.isChecked():
            self.sortingTrend.setComp("inf")
        else:
            self.sortingTrend = None

    ###############################################
    @pyqtSlot(bool)
    def setSkewnessTrend(self):
        self.skewnessTrend = mstaTrendCase(self.getNameFromVariableList(self.variables, "Skewness"), "none")
        if self.radioGSTASkewnessPlus.isChecked():
            if self.skewnessTrend.getLeftVar().isMetric():
                self.skewnessTrend.setComp("sup")
            else:
                self.skewnessTrend.setComp("inf")
        elif self.radioGSTASkewnessMinus.isChecked():
            if self.skewnessTrend.getLeftVar().isMetric():
                self.skewnessTrend.setComp("inf")
            else:
                self.skewnessTrend.setComp("sup")
        else:
            self.skewnessTrend = None

    ###############################################
    # Add the new trend case to the main object
    @pyqtSlot(bool)
    def addTrendCase(self):
        # Two cases must defined at least to defined a new operand
        cList = [i for i in [self.meanTrend, self.sortingTrend, self.skewnessTrend] if i]
        # A GSTA trend inside a case is always linked by an AND operator
        if len(cList) == 2: # New combined trend case to add
            newCombinedTC = mstaComposedTrendCase(cList, \
                            [mstaOperand(cfg.OPERAND['et'], cList[0].getID(), cList[1].getID(), 0)])
        elif len(cList) == 3:
            newCombinedTC = mstaComposedTrendCase(cList, \
                            [mstaOperand(cfg.OPERAND['et'], cList[0].getID(), cList[1].getID(), 0), \
                             mstaOperand(cfg.OPERAND['et'], cList[1].getID(), cList[2].getID(), 0)])
        elif len(cList) == 1:
            newCombinedTC = mstaComposedTrendCase(cList[0])
        else:
            return # Nothing to create
        newCombinedTC.setComposedGSTATrend(True)  # It is a GSTA trend !! IMPORTANT TO SET IT AT TRUE
        #for tc in self.mainTrends.getTrend():
        for tc in self.mainTrends:
            if tc.isGSTATrend() and tc == newCombinedTC:  # Test if it is a GSTA trend
                return # The new GSTA trend was previously defined
        #self.mainTrends.addTrendCase(newCombinedTC, self.linkOperand)  # New GSTA trend case is added to the global object
        self.mainTrends.append(newCombinedTC)  # New GSTA trend case is added to the global object
        self.linkOperand = cfg.OPERAND['et'] # Default operand to link multiple GSTA trend case
        self.linkOperandComboBox.setCurrentText(cfg.OPERAND['et'])
        self.linkOperandComboBox.setEnabled(True)
        self.updateGSTATrendCasesText(self.mainTrends)
        return

    ###############################################
    # Remove the current trend case to the main object
    @pyqtSlot(bool)
    def removeGSTATrendCase(self):
        # Current combined trend case object to remove
        currentCombinedTC = mstaComposedTrendCase([self.meanTrend, self.sortingTrend, self.skewnessTrend], cfg.OPERAND['et'])
        currentCombinedTC.setComposedGSTATrend(True)
        #for tc in self.mainTrends.getTrend():
        for tc in self.mainTrends:
            if tc.isGSTATrend():  # Test if it is a GSTA trend
                if tc == currentCombinedTC:  # The current GSTA trend is defined
                    self.mainTrends.remove(tc)  # The GSTA trend case is deleted of the global object
        #if self.mainTrends.getTrendCount() <= 0:
        if len(self.mainTrends) == 0:
            self.linkOperandComboBox.setEnabled(False)
        self.updateGSTATrendCasesText(self.mainTrends)
        return

    ###############################################
    '''
    def updateGSTATrendCases(self, _newTC):
        assert isinstance(_newTC, list)
        # New combined trend case object to add
        newCombinedTC = mstaComposedTrendCase(_newTC, cfg.OPERAND['et'])
        newCombinedTC.setComposedGSTATrend(True)  # It is a GSTA trend !! IMPORTANT TO SET IT AT TRUE
        for tc in self.mainTrends.getTrend():
            if tc.isGSTATrend(): # Test if it is a GSTA trend
                if tc == newCombinedTC: # The new GSTA trend is defined
                    return
        self.mainTrends.addTrendCase(newCombinedTC, '') # New GSTA trend case is added to the global list
        return
    '''
    ###############################################
    def updateGSTATrendCasesText(self, _theTrendCase):
        # Erase all previous text
        self.TrendCaseTextEdit.clear()
        # If no trends defined-> nothing to do
        #if _theTrendCase.getTrendCount() == 0:
        if len(_theTrendCase) == 0:
            return
        # Construction of the text
        textCasesTrend = ""
        #for tc in _theTrendCase.getTrend():
        for tc in _theTrendCase:
            if tc.isGSTATrend():
                textCasesTrend += tc.getGSTATrendText()
            else:
                textCasesTrend += (tc.__str__() + '\n')
        textCasesTrend += '\n'
        # Print the text in the widget
        self.TrendCaseTextEdit.setText(textCasesTrend)
        return

    ###############################################
    def getGSTATrendCaseListNames(self):
        #if self.mainTrends.getTrendCount() > 0:
        if len(self.mainTrends) > 0:
            return [t.__str__() for t in self.mainTrends]
        else:
            return list()

    ###############################################
    def getTrendCases(self):
        # TODO: mettre à jour la liste des variables utilisées et la renvoyer
        return self.mainTrends

    ###############################################
    @pyqtSlot('const QString')
    def currentTextChanged(self, _text):
        self.linkOperand = _text

    ###############################################
    def getNameFromVariableList(self, _varList, _name):
        assert isinstance(_varList, list)
        for v in _varList:
            if v.getAlias() == _name:
                return v

    ###############################################
    def getSelectedMSTAVarnames(self):
        retValue = list()
        for tc in self.mainTrends:
            for vtc in list(it.chain(*tc.getVars())): # Flatten the list of list in a list
                retValue.append(vtc.getName())
        return list(set(retValue)) # Allows to have unique element in the returned list

#############################################################################
# MSTA variable definition
#############################################################################
class setMSTAVariableOptionDlg(QDialog, setMSTAVariableDlg):
    def __init__(self, _variables, parent=None):
        super(setMSTAVariableOptionDlg, self).__init__(parent)
        self.setupUi(self)
        # Default unit
        self.unit = "%"
        self.aliasForced = False
        self.nameChanged = False
        self.variablesObjectsList = _variables  # List of all the variables defined
        self.variableNameComboBox.addItem("Choose a variable...")
        self.variableNameComboBox.addItems([v.getName() for v in self.variablesObjectsList])

        # Initialisation from previous variable
        self.variableDgLineEdit.setText("0.0")
        self.pmVariableRangeLineEdit.setText("0.0")
        self.directionVariableLineEdit.setText("0.0")
        self.tolangVariableLineEdit.setText("0.0")
        self.variableUnitComboBox.setCurrentText(self.unit)

        # Connection définition
        self.variableUnitComboBox.currentTextChanged.connect(self.currentUnitChanged)
        self.variableNameComboBox.currentTextChanged.connect(self.variableNameChange)
        # Handle default Ok message
        self.buttonBox.accepted.connect(self.okBoutonGroupClicked)

    # Handle the ok button signal to verify that a variable name has been defined/chosen
    @pyqtSlot()
    def okBoutonGroupClicked(self):
        if self.variableNameComboBox.currentText() == "Choose a variable...":
            QDialog.reject(self)  # Quit the dialog as a Cancel operation
        else:
            QDialog.accept(self)

    @pyqtSlot('const QString')
    def currentUnitChanged(self, _unit):
        if _unit in cfg.UNIT.values():
            self.unit = _unit
            self.variableUnitComboBox.setCurrentIndex(self.variableUnitComboBox.findText(_unit))

    # Update fields of the dialog in case variable name change
    @pyqtSlot('const QString')
    def variableNameChange(self, _name):
        for v in self.variablesObjectsList:
            if v.getName() == _name:
                self.currentUnitChanged(v.getUnit())
                if not self.aliasForced:
                    self.variableAliasLineEdit.setText(v.getAlias())
                self.setVariableDg(v.getDg())
                self.setVariableRange(v.getRange())
                self.setVariableAnysotropyDirection(v.getDirection())
                self.setVariableAnysotropyToAngle(v.getTolerance())
                self.nameChanged = True
                return

    def getVariableDefinition(self):
        newvar = mstaVariable()
        newvar.setName(self.getVariableName())
        newvar.setAlias(self.getVariableAlias())
        newvar.setUnit(self.getVariableUnit())
        newvar.setDg(self.getVariableDg())
        newvar.setRange(self.getVariableRange())
        newvar.setSearch(self.getVariableAnysotropyDirection(), self.getVariableAnysotropyTolangle())
        return newvar

    def getVariableName(self):
        return self.variableNameComboBox.currentText()

    def getVariableAlias(self):
        return self.variableAliasLineEdit.text()

    def setVariableAlias(self, _alias):
        self.variableAliasLineEdit.setText(_alias)
        self.aliasForced = True

    def getVariableUnit(self):
        return self.unit

    def getVariableDg(self):
        return float(self.variableDgLineEdit.text())

    def setVariableDg(self, _dg):
        self.variableDgLineEdit.setText(str(_dg))

    def getVariableRange(self):
        return float(self.pmVariableRangeLineEdit.text())

    def setVariableRange(self, _range):
        self.pmVariableRangeLineEdit.setText(str(_range))

    def getVariableAnysotropyDirection(self):
        return float(self.directionVariableLineEdit.text())

    def setVariableAnysotropyDirection(self, _anisotropy):
        self.directionVariableLineEdit.setText(str(_anisotropy))

    def getVariableAnysotropyTolangle(self):
        return float(self.tolangVariableLineEdit.text())

    def setVariableAnysotropyToAngle(self, _angle):
        self.tolangVariableLineEdit.setText(str(_angle))

#############################################################################
# MSTA trend definition
#############################################################################
class setMSTATrendCasesDlg(QDialog, setMSTATrendDlg):
    def __init__(self, _variables, _trends, parent=None):
        super(setMSTATrendCasesDlg, self).__init__(parent)
        self.setupUi(self)
        # _variables should be a list of mstaVariable objects
        assert isinstance(_variables, list)
        assert isinstance(_variables[0], mstaVariable)
        # _trends must be of type mstaComposedTrendCase
        #assert isinstance(_trends, mstaComposedTrendCase)
        assert isinstance(_trends, list)
        # Construct the variable names list
        self.varObjectsList = _variables.copy()
        self.varNames = [v.getName() for v in self.varObjectsList]
        # Composed trend case object (contains all the other case)
        self.mainTrends = _trends
        # Update the text of defined trend cases
        self.updateMSTATrendCaseText(self.mainTrends)

        # Initialisations
        # Lists of comboboxes
        self.variableAComboBox.addItems(self.varNames)
        self.variableBComboBox.addItems(self.varNames)
        self.variableAName = self.variableAComboBox.currentText()
        self.variableBName = self.variableBComboBox.currentText()
        self.signType = self.comparatorComboBox.currentText()
        self.linkOperand = self.linkOperandComboBox.currentText()

        self.clearPushButton.clicked.connect(self.ClearTrendListLabel)
        self.addPushButton.clicked.connect(self.addTrendCase)
        self.deletePushButton.clicked.connect(self.deleteTrendCase)
        self.variableAComboBox.currentTextChanged.connect(self.currentVariableATextChanged)
        self.variableBComboBox.currentTextChanged.connect(self.currentVariableBTextChanged)
        self.comparatorComboBox.currentTextChanged.connect(self.currentSignTextChanged)
        self.linkOperandComboBox.currentTextChanged.connect(self.currentLinkOperandChanged)

    def getComp(self, _sign):
        assert _sign in cfg.COMP.values()
        return list(cfg.COMP.keys())[list(cfg.COMP.values()).index(_sign)]

    @pyqtSlot(bool)
    def ClearTrendListLabel(self):
        msg = 'Are you sure you want delete all trends ?'
        if QMessageBox.information(self, "MSTA Variables", msg, QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return
        self.trendCaseTextEdit.clear()
        #self.mainTrends = mstaComposedTrendCase()
        self.mainTrends = list()
        return

    @pyqtSlot(bool)
    def addTrendCase(self):
        # Two different variables can be mix only of they have same Dg or (direction, tolerance) and unit
        varA = self.varObjectsList[self.variableAComboBox.currentIndex()]
        varB = self.varObjectsList[self.variableBComboBox.currentIndex()]
        if not varA.isEqual(varB):
            QMessageBox.warning(self, "Trend definition error",
                                "Can\'t mix two variables with different characteristic distance, research angle or tolerance value:\n \
                                {}\n{}".format(varA.__repr__(), varB.__repr__()))
            return

        # Create a simple trend case
        if self.variableAName != self.variableBName: # In case varA is different to varB
            simpleCase = mstaTrendCase([varA, varB], self.getComp(self.signType))
        else:
            simpleCase = mstaTrendCase(varA, self.getComp(self.signType))
        # Create the new composed trend case to add to the list
        if self.linkOperand == cfg.OPERAND['none']:
            newTrendCase = mstaComposedTrendCase(simpleCase)
        else:
            newTrendCase = mstaComposedTrendCase(simpleCase, self.linkOperand)
        newTrendCase.setComposedGSTATrend(False)
        #for tc in self.mainTrends.getTrend():
        for tc in self.mainTrends:
            if tc == newTrendCase:
                return
        # An operand must be set when adding more than one trend
        #if self.mainTrends.getTrendCount() > 0 and self.linkOperand == cfg.OPERAND['none']:
        if len(self.mainTrends) > 0 and self.linkOperand == cfg.OPERAND['none']:
            QMessageBox.warning(self, "Trend definition error", \
                                "Two successive trends must be link with an operand\n \
                                Actual selected: {}\n".format(self.linkOperand))
            return
        # Add the new composed trend case to the global list
        #self.mainTrends.addTrendCase(newTrendCase, self.linkOperand)
        self.mainTrends.append(newTrendCase)
        # Update the text of defined trend cases
        self.updateMSTATrendCaseText(self.mainTrends)
        return

    @pyqtSlot(bool)
    def deleteTrendCase(self):
        varA = self.varObjectsList[self.variableAComboBox.currentIndex()]
        varB = self.varObjectsList[self.variableBComboBox.currentIndex()]
        # Create the current trend case
        if self.variableAName != self.variableBName:  # In case varA is different to varB
            simpleCase = mstaTrendCase([varA, varB], self.getComp(self.signType))
        else:
            simpleCase = mstaTrendCase(varA, self.getComp(self.signType))
        # Create composed trend case to delete from the list
        trendCaseToDelete = mstaComposedTrendCase(simpleCase, self.linkOperand)
        #for t in self.mainTrends.getTrend():
        for tc in self.mainTrends:
            if tc == trendCaseToDelete:
                self.mainTrends.remove(tc)
        # Update the text of defined trend cases
        self.updateMSTATrendCaseText(self.mainTrends)
        return

    def updateMSTATrendCaseText(self, _theTrendCase):
        # Erase all previous text
        self.trendCaseTextEdit.clear()
        # Construction of the text
        textCasesTrend = ""
        #for tc in _theTrendCase.getTrend():
        for tc in _theTrendCase:
            if tc.isGSTATrend():
                textCasesTrend += tc.getGSTATrendText()
            else:
                textCasesTrend += (tc.__str__() + '\n')
        textCasesTrend += '\n'
        # Print the text in the widget
        self.trendCaseTextEdit.setText(textCasesTrend)
        return

    @pyqtSlot('const QString')
    def currentVariableATextChanged(self, _str):
        self.variableAName = _str
        self.variableBComboBox.setCurrentIndex(self.variableAComboBox.currentIndex())
        return

    @pyqtSlot('const QString')
    def currentVariableBTextChanged(self, _str):
        self.variableBName = _str
        return

    @pyqtSlot('const QString')
    def currentSignTextChanged(self, _str):
        self.signType = _str
        return

    @pyqtSlot('const QString')
    def currentLinkOperandChanged(self, _str):
        self.linkOperand = _str
        return

    def getSelectedMSTAVarnames(self):
        retValue = list()
        for tc in self.mainTrends:
            for vtc in list(it.chain(*tc.getVars())): # Flatten the list of list in a list
                retValue.append(vtc.getName())
        return list(set(retValue)) # Allows to have unique element in the returned list

    def getTrendCases(self):
        return self.mainTrends #, usedVariables

#############################################################################
# Variable selection dialog
#############################################################################
class setSelectedVariablesDlg(QDialog):
    def __init__(self, _variablesList, _currentSelectedList):
        super().__init__()
        self.vars = _variablesList
        self.selVars = _currentSelectedList
        self.varCheckBoxList = []
        self.buttonBox = QDialogButtonBox(self)
        self.windowLayout = QVBoxLayout()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(self.accept)
        self.initUI()
        return

    def initUI(self):
        self.setWindowTitle("Selected variables")
        self.horizontalGroupBox = QGroupBox("Variables")
        self.layout = QGridLayout()
        self.layout.setColumnStretch(0,1)
        i = 0
        if len(self.selVars) > 0:
            for v in self.vars:
                cb = QCheckBox(v.getName())
                self.layout.addWidget(cb, i, 0)
                if v.getName() in self.selVars:
                    cb.setChecked(True)
                    self.varCheckBoxList.append(cb)
                i += 1
        else:
            for v in self.vars:
                cb = QCheckBox(v.getName())
                self.layout.addWidget(cb, i, 0)
                i += 1
                self.varCheckBoxList.append(cb)
        self.horizontalGroupBox.setLayout(self.layout)
        self.windowLayout.addWidget(self.horizontalGroupBox)
        self.windowLayout.addWidget(self.buttonBox)
        self.setLayout(self.windowLayout)

    def getSelectedVariables(self):
        retValue = []
        for i in range(self.layout.count()):
            if self.layout.itemAt(i).widget().isChecked():
                retValue.append(self.layout.itemAt(i).widget().text())
        return retValue


#############################################################################
# MSTA trend definition
#############################################################################
class setMSTAExpressionBuilderDlg(QDialog, setMSTAExpressionDlg):
    def __init__(self, _trendsList, _mainTrend, parent=None):
        super(setMSTAExpressionBuilderDlg, self).__init__(parent)
        self.setupUi(self)
        # _trends should not be empty here
        assert len(_trendsList) > 0
        # all defined trends are in one main mstaComposedTrendCase
        assert isinstance(_mainTrend, mstaComposedTrendCase)
        self.trendList = _trendsList
        self.mainTrend = _mainTrend

        # Initialisation of combobox
        self.definedTrendCaseComboBox.addItems([tc.__str__() for tc in self.trendList])
        self.andRadioButton.setChecked(True)

        # Definition of connectors to handle user action
        self.leftParenthesisButton.clicked.connect(self.AddLeftParenthesis)
        self.rightParenthesisButton.clicked.connect(self.AddRightParenthesis)
        self.addToolButton.clicked.connect(self.AddTrendCase)
        self.addOperandToolButton.clicked.connect(self.AddOperand)

    @pyqtSlot(bool)
    def AddLeftParenthesis(self):
        self.UpdaTextEditor()
        return

    @pyqtSlot(bool)
    def AddRightParenthesis(self):
        self.UpdaTextEditor()
        return

    @pyqtSlot(bool)
    def AddTrendCase(self):
        for tc in self.trendList:
            if tc.__str__() == self.definedTrendCaseComboBox.currentText():
                currentTrend = tc
        #self.expressionTextEdit.insertPlainText(currentTrend.__str__())
        self.mainTrend.addTrendCase(currentTrend, "And")
        self.UpdaTextEditor()
        return

    @pyqtSlot(bool)
    def AddOperand(self):
        self.UpdaTextEditor()
        return

    def UpdaTextEditor(self):
        # if the main trend case does not containts anythink, nothing to do
        if self.mainTrend.getOperand() == 0:
            return
        # Clear the text of the widget
        self.expressionTextEdit.clear()
        # Insert the text of the defined trend cases
        for op in self.mainTrend.getOperand():
            self.expressionTextEdit.insertPlainText("{} {} {} ".format(self.mainTrend.getTrendByID()[op.getLeftTrendID()],
                                                    op.getOP(),
                                                    self.mainTrend.getTrendByID()[op.getRightTrendID()]))

