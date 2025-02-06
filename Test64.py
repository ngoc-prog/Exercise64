from PyQt6.QtWidgets import QApplication, QMainWindow

from MODULE3.Exercise64.ui.MainWindow64Ext import MainWindow64Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow64Ext()
myui.setupUI(mainwindow)
myui.showWindow()
app.exec()