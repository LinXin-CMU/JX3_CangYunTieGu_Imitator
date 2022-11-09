# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QMainWindow
from .ui import Ui_MainWindow


class MainUI(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)







