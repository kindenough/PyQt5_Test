#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5创建了一个简单的窗口。

作者: Jan Bodnar
网站: zetcode.com
最后一次编辑: January 2015
"""

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLabel, QGridLayout, QMainWindow, QDialog

from ui1 import Ui_Dialog


def ShowDialog(self):
    text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
    if ok:
        self.le.setText(str(text))

class QDialogTest():
    mainWindow=None
    def __init__(self):
        ui = Ui_Dialog()
        self.mainWindow = QDialog()
        ui.setupUi(self.mainWindow)
        ui.lineEdit.setText("PyQt Demo")
    def show(self):
        self.mainWindow.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('My Widget')
    # w.show()
    # le = QLabel(w)
    # w.le = le
    # ml = QGridLayout(w)
    # ml.addWidget(le)
    # print(type(le))
    # # ShowDialog(w)

    dd = QDialogTest()
    dd.show()
    sys.exit(app.exec_())