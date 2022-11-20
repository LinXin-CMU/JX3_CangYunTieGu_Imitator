# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QGroupBox, QPushButton, QLabel, QInputDialog, QMainWindow, QLineEdit
from PyQt5.QtCore import Qt
from typing import Union

from TieGu.ui.ui import Ui_MainWindow
from settings.config import ConfigSetting


class UiSetter:

    def __init__(self, ui: Union[Ui_MainWindow, QMainWindow]):
        self.ui = ui
        self.config = ConfigSetting()

        # 设置界面的隐藏
        self.ui.groupBox_14.setVisible(False)
        self.ui.setting_button.clicked.connect(
            lambda: self.ui.groupBox_14.setVisible(not self.ui.groupBox_14.isVisible()))
        self.ui.envior_button.clicked.connect(
            lambda: self.ui.groupBox_15.setVisible(not self.ui.groupBox_15.isVisible()))
        self.ui.halo_button.clicked.connect(
            lambda: self.ui.groupBox_16.setVisible(not self.ui.groupBox_16.isVisible()))

        for i in range(1, 4):
            btn: QPushButton = getattr(self.ui, f'envior_button_{i}')
            btn.clicked.connect(self.envior_button_clicked(i))

        for i in range(10):
            btn: QPushButton = getattr(self.ui, f'pushButton_{80+i}')
            btn.clicked.connect(self.halo_button_clicked(btn.text()[:2]))

    def envior_button_clicked(self, value):
        def inner():
            lb = getattr(self.ui, f'label_{51+value}')
            self.ui.envior_button.setText(lb.text())
            self.ui.groupBox_15.setVisible(False)
        return inner


    def halo_button_clicked(self, value):
        def inner():
            if value == '无阵':
                self.ui.halo_button.setText("无阵眼")
            else:
                self.ui.halo_button.setText(f"{value}阵")
            self.ui.groupBox_16.setVisible(False)
        return inner