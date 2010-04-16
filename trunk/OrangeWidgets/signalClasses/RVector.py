from PyQt4.QtCore import *
from PyQt4.QtGui import *
from RSessionThread import Rcommand
from RDataFrame import RDataFrame
class RVector(RDataFrame):
    def __init__(self, data, parent = None, cm = None):
        #if not cm: # we should give a cm to the 
            #cm = self.R('cm_'+data+'<-data.frame(row.names = make.names(rep(1, length('+data+'))))')
        RDataFrame.__init__(self, data = data, parent = parent, cm = cm)
    def copy(self):
        newVariable = RVector(self.data, self.parent, self.cm)
        newVariable['dictAttrs'] = self.dictAttrs
        return newVariable
    def getSimpleOutput(self, subsetting = '[1:5]'):
        # return the text for a simple output of this variable
        text = 'Simple Output\n\n'
        text += 'Class: '+self.getClass_data()+'\n\n'
        text += self._simpleOutput(subsetting)
        return text
    
    def getColumnnames_call(self):
        return self.getNames_call()
    def getColumnnames_data(self):
        return self.getNames_data()
    def getNames_call(self):
        return self.data
    def getNames_data(self):
        return self.data # the only name to speek of the name of the variable

    def getRange_call(self, rowRange = None, colRange = None):
        if rowRange == None: return self.data
        else: return self.data+'['+str(rowRange)+']'
        
        