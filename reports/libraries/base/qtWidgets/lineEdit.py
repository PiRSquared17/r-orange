from redRGUI import widgetState
from libraries.base.qtWidgets.widgetBox import widgetBox
from libraries.base.qtWidgets.widgetLabel import widgetLabel

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class lineEdit(QLineEdit,widgetState):
    def __init__(self,widget,text='', label=None, displayLabel=True, includeInReports=True,
    id=None, orientation='horizontal', toolTip = None,  width = 0, callback = None, textChangedCallBack=None,
    sp='shrinking', **args):

        widgetState.__init__(self,widget,label,includeInReports)
        QLineEdit.__init__(self,widget)
        
        if displayLabel:
            self.hb = widgetBox(self.controlArea,orientation=orientation, spacing=2)
            if sp == 'shrinking':
                self.hb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            widgetLabel(self.hb, label)
            if width != -1:
                sb = widgetBox(self.hb)
                sb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            self.hb.layout().addWidget(self)
        else:
            self.controlArea.layout().addWidget(self)
        
        if toolTip and displayLabel: 
            self.hb.setToolTip(toolTip)
        elif toolTip:
            self.setToolTip(toolTip)
            
        if width == 0:
            self.setMaximumWidth(175)
            self.setMinimumWidth(175)
        elif width == -1:
            pass
        else:
            self.setMaximumWidth(width)
            self.setMinimumWidth(width)
        self.setText(text)
        self.id = id
        self.label = label
        # self.setText('asdf')
        if callback:
            QObject.connect(self, SIGNAL('returnPressed()'), callback)
        
        if textChangedCallBack:
            QObject.connect(self, SIGNAL('textEdited(QString)'), textChangedCallBack)
    
    def text(self):
        return str(QLineEdit.text(self).toAscii())
    def widgetId(self):
        return self.id
    def widgetLabel(self):
        return self.label
    def getSettings(self):
        #print 'in get settings' + self.text()
        r = {'text': self.text(),'id': self.id}
        # print r
        return r
    def loadSettings(self,data):
        try:
            #print 'called load' + str(value)     
            self.setText(data['text'])
            if 'id' in data.keys():
                self.id = data['id']
            #self.setEnabled(data['enabled'])
        except:
            print 'Loading of lineEdit encountered an error.'
            
    def getReportText(self, fileDir):
        r = {self.widgetName:{'includeInReports': self.includeInReports, 'text': self.text()}}
        return r