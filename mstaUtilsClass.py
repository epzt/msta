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

#from .ui_about_msta import Ui_AboutDlg
from .ui_set_gsta_variables_dialog import Ui_setGSTAVariablesDialog as setGSTAVarDlg
from .ui_gsta_trend_definition import Ui_setGSTATrendCaseDialog as setGSTATrendDlg
from .ui_msta_variable_definition import Ui_SetMSTAVarOptionsDlg as setMSTAVariableDlg
from .ui_msta_trend_definition import Ui_mstaTrendDefinitionDialog as setMSTATrendDlg

from .mstaCoreClass import mstaTrendCase, mstaComposedTrendCase, mstaVariable

# Unit of variables,must be the same as mstaCoreClass.py definition
UNIT = {
    '%': 'percent',
    'metric': 'metre',
    'phi': 'phi',
    'other': 'unknown'
}

# Operand operations
OPERAND = {
    'ou' : 'OR',
    'et' : 'AND',
    'xou' : 'XOR',
    'none' : ''
}

# Trend operations
COMP = {
    'sup' : '>',
    'inf' : '<',
    'none' : ''
}

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
    def __init__(self, _variablesName, _variables, _trends, parent=None):
        super(setGSTATrendCasesDlg,self).__init__(parent)
        self.setupUi(self)
        #  _variablesName should be a list of three variable names (mean,sorting,skewness)
        assert isinstance(_variablesName, list) and len(_variablesName) >= 3
        # _variables should be a list of three mstaVariable objects
        assert isinstance(_variables, list) and len(_variables) >= 3
        assert isinstance(_variables[0], mstaVariable)
        # _trends must be of type mstaComposedTrendCase
        assert isinstance(_trends, mstaComposedTrendCase)
        # Assignements
        self.trendCases = _trends  # Type mstaComposedTrendCase
        # Initial variables
        self.meanTrendText = ""
        self.meanTrend = mstaTrendCase(self.getNameFromVariableList(_variables, "Mean"),"none")
        self.sortingTrendText = ""
        self.sortingTrend = mstaTrendCase(self.getNameFromVariableList(_variables, "Sorting"),"none")
        self.skewnessTrendText = ""
        self.skewnessTrend = mstaTrendCase(self.getNameFromVariableList(_variables, "Skewness"),"none")
        self.GSTATrendCaseListNames = []
        self.linkOperand = OPERAND['et'] # Default operand which link multiple GSTA trend case
        self.linkOperandComboBox.setEnabled(False)

        self.buttonAddGSTATrendCase.clicked.connect(self.addGSTATrendCase)
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

    ###############################################
    def setMeanTrend(self):
        if self.radioGSTAMeanFiner.isChecked():
            self.meanTrendText = "F"
            if self.meanTrend.getLeftVar().isMetric():
                self.meanTrend.setComp("sup")
            else:
                self.meanTrend.setComp("inf")
        elif self.radioGSTAMeanCoarser.isChecked():
            self.meanTrendText = "C"
            if self.meanTrend.getLeftVar().isMetric():
                self.meanTrend.setComp("inf")
            else:
                self.meanTrend.setComp("sup")
        else:
            self.meanTrendText = ""
            self.meanTrend.setComp("none")

    ###############################################
    def setSortingTrend(self):
        if self.radioGSTASortingBetter.isChecked():
            self.sortingTrendText = "B"
            self.sortingTrend.setComp("sup")
        elif self.radioGSTASortingPorer.isChecked():
            self.sortingTrendText = "P"
            self.sortingTrend.setComp("inf")
        else:
            self.sortingTrendText = ""
            self.sortingTrend.setComp("none")

    ###############################################
    def setSkewnessTrend(self):
        if self.radioGSTASkewnessPlus.isChecked():
            self.skewnessTrendText = "+"
            if self.skewnessTrend.getLeftVar().isMetric():
                self.skewnessTrend.setComp("sup")
            else:
                self.skewnessTrend.setComp("inf")
        elif self.radioGSTASkewnessMinus.isChecked():
            self.skewnessTrendText = "-"
            if self.skewnessTrend.getLeftVar().isMetric():
                self.skewnessTrend.setComp("inf")
            else:
                self.skewnessTrend.setComp("sup")
        else:
            self.skewnessTrendText = ""
            self.skewnessTrend.setComp("none")

    ###############################################
    # Add the new trend case to the main list
    def addGSTATrendCase(self):
        # New combined trend case object to add
        newCombinedTC = mstaComposedTrendCase([self.meanTrend,self.sortingTrend,self.skewnessTrend], OPERAND['et'])
        newCombinedTC.setComposedGSTATrend(True)  # It is a GSTA trend !! IMPORTANT TO SET IT AT TRUE
        for tc in self.trendCases:
            if tc.isGSTATrend():  # Test if it is a GSTA trend
                if tc == newCombinedTC:  # The new GSTA trend is still defined
                    return
        self.trendCases.addTrendCase(newCombinedTC, '')  # New GSTA trend case is added to the global list
        print(self.trendCases)
        self.updateGSTATrendCasesText(self.trendCases)
        return

    ###############################################
    def removeGSTATrendCase(self):
        # Current combined trend case object to remove
        currentCombinedTC = mstaComposedTrendCase([self.meanTrend, self.sortingTrend, self.skewnessTrend], OPERAND['et'])
        currentCombinedTC.setComposedGSTATrend(True)
        for tc in self.trendCases:
            if tc.isGSTATrend():  # Test if it is a GSTA trend
                if tc == currentCombinedTC:  # The current GSTA trend is defined
                    self.trendCases.deleteTrendCase(tc)  # New GSTA trend case is added to the global list
        self.updateGSTATrendCasesText(self.trendCases)
        return

    ###############################################
    '''
    def updateGSTATrendCases(self, _newTC):
        assert isinstance(_newTC, list)
        # New combined trend case object to add
        newCombinedTC = mstaComposedTrendCase(_newTC, OPERAND['et'])
        newCombinedTC.setComposedGSTATrend(True)  # It is a GSTA trend !! IMPORTANT TO SET IT AT TRUE
        for tc in self.trendCases:
            if tc.isGSTATrend(): # Test if it is a GSTA trend
                if tc == newCombinedTC: # The new GSTA trend is defined
                    return
        self.trendCases.addTrendCase(newCombinedTC, '') # New GSTA trend case is added to the global list
        return
    '''
    ###############################################
    def updateGSTATrendCasesText(self, _trendCasesList):
        # Erase all previous text
        self.TrendCaseTextEdit.clear()
        # If no trends defined-> nothing to do
        if _trendCasesList.getTrendCount() == 0:
            return
        # Construction of the text
        textCasesTrend = ""
        for tc in _trendCasesList.getTrend():
            textCasesTrend += tc.getGSTATrendText()
        textCasesTrend += '\n'
        # Print the text in the widget
        self.TrendCaseTextEdit.setText(textCasesTrend)
        return

    ###############################################
    def getGSTATrendCaseListNames(self):
        if self.GSTATrendCaseListNames:
            return self.GSTATrendCaseListNames
        else:
            return []

    ###############################################
    def getTrendCases(self):
        return self.trendCases

    ###############################################
    def currentTextChanged(self, _text):
        self.linkOperand = _text

    ###############################################
    def getNameFromVariableList(self, _varList, _name):
        assert isinstance(_varList, list)
        for v in _varList:
            if v.getAlias() == _name:
                return v
        return

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

    # Handle the ok button signal to verify that a variable name
    @pyqtSlot()
    def okBoutonGroupClicked(self):
        if self.variableNameComboBox.currentText() == "Choose a variable...":
            QDialog.reject(self)  # Quit the dialog as a Cancel operation
        else:
            QDialog.accept(self)

    @pyqtSlot('const QString')
    def currentUnitChanged(self, _unit):
        if _unit in UNIT.keys():
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
    def __init__(self, _variablesName, _variables, _trends, parent=None):
        super(setMSTATrendCasesDlg, self).__init__(parent)
        self.setupUi(self)

        # _variables should be a list of mstaVariable objects
        assert isinstance(_variables, list)
        assert isinstance(_variables[0], mstaVariable)
        # _trends must be of type mstaComposedTrendCase
        assert isinstance(_trends, mstaComposedTrendCase)
        # Construct the variable names list
        self.varObjectsList = _variables.copy()
        self.varNames = _variablesName.copy()
        # List of composed trend case objects (can have just one case)
        self.trendCases = _trends
        # List of names of the defined trend case, just usefull for interface information
        self.trendListLabel.setText(self.trendCases.__str__())

        # Initialisations
        # Lists of comboboxes
        self.variableAComboBox.addItems(self.varNames)
        self.variableBComboBox.addItems(self.varNames)
        self.variableAName = self.variableAComboBox.currentText()
        self.variableBName = self.variableBComboBox.currentText()
        self.signType = self.comparatorComboBox.currentText()
        self.linkOperand = self.linkOperandComboBox.currentText()

        self.linkOperandComboBox.setEnabled(False)

        self.clearPushButton.clicked.connect(self.ClearTrendListLabel)
        self.addPushButton.clicked.connect(self.addMSTATrendCase)
        self.deletePushButton.clicked.connect(self.deleteTrendCase)
        self.variableAComboBox.currentTextChanged.connect(self.currentVariableATextChanged)
        self.variableBComboBox.currentTextChanged.connect(self.currentVariableBTextChanged)
        self.comparatorComboBox.currentTextChanged.connect(self.currentSignTextChanged)
        self.linkOperandComboBox.currentTextChanged.connect(self.currentLinkOperandChanged)

    def getComp(self, _sign):
        if _sign == ">":
            return 'sup'
        elif _sign == "<":
            return 'inf'
        else:
            return 'none'

    def ClearTrendListLabel(self):
        msg = 'Are you sure you want delete all trends ?'
        if QMessageBox.information(self, "MSTA Variables", msg, QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return
        self.trendListLabel.clear()
        self.trendTextCases.clear()
        self.trendCases = mstaComposedTrendCase()
        self.linkOperandComboBox.setEnabled(False)
        return

    def addMSTATrendCase(self):
        # Two different variables can be mix only of they have same Dg
        if not self.varObjectsList[self.variableAComboBox.currentIndex()].isEqual(self.varObjectsList[self.variableBComboBox.currentIndex()]):
            indexA = self.variableAComboBox.currentIndex()
            indexB = self.variableBComboBox.currentIndex()
            QMessageBox.warning(self, "Trend definition error",
                                "Can\'t mix two variables with different characteristic distance, research angle or tolerance value:\n"
                                "{}: {}\n"
                                "{}: {}".format(self.varObjectsList[indexA].getName(),
                                                self.varObjectsList[indexA].getDg(),
                                                self.varObjectsList[indexB].getName(),
                                                self.varObjectsList[indexB].getDg()))
            return
        newTrendCaseText = f'{self.variableAName}(i) {self.signType} {self.variableBName}(j)'
        if newTrendCaseText in self.trendTextCases:
            return
        self.trendTextCases.append(newTrendCaseText)
        # update the GUI
        labelTrendCaseText = ""
        for tc in self.trendTextCases:
            labelTrendCaseText += tc + '\n'
        self.trendListLabel.setText(labelTrendCaseText)

        # Update trend cases list
        QMessageBox.information(self, "MSTA Variables", "{}".format(self.variableAComboBox.currentIndex()))
        newTrendCase = mstaTrendCase(self.varObjectsList[self.variableAComboBox.currentIndex()])
        if self.variableAName != self.variableBName: # In case varA is different to varB
            QMessageBox.information(self, "MSTA Variables", "{}".format(self.variableBComboBox.currentIndex()))
            newTrendCase.setRightVar(self.varObjectsList[self.variableBComboBox.currentIndex()])

        newTrendCase.setComp(self.getComp(self.signType))
        if newTrendCase.getID() == 0:
            self.trendCases.addTrendCase(newTrendCase, '')
            self.linkOperandComboBox.setEnabled(True)
        else:
            self.trendCases.addTrendCase(newTrendCase, self.linkOperand)
        return

    def deleteTrendCase(self):
        trendCaseToDelete = f'{self.variableAName}(i) {self.signType} {self.variableBName}(j)'
        try:
            id = self.trendTextCases.index(trendCaseToDelete)
        except ValueError:
            return
        self.trendTextCases.remove(trendCaseToDelete)
        # update the GUI
        labelTrendCaseText = ""
        for tc in self.trendTextCases:
            labelTrendCaseText += tc + '\n'
        self.trendListLabel.setText(labelTrendCaseText)

        self.trendCases.deleteTrendCase(self.trendCases.getTrend(id))
        return

    def currentVariableATextChanged(self):
        self.variableAName = self.variableAComboBox.currentText()
        self.variableBComboBox.setCurrentIndex(self.variableAComboBox.currentIndex())
        return

    def currentVariableBTextChanged(self):
        self.variableBName = self.variableBComboBox.currentText()
        return

    def currentSignTextChanged(self):
        self.signType = self.comparatorComboBox.currentText()
        return

    def currentLinkOperandChanged(self):
        self.linkOperand = self.linkOperandComboBox.currentText()
        return

    def getTrendCases(self):
        return self.trendCases

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
