import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
from random import randint
from Shapes import *


class ShapeDrawer(QWidget, rectangle):

  def __init__(self):
    super().__init__()
    rectangle().__init__()
    self.__shapes = list()
    self.setGeometry(50, 50, 500, 500)
    self.setWindowTitle('Shapes')
    self.show()
    self.__x = 0
    self.__y = 0

  def draw(self, qp):
    qp.drawRect(self.__x,self.__y, self.__width, self.__height)

  def paintEvent(self, event):
    rbg_1 = randint(0,255)
    rbg_2 = randint(0,255)
    rbg_3 = randint(0,255)
    qp = QPainter()
    qp.begin(self)
    qp.setPen(QColor(rbg_1,rbg_2,rbg_3))
    qp.setBrush(QColor(rbg_1,rbg_2,rbg_3))
    if(self.__x > 0 and self.__y > 0):
        self.draw(qp)


    #TODO draw the shapes

    qp.end()

  def mousePressEvent(self, event):
      self.__x = event.x()
      self.__y = event.y()
      self.update()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = ShapeDrawer()
  sys.exit(app.exec_())

        #qp.drawRect(self.__x,self.__y,100,100)
        #qp.drawRect(self.__x, self.__y, width, length)
