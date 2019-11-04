from distutils.core import setup
import py2exe
 
setup(windows=[{"script" : "first_prog_griba.py"}], options={"py2exe" : {"includes" : ["sip", "PyQt5._qt"]}})
