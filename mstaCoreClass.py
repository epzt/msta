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

from qgis.core import QgsPoint
import numpy as np

# Trend operations
TREND = {
    'sup' : '>',
    'inf' : '<',
    'none' : ''
}

# Operand operations
OPERAND = {
    'ou' : 'OR',
    'et' : 'AND',
    'xou' : 'XOR',
    'none' : ''
}

# Unit of variables
UNIT = {
    'percent' : '%',
    'metre' : 'm',
    'phi' : 'phi',
    'other' : 'unknown'
}

#############################################################################
## class RANGE: manage variables range                                     ##
#############################################################################
'''
class RANGE():
    def __init__(self, _min, _max):
        self.min = _min
        self.max = _max

    def __repr__(self):
        return(f'min: {self.min} - max: {self.max}')

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max

    def getDeltaRange(self):
        return(self.max - self.min)
'''
#############################################################################
## class RADIUS: manage variables search procedure                         ##
#############################################################################

class RADIUS():
    def __init__(self, _a, _b):
        self.major = _b
        self.minor = _a

    def getMinor(self):
        return self.minor

    def getMajor(self):
        return self.major

    def isCircle(self):
        return((self.major-self.minor) == 0)

#############################################################################
## class mstaPoint: manage data points                                     ##
#############################################################################

class mstaPoint(QgsPoint):
    def __init__(self, _x, _y):
        """Constructor."""
        super().__init__(_x,_y)
        self.ID = 0
        self.variables = []

    def __repr__(self):
        return(f'ID: {self.ID}, {super().asWkt()}\n\t{[i for i in  self.variables]}')

    def setID(self,_ID):
        self.ID = _ID

    def getID(self):
        return self.ID

    def getVariablesName(self):
        return self.variables

    def addVariable(self, _newvar):
        # Check if _newvar is still present the variable list at this point
        if _newvar in self.variables:
            return False
        self.variables.append(_newvar)
        return(True)

    def getVariableByName(self, _varname):
        retValue = None
        for i in self.variables:
            if i.getName() == _varname:
                retValue = i
                break
        return retValue

    def getVariableByID(self, _varid):
        retValue = None
        for i in self.variables:
            if i.getID() == _varid:
                retValue = i
                break
        return retValue

    def getVariableValueByName(self, _varname):
        self.getVariableByName(_varname).getValue()

    def getVariableValueByID(self, _varid):
        self.getVariableByID(_varid).getValue()


