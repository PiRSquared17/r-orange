"""
<name>Size Plot</name>
<author>Generated using Widget Maker written by Kyle R. Covington</author>
<RFunctions>plotrix:sizeplot</RFunctions>
<tags>Plotting</tags>
<icon>plot.png</icon>
"""
from OWRpy import * 
import redRGUI 
class sizeplot(OWRpy): 
	settingsList = []
	def __init__(self, parent=None, signalManager=None):
		OWRpy.__init__(self, parent, signalManager, "sizeplot", wantMainArea = 0, resizingEnabled = 1)
		self.RFunctionParam_y = ''
		self.RFunctionParam_x = ''
		self.inputs = [("y", signals.RVector, self.processy),("x", signals.RVector, self.processx)]
		
		self.help.setHtml('<small>Default Help HTML, one should update this as soon as possible.  For more infromation on widget functions and RedR please see either the <a href="http://www.code.google.com/p/r-orange">google code repository</a> or the <a href="http://www.red-r.org">RedR website</a>.</small>')
		box = redRGUI.tabWidget(self.controlArea)
		self.standardTab = box.createTabPage(name = "Standard")
		self.advancedTab = box.createTabPage(name = "Advanced")
		self.RFunctionParamy_lineEdit =  redRGUI.lineEdit(self.standardTab,  label = "y:", text = '')
		self.RFunctionParamx_lineEdit =  redRGUI.lineEdit(self.standardTab,  label = "x:", text = '')
		self.RFunctionParamscale_lineEdit =  redRGUI.lineEdit(self.standardTab,  label = "scale:", text = '1')
		self.RFunctionParamsize_lineEdit =  redRGUI.lineEdit(self.standardTab,  label = "size:", text = 'c(1,4)')
		self.RFunctionParampow_lineEdit =  redRGUI.lineEdit(self.standardTab,  label = "pow:", text = '0.5')
		redRGUI.button(self.bottomAreaRight, "Commit", callback = self.commitFunction)
	def processy(self, data):
		if not self.require_librarys(["plotrix"]):
			self.status.setText('R Libraries Not Loaded.')
			return
		if data:
			self.RFunctionParam_y=data.getData()
			#self.data = data
			self.commitFunction()
		else:
			self.RFunctionParam_y=''
	def processx(self, data):
		if not self.require_librarys(["plotrix"]):
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
		if str(self.RFunctionParamy_lineEdit.text()) != '':
			string = 'y='+str(self.RFunctionParamy_lineEdit.text())+''
			injection.append(string)
		if str(self.RFunctionParamx_lineEdit.text()) != '':
			string = 'x='+str(self.RFunctionParamx_lineEdit.text())+''
			injection.append(string)
		if str(self.RFunctionParamscale_lineEdit.text()) != '':
			string = 'scale='+str(self.RFunctionParamscale_lineEdit.text())+''
			injection.append(string)
		if str(self.RFunctionParamsize_lineEdit.text()) != '':
			string = 'size='+str(self.RFunctionParamsize_lineEdit.text())+''
			injection.append(string)
		if str(self.RFunctionParampow_lineEdit.text()) != '':
			string = 'pow='+str(self.RFunctionParampow_lineEdit.text())+''
			injection.append(string)
		inj = ','.join(injection)
		self.R('sizeplot(y='+str(self.RFunctionParam_y)+',x='+str(self.RFunctionParam_x)+','+inj+')')