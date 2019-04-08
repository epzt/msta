# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtWidgets
from .ui_msta_text_file_analysis import Ui_msta_text_file_analysis

YCOORDTEXT = ["y","lat","latitude","coordx","xx","xcoord"]
XCOORDTEXT = ["x","lon","long","longitude","coordy","yy","ycoord"]

class IDNAME(object):
    def __init__(self,_id, _name):
        self.ID=_id
        self.NAME=_name
    def setID(self,_id):
        self.ID=_id
    def setNAME(self,_name):
        self.NAME=_name
    def getID(self):
        return self.ID
    def getNAME(self):
        return self.NAME
    def __repr__(self):
        return(f'ID:{self.ID} NAME:{self.NAME}')

# -------------------------------------------------------
# -------------------------------------------------------
#        CLASS FOR TEXT IMPORT DIALOG MANAGEMENT
# -------------------------------------------------------
# -------------------------------------------------------
class pyMstaTextFileAnalysisDialog(QtWidgets.QDialog, Ui_msta_text_file_analysis):
    def __init__(self, initFileName, parent=None):
        super(pyMstaTextFileAnalysisDialog, self).__init__(parent)
        self.setupUi(self)
        # Initialisation
        self.setWindowTitle(initFileName)
        
        # Variables
        self.fileName = initFileName
        self.currentSeparator = ' '
        self.firstLineAsHeader = False
        self.numberLineToSkip = 0
        self.lineItemsList = []
        self.variableNameList = []
        self.sampleNameIndex = IDNAME(-1,'')
        self.xCoordinateIndex = IDNAME(-1,'')
        self.yCoordinateIndex = IDNAME(-1,'')
        self.commaDecimalSeparator = False
        
        # Connections definition
        self.radioSpace.toggled.connect(self.spaceToggled)
        self.radioTabulation.toggled.connect(self.tabulationToggled)
        self.radioComma.toggled.connect(self.commaToggled)
        self.radioSimilicon.toggled.connect(self.similiconToggled)
        self.radioPipe.toggled.connect(self.pipeToggled)
        self.radioOther.toggled.connect(self.otherToggled)
        self.checkBoxHeader.toggled.connect(self.headerToggled)
        self.checkBoxCommaSeparator.toggled.connect(self.commaSeparatorToggled)
        self.xCoordComboBox.currentTextChanged.connect(self.setXCoord)
        self.yCoordComboBox.currentTextChanged.connect(self.setYCoord)
        self.spinBoxSkipLine.valueChanged.connect(self.lineToSkip)
        self.lineEditOther.textChanged.connect(self.separatorOther)
        self.sampleNameComboBox.currentIndexChanged.connect(self.sampleNameGroupToggled)
        self.sampleNameGroupBox.toggled.connect(self.sampleNameGroupToggled)
        self.numberofLinesToRead.valueChanged.connect(self.setNumberofLinesToRead)
        self.allLinesToRead.toggled.connect(self.setAllLinesToRead)

        self.updateTableView()
        
    #----------------------------------------------------
    # Set of functions related to widgets connection
    def spaceToggled(self, value):
        if not value:
            return
        self.currentSeparator = ' '
        self.updateTableView()
        
    def tabulationToggled(self, value):
        if not value:
            return
        self.currentSeparator = '\t'
        self.updateTableView()
    
    def commaToggled(self, value):
        if not value:
            return
        self.currentSeparator = ','
        self.updateTableView()
        
    def similiconToggled(self, value):
        if not value:
            return
        self.currentSeparator = ';'
        self.updateTableView()
        
    def pipeToggled(self, value):
        if not value:
            return
        self.currentSeparator = '|'
        self.updateTableView()
        
    def otherToggled(self, value):
        if not value:
            return
        separator = self.lineEditOther.text()
        if separator != "":
            self.currentSeparator = separator
            self.updateTableView()
        
    def headerToggled(self, value):
        self.firstLineAsHeader = value
        self.updateTableView()
    
    def lineToSkip(self, newValue):
        linestoread = self.numberofLinesToRead.value()
        if self.numberLineToSkip < newValue:
            self.numberofLinesToRead.setValue(linestoread+1)
        else:
            self.numberofLinesToRead.setValue(linestoread-1)
        self.numberLineToSkip = newValue
        self.updateTableView()
        
    #def linesToAnalyse(self, newValue):
    #    self.numberLinesToAnalyse = newValue
    #    self.updateTableView()
        
    def separatorOther(self, other):
        if other != "":
            self.currentSeparator = other
            self.updateTableView()

    def commaSeparatorToggled(self, value):
        self.commaDecimalSeparator = value
        self.updateTableView()
            
    def setXCoord(self, value):
       if len(value) == 0:
          return
       self.xCoordinatesIndex = IDNAME(self.xCoordComboBox.currentIndex(), value)
        
    def setYCoord(self, value):
        if len(value) == 0:
            return
        self.yCoordinatesIndex = IDNAME(self.yCoordComboBox.currentIndex(), value)

    def getXIndex(self):
        return self.xCoordinatesIndex.getID()

    def getYIndex(self):
        return self.yCoordinatesIndex.getID()

    def getXName(self):
        return self.xCoordinatesIndex.getNAME()

    def getYName(self):
        return self.yCoordinatesIndex.getNAME()
    
    def updateXCoord(self):
        if self.xCoordinatesIndex.getID() == -1 or self.xCoordComboBox.currentIndex() == -1 :
            # default initialisation
            self.xCoordComboBox.setCurrentIndex(0)
            self.xCoordinatesIndex.setID(0)
            self.xCoordinatesIndex.setNAME(self.xCoordComboBox.currentText())
            # Check standard coordinate list names eventually to help user selecting
            for i in range(self.xCoordComboBox.count()):
                if self.xCoordComboBox.currentText().lower() in XCOORDTEXT:
                    self.xCoordComboBox.setCurrentIndex(i)
                    self.xCoordinatesIndex.setID(i)
                    self.xCoordinatesIndex.setNAME(self.xCoordComboBox.currentText())
                    break

    def updateYCoord(self):
        if self.yCoordinatesIndex.getID() == -1 or self.yCoordComboBox.currentIndex() == -1:
            # default initialisation
            self.yCoordComboBox.setCurrentIndex(0)
            self.yCoordinatesIndex.setID(0)
            self.yCoordinatesIndex.setNAME(self.yCoordComboBox.currentText())
            # Check standard coordinate list names eventually to help user selecting
            for i in range(self.yCoordComboBox.count()):
                if self.yCoordComboBox.currentText().lower() in YCOORDTEXT:
                    self.yCoordComboBox.setCurrentIndex(i)
                    self.yCoordinatesIndex.setID(i)
                    self.yCoordinatesIndex.setNAME(self.yCoordComboBox.currentText())
                    break

    def sampleNameGroupToggled(self, value):
        if value:
            self.sampleNameIndex = IDNAME(self.sampleNameComboBox.currentIndex(),self.sampleNameComboBox.currentText())
        else:
            self.sampleNameIndex = IDNAME(-1,'')

    def getSampleNameIndex(self):
        return self.sampleNameIndex.getID()

    def getSampleNameName(self):
        return self.sampleNameIndex.getNAME()

    def setNumberofLinesToRead(self, newValue):
        self.updateTableView()

    def setAllLinesToRead(self):
        self.updateTableView()

    # this retunr the number of line to skip when reading data from text file
    # if first line contains header, it will b skip during reading by numpy later
    def getNumberOfFirstLineToSkip(self):
        if self.firstLineAsHeader:
            return self.numberLineToSkip + 1
        else:
            return self.numberLineToSkip
        
    #-------------------------------------------------------
    # Update the tableView widget base on the user choosen settings
    def updateTableView(self):
        try:
            # Test opening the file
            with open(self.fileName, mode="r") as textFile:
                fields = []
                self.variableNameList.clear()
                currentFileLineNumber = 0
                firstLineToTreat = True
                self.xCoordComboBox.clear()
                self.yCoordComboBox.clear()
                self.sampleNameComboBox.clear()
                self.tableAnalysisResult.setRowCount(0)
                self.tableAnalysisResult.setColumnCount(0)
        
                # Read the file until the end
                # Choice to read the file line by line is done because file can have a huge size
                while True:
                    line = textFile.readline()
                    currentFileLineNumber += 1

                    if (currentFileLineNumber > self.numberofLinesToRead.value()) and (self.allLinesToRead.isChecked() == False):
                        break

                    if self.numberLineToSkip >= currentFileLineNumber:
                        continue

                    fields = line.strip().split(self.currentSeparator)
                    # Analysis of the first line
                    if firstLineToTreat:
                        firstLineToTreat = False
                        # First line containts variable names
                        if self.firstLineAsHeader:
                            self.tableAnalysisResult.setColumnCount(len(fields))
                            self.tableAnalysisResult.setHorizontalHeaderLabels(fields)
                            self.xCoordComboBox.addItems(fields)
                            self.yCoordComboBox.addItems(fields)
                            self.sampleNameComboBox.addItems(fields)
                            i = 0
                            for field in fields:
                                self.variableNameList.append(IDNAME(i,field))
                                i += 1
                            # the current line of the file is treated as header, so read next line
                            continue
                        else:
                        # First line containts data directly
                            self.tableAnalysisResult.setColumnCount(len(fields))
                            for i in range(len(fields)):
                                # Set the default name of the columns, i.e. variable names
                                item = QtGui.QTableWidgetItem(f'V{i+1}')
                                self.tableAnalysisResult.setHorizontalHeaderItem(i,item)
                                self.xCoordComboBox.addItem(f'V{i+1}')
                                self.yCoordComboBox.addItem(f'V{i+1}')
                                self.sampleNameComboBox.addItem(f'V{i+1}')
                                self.variableNameList.append(IDNAME(i,f'V{i+1}'))
    
                    self.updateXCoord()
                    self.updateYCoord()
                    self.tableAnalysisResult.insertRow(self.tableAnalysisResult.rowCount())

                    # Check for the number of fields, it must be the same all along the file
                    #if len(fields) != self.tableAnalysisResult.columnCount():
                    #    QtGui.QMessageBox.information(self, "Text file analysis", f'Number of fields at line {currentFileLineNumber} is not equal to {self.tableAnalysisResult.columnCount()}')
                    #    return
                
                    # Fill the table view
                    self.lineItemsList = []
                    for f in range(len(fields)):
                        if self.commaDecimalSeparator:
                            item = QtGui.QTableWidgetItem(fields[f].replace(",", "."))
                        else:
                            item = QtGui.QTableWidgetItem(fields[f])
                        self.lineItemsList.append(item)
                        self.tableAnalysisResult.setItem(self.tableAnalysisResult.rowCount()-1, f, item)

        except IOError:
            QtGui.QMessageBox.information(self, "Text file analysis", f'An error occured with file:\n{self.fileName}')
            return

        textFile.close()

    #----------------------------------------------------
    # Return the list of variable names without coordinates variables 
    #  and eventualy samples name variable     
    def getVariableNameList(self):
        retListVarNames = []
        retListVarIds = []
        retListCoordsNames = []
        retListCoordsIds = []
        if self.getSampleNameIndex() != -1:
            self.variableNameList.remove(self.getSampleNameName())
        if self.getXIndex() == self.getYIndex():
            QtGui.QMessageBox.critical(self, "Text file analysis", 'X and Y ccordinates must be different.')
            return(retListCoordsIds, retListCoordsNames, retListVarIds, retListVarNames)
        
        # print(self.variableNameList)

        for idname in self.variableNameList:
            if idname.getID() != self.getXIndex() and idname.getID() != self.getYIndex():
                retListVarIds.append(idname.getID())
                retListVarNames.append(idname.getNAME())

        retListCoordsIds = [self.getXIndex(), self.getYIndex()]
        retListCoordsNames = [self.getXName(), self.getYName()]

        #print(retListCoordsIds, retListCoordsNames, retListVarIds, retListVarNames)
    
        return(retListCoordsIds, retListCoordsNames, retListVarIds, retListVarNames)
   
