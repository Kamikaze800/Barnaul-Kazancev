import random
import sys

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from random import randint
from UI import Ui_MainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        qp.setBrush(QColor(red, green, blue))
        diameter = randint(20, 100)  # Случайный диаметр от 20 до 100
        x = randint(0, self.width() - diameter)
        y = randint(0, self.height() - diameter)
        circle_rect = QRectF(x, y, diameter, diameter)
        qp.drawEllipse(circle_rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
