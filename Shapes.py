import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
from random import randint



class shapes(object):

    def __init__ (self, x, y, width, height):

        self.__width = randint(10,30)
        self.__height = randint(10,30)
        self.__x = x
        self.__y = y


class rectangle(shapes):

    def __init__(self):
        pass
