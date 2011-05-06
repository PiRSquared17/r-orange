"""
<name>Extract Predictions and Probs (Caret)</name>
<author>Generated using Widget Maker written by Kyle R. Covington</author>
<description></description>
<RFunctions>caret:train</RFunctions>
<tags>Prototypes</tags>
<icon></icon>
"""
from OWRpy import * 
from libraries.base.qtWidgets.lineEdit import lineEdit as redRlineEdit 
from libraries.base.qtWidgets.radioButtons import radioButtons as redRradioButtons 
from libraries.base.qtWidgets.comboBox import comboBox as redRcomboBox 
from libraries.base.qtWidgets.checkBox import checkBox as redRcheckBox 
from libraries.base.qtWidgets.textEdit import textEdit as redRtextEdit 
from libraries.base.qtWidgets.RFormulaEntry import RFormulaEntry as redRRFormulaEntry
from libraries.base.qtWidgets.widgetLabel import widgetLabel
import libraries.base.signalClasses as signals
import libraries.RedRCaret.signalClasses as caret

class extractPredsProbs(OWRpy): 
    settingsList = []
    def __init__(self, **kwargs):
        OWRpy.__init__(self, **kwargs)
        self.require_librarys(["caret"])
        self.setRvariableNames(["preds", 'probs'])
        self.data = {}
        self.RFunctionParam_predictions = ''
        self.RFunctionParam_classes = ''
        self.inputs.addInput("data", "Fitted Prediction Model", signals.RModelFit.RModelFit, self.processdata, multiple = True)
        self.inputs.addInput('predicationData', 'Classification Data', caret.CaretData.CaretData, self.processpreds)
        self.outputs.addOutput("predictions","Caret Predictions", signals.RDataFrame.RDataFrame)
        self.outputs.addOutput("probabilities", "Caret Probabilities", signals.RDataFrame.RDataFrame)
        self.widgetLabel = widgetLabel(self.bottomAreaLeft, label = '')
        self.RoutputWindow = redRtextEdit(self.controlArea, label = "R Output Window")
        redRCommitButton(self.bottomAreaRight, "Commit", callback = self.commitFunction)
    def processpreds(self, data):
        if data:
            self.RFunctionParam_predictions = data.getData()
            self.RFunctionParam_classes = data.getClasses()
            self.commitFunction()
        else:
            self.RFunctionParam_predictions = ''
            self.RFunctionParam_classes = ''
    def processdata(self, data, id):
        
        if data:
            self.data[id] = data.getData()
            self.commitFunction()
        else:
            self.data[id] = None
            
    def commitFunction(self):
        if self.RFunctionParam_predictions == '':
            self.status.setText('No classification data')
            return
        models = [i for i in self.data.values() if i != None]
        if len(models) == 0:
            self.status.setText('No data to predict on')
            return
        dataInputs = {'MODEL':','.join(models), 'PRED':self.Rvariables['preds'], 'PROB':self.Rvariables['probs']}
        if self.RFunctionParam_predictions != '':
            dataInputs['testX'] = self.RFunctionParam_predictions
        else:
            dataInputs['testX'] = 'NULL'
        if self.RFunctionParam_classes != '':
            dataInputs['testY'] = self.RFunctionParam_classes
        else:
            dataInputs['testY'] = 'NULL'
            
        tmp = ''
        try:
            self.R('%(PRED)s<-extractPrediction(list(%(MODEL)s), testX = %(testX)s, testY = %(testY)s)' % dataInputs, wantType = 'NoConversion') 
            newDataPred = signals.RDataFrame.RDataFrame(self, data = self.Rvariables['preds'])
            self.rSend("predictions", newDataPred)
            tmp += 'Predictions\n\n'
            tmp += self.R('paste(capture.output(str('+self.Rvariables['preds']+')), collapse ="\n")') + '\n\n'
        except RuntimeError:
            self.widgetLabel.setText('Could not format predicitons')
            self.rSend('predictions', None)
            
        try:
            self.R('%(PROB)s<-extractProb(list(%(MODEL)s), testX = %(testX)s, testY = %(testY)s)' % dataInputs, wantType = 'NoConversion')
            newDataProbs = signals.RDataFrame.RDataFrame(self, data = self.Rvariables['probs'])
            self.rSend('probabilities', newDataProbs)
            tmp += 'Probabilities\n\n'
            tmp += self.R('paste(capture.output(str('+self.Rvariables['probs']+')), collapse ="\n")')
        except RuntimeError:
            self.widgetLabel.setText('Could not format predictions')
            self.rSend('probabilities', None)
        
        
        
        self.RoutputWindow.clear()
        self.RoutputWindow.insertPlainText(tmp)