from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit

class SiLayoutV(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.contents_top = []
        self.contents_bottom = []
        self.align_center = False

        self.interval = 16

    def setCenter(self, b):
        self.align_center = b

    def setInterval(self, interval):
        self.interval = interval

    def addItem(self, item, side):
        item.setParent(self)
        item.parent = self

        if side != 'top' and side != 'bottom':
            raise ValueError(side)

        if side == 'top':
            self.contents_top.append(item)
        if side == 'bottom':
            self.contents_bottom.append(item)
        self.refresh_components()

    def refresh_components(self):
        size = self.geometry()
        w, h = size.width(), size.height()

        top_used = 0
        bottom_used = 0

        for obj in self.contents_top:
            obj_geo = obj.geometry()
            ow, oh = obj_geo.width(), obj_geo.height()
            obj.move((w - ow)//2 if self.align_center else 0, top_used)
            top_used += oh + self.interval

        for obj in self.contents_bottom:
            obj_geo = obj.geometry()
            ow, oh = obj_geo.width(), obj_geo.height()
            obj.move((w - ow)//2 if self.align_center else 0, h - oh - bottom_used)
            bottom_used += oh + self.interval

    def resizeEvent(self, event):
        self.refresh_components()

class SiLayoutH(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.contents_left = []
        self.contents_right = []
        self.interval = 16

    def setInterval(self, interval):
        self.interval = interval

    def addItem(self, item, side):
        item.setParent(self)
        item.parent = self

        if side != 'left' and side != 'right':
            raise ValueError(side)

        if side == 'left':
            self.contents_left.append(item)
        if side == 'right':
            self.contents_right.append(item)
        self.refresh_components()

    def refresh_components(self):
        size = self.geometry()
        w, h = size.width(), size.height()

        left_used = 0
        right_used = 0

        for obj in self.contents_left:
            obj_geo = obj.geometry()
            ow, oh = obj_geo.width(), obj_geo.height()
            obj.move(left_used, (h - oh) // 2)
            left_used += ow + self.interval

        for obj in self.contents_right:
            obj_geo = obj.geometry()
            ow, oh = obj_geo.width(), obj_geo.height()
            obj.move(w - ow - right_used, (h - oh) // 2)
            right_used += ow + self.interval

    def resizeEvent(self, event):
        self.refresh_components()