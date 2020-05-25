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
import itertools

from config import config as cfg

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
## class ELLIPSE: manage variables search procedure                         ##
#############################################################################

class ELLIPSE():
    def __init__(self, _d, _t):
        self.direction = _d
        self.tolerance = _t

    def __eq__(self, _other):
        return self.direction == _other.getDirection() and self.tolerance == _other.getTolerance()

    def getDirection(self):
        return self.direction

    def getTolerance(self):
        return self.tolerance

    def isCircular(self, _r):
        return _r == self.tolerance

#############################################################################
## class mstaPoint: manage data points                                     ##
#############################################################################

class mstaPoint(QgsPoint):
    def __init__(self, _x, _y):
        """Constructor."""
        super().__init__(_x, _y)
        self.ID = 0
        self.variables = [] # List of mstaVariable type

    def __repr__(self):
        return(f'ID: {self.ID}, {super().asWkt()}\n\t{[i for i in  self.variables]}')

    def setID(self, _ID):
        self.ID = _ID

    def getID(self):
        return self.ID

    def getVariables(self):
        return self.variables

    def updateVariable(self, _newVar):
        for v in self.variables:
            if v.getName() == _newVar.getName():
                # Backup the value of the variable for this point because this is the only field
                # the user cannot change/modify
                _newVar.setValue(v.getValue())
                # Delete the variable to update in the list
                del self.variables[self.variables.index(v)]
                # Append the updated variable
                self.variables.append(_newVar)
                return

    def addVariable(self, _newvar):
        # Check if _newvar is still present the variable list at this point
        #if _newvar in self.variables and not isinstance(mstaVariable, _newvar):
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
    mVR = itertools.count()
    def __init__(self):
        """Constructor."""
        self.ID = next(mstaVariable.mVR)
        self.name = ""
        self.alias = ""
        self.unit = self.setUnit("%") #Default value, i.e. percent
        self.value = 0.0
        self.dg = 0.0
        self.range = 0.0 # +/- range centred around value
        self.search = ELLIPSE(0.0,  self.dg) # By default circle search

    # Default operations
    # + addition
    def __add__(self, _other):
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
    def __iadd__(self, _other):
        self.range = self.getRange()+self._other.getRange()
        self.value = self.value+_other.getValue()
        return self
    # - substraction
    def __sub__(self, _other):
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
    def __isub__(self, _other):
        self.range = self.getRange()+self._other.getRange()
        self.value = self.value-_other.getValue()
        return self
    # * multiplication
    def __mul__(self, _other):
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
    def __imul__(self, _other):
        self.range = (_other.getValue()*self.getRange())+(self.getValue()*_other.getRange())
        self.setvalue = self.value*_other.getValue()
        return self
    # / division
    def __truediv__(self, _other):
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
    def __itruediv__(self, _other):
        self.range = (1/_other.getValue())*(self.getRange()+(self.getValue()/_other.getgetValue()*_other.getRange()))
        self.value = self.value / _other.getValue()
        return self
    # == equality
    def __eq__(self, _other):
        if self.isInRange(_other.getValue()) or _other.isInRange(self.getValue()):
            return True
        else:
            return False
    # != non equility
    def __ne__(self, _other):
        if not self.isInRange(_other.getValue()) and not _other.isInRange(self.getValue()):
            return True
        else:
            return False
    # < lower than
    def __lt__(self, _other):
        return(self.getMax() < _other.getMin())
    def __le__(self, _other):
        return(self.getMax() <= _other.getMin())
    # > upper thn
    def __gt__(self, _other):
        return(self.getMin() > _other.getMax())
    def __ge__(self, _other):
        return(self.getMin() >= _other.getMax())

    # Print itself
    def __repr__(self):
        return(f'Name: {self.name}, alias: {self.alias}\n \
                distance: {self.dg}, unit: {self.unit}\n \
                range: +/-{self.getRange()}\n \
                dir : {self.getDirection()}, Tol: {self.getTolerance()}')

    # Test if the current variable as same Dg, direction and tolerance than variable _other
    # convenient during process
    def isEqual(self, _other):
        retValue = True
        if self.getDg() != _other.getDg():
            retValue = False
        if self.getSearch() != _other.getSearch():
            retValue = False
        if self.getUnit() != _other.getUnit():
            retValue = False
        return retValue

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
        assert _unit in UNIT.keys()
        self.unit = _unit
    def getUnit(self):
        return self.unit

    def setValue(self,_value):
        self.value = _value
    def getValue(self):
        return self.value

    def getMin(self):
        return self.value - self.getRange()
    def getMax(self):
        return self.value + self.getRange()

    def setSearch(self,_d, _t):
        assert isinstance(_d, float)
        assert isinstance(_t, float)
        self.search = ELLIPSE(_d,_t)
    def getSearch(self):
        return self.search

    def getDirection(self):
        return self.search.getDirection() # Direction is stored as the first element of the list
    def getTolerance(self):
        return self.search.getTolerance() # Tol. angle is stored as the second element of the list

    def setDg(self, _dg):
        assert isinstance(_dg, float)
        self.dg = _dg
    def getDg(self):
        return self.dg

    def setRange(self, _pm):
        assert isinstance(_pm, float)
        self.range = _pm
    def getRange(self):
        return self.range

    def isInRange(self, _value):
        return(_value >= self.getMin() and _value <= self.getMax())

    # Return False only for phi units and other (not affected)
    def isMetric(self):
        return not (self.getUnit() == UNIT['phi'] or self.getUnit() == UNIT['other'])

