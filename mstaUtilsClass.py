from PyQt5.QtCore import *
from PyQt5.QtGui import *


class setGSTAVariables(QWidget):
    def __init__(self, _variablesList, parent=None):
        super().__init__(parent)
        #super(QWidget, self).__init__(parent)

        self.items = _variablesList
        self.initUI()

    def initUI(self):
        layout = QFormLayout()

        self.btnMean = QPushButton("Choose mean")
        self.btnMean.clicked.connect(self.getMean)
        self.leMean = QLineEdit()
        layout.addRow(self.btnMean, self.leMean)

        self.btnSorting = QPushButton("Choose sorting")
        self.btnSorting.clicked.connect(self.getSorting)
        self.leSorting = QLineEdit()
        layout.addRow(self.btnSorting, self.leSorting)

        self.btnSkewness = QPushButton("Choose skewness")
        self.btnSkewness.clicked.connect(self.getSkewness)
        self.leSkewness = QLineEdit()
        layout.addRow(self.btnSkewness, self.leSkewness)

        self.setLayout(layout)
        self.setWindowTitle("Select GSTA variables")

        self.show()

    def getMean(self):
        item, ok = QInputDialog(self).getItem(self, "Select Mean",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            self.leMean.setText(item)

    def getSorting(self):
        item, ok = QInputDialog(self).getItem(self, "Select Sorting",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            self.leSorting.setText(item)

    def getSkewness(self):
        item, ok = QInputDialog(self).getItem(self, "Select Skewness",
                                        "List of available variables", self.items, 0, False)
        if ok and item:
            self.leSkewness.setText(item)

    def getMeanVariable(self):
        retValue = self.leMean.text()
        if retValue:
            return retValue
        else:
            return(None)

    def getSortingVariable(self):
        retValue = self.leSorting.text()
        if retValue:
            return retValue
        else:
            return(None)

    def getSkewnessVariable(self):
        retValue = self.leSkewness.text()
        if retValue:
            return retValue
        else:
            return(None)
