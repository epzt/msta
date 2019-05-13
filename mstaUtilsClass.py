from PyQt5.QtGui import QDialog, QInputDialog

from .ui_about_msta import Ui_AboutDlg
from .ui_set_gsta_variables_dialog import Ui_setGSTAVariablesDialog as setGSTAVarDlg
from .ui_gsta_trend_definition import Ui_setGSTATrendCaseDialog as setGSTATrendDlg
from .ui_msta_variable_definition import Ui_SetMSTAVarOptionsDlg as setMSTAVariableDlg

from .mstaCoreClass import mstaTrendCase, mstaComposedTrendCase

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
class setGSTAVariables(QDialog, setGSTAVarDlg):
    def __init__(self, _variablesList, parent=None):
        super(setGSTAVariables,self).__init__(parent)
        self.setupUi(self)

        self.meanButton.clicked.connect(self.getMean)
        self.sortingButton.clicked.connect(self.getSorting)
        self.skewnessButton.clicked.connect(self.getSkewness)
        # Initialisations
        self.variablesDict = {'mean':'','sorting':'','skewness':''}
        self.items = _variablesList

    def getMean(self):
        item, ok = QInputDialog(self).getItem(self, "Select Mean",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            for k in self.variablesDict:
                if item == self.variablesDict[k]:
                    return
            variableDlg = setMSTAVariableOptionDlg("mean")
            result = variableDlg.exec_()
            if not result:
                msg = "Mean variable set to default:\nName: mean, alias: mean, range: (0,0), no anysotropy"
                QMessageBox.information(self, "GSTA Variables", msg)
            else:
                variableDlg.getVariableName()
                variableDlg.getVariableAlias()
                variableDlg.getVariableRange()
                variableDlg.getVariableAnaysotropy()

            self.variablesDict['mean'] = item
            self.meanLineEdit.setText(item)

    def getSorting(self):
        item, ok = QInputDialog(self).getItem(self, "Select Sorting",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            for k in self.variablesDict:
                if item == self.variablesDict[k]:
                    return
            self.variablesDict['sorting'] = item
            self.sortingLineEdit.setText(item)

    def getSkewness(self):
        item, ok = QInputDialog(self).getItem(self, "Select Skewness",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            for k in self.variablesDict:
                if item == self.variablesDict[k]:
                    return
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

    def getVariableName(self):
        return self.variableNameLineEdit.text()

    def getVariableAlias(self):
        return self.variableAliasLineEdit.text()

    def getVariableRange(self):
        return [self.minVariableRangeLineEdit, self.maxVariableRangeLineEdit]

    def getVariableAnaysotropy(self):
        return [self.directionVariableLineEdit, self.tolangVariableLineEdit]