#############################################################################
## class mstaTrendCase: manage trend case                                  ##
#############################################################################
class mstaTrendCase():
    mTC = itertools.count()
    def __init__(self, _variables = None, _comp = None):
        """Constructor."""
        self.ID = next(mstaTrendCase.mTC)
        # Normally one case should be defined for same variable but
        # it is eventually possible to manage 2 different variables
        if isinstance(_variables, list): # Two different variables
            assert len(_variables) == 2
            assert _comp in COMP.keys()
            assert isinstance(_variables[0], mstaVariable) and isinstance(_variables[1], mstaVariable)
            self.compSigne = COMP[_comp]
            self.leftVar = _variables[0]
            self.rightVar = _variables[1]
        elif _variables: # Same variable
            assert _comp in COMP.keys()
            assert isinstance(_variables, mstaVariable)
            self.compSigne = COMP[_comp]
            self.leftVar = _variables
            self.rightVar = _variables
        else: # Default init
            self.compSigne = COMP['none']
            self.leftVar = mstaVariable()
            self.rightVar = mstaVariable()

    # Print itself
    def __str__(self):
        if self.compSigne != '':
            return (f'{self.ID}:{self.leftVar.getName()}(i) {self.compSigne} {self.rightVar.getName()}(j)')
        else:
            return ''

    def __repr__(self):
        if self.compSigne != '':
            return (f'{self.ID}:{self.leftVar.getAlias()}(i) {self.compSigne} {self.rightVar.getAlias()}(j)')
        else:
            return ''

    # define equality or not between two mstaTrendCase objects
    def __eq__(self,_other):
        assert isinstance(_other, mstaTrendCase)
        if self.getLeftVar().getName() == _other.getLeftVar().getName() and \
           self.getRightVar().getName() == _other.getRightVar().getName() and \
           self.getComp() == _other.getComp():
            return True
        else:
            return False

    # Convenient to test if a case is of type GSTA. mstaTrendCase are never of type GSTA -> always False
    def isGSTATrend(self):
        return False

    # Use for specific printing in case of a GSTA trend
    def getGSTATrendText(self):
        assert isinstance(self.leftVar, mstaVariable)
        assert isinstance(self.rightVar, mstaVariable)
        assert self.leftVar.getAlias() == self.rightVar.getAlias()  # The variables have to be the same (m, sd or sk)
        if self.leftVar.getAlias() == "mean":  # Mean
            if self.compSigne == COMP['sup']:
                if self.leftVar.isMetric():
                    return 'F'
                else:
                    return 'C'
            else:
                if self.leftVar.isMetric():
                    return 'C'
                else:
                    return 'F'
        elif self.leftVar.getAlias() == "sorting":  # Sorting
            if self.compSigne == COMP['sup']:
                return 'B'
            else:
                return 'P'
        else:  # Skewness
            if self.compSigne == COMP['sup']:
                if self.leftVar.isMetric():
                    return '-'
                else:
                    return '+'
            else:
                if self.leftVar.isMetric():
                    return '+'
                else:
                    return '-'

    def getID(self):
        return self.ID

    def setComp(self, _op):
        assert _op != ''
        self.compSigne = COMP[_op]

    def getComp(self):
        return(self.compSigne)

    def setLeftVar(self, _var):
        assert isinstance(_var, mstaVariable)
        self.leftVar = _var

    def getLeftVar(self):
        return self.leftVar

    def setRightVar(self, _var):
        assert isinstance(_var, mstaVariable)
        self.rightVar = _var

    def getRightVar(self):
        return self.rightVar

