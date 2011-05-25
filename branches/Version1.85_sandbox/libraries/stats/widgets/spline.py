"""
<name>Spline Fit</name>
<author>Generated using Widget Maker written by Kyle R. Covington</author>
<Description>Generates a spline fit to X, Y data.  This can be used for plotting or for interogating the splines.</Description>
<RFunctions>stats:spline</RFunctions>
<tags>Parametric</tags>
<icon>stats.png</icon>
"""
from OWRpy import * 
import redRGUI, signals
import redRGUI 


class spline(OWRpy): 
    settingsList = []
    def __init__(self, **kwargs):
        OWRpy.__init__(self, **kwargs)
        self.setRvariableNames(["spline"])
        self.data = {}
        self.RFunctionParam_y = ''
        self.RFunctionParam_x = ''
        self.inputs.addInput('id0', 'y', signals.base.RVector, self.processy)
        self.inputs.addInput('id1', 'x', signals.base.RVector, self.processx)

        self.outputs.addOutput('id0', 'spline Output', signals.base.RModelFit)
        self.outputs.addOutput('id1', 'spline plot attribute', signals.plotting.RPlotAttribute)

        
        self.standardTab = redRGUI.base.groupBox(self.controlArea, label = 'Parameters')
        self.RFunctionParamxmin_lineEdit =  redRGUI.base.lineEdit(self.standardTab,  label = "xmin:", text = 'min(x)')
        self.RFunctionParamties_lineEdit =  redRGUI.base.lineEdit(self.standardTab,  label = "ties:", text = 'mean')
        self.RFunctionParammethod_lineEdit =  redRGUI.base.lineEdit(self.standardTab,  label = "method:", text = '"fmm"')
        self.RFunctionParamxmax_lineEdit =  redRGUI.base.lineEdit(self.standardTab,  label = "xmax:", text = 'max(x)')
        self.RFunctionParamn_lineEdit =  redRGUI.base.lineEdit(self.standardTab,  label = "n:", text = '3*length(x)')
        
        self.xcolumnComboBox = redRGUI.base.comboBox(self.standardTab, label = 'X data')
        self.ycolumnComboBox = redRGUI.base.comboBox(self.standardTab, label = 'Y data')
        redRGUI.base.commitButton(self.bottomAreaRight, "Commit", callback = self.commitFunction)
        self.RoutputWindow = redRGUI.base.textEdit(self.controlArea, label = "RoutputWindow")
    def processy(self, data):
        if not self.require_librarys(["stats"]):
            self.status.setText('R Libraries Not Loaded.')
            return
        if data:
            self.RFunctionParam_y=data.getData()
            #self.data = data
            self.commitFunction()
        else:
            self.RFunctionParam_y=''
    def processx(self, data):
        if not self.require_librarys(["stats"]):
            self.status.setText('R Libraries Not Loaded.')
            return
        if data:
            self.RFunctionParam_x=data.getData()
            self.data = data
            colnames = self.R('colnames('+self.RFunctionParam_x+')', wantType = 'list')
            if len(colnames) > 1:
                self.xcolumnComboBox.update(colnames)
                self.ycolumnComboBox.update(colnames)
            else:
                self.xcolumnComboBox.clear()
                self.ycolumnComboBox.clear()
            self.commitFunction()
        else:
            self.RFunctionParam_x=''
    def commitFunction(self):
        if unicode(self.ycolumnComboBox.currentText()) == '':
            if unicode(self.RFunctionParam_y) == '': return
            if unicode(self.RFunctionParam_x) == '': return
        else:
            data = self.data.getData()
            self.RFunctionParam_x = data+'$'+unicode(self.xcolumnComboBox.currentText())
            self.RFunctionParam_y = data+'$'+unicode(self.ycolumnComboBox.currentText())
        injection = []
        if unicode(self.RFunctionParamxmin_lineEdit.text()) != '':
            string = 'xmin='+unicode(self.RFunctionParamxmin_lineEdit.text())+''
            injection.append(string)
        if unicode(self.RFunctionParamties_lineEdit.text()) != '':
            string = 'ties='+unicode(self.RFunctionParamties_lineEdit.text())+''
            injection.append(string)
        if unicode(self.RFunctionParammethod_lineEdit.text()) != '':
            string = 'method='+unicode(self.RFunctionParammethod_lineEdit.text())+''
            injection.append(string)
        if unicode(self.RFunctionParamxmax_lineEdit.text()) != '':
            string = 'xmax='+unicode(self.RFunctionParamxmax_lineEdit.text())+''
            injection.append(string)
        if unicode(self.RFunctionParamn_lineEdit.text()) != '':
            string = 'n='+unicode(self.RFunctionParamn_lineEdit.text())+''
            injection.append(string)
        inj = ','.join(injection)
        self.R('x <- as.vector('+unicode(self.RFunctionParam_x)+')')
        self.R(self.Rvariables['spline']+'<-spline(x = as.vector('+unicode(self.RFunctionParam_x)+'),y=as.vector('+unicode(self.RFunctionParam_y)+'),'+','+inj+')')
        self.R('rm(x)')
        self.R('txt<-capture.output('+self.Rvariables['spline']+')')
        self.RoutputWindow.clear()
        tmp = self.R('paste(txt, collapse ="\n")')
        self.RoutputWindow.insertHtml('<br><pre>'+tmp+'</pre>')
        newData = signals.base.RModelFit(self, data = self.Rvariables["spline"]) # moment of variable creation, no preexisting data set.  To pass forward the data that was received in the input uncomment the next line.
        #newData.copyAllOptinoalData(self.data)  ## note, if you plan to uncomment this please uncomment the call to set self.data in the process statemtn of the data whose attributes you plan to send forward.
        self.rSend("id0", newData)
        
        newLine = signals.plotting.RPlotAttribute(self, data = 'lines('+self.Rvariables['spline']+')')
        self.rSend("id1", newLine)