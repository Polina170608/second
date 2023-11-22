from PyQt5 import uic
import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUI('UI.ui', self)
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.flag = False

    def draw_flag(self, qp):
        self.flag = True
        qp.setBrush(QColor(255, 255, 0))
        x, y = randint(0, 790), randint(0, 590)
        d = randint(10, 30)
        qp.drawEllipse(x, y, d, d)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