#############################################################################
## class mstaComposedTrendCase: manage trend case                          ##
#############################################################################
class mstaComposedTrendCase():
    mCTC = itertools.count()
    # By default _trendCase is null, but most of the time a mstaComposedTrendCase is
    # initialized with a simple trend case or a list of trend case (GSTA). In this latter case _op must be given also.
    def __init__(self, _trendCase = None, _op = None):
        self.ID = next(mstaComposedTrendCase.mCTC)
        """Constructor."""
        self.composedGSTATrend = False # by default it is false, can be change through dedicated function
        if isinstance(_trendCase, list): # list of trend case
            assert _op in OPERAND.values()
            self.trendsList = _trendCase
            self.linkOperand = _op # whatever the trend cases number, only one type of operand links them all
        elif isinstance(_trendCase, mstaTrendCase): # simple trend case (just one)
            assert _op in OPERAND.values()
            self.trendsList = [_trendCase]
            # TODO: verifier qu'il est necessaire de donner un operand a tous les coups
            # voir si on ne peut/doit pas gérer ici le cas ou _op est "None"
            self.linkOperand = _op
        else:
            self.trendsList = []
            self.linkOperand = OPERAND['none']

    def __getitem__(self, item):
            return self.trendsList[item]

    def __repr__(self): # Full printing of trend case without taking care of simple or complex cases (GSTA)
        if len(self.trendsList) == 0:
            return
        retValue = ""
        for t in self.trendsList:
            retValue += t.__repr__() + '\n'
        retValue += self.linkOperand + '\n'
        return(retValue)

    def __str__(self): # Complex print which take care of GSTA like trend cases
        if len(self.trendsList) == 0:
            return
        retValue = ""
        for t in self.trendsList:
            if t.isGSTATrend():
                retValue += t.getGSTATrendText()
            else:
                retValue += (t.__str__() + '\n')
        retValue += self.linkOperand + '\n'
        return(retValue)

    # For convenience and to be homogeneous with mstaTrendCase class
    def getGSTATrendText(self):
        return self.__str__()

    def setComposedGSTATrend(self, _bool):
        self.composedGSTATrend = _bool

    def isGSTATrend(self):
        return self.composedGSTATrend

    def getID(self):
        return self.ID

    # Equality between two mstaComposedTrendCase objects
    def __eq__(self,_other):
        assert isinstance(_other, mstaComposedTrendCase)
        if self.getTrendCount() != _other.getTrendCount(): # if not same length of trend list -> equal = False
            return False
        # Both list have same length
        for i in range(self.getTrendCount()):
            if self.getTrend(i) != _other.getTrend(i): # It is consider that order is the same in both list
                return False
        return True

    # return the higher ID of mstaTrendCase object in the list
    def getMaxCaseID(self):
        if len(self.trendsList) > 0:
            return max(t.getID for t in self.trendsList)
        else:
            return 0

    # Change the operand
    def setOperand(self, _op):
        assert _op in OPERAND.values()
        self.linkOperand = _op

    def getTrend(self, *args):
        if len(args) > 0:
            _id = args[0]
            assert _id < len(self.trendsList)
            return self.trendsList[_id]
        else:
            return self.trendsList

    def getFirstTrend(self):
        assert len(self.trendsList) >= 1
        return self.trendsList[0]

    def getLastTrend(self):
        assert len(self.trendsList) >= 1
        return self.trendsList[-1]

    def getTrendCount(self):
        return len(self.trendsList)

    def addTrendCase(self, _trendcase, _operand):
        assert isinstance(_trendcase, mstaTrendCase) or isinstance(_trendcase, mstaComposedTrendCase)
        assert _operand in OPERAND.values()
        self.linkOperand = _operand
        self.trendsList.append(_trendcase)

    def deleteTrendCase(self, _trendcase):
        for t in self.trendsList:
            if t == _trendcase:
                index = self.trendsList.index(t)
                self.trendsList.remove(t)
        return


   