from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
import sys
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Rounds')
        self.flag = False
        self.button = QPushButton('click me', self)
        self.button.move(200, 200)
        self.button.resize(100, 20)
        self.button.clicked.connect(self.onClicked)

    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            col = QColor(0, 0, 0)
            col.setNamedColor('#d4d4d4')
            qp.setPen(col)
            c1 = random.randint(0, 256)
            c2 = random.randint(0, 256)
            c3 = random.randint(0, 256)
            qp.setBrush(QColor(c1, c2, c3))
            r = random.randint(10, 100)
            qp.drawEllipse(60, 60, r, r)
            r = random.randint(10, 100)
            qp.drawEllipse(200, 60, r, r)
            qp.end()

    def onClicked(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
