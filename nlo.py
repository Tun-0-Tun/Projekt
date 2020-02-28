import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMouseTracking(True)
        self.setGeometry(100, 100, 1000, 1000)
        self.heigt = 1000
        self.weight = 1000
        self.setWindowTitle('Рисование')
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('nlo2.png'))
        self.x = 20
        self.y = 20
        self.label.move(self.x, self.y)
        self.show()
        self.a = 1
        self.fl = False
        self.status = 1

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            if self.x >= 0:
                self.x -= 10
            else:
                self.x = self.weight
            self.label.move(self.x, self.y)
        if event.key() == Qt.Key_Up:
            if self.y <= self.weight:
                self.y -= 10
            else:
                self.y = 0
            self.label.move(self.x, self.y)

        if event.key() == Qt.Key_Down:
            if self.y >= 0:
                self.y += 10
            else:
                self.y = self.heigt
            self.label.move(self.x, self.y)
        if event.key() == Qt.Key_Right:
            if self.x <= self.heigt:
                self.x += 10
            else:
                self.x = 0
            self.label.move(self.x, self.y)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
