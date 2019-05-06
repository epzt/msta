from PyQt5.QtGui import QDialog, QInputDialog

from .ui_about_msta import Ui_AboutDlg
from .ui_set_gsta_variables_dialog import Ui_setGSTAVariablesDialog as setGSTAVarDlg
from .ui_gsta_trend_definition import Ui_setGSTATrendCaseDialog as setGSTATrendDlg

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
# GSTA trend definnition
#############################################################################
class setGSTATrendCases(QDialog, setGSTATrendDlg):
    def __init__(self, parent=None):
        super(setGSTATrendCases,self).__init__(parent)
        self.setupUi(self)

        # Initial variables
        self.meanTrend = ""
        self.sortingTrend = ""
        self.skewnessTrend = ""
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
            self.meanTrend = "F"
        elif self.radioGSTAMeanCoarser.isChecked():
            self.meanTrend = "C"
        else:
            self.meanTrend = ""

    def setSortingTrend(self):
        if self.radioGSTASortingBetter.isChecked():
            self.sortingTrend = "B"
        elif self.radioGSTASortingPorer.isChecked():
            self.sortingTrend = "P"
        else:
            self.sortingTrend = ""

    def setSkewnessTrend(self):
        if self.radioGSTASkewnessPlus.isChecked():
            self.skewnessTrend = "+"
        elif self.radioGSTASkewnessMinus.isChecked():
            self.skewnessTrend = "-"
        else:
            self.skewnessTrend = ""

    def addGSTATrendCase(self):
        newTrendCase = f'{self.meanTrend}{self.sortingTrend}{self.skewnessTrend}'
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
        delTrendCase = f'{self.meanTrend}{self.sortingTrend}{self.skewnessTrend}'
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


