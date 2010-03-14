import os, sys
from distutils.core import setup
import py2exe
sys.path.insert(0, 'C:\\Python25\\Lib\\site-packages\\redR-dist\\')
sys.path.insert(0, 'C:\\Python25\\Lib\\site-packages\\redR-dist\\OrangeCanvas\\')
sys.path.insert(0, 'C:\\Python25\\Lib\\site-packages\\redR-dist\\OrangeWidgets\\')
sys.path.insert(0, 'C:\\Program Files (x86)\\R\\R-2.7.0\\bin')

Mydata_files = [
#('', ['C:\\Program Files (x86)\\R\\R-2.7.0\\bin\\R.dll']),
# ('', ['C:\\Python25\\Lib\\site-packages\\_rpy2070.pyd'])#,
('',[
# 'C:\\Windows\\system32\\OLE32.dll'
# ,'C:\\Windows\\system32\\OLEAUT32.dll'
# ,'C:\\Windows\\system32\\USER32.dll'
# ,'C:\\Windows\\system32\\IMM32.DLL'
# ,'C:\\Windows\\system32\\SHELL32.dll'
# ,'C:\\Windows\\system32\\KERNEL32.dll'
# ,'C:\\Windows\\system32\\COMDLG32.DLL'
# ,'C:\\Windows\\system32\\WSOCK32.dll'
# ,'C:\\Windows\\system32\\COMCTL32.DLL'
# ,'C:\\Windows\\system32\\ADVAPI32.dll'
# ,'C:\\Windows\\system32\\CRYPT32.dll'
# ,'C:\\Windows\\system32\\msvcrt.dll'
# ,'C:\\Windows\\system32\\WS2_32.dll'
# ,'C:\\Windows\\system32\\WINSPOOL.DRV'
# ,'C:\\Windows\\system32\\GDI32.dll'
'C:\\Python25\\Lib\\site-packages\\PyQt4\\QtSvg4.dll'
# ,'C:\\Windows\\system32\\WINMM.DLL'
# ,'C:\\Windows\\system32\\VERSION.dll'
#,'C:\\Python25\\lib\\site-packages\\pysvn\\MSVCP71.dll'
# ,'C:\\Windows\\system32\\ntdll.dll'
# ,'C:\\Windows\\system32\\RPCRT4.dll'
])]

setup(name="Red-R",
      version="0.1",
      author="Anup  Parikh",
      author_email="anup.parikh@gmail.com",
      url="http://www.red-r.org",
      license="GNU General Public License (GPL)",
      data_files = Mydata_files,
      windows=["OrangeCanvas/orngCanvas.pyw"],
      options={"py2exe": {
      "skip_archive": True, 
      # "compressed": True, 
      # "bundle_files": 3, 
      "includes": ["sip",'OWRpy','OWColorPalette',
      'OWGraphTools','OWReport','OWToolbars','RRGUI','PyQt4.Qwt5','PyQt4.QtSvg','_rpy2070'],
      # 'excludes' : ['rpy']
      }})

      
      
# import sys
# from cx_Freeze import setup, Executable

# executables = [
        # Executable("OrangeCanvas/orngCanvas.pyw",base = "Win32GUI"),
# ]

# buildOptions = dict(
        # compressed = True,
        # includes = ['sip'],
        # path = sys.path + ["OrangeCanvas","OrangeWidgets"])
        

# setup(
        # name = "advanced_cx_Freeze_sample",
        # version = "0.1",
        # description = "Advanced sample cx_Freeze script",
        # options = dict(build_exe = buildOptions),
        # executables = executables)
