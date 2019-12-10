import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QMessageBox
import sqlite3
from PyQt5.QtGui import *
from random import randint
import random
import xlsxwriter
from xlrd import open_workbook
from openpyxl import load_workbook


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ggwp.ui', self)
        self.con = sqlite3.connect("GGWP.db")
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Предупреждение!")
        self.msg.setText("Введите имя")
        self.pushButton.clicked.connect(self.update_result)
        self.pushButton_2.clicked.connect(self.otv)
        self.pushButton_3.clicked.connect(self.Ref)
        self.lineEdit.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.modified = {}
        self.a = 0
        self.titles = None
        self.score = 0
        self.end = False

    def update_result(self):
        if self.lineEdit_2.text() == '':
            self.msg.exec_()
        else:
            self.lineEdit_2.setEnabled(False)
            self.lineEdit.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(False)
            self.pushButton.setEnabled(False)

            self.name = self.lineEdit_2.text()

            cur = self.con.cursor()
            if self.a == 0:
                n1 = cur.execute("SELECT COUNT(1) FROM  Task").fetchall()
                n = list(n1[0])[0]
                self.sp = list(range(1, n + 1))
                random.shuffle(self.sp)
            if self.a > len(self.sp) - 1:
                self.label_4.setText('Игра окончена')
                self.pushButton_2.setEnabled(False)
                self.pushButton_3.setEnabled(False)
                self.pushButton.setEnabled(False)
                self.itog()
            else:

                result = cur.execute("Select * from Task WHERE id=?",
                                     str(self.sp[self.a])).fetchall()
                self.a += 1
                print(self.sp)

                self.m = list(result[0])
                print(self.m)
                self.label_2.setText(self.m[3])
                self.label_3.setPixmap(QPixmap(self.m[1]))
                self.titles = [description[0] for description in cur.description]
                self.modified = {}

    def otv(self):
        self.pushButton_3.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        a = self.lineEdit.text()
        f = open('баллы.txt', 'r')
        g = f.read(1)
        print(g)
        if a.lower() == self.m[2]:
            self.label_4.setText('Правильно!')
            self.score += 50
            self.lbScore.setText(str(self.score))

        else:
            self.label_4.setText('Неравильно!')
            self.score -= 50
            self.lbScore.setText(str(self.score))


    def itog(self):
        fn = r"Суммы2.xlsx"
        wb = load_workbook(fn)
        ws = wb["Sheet1"]
        row = (self.name, self.score)
        ws.append(row)
        wb.save(fn)
        wb.close()


    def Ref(self):
        self.update_result()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
