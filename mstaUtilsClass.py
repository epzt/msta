from PyQt5.QtWidgets import  QMessageBox, QDialog, QInputDialog

from .ui_about_msta import Ui_AboutDlg
from .ui_set_gsta_variables_dialog import Ui_setGSTAVariablesDialog as setGSTAVarDlg
from .ui_gsta_trend_definition import Ui_setGSTATrendCaseDialog as setGSTATrendDlg
from .ui_msta_variable_definition import Ui_SetMSTAVarOptionsDlg as setMSTAVariableDlg
from .ui_msta_trend_definition import Ui_mstaTrendDefinitionDialog as setMSTATrendDlg

from .mstaCoreClass import mstaTrendCase, mstaComposedTrendCase, mstaVariable

# Unit of variables,must be the same as mstaCoreClass.py definition
UNIT = {
    '%' : 'percent',
    'm' : 'metre',
    'mm' : 'millimetre',
    'mu' : 'micronmetre',
    'phi' : 'phi',
    'other' : 'unknown'
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
class aboutMSTA(QDialog, Ui_AboutDlg):
    def __int__(self, parent=None):
        super(aboutMSTA,self).__init__(parent)
        self.setupUi(self)

#############################################################################
# GSTA variables definition from global variable list
#############################################################################
class setGSTAVariablesDlg(QDialog, setGSTAVarDlg):
    def __init__(self, _variablesList, parent=None):
        super(setGSTAVariablesDlg,self).__init__(parent)
        self.setupUi(self)

        self.meanButton.clicked.connect(self.getMean)
        self.sortingButton.clicked.connect(self.getSorting)
        self.skewnessButton.clicked.connect(self.getSkewness)
        # Initialisations
        self.variablesDict = {'mean':'','sorting':'','skewness':''}
        self.items = _variablesList  # List of variable names
        self.variablesDefinition = [] # List of variable definitions (list of class mstaVariable)

    def getMean(self):
        item, ok = QInputDialog(self).getItem(self, "Select Mean",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            for k in self.variablesDict:
                if item == self.variablesDict[k]:
                    return
            # Launch the dialog box of variable options definition
            variableDlg = setMSTAVariableOptionDlg(item)
            result = variableDlg.exec_()
            if not result:
                msg = "Mean variable set to default:\nName: mean, alias: mean, distance: 0.0, range: (0,0) and no anysotropy"
                QMessageBox.information(self, "GSTA Variables", msg)

            # Even if in variableDlg no definition is set for the mean variable, it is set to default values
            newVar = variableDlg.getVariableDefinition()
            # This is o force alias to have "Mean" value
            newVar.setAlias("Mean")
            self.variablesDefinition.append(newVar)
            # Updates of the dialog
            self.variablesDict['mean'] = item
            self.meanLineEdit.setText(item)

    def getSorting(self):
        item, ok = QInputDialog(self).getItem(self, "Select Sorting",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            for k in self.variablesDict:
                if item == self.variablesDict[k]:
                    return
            # Launch the dialog box of variable options definition
            variableDlg = setMSTAVariableOptionDlg(item)
            result = variableDlg.exec_()
            if not result:
                msg = "Sorting variable set to default:\nName: sorting, alias: sorting, distance: 0.0, range: (0,0) and no anysotropy"
                QMessageBox.information(self, "GSTA Variables", msg)

            # Even if in variableDlg no definition is set for the mean variable, it is set to default values
            newVar = variableDlg.getVariableDefinition()
            # This is o force alias to have "Sorting" value
            newVar.setAlias("Sorting")
            self.variablesDefinition.append(newVar)
            # Updates of the dialog
            self.variablesDict['sorting'] = item
            self.sortingLineEdit.setText(item)

    def getSkewness(self):
        item, ok = QInputDialog(self).getItem(self, "Select Skewness",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            for k in self.variablesDict:
                if item == self.variablesDict[k]:
                    return
            # Launch the dialog box of variable options definition
            variableDlg = setMSTAVariableOptionDlg(item)
            result = variableDlg.exec_()
            if not result:
                msg = "Skewness variable set to default:\nName: skewness, alias: skewness, distance: 0.0, range: (0,0) and no anysotropy"
                QMessageBox.information(self, "GSTA Variables", msg)
            # Even if in variableDlg no definition is set for the mean variable, it is set to default values
            newVar = variableDlg.getVariableDefinition()
            # This is o force alias to have "Skewness" value
            newVar.setAlias("Skewness")
            self.variablesDefinition.append(newVar)

            # Updates of the dialog
            self.variablesDict['skewness'] = item
            self.skewnessLineEdit.setText(item)

    def areGSTAVariablesSet(self):
        retValue  = False
        if self.getMeanVariableName() and self.getSortingVariableName() and self.getSkewnessVariableName():
            retValue = True
        return retValue

    def getMeanVariableName(self):
        return(self.variablesDict['mean'])

    def getSortingVariableName(self):
        return(self.variablesDict['sorting'])

    def getSkewnessVariableName(self):
        return(self.variablesDict['skewness'])

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
        self.trendCases = _trends  # Type mstaComposedTrendcase
        # Initial variables
        self.meanTrendText = ""
        self.meanTrend = mstaTrendCase(self.getNameFromVariableList(_variables, "mean"))
        self.sortingTrendText = ""
        self.sortingTrend = mstaTrendCase(self.getNameFromVariableList(_variables, "sorting"))
        self.skewnessTrendText = ""
        self.skewnessTrend = mstaTrendCase(self.getNameFromVariableList(_variables, "skewness"))
        self.GSTATrendCaseListNames = []
        # self.trendCaseList = [] # List of single mstaTrendCase objects such as F or C or B etc.
        self.linkOperand = "AND" # Default operand which link multiple trend case

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
        newTrendCaseText = f'{self.meanTrendText}{self.sortingTrendText}{self.skewnessTrendText}'
        if newTrendCaseText == "" or newTrendCaseText in self.GSTATrendCaseListNames:
            return

        self.GSTATrendCaseListNames.append(newTrendCaseText)
        labelTrendCaseText = ""
        for c in self.GSTATrendCaseListNames:
            labelTrendCaseText = labelTrendCaseText + c + '\n'
        self.labelTrendCase.setText(labelTrendCaseText)
        # if more than one trend case, enable the link operand combobox
        if len(self.GSTATrendCaseListNames) >= 1:
            self.linkOperandComboBox.setEnabled(True)
        else:
            self.linkOperandComboBox.setEnabled(False)
            self.linkOperand = "AND" # return to default value
        # Update the trend case list - IMPORTANT OPERATION -> ADD
        self._updateGSTATrendCases([self.meanTrend,self.sortingTrend,self.skewnessTrend], True)
        return

    ###############################################
    def removeGSTATrendCase(self):
        delTrendCase = f'{self.meanTrendText}{self.sortingTrendText}{self.skewnessTrendText}'
        if delTrendCase == "" or delTrendCase not in self.GSTATrendCaseListNames:
            return
        self.GSTATrendCaseListNames.remove(delTrendCase)
        labelTrendCaseText = ""
        for c in self.GSTATrendCaseListNames:
            labelTrendCaseText = labelTrendCaseText + c + '\n'
        self.labelTrendCase.setText(labelTrendCaseText)
        # if more than one trend case, enable the link operand combobox
        if len(self.GSTATrendCaseListNames) > 1:
            self.linkOperandComboBox.setEnabled(True)
        else:
            self.linkOperandComboBox.setEnabled(False)
            self.linkOperand = "AND"  # return to default value
        # Update the trend case list - IMPORTANT OPERATION -> delete
        self._updateGSTATrendCases([self.meanTrend, self.sortingTrend, self.skewnessTrend], False)
        return

    ###############################################
    def _updateGSTATrendCases(self, _newTC, add=True):
        assert isinstance(_newTC, list)
        # Should not append
        if len(_newTC) == 0:
            return

        # New combined trend case object to add to the main unique combined trend object
        newCombinedTC = mstaComposedTrendCase()
        # Loop over the (eventually) combined GSTA trend case (could de FB, FB+, B, C, etc.)
        for tc in range(len(_newTC)-1):
            newCombinedTC.addTrendCase(_newTC[tc],"et") # always "and" when mixing mean, sorting, skewness
            newCombinedTC.setID(tc+1)
        newCombinedTC.addTrendCase(_newTC[-1], "none") # Treatement of the last trend case
        newCombinedTC.setID(len(_newTC))

        # Delete the trend case from the list
        if not add:
            # delete the trend case
            index = self.trendCases.deleteTrendCase(newCombinedTC)
            return

        # Add the new trend case
        self.trendCases.addTrendCase(newCombinedTC, "none")
        nbrTrend = self.trendCases.getTrendCount()
        # Set the ID of the trend in the main list
        self.trendCases.setID(nbrTrend)
        #DEBUG
        print(self.trendCases)
        # If trend cases have been defined previously the operand between the previous
        #  and the current trend case should be change according current dialog settings
        if nbrTrend > 1:
            if self.linkOperand == "OR":
                self.trendCases.setOperand(nbrTrend-2, "ou")
            elif self.linkOperand == "XOR":
                self.trendCases.setOperand(nbrTrend-2, "xou")
            else:
                self.trendCases.setOperand(nbrTrend-2, "et")
        return


    ###############################################
    def getGSTATrendCaseListNames(self):
        if self.GSTATrendCaseListNames:
            return self.GSTATrendCaseListNames
        else:
            return []

    ###############################################
    def getGSTATrendCases(self):
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
    def __init__(self, _variable, parent=None):
        super(setMSTAVariableOptionDlg,self).__init__(parent)
        self.setupUi(self)
        # Default unit
        self.unit = "%"
        # Initialisation from previous variable
        if isinstance(_variable, mstaVariable):
            self.variableNameLineEdit.setText(_variable.getName())
            self.variableAliasLineEdit.setText(_variable.getAlias())
            self.variableDgLineEdit.setText(str(_variable.getDg()))
            self.pmVariableRangeLineEdit.setText(str(_variable.getRange()))
            self.directionVariableLineEdit.setText(str(_variable.getDirection()))
            self.tolangVariableLineEdit.setText(str(_variable.getToleranceAngle()))
            self.variableUnitComboBox.setCurrentText(_variable.getUnit())
        # Initialisation with initial variables name
        elif isinstance(_variable, str):
            self.variableNameLineEdit.setText(_variable)
            self.variableAliasLineEdit.setText(_variable)
            self.variableDgLineEdit.setText("0.0")
            self.pmVariableRangeLineEdit.setText("0.0")
            self.directionVariableLineEdit.setText("0.0")
            self.tolangVariableLineEdit.setText("0.0")
            self.variableUnitComboBox.setCurrentText(self.unit)
        else:
            self.variableDgLineEdit.setText("0.0")
            self.pmVariableRangeLineEdit.setText("0.0")
            self.directionVariableLineEdit.setText("0.0")
            self.tolangVariableLineEdit.setText("0.0")
            self.variableUnitComboBox.setCurrentText(self.unit)

        # Connection définition
        self.variableUnitComboBox.currentTextChanged.connect(self.currentUnitChanged)

    def currentUnitChanged(self, _unit):
        if _unit in UNIT.keys():
            self.unit = _unit

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
        return self.variableNameLineEdit.text()

    def getVariableAlias(self):
        return self.variableAliasLineEdit.text()

    def getVariableUnit(self):
        return self.unit

    def getVariableDg(self):
        return float(self.variableDgLineEdit.text())

    def getVariableRange(self):
        return float(self.pmVariableRangeLineEdit.text())

    def getVariableAnysotropyDirection(self):
        return float(self.directionVariableLineEdit.text())

    def getVariableAnysotropyTolangle(self):
        return float(self.tolangVariableLineEdit.text())

#############################################################################
# MSTA trend definition
#############################################################################
class setMSTATrendCasesDlg(QDialog, setMSTATrendDlg):
    def __init__(self, _variablesName, _variables, _trends, parent=None):
        super(setMSTATrendCasesDlg,self).__init__(parent)
        self.setupUi(self)

        # _variables should be a list of mstaVariable objects
        assert isinstance(_variables, list)
        assert isinstance(_variables[0], mstaVariable)
        # _trends must be of type mstaComposedTrendCase
        assert isinstance(_trends, mstaComposedTrendCase)
        # Construct the variable names list
        self.varObjectsList = _variables.copy()
        self.varNames =  _variablesName.copy()
        # List of composed trend case objects (can have just one case)
        self.trendCases = _trends
        # ID for the trendcases which will be defined by the user
        self.currentID = self.trendCases.getMaxCaseID()
        if self.currentID == -1: # no trend yet defined
            self.currentID = 0
        # List of names of the defined trend case, just usefull for interface information
        self.trendTextCases = self.trendCases.getTrendsText()
        labelTrendCaseText = ""
        for tc in self.trendTextCases:
            labelTrendCaseText += tc + '\n'
        self.trendListLabel.setText(labelTrendCaseText)

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
        self.addPushButton.clicked.connect(self.addTrendCase)
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

    def getOperand(self, _op):
        if _op == "AND":
            return 'et'
        elif _op == "OR":
            return 'ou'
        elif _op == "XOR":
            return 'xou'
        else:
            return 'none'

    def ClearTrendListLabel(self):
        msg = 'Are you sure you want delete all trends ?'
        if QMessageBox.information(self, "GSTA Variables", msg, QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return
        self.trendListLabel.clear()
        self.trendTextCases.clear()
        self.trendCases = mstaComposedTrendCase()
        self.currentID = 0
        self.linkOperandComboBox.setEnabled(False)
        return

    def addTrendCase(self):
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
        newTrendCase = mstaTrendCase(self.varObjectsList[self.variableAComboBox.currentIndex()])
        if self.variableAName != self.variableBName: # In case varA is different to varB
            newTrendCase.setRightVar(self.varObjectsList[self.variableBComboBox.currentIndex()])
        newTrendCase.setID(self.currentID)
        self.currentID +=  1
        newTrendCase.setComp(self.getComp(self.signType))
        if self.currentID == 0:
            self.trendCases.addTrendCase(newTrendCase, 'none')
            self.linkOperandComboBox.setEnabled(True)
        else:
            self.trendCases.addTrendCase(newTrendCase, self.getOperand(self.linkOperand))
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

        self.currentID -= 1
        self.trendCases.deleteTrendCase(self.trendCases.getTrend(id))
        return

    def currentVariableATextChanged(self):
        self.variableAName = self.variableAComboBox.currentText()
        self.variableBComboBox.setCurrentIndex(self.variableAComboBox.currentIndex())
        return

    def currentVariableBTextChanged(self):
        self.variableBName = self.variableBComboBox.currentText()
        self.variableAComboBox.setCurrentIndex(self.variableBComboBox.currentIndex())
        return

    def currentSignTextChanged(self):
        self.signType = self.comparatorComboBox.currentText()
        return

    def currentLinkOperandChanged(self):
        self.linkOperand = self.linkOperandComboBox.currentText()
        return

    def getTrendCases(self):
        return self.trendCases