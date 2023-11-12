import sys

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from random import randint

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(70, 150)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

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
        qp.setBrush(QColor('yellow'))
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