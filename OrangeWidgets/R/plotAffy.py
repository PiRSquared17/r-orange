"""
<name>Plot Affy Image</name>
<description>Obtains an affybatch and plots the images of the files</description>
<icon>icons/plotAffy.png</icon>
<priority>70</priority>
"""

from OWRpy import *
import OWGUI
import RAffyClasses

class plotAffy(OWRpy):
    def __init__(self, parent=None, signalManager=None):
        OWRpy.__init__(self, parent, signalManager, "plotAffy")
        
        #default values        
        self.loadSettings()

        #set R variable names
        #self.setRvariableNames()

        self.inputs = [("Affybatch", RAffyClasses.RAffyBatch, self.init)]
        self.outputs = None
        
        self.testLineEdit = ""
        self.irows = 1 #this sets the global variable for the rows
        self.icols = 1 #this sets the global variable for the cols
        
        #the GUI
        info = OWGUI.widgetBox(self.controlArea, "Info")
        self.infoa = OWGUI.widgetLabel(info, 'No data loaded.')
        plotbutton = OWGUI.button(info, self, "Show Image", callback = self.process, width = 200)
        boxplotbutton = OWGUI.button(info, self, "Show Boxplot", callback = self.myboxplot, width = 200)
        
        optionsa = OWGUI.widgetBox(self.controlArea, "Options")
        self.infob = OWGUI.widgetLabel(optionsa, 'Button not pressed')
        #OWGUI.lineEdit(optionsa, self, "testLineEdit", "Test Line Edit", orientation = "horizontal")
        OWGUI.lineEdit(optionsa, self, "irows", "Number of rows:", orientation="horizontal") #make line edits that will set the values of the irows and icols variables, this seems to happen automatically.  Only need to include variable name where the "irows" is in this example
        OWGUI.lineEdit(optionsa, self, "icols", "Number of columns:", orientation="horizontal")
        #testlineButton = OWGUI.button(optionsa, self, "test line edit", callback = self.test, width = 200)
        
        
    
    def init(self, dataset):
        if dataset:
            self.data = dataset['eset']
            self.infoa.setText("Data Connected")
        else:
            self.infoa.setText("No data loaded.")
    
    def process(self):
        #required librarys
        self.require_librarys(['affy'])
        #try: 
        self.rsession('par(mfrow=c('+str(self.irows)+','+str(self.icols)+'))') #get the values that are in the irows and icols and put them into the par(mfrow...) function in r
        self.Rplot('image('+self.data+')')
        #except: 
        #    self.infob.setText("Data not able to be processed")
    
    def myboxplot(self):
        #required librarys
        self.require_librarys(['affy'])
        #try:
        self.Rplot('boxplot('+self.data+')')
        #except:     
        #    self.infob.setText("Data not able to be processed")