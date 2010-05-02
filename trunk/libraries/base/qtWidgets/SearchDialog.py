from redRGUI import widgetState

from webViewBox import webViewBox
from widgetBox import widgetBox
from widgetLabel import widgetLabel
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SearchDialog(QDialog):
    def __init__(self, caption = 'Search Dialog', url = '', icon = None, orientation = 'horizontal'):
        QDialog.__init__(self)
        
        self.setWindowTitle(caption)
        try:
            if isinstance(orientation, QLayout):
                self.setLayout(orientation)
            elif orientation == 'horizontal' or not orientation:
                self.setLayout(QHBoxLayout())
            else:
                self.setLayout(QVBoxLayout())
        except:
            self.setLayout(QVBoxLayout())
        self.thisLayout = self.layout()
        self.webView = webViewBox(self)
        self.setMinimumSize(600, 400)
        if url and url != '':
            self.webView.load(QUrl(url))
        
        if icon:
            self.setWindowIcon(icon)
            
    def updateUrl(self, url):
        self.webView.load(QUrl(url))
        