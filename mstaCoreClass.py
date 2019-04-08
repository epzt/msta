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

# Trend operations
TREND = {
   'sup' : '>',
   'inf' : '<',
}

# Operand operations
OPERAND = {
   'ou' : 'OR',
   'et' : 'AND',
   'xou' : 'XOR',
}

#############################################################################
## class RANGE: manage variables range                                     ##
#############################################################################

class RANGE():
   def __init__(self, _min, _max):
      self.min = _min
      self.max = _max

   def getMin(self):
      return self.min

   def getMax(self):
      return self.max

   def getDeltaRange(self):
      return(self.max - self.min)


#############################################################################
## class mstaPoint: manage data points                                     ##
#############################################################################

class mstaPoint(QgsPoint):
   def __init__(self):
      """Constructor."""
      self.ID = 0
      self.variables = []

   def setID(self,_ID):
      self.ID = _ID
   
   def getID(self):
      return self.ID

   def addVariable(self,newvar):
      # Check if newvar is still present the variable list at this point
      if newvar in self.variables:
         return False
      self.variables.append(newvar)
      return(True)

   def getVariableByName(self, varname):
      retValue = False
      for i in self.variables:
         if i.getName() == varname:
            retValue = i
            break
      return retValue

   def getVariableByID(self, varid):
      retValue = False
      for i in self.variables:
         if i.getID() == varid:
            retValue = i
            break
      return retValue
      


#############################################################################
## class mstaVariable: manage variable                                     ##
#############################################################################
class mstaVariable():
   def __init__(self):
      """Constructor."""
      self.ID = 0
      self.name = ""
      self.unit = ""
      self.value = 0.0
      self.range = RANGE(0.0,0.0)
      self.search = []

   # Default operations
   # +
   def __add__(self,other):
      res = mstaVariable()
      if not other.__class__ is mstaVariable:
         return NotImplemented
      if self.getUnit() != other.getUnit():
         return NotImplemented
      else:
         res.setUnit(self.getUnit())
      if self.getName() != other.getName():
         res.setName("")
      else:
         res.setName(self.getName())
      res = mstaVariable()
      res.range = RANGE(self.getMin()+self.other.getMin(),self.getMax()+self.other.getMax())
      res.setValue(res.getDeltaRange()/2.0)
      return res
   def __iadd__(self,other):
      self.range = RANGE(self.getMin()+self.other.getMin(),self.getMax()+self.other.getMax())
      self.setValue(self.range.getDeltaRange()/2.0)
      return self
   # -
   def __sub__(self,other):
      res = mstaVariable()
      if not other.__class__ is mstaVariable:
         return NotImplemented
      if self.getUnit() != other.getUnit():
         return NotImplemented
      else:
         res.setUnit(self.getUnit())
      if self.getName() != other.getName():
         res.setName("")
      else:
         res.setName(self.getName())
      res = mstaVariable()
      res.range = RANGE(self.getMin()-self.other.getMax(),self.getMax()-self.other.getMin())
      res.setValue(res.range.getDeltaRange()/2.0)
      return res
   def __isub__(self,other):
      self.range = RANGE(self.getMin()-self.other.getMax(),self.getMax()-self.other.getMin())
      self.setValue(self.range.getDeltaRange()/2.0)
      return self
   # *
   def __mul__(self,other):
      res = mstaVariable()
      if not other.__class__ is mstaVariable:
         return NotImplemented
      if self.getUnit() != other.getUnit():
         return NotImplemented
      else:
         res.setUnit(self.getUnit())
      if self.getName() != other.getName():
         res.setName("")
      else:
         res.setName(self.getName())
      res = mstaVariable()
      lvalues = [self.getMin()*self.other.getMin(),self.getMin()*self.other.getMax(),self.getMax()*self.other.getMin(),self.getMax()*self.other.getMax()]
      res.range = RANGE(min(lvalues),max(lvalues))
      res.setValue(res.getDeltaRange()/2.0)
      return res
   def __imul__(self,other):
      lvalues = [self.getMin()*self.other.getMin(),self.getMin()*self.other.getMax(),self.getMax()*self.other.getMin(),self.getMax()*self.other.getMax()]
      self.range = RANGE(min(lvalues),max(lvalues))
      self.setValue(self.getDeltaRange()/2.0)
      return self
   # ==
   def __eq__(self,other):
      if self.isInRange(other.getValue()) or other.isInRange(self.getValue()):
         return True
      else:
         return False
   # !=
   def __ne__(self,other):
      if not self.isInRange(other.getValue()) and not other.isInRange(self.getValue()):
         return True
      else:
         return False
   # <
   def __lt__(self,other):
      return(self.getMax() < other.getMin())
   def __le__(self,other):
      return(self.range.getMax() <= other.getMin())
   # >
   def __gt__(self,other):
      return(self.getMin() > other.getMax())
   def __ge__(self,other):
      return(self.getMin() >= other.getMax())

   def setID(self,_ID):
      self.ID = _ID   
   def getID(self):
      return self.ID

   def setName(self,_name):
      self.name = _name  
   def getName(self):
      return self.name

   def setUnit(self,_unit):
      self.unit = _unit  
   def getUnit(self):
      return self.unit

   def setValue(self,_value):
      self.value = _value
   def getValue(self):
      return self.value
   def getMin(self):
      return self.range.getMin()
   def getMax(self):
      return self.range.getMax()

   def setSearch(self,_a, _b):
      self.search = [_a,_b] 
   def getSearch(self):
      if self.search[0] == self.search[1]:
         return self.search[0]
      else:
         return self.search

   def isInRange(self, value):
      return(value >= self.getMin() and value <= self.getMax())

#############################################################################
## class mstaTrendCase: manage trend case                                  ##
#############################################################################
class mstaTrendCase():
   def __init__(self):
      """Constructor."""
      self.trend = ""


#############################################################################
## class mstaComposedTrendCase: manage trend case                          ##
#############################################################################
class mstaComposedTrendCase():
   def __init__(self):
      """Constructor."""
      self.operand = ""

   