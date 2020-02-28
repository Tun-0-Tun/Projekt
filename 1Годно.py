import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem
import sqlite3

def min(*args):
    "Минимум из чисел"
    res = float('inf')
    for x in args:
        res = x if x < res else res
    return res

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('krnol.ui', self)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

