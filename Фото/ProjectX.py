import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem
import sqlite3
from PyQt5.QtGui import *
import xlsxwriter
import random


class studentWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ggwp.ui', self)
        self.con = sqlite3.connect("GGWP.db")
        self.pushButton.clicked.connect(self.update_result)
        self.pushButton_2.clicked.connect(self.otv)
        self.pushButton_3.clicked.connect(self.Ref)
        self.modified = {}
        self.a = 0
        self.titles = None
        self.score = 0

    def update_result(self):
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton.setEnabled(False)
        self.textEdit.setEnabled(False)

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
        else:

            result = cur.execute("Select * from Task WHERE id=?",
                                 str(self.sp[self.a])).fetchall()
            self.a += 1
            print(self.sp)

            self.m = list(result[0])
            print(self.m)
            self.label_2.setText(self.m[3])
            self.tableWidget.setRowCount(len(result))

            self.tableWidget.setColumnCount(len(result[0]))
            self.label_3.setPixmap(QPixmap(self.m[1]))
            self.titles = [description[0] for description in cur.description]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.modified = {}

    def otv(self):
        workbook = xlsxwriter.Workbook('Суммы.xlsx')
        worksheet = workbook.add_worksheet()
        self.pushButton_2.setEnabled(False)
        a = self.lineEdit.text()
        f = open('баллы.txt', 'w')
        if a.lower() == self.m[2]:
            self.label_4.setText('Правильно!')
            self.score += 50
            self.lbScore.setText(str(self.score))

        else:
            self.label_4.setText('Неравильно!')
            self.score -= 50
            self.lbScore.setText(str(self.score))
        f.write('Итог - ' + ' ' + str(self.score))
        f.close()

        worksheet.write(1, 0, self.name())
        worksheet.write(1, 1, str(self.score))
        workbook.close()

    def Ref(self):
        self.update_result()


app = QApplication(sys.argv)
ex = studentWidget()
ex.show()
sys.exit(app.exec_())
