"""
<name>RedRks.test</name>
<author>Generated using Widget Maker written by Kyle R. Covington</author>
<description></description>
<RFunctions>stats:ks.test</RFunctions>
<tags>Prototypes</tags>
<icon></icon>
"""
from OWRpy import * 
import redRGUI 
import libraries.base.signalClasses as signals

class RedRks_test(OWRpy): 
	settingsList = []
	def __init__(self, parent=None, signalManager=None):
		OWRpy.__init__(self, parent, signalManager, "ks_test", wantMainArea = 0, resizingEnabled = 1)
		self.setRvariableNames(["ks.test"])
		self.data = {}
		self.RFunctionParam_y = ''
		self.RFunctionParam_x = ''
		self.inputs = [("y", signals.RVector.RVector, self.processy),("x", signals.RVector.RVector, self.processx)]
		
		self.RFunctionParamalternative_comboBox = redRGUI.comboBox(self.controlArea, label = "alternative:", items = ["two.sided","less","greater"])
		self.RFunctionParamexact_lineEdit = redRGUI.lineEdit(self.controlArea, label = "exact:", text = 'NULL')
		redRGUI.button(self.bottomAreaRight, "Commit", callback = self.commitFunction)
		self.RoutputWindow = redRGUI.textEdit(self.controlArea, label = "RoutputWindow")
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
			#self.data = data
			self.commitFunction()
		else:
			self.RFunctionParam_x=''
	def commitFunction(self):
		if str(self.RFunctionParam_y) == '': return
		if str(self.RFunctionParam_x) == '': return
		injection = []
		string = 'alternative=\''+str(self.RFunctionParamalternative_comboBox.currentText())+'\''
		injection.append(string)
		if str(self.RFunctionParamexact_lineEdit.text()) != '':
			string = 'exact='+str(self.RFunctionParamexact_lineEdit.text())+''
			injection.append(string)
		inj = ','.join(injection)
		self.R(self.Rvariables['ks.test']+'<-ks.test(y='+str(self.RFunctionParam_y)+',x='+str(self.RFunctionParam_x)+','+inj+')')
		self.R('txt<-capture.output('+self.Rvariables['ks.test']+')')
		self.RoutputWindow.clear()
		tmp = self.R('paste(txt, collapse ="\n")')
		self.RoutputWindow.insertHtml('<br><pre>'+tmp+'</pre>')