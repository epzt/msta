from PyQt5.QtGui import QDialog, QInputDialog
from PyQt5.QtWidgets import  QMessageBox

from .ui_about_msta import Ui_AboutDlg
from .ui_set_gsta_variables_dialog import Ui_setGSTAVariablesDialog as setGSTAVarDlg
from .ui_gsta_trend_definition import Ui_setGSTATrendCaseDialog as setGSTATrendDlg
from .ui_msta_variable_definition import Ui_SetMSTAVarOptionsDlg as setMSTAVariableDlg

from .mstaCoreClass import mstaTrendCase, mstaComposedTrendCase, mstaVariable

# Unit of variables,must be the same as mstaCoreClass.py definition
UNIT = {
    'percent' : '%',
    'metre' : 'm',
    'phi' : 'phi',
    'other' : 'unknown'
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
        self.variablesDefinition = [] # List of variable definitions (of type class mstaVariable)

    def getMean(self):
        item, ok = QInputDialog(self).getItem(self, "Select Mean",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            for k in self.variablesDict:
                if item == self.variablesDict[k]:
                    return
            # Launch the dialog box of variable options definition
            variableDlg = setMSTAVariableOptionDlg("mean")
            result = variableDlg.exec_()
            if not result:
                msg = "Mean variable set to default:\nName: mean, alias: mean, distance: 0.0, range: (0,0) and no anysotropy"
                QMessageBox.information(self, "GSTA Variables", msg)
            # Even if in variableDlg no definition is set of the mean variable, it is set to default values
            self.variablesDefinition.append(variableDlg.getVariableDefinition())
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
            variableDlg = setMSTAVariableOptionDlg("sorting")
            result = variableDlg.exec_()
            if not result:
                msg = "Sorting variable set to default:\nName: sorting, alias: sorting, distance: 0.0, range: (0,0) and no anysotropy"
                QMessageBox.information(self, "GSTA Variables", msg)
            # Even if in variableDlg no definition is set of the mean variable, it is set to default values
            self.variablesDefinition.append(variableDlg.getVariableDefinition())
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
            variableDlg = setMSTAVariableOptionDlg("skewness")
            result = variableDlg.exec_()
            if not result:
                msg = "Skewness variable set to default:\nName: skewness, alias: skewness, distance: 0.0, range: (0,0) and no anysotropy"
                QMessageBox.information(self, "GSTA Variables", msg)
            # Even if in variableDlg no definition is set of the mean variable, it is set to default values
            self.variablesDefinition.append(variableDlg.getVariableDefinition())
            # Updates of the dialog
            self.variablesDict['skewness'] = item
            self.skewnessLineEdit.setText(item)

    def areGSTAVariablesSet(self):
        retValue  = False
        if self.getMeanVariable() and self.getSortingVariable() and self.getSkewnessVariable():
            retValue = True
        return retValue

    def getMeanVariable(self):
        return(self.variablesDict['mean'])

    def getSortingVariable(self):
        return(self.variablesDict['sorting'])

    def getSkewnessVariable(self):
        return(self.variablesDict['skewness'])

#############################################################################
# GSTA trend definition
#############################################################################
class setGSTATrendCases(QDialog, setGSTATrendDlg):
    def __init__(self, _variables, parent=None):
        super(setGSTATrendCases,self).__init__(parent)
        self.setupUi(self)

        # Initial variables
        self.meanTrendText = ""
        self.meanTrend = mstaTrendCase()
        self.sortingTrendText = ""
        self.sortingTrend = mstaTrendCase()
        self.skewnessTrendText = ""
        self.skewnessTrend = mstaTrendCase()
        self.trendCaseList = []
        self.linkOperand = "AND" # Default operand which link multiple trend case

        self.linkOperandComboBox.setEnabled(False)

        self.GSTATrendCase = mstaComposedTrendCase()
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


    def setMeanTrend(self):
        if self.radioGSTAMeanFiner.isChecked():
            self.meanTrendText = "F"
        elif self.radioGSTAMeanCoarser.isChecked():
            self.meanTrendText = "C"
        else:
            self.meanTrendText = ""

    def setSortingTrend(self):
        if self.radioGSTASortingBetter.isChecked():
            self.sortingTrendText = "B"
        elif self.radioGSTASortingPorer.isChecked():
            self.sortingTrendText = "P"
        else:
            self.sortingTrendText = ""

    def setSkewnessTrend(self):
        if self.radioGSTASkewnessPlus.isChecked():
            self.skewnessTrendText = "+"
        elif self.radioGSTASkewnessMinus.isChecked():
            self.skewnessTrendText = "-"
        else:
            self.skewnessTrendText = ""

    def addGSTATrendCase(self):
        newTrendCase = f'{self.meanTrendText}{self.sortingTrendText}{self.skewnessTrendText}'
        if newTrendCase == "":
            return
        if newTrendCase not in self.trendCaseList:
            self.trendCaseList.append(newTrendCase)
            labelTrendCaseText = ""
            for c in self.trendCaseList:
                labelTrendCaseText = labelTrendCaseText + c + '\n'
            self.labelTrendCase.setText(labelTrendCaseText)
        # if more than one trend case, enable the link operand combobox
        if len(self.trendCaseList) > 1:
            self.linkOperandComboBox.setEnabled(True)
        else:
            self.linkOperandComboBox.setEnabled(False)
            self.linkOperand = "AND" # return to default value
        return

    def removeGSTATrendCase(self):
        delTrendCase = f'{self.meanTrendText}{self.sortingTrendText}{self.skewnessTrendText}'
        if delTrendCase == "" or delTrendCase not in self.trendCaseList:
            return
        self.trendCaseList.remove(delTrendCase)
        labelTrendCaseText = ""
        for c in self.trendCaseList:
            labelTrendCaseText = labelTrendCaseText + c + '\n'
        self.labelTrendCase.setText(labelTrendCaseText)
        # if more than one trend case, enable the link operand combobox
        if len(self.trendCaseList) > 1:
            self.linkOperandComboBox.setEnabled(True)
        else:
            self.linkOperandComboBox.setEnabled(False)
            self.linkOperand = "AND"  # return to default value
        return

    def getTrendCaseList(self):
        if self.trendCaseList:
            return self.trendCaseList
        else:
            return []

    def currentTextChanged(self, _text):
        self.linkOperand = _text


#############################################################################
# MSTA variable definition
#############################################################################
class setMSTAVariableOptionDlg(QDialog, setMSTAVariableDlg):
    def __init__(self, _variable, parent=None):
        super(setMSTAVariableOptionDlg,self).__init__(parent)
        self.setupUi(self)

        # Initialisation from previous variable
        if isinstance(_variable, mstaVariable):
            self.variableNameLineEdit.setText(_variable.getName())
            self.variableAliasLineEdit.setText(_variable.getAlias())
            self.variableDgLineEdit.setText(str(_variable.getDg()))
            self.minVariableRangeLineEdit.setText(str(_variable.getMin()))
            self.maxVariableRangeLineEdit.setText(str(_variable.getMax()))
            self.directionVariableLineEdit.setText(str(_variable.getDirection()))
            self.tolangVariableLineEdit.setText(str(_variable.getToleranceAngle()))
            self.variableUnitComboBox.setEditText(_variable.getUnit())
        elif isinstance(_variable, str):
            self.variableNameLineEdit.setText(_variable)
            self.variableAliasLineEdit.setText(_variable)
            self.variableDgLineEdit.setText("0.0")
            self.minVariableRangeLineEdit.setText("0.0")
            self.maxVariableRangeLineEdit.setText("0.0")
            self.directionVariableLineEdit.setText("0.0")
            self.tolangVariableLineEdit.setText("0.0")
            # Variable definition
            self.unit = "other"
            self.variableUnitComboBox.setCurrentIndex(3)
        else:
            self.variableDgLineEdit.setText("0.0")
            self.minVariableRangeLineEdit.setText("0.0")
            self.maxVariableRangeLineEdit.setText("0.0")
            self.directionVariableLineEdit.setText("0.0")
            self.tolangVariableLineEdit.setText("0.0")
            # Variable definition
            self.unit = "other"
            self.variableUnitComboBox.setCurrentIndex(3)

        # Connection définition
        self.variableUnitComboBox.currentTextChanged.connect(self.currentUnitChanged)

    def currentUnitChanged(self, _unit):
        if _unit == "persent":
            self.unit = UNIT["persent"]
        elif _unit == "metre":
            self.unit = UNIT["metre"]
        elif _unit == "phi":
            self.unit = UNIT["phi"]
        else:
            self.unit = UNIT["other"]

    def getVariableDefinition(self):
        newvar = mstaVariable()
        newvar.setName(self.getVariableName())
        newvar.setAlias(self.getVariableAlias())
        newvar.setUnit(self.getVariableUnit())
        newvar.setDg(self.getVariableDg())
        newvar.setRange(self.getVariableRangeMin(),self.getVariableRangeMax())
        newvar.setSearch(self.getVariableAnysotropyDirection(), self.getVariableAnysotropyTolangle())
        # DEBUG
        print(newvar)
        return newvar

    def getVariableName(self):
        return self.variableNameLineEdit.text()

    def getVariableAlias(self):
        return self.variableAliasLineEdit.text()

    def getVariableUnit(self):
        return next(i for i in UNIT if UNIT[i] == self.unit)

    def getVariableDg(self):
        return float(self.variableDgLineEdit.text())

    def getVariableRangeMin(self):
        return float(self.minVariableRangeLineEdit.text())

    def getVariableRangeMax(self):
        return float(self.maxVariableRangeLineEdit.text())

    def getVariableAnysotropyDirection(self):
        return float(self.directionVariableLineEdit.text())

    def getVariableAnysotropyTolangle(self):
        return float(self.tolangVariableLineEdit.text())
