"""
<name>Significance Criteria</name>
<description>Calculates differential expression of genes from an eSet object</description>
<tags>Microarray</tags>
<RFunctions>limma:decideTests</RFunctions>
<icon>icons/readcel.png</icon>
<priority>2030</priority>
"""

import redRGUI
from OWRpy import *


class limmaDecide(OWRpy):
    def __init__(self, parent=None, signalManager=None):
        OWRpy.__init__(self, parent, signalManager, "File", wantMainArea = 0, resizingEnabled = 1)

        self.data = ''
        self.ebdata = ''
        self.olddata = None
        self.newdata = None
        
        self.eset = None
        self.sending = None
        self.modelProcessed = 0
        
        
        self.setRvariableNames(['gcm', 'eset_sub', 'geneissig', 'dfsg', 'cm', 'gcm_matrix'])
        
        
        self.inputs = [("eBayes fit", signals.RModelFit, self.process)]
        #, ('Normalized Eset', signals.RDataFrame, self.processeset)]
        self.outputs = [("Gene Change Matrix", signals.RDataFrame)]
        #("Expression Subset", signals.RDataFrame), 
        
        #GUI
        #want to have an options part, a data viewing part and a run part
        
        layk = QWidget(self)
        self.controlArea.layout().addWidget(layk)
        grid = QGridLayout()
        grid.setMargin(0)
        layk.setLayout(grid)
        
        optionsbox = redRGUI.widgetBox(self.controlArea, "Options")
        grid.addWidget(optionsbox, 0,0)
        self.dmethod = redRGUI.comboBox(optionsbox, label = "Combine Method"+"  ", items = ["separate", "global", "hierarchical", "nestedF"], orientation=0)
        self.adjmethods = redRGUI.comboBox(optionsbox, label = "P-value Adjust Methods", items = ["BH", "none", "fdr", "BY", "holm"], orientation=0)
        self.pval = redRGUI.lineEdit(optionsbox, text = '0.01', label = "Minimum p-value change:", orientation = 0)
        self.foldchange = redRGUI.lineEdit(optionsbox, text = '0', label = "Minimum fold change:", orientation = 0)
        
        computebox = redRGUI.widgetBox(self.controlArea, "Compute")
        grid.addWidget(computebox, 1,0)
        #self.infoa = redRGUI.widgetLabel(computebox, "Data not yet connected")
        # self.pickGroup = redRGUI.button(computebox, "Change Model Group Subset", tooltip = 'Change the interaction term of your model if more than one term is available.', callback = self.showModelGroupDialog)
        # self.pickGroup.setEnabled(False)
        self.runbutton = redRGUI.button(self.bottomAreaRight, "Run Analysis", callback = self.runAnalysis)
        self.runbutton.setEnabled(False)
        
        # self.modelGroupDialog = QDialog()
        # self.modelGroupDialog.setLayout(QVBoxLayout())
        #self.modelGroupDialog.setWindowTitle('Model Group for '+self.captionTitle)
        #self.modelMessage = redRGUI.widgetLabel(self.modelGroupDialog, "Choose Group For Subsetting")
        #self.modelListBox = redRGUI.listBox(self.modelGroupDialog, callback = self.sendesetsubset)
        # self.modelGroupDialog.hide()

    def showModelGroupDialog(self):
        self.modelGroupDialog.show()
    def process(self, dataset):
        self.require_librarys(['affy', 'limma'])
        self.data = '' # protect from using obsolete data
        self.removeWarning()
        if dataset == None:
            print dataset
            self.status.setText("Blank data recieved")
            self.runbutton.setEnabled(False)
            self.pickGroup.setEnabled(False)
            return
        
        self.data = dataset.data
        self.olddata = dataset
        self.ebdata = dataset
        self.status.setText("Data connected")
        self.runbutton.setEnabled(True)
        # if 'eset' in dataset.dictAttrs.keys():
        # if signals.globalDataExists('eset'):
            # self.eset = signals.getGlobalData('eset')
            #self.processeset(signals.getGlobalData('eset'))
        
        
    def runAnalysis(self):
        #self.Rvariables['gcm'] = 'gcm'+self.variable_suffix
        if self.data == '': 
            self.setWarning(id = 'NoData', text = 'No data to send')
            return # there isn't any data
        #run the analysis using the parameters selected or input
        self.R(self.Rvariables['gcm']+'<-decideTests('+self.data+', method="'+str(self.dmethod.currentText())+'", adjust.method="'+str(self.adjmethods.currentText())+'", p.value='+str(self.pval.text())+', lfc='+str(self.foldchange.text())+')')
        #self.infoa.setText("Gene Matrix Processed and sent!")
        self.R(self.Rvariables['gcm_matrix']+'<-'+self.Rvariables['gcm']+'[]')
        self.sending = signals.RMatrix(data = self.Rvariables['gcm_matrix'])
        self.rSend("Gene Change Matrix", self.sending)
        self.groupNames = self.R('colnames('+self.Rvariables['gcm']+')', wantType = 'list')
        #if len(self.groupNames) > 2:
        # print len(self.groupNames), self.groupNames
        # self.pickGroup.setEnabled(True)
        # self.modelListBox.update(self.groupNames)
        # if self.eset != None:
            # self.modelGroupDialog.show()
            # self.R(self.Rvariables['gcm']+'[,2]!=0 ->'+self.Rvariables['geneissig'])
            # self.R(self.Rvariables['gcm']+'['+self.Rvariables['geneissig']+',] ->'+self.Rvariables['dfsg'])
            # self.sendesetsubset()
                   
            
    # def processeset(self, data):
        # self.removeWarning()
        # self.eset = data['data'] #this is data from an expression matrix or data.frame
        # if self.sending != None and self.ebdata != '':
            # self.sendesetsubset()

    # def sendesetsubset(self):
        # self.R(self.Rvariables['gcm']+'[,'+str(int(self.modelListBox.currentRow())+1)+']!=0 ->'+self.Rvariables['geneissig'])
        # self.R(self.Rvariables['gcm']+'['+self.Rvariables['geneissig']+',] ->'+self.Rvariables['dfsg'])
        # self.R(self.Rvariables['eset_sub']+'<-'+self.eset+'[rownames('+self.Rvariables['dfsg']+'),]')
        # newdata = signals.RDataFrame(self.Rvariables['eset_sub'])
        # self.rSend("Expression Subset", newdata)
