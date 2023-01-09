# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QPushButton, QMainWindow
from typing import Union

from ui.ui import Ui_MainWindow
from settings.config import ConfigSetting


class UiSetter:

    def __init__(self, ui: Union[Ui_MainWindow, QMainWindow]):
        self.ui = ui
        self.config = ConfigSetting()

        # 设置界面的隐藏
        self.ui.groupBox_15.move(50, 150)
        self.ui.groupBox_15.setVisible(False)
        self.ui.groupBox_15.raise_()
        self.ui.groupBox_16.move(440, 250)
        self.ui.groupBox_16.setVisible(False)
        self.ui.groupBox_16.raise_()
        self.ui.groupBox_14.move(1033, 0)
        self.ui.groupBox_14.setVisible(False)
        self.ui.groupBox_17.setVisible(False)
        self.ui.groupBox_25.move(1030, 410)
        self.ui.groupBox_25.setVisible(False)
        self.ui.setting_button.clicked.connect(
            lambda: self.ui.groupBox_14.setVisible(not self.ui.groupBox_14.isVisible()))
        self.ui.envior_button.clicked.connect(
            lambda: self.ui.groupBox_15.setVisible(not self.ui.groupBox_15.isVisible()))
        self.ui.halo_button.clicked.connect(
            lambda: self.ui.groupBox_16.setVisible(not self.ui.groupBox_16.isVisible()))
        self.ui.equip_button.clicked.connect(
            lambda: self.ui.groupBox_17.setVisible(not self.ui.groupBox_17.isVisible()))
        self.ui.pushButton_125.clicked.connect(
            lambda: self.ui.groupBox_25.setVisible(not self.ui.groupBox_25.isVisible()))
        self.ui.equip_close_button.clicked.connect(
            lambda: self.ui.groupBox_17.setVisible(False))
        self.ui.equip_close_button.clicked.connect(
            lambda: self.ui.groupBox_24.setVisible(False))
        self.ui.equip_close_button_2.clicked.connect(
            lambda: self.ui.groupBox_15.setVisible(False))
        self.ui.equip_close_button_4.clicked.connect(
            lambda: self.ui.groupBox_25.setVisible(False))

        # 清除阵眼
        self.ui.pushButton_124.clicked.connect(
            lambda: self.ui.halo_button.setText('无阵眼')
        )
        self.ui.pushButton_124.clicked.connect(
            lambda: self.ui.groupBox_16.setVisible(False)
        )

        # 寒甲环境
        for i in range(1, 4):
            btn: QPushButton = getattr(self.ui, f'envior_button_{i}')
            btn.clicked.connect(self.envior_button_clicked(i))

        # 阵眼
        for i in range(10):
            btn: QPushButton = getattr(self.ui, f'pushButton_{80+i}')
            btn.clicked.connect(self.halo_button_clicked(btn.text()[:2]))
        # 扩展阵眼
        for btn in [self.ui.pushButton_122, self.ui.pushButton_123]:
            btn.clicked.connect(self.halo_button_clicked(btn.text()[:2]))
        self.ui.equip_close_button_3.clicked.connect(lambda: self.ui.groupBox_16.setVisible(False))

        # 五彩石收益表格宽度
        for index, width in enumerate([125, 125, 50]):
            self.ui.tableWidget_7.setColumnWidth(index, width)


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