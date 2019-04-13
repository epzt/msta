from PyQt5.QtGui import QDialog, QInputDialog

from .ui_about_msta import Ui_AboutDlg
from .ui_set_gsta_variables_dialog import Ui_setGSTAVariablesDialog as setGSTAVarDlg
from .ui_gsta_trend_definition import Ui_setGSTATrendCaseDialog as setGSTATrendDlg

from mstaCoreClass import mstaTrendCase, mstaComposedTrendCase

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

        self.GSTATrendCase = mstaComposedTrendCase()
        self.buttonAddGSTATrendCase.clicked.connect(self.addGSTATrendCase)


    def addGSTATrendCase(self, _var):
        return
    