#############################################################################
## class mstaVariable: manage variable                                     ##
#############################################################################
class mstaVariable():
    def __init__(self):
        """Constructor."""
        self.ID = 0
        self.name = ""
        self.alias = ""
        self.unit = "other" #Default value, i.e. unknown type
        self.value = 0.0
        self.dg = 0.0
        self.range = 0.0 # +/- range centred around value
        self.search = RADIUS(0.0,0.0)

    # Default operations
    # +
    def __add__(self,_other):
        res = mstaVariable()
        if not _other.__class__ is mstaVariable:
            return NotImplemented
        if self.getUnit() != _other.getUnit():
            return NotImplemented
        else:
            res.setUnit(self.getUnit())
        if self.getName() != _other.getName():
            res.setName(f'{self.getName()}/{_other.getName()}')
        else:
            res.setName(self.getName())
        res = mstaVariable()
        res.setRange(self.getRange()+self._other.getRange())
        res.setValue(self.getValue()+_other.getValue())
        return res
    def __iadd__(self,_other):
        self.range = self.getRange()+self._other.getRange()
        self.value = self.value+_other.getValue()
        return self
    # -
    def __sub__(self,_other):
        res = mstaVariable()
        if not _other.__class__ is mstaVariable:
            return NotImplemented
        if self.getUnit() != _other.getUnit():
            return NotImplemented
        else:
            res.setUnit(self.getUnit())
        if self.getName() != _other.getName():
            res.setName(f'{self.getName()}/{_other.getName()}')
        else:
            res.setName(self.getName())
        res = mstaVariable()
        self.setRange(self.getRange()+self._other.getRange())
        res.setValue(self.getValue()-_other.getValue())
        return res
    def __isub__(self,_other):
        self.range = self.getRange()+self._other.getRange()
        self.value = self.value-_other.getValue()
        return self
    # *
    def __mul__(self,_other):
        res = mstaVariable()
        if not _other.__class__ is mstaVariable:
            return NotImplemented
        if self.getUnit() != _other.getUnit():
            return NotImplemented
        else:
            res.setUnit(self.getUnit())
        if self.getName() != _other.getName():
            res.setName(f'{self.getName()}/{_other.getName()}')
        else:
            res.setName(self.getName())
        res = mstaVariable()
        res.range = (_other.getValue()*self.getRange())+(self.getValue()*_other.getRange())
        res.setValue(self.getValue()*_other.getValue())
        return res
    def __imul__(self,_other):
        self.range = (_other.getValue()*self.getRange())+(self.getValue()*_other.getRange())
        self.setvalue = self.value*_other.getValue()
        return self

    # /
    def __truediv__(self, other):
        res = mstaVariable()
        if not _other.__class__ is mstaVariable:
            return NotImplemented
        if self.getUnit() != _other.getUnit():
            return NotImplemented
        else:
            res.setUnit(self.getUnit())
        if self.getName() != _other.getName():
            res.setName(f'{self.getName()}/{_other.getName()}')
        else:
            res.setName(self.getName())
        res = mstaVariable()
        res.range = (1/_other.getValue())*(self.getRange()+(self.getValue()/_other.getgetValue()*_other.getRange()))
        res.setValue(self.getValue() / _other.getValue())
        return res
    def __itruediv__(self, other):
        self.range = (1/_other.getValue())*(self.getRange()+(self.getValue()/_other.getgetValue()*_other.getRange()))
        self.value = self.value / _other.getValue()
        return self
    # ==
    def __eq__(self,_other):
        if self.isInRange(_other.getValue()) or _other.isInRange(self.getValue()):
            return True
        else:
            return False
    # !=
    def __ne__(self,_other):
        if not self.isInRange(_other.getValue()) and not _other.isInRange(self.getValue()):
            return True
        else:
            return False
    # <
    def __lt__(self,_other):
        return(self.getMax() < _other.getMin())
    def __le__(self,_other):
        return(self.getMax() <= _other.getMin())
    # >
    def __gt__(self,_other):
        return(self.getMin() > _other.getMax())
    def __ge__(self,_other):
        return(self.getMin() >= _other.getMax())

    # Print itself
    def __repr__(self):
        return(f'Name: {self.name}, alias: {self.alias} unit: {self.unit}\n \
                value: {self.value}, distance: {self.dg}\n \
                range: {self.getMin()},{self.getMax()}')

    def setID(self,_ID):
        self.ID = _ID
    def getID(self):
        return self.ID

    def setName(self,_name):
        self.name = _name
    def getName(self):
        return self.name

    def setAlias(self,_alias):
        self.alias = _alias
    def getAlias(self):
        return self.alias

    def setUnit(self,_unit):
        assert UNIT[_unit] != ''
        self.unit = _unit
    def getUnit(self):
        return UNIT[self.unit]

    def setValue(self,_value):
        self.value = _value
    def getValue(self):
        return self.value

    def getMin(self):
        return self.value - self.getRange()
    def getMax(self):
        return self.value + self.getRange()

    def setSearch(self,_a, _b):
        self.search = [_a,_b]
    def getSearch(self):
        return self.search
    def getDirection(self):
        return self.search[0] # Direction is stored as the first element of the list
    def getToleranceAngle(self):
        return self.search[1] # Tol. angle is stored as the second element of the list

    def setDg(self, _dg):
        self.dg = _dg
    def getDg(self):
        return self.dg

    def setRange(self, _pm):
        self.range = _pm
    def getRange(self):
        return self.range

    def isInRange(self, _value):
        return(_value >= self.getMin() and _value <= self.getMax())

#############################################################################
## class mstaTrendCase: manage trend case                                  ##
#############################################################################
class mstaTrendCase():
    def __init__(self, _variable):
        """Constructor."""
        self.ID = -1
        self.trend = TREND['none']
        assert _variable
        # Normally one case should be defined for same variable but
        # it is eventually possible to manage 2 different variables
        if isinstance(_variable, list):
            assert len(_variable) == 2
            self.leftVar = _variable[0]
            self.rightVar = _variable[1]
        else:
            self.leftVar = _variable
            self.rightVar = _variable

    # Print itself
    def __repr__(self):
        return (f'{self.leftVar} {TREND[self.trend]} {self.rightVar}')

    def getID(self):
        return self.ID

    def setID(self, _id):
        assert _id >= 0
        self.ID = _id

    def setOperand(self, _op):
        assert TREND[_op]
        self.trend = TREND[_op]

    def getOperand(self):
        return(self.trend)

    def setLeftVar(self, _var):
        self.leftVar = _var

    def setRightVar(self, _var):
        self.rightVar = _var

#############################################################################
## class mstaComposedTrendCase: manage trend case                          ##
#############################################################################
class mstaComposedTrendCase():
    def __init__(self):
        """Constructor."""
        self.ID = -1
        self.linkOperand = []
        self.trendList = []

    def getID(self):
        return self.ID

    def setID(self, _id):
        assert _id >= 0
        self.ID = _id

    def getTrend(self, _id):
        assert _id <= len(self.trendList)
        return self.trendList[_id]

    def getFirstTrend(self):
        assert len(self.trendList) >= 1
        return self.trendList[0]

    def getLastTrend(self):
        assert len(self.trendList) >= 1
        return self.trendList[len(self.trendList)-1]

    def addTrendCase(self, _trendcase, _operand):
        assert isinstance(_trendcase, mstaTrendCase)
        # if more than one trend case
        if len(self.trendList) > 0:
            assert OPERAND[_operand] # is _operand valid

        self.trendList.append(_trendcase)
        self.operand.append(OPERAND[_operand])
        # there must be (operand + 1) trend cases
        assert len(self.trendList) == len(self.linkOperand) + 1

   