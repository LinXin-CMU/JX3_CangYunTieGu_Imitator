# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QLogValueAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from typing import Union

from ui.ui import Ui_MainWindow
from settings.config import ConfigSetting


class UiPainter:

    def __init__(self, ui: Union[Ui_MainWindow, QMainWindow]):
        self.ui = ui
        self.config = ConfigSetting()

        self.marker_labels = []
        self.ui.chartView.setRenderHint(QPainter.Antialiasing)
        self.ui.chartView_3.setRenderHint(QPainter.Antialiasing)

    def DrawAttributeProfits(self, marker_profits, text):
        if not marker_profits:
            return
        # chart_view = QChartView(self.ui.chartView)
        profits = {
            'Vitality': [1, 2, 5, 10, 20, 50],
            'Agility': [1, 2, 5, 10, 20, 50],
            'Strength': [1, 2, 5, 10, 20, 50],
            'PhysicsAttackPowerBase': [1, 2, 5, 10, 20, 50],
            'PhysicsCriticalStrike': [1, 2, 5, 10, 20, 50],
            'PhysicsCriticalDamagePower': [1, 2, 5, 10, 20, 50],
            'PhysicsOvercome': [1, 2, 5, 10, 20, 50],
            'Strain': [1, 2, 5, 10, 20, 50],
            'SurplusValue': [1, 2, 5, 10, 20, 50],
            'ParryValue': [1, 2, 5, 10, 20, 50],
            'WeaponDamage': [1, 2, 5, 10, 20, 50],
        }
        names = {
            'Vitality': '体质',
            'Agility': '身法',
            'Strength': '力道',
            'PhysicsAttackPowerBase': '攻击',
            'PhysicsCriticalStrike': '会心',
            'PhysicsCriticalDamagePower': '会效',
            'PhysicsOvercome': '破防',
            'Strain': '无双',
            'SurplusValue': '破招',
            'ParryValue': '拆招',
            'WeaponDamage': '武伤',
        }
        x_axis_text = {
            '单点收益': '属性量(每点)×100',
            '同分收益(装备)': '倍率(装备，单位装分)',
            '同分收益(其他增益)': '倍率(附魔/小药/五彩石等，单位装分)',
        }
        # chartView: 主属性
        # chartView_2: 其他属性
        chart = self.ui.chartView.chart()
        [series.hide() for series in chart.series()]
        [axis.hide() for axis in chart.axes()]
        axis_x = QLogValueAxis()
        axis_y = QValueAxis()
        axis_x.setTitleText(x_axis_text[text])
        axis_y.setTitleText('相对提升')
        axis_x.setBase(2)
        axis_x.setMinorTickCount(-1)
        axis_y.setTickCount(-1)
        chart.addAxis(axis_x, Qt.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignLeft)
        top_y = 0
        for k in ['Vitality', 'Agility', 'Strength']:
            name = names[k]
            v = marker_profits[k]
            series = QLineSeries()
            chart.addSeries(series)
            series.setName(name)
            for index, value in enumerate(v):
                if value * 100 > top_y:
                    top_y = value * 100
                series.append(profits[k][index], value*100)
            series.attachAxis(axis_x)
            series.attachAxis(axis_y)
        axis_y.setMax(top_y)

        chart2 = self.ui.chartView_3.chart()
        [series.hide() for series in chart2.series()]
        [axis.hide() for axis in chart2.axes()]
        axis_x = QLogValueAxis()
        axis_y = QValueAxis()
        axis_x.setTitleText(x_axis_text[text])
        axis_y.setTitleText('相对提升')
        axis_x.setBase(2)
        axis_x.setMinorTickCount(-1)
        axis_y.setTickCount(-1)
        chart2.addAxis(axis_x, Qt.AlignBottom)
        chart2.addAxis(axis_y, Qt.AlignLeft)
        top_y = 0
        for k in ['PhysicsAttackPowerBase', 'PhysicsCriticalStrike', 'PhysicsCriticalDamagePower',
                  'PhysicsOvercome', 'Strain', 'SurplusValue', 'ParryValue', 'WeaponDamage']:
            name = names[k]
            v = marker_profits[k]
            series = QLineSeries()
            chart2.addSeries(series)
            series.setName(name)
            for index, value in enumerate(v):
                if value * 100 > top_y:
                    top_y = value * 100
                series.append(profits[k][index], value * 100)
            series.attachAxis(axis_x)
            series.attachAxis(axis_y)
        axis_y.setMax(top_y)

        # 添加右侧曲线标签提示
        # 先清除原有的标签
        for lb in self.marker_labels:
            lb.setVisible(False)
            lb.deleteLater()
        self.marker_labels.clear()

        x_pos = 485
        y_top = 110     # 实际绘图区最高y值
        y_bot = 495     # 实际绘图区最低y值
        y_range = y_bot - y_top
        y_poses = []    # 储存标签提示的y值
        v_top = axis_y.max()
        v_bot = axis_y.min()
        for k in ['PhysicsAttackPowerBase', 'PhysicsCriticalStrike', 'PhysicsCriticalDamagePower',
                  'PhysicsOvercome', 'Strain', 'SurplusValue', 'ParryValue', 'WeaponDamage']:
            v = marker_profits[k][-1] * 100
            k = names[k]
            # 计算需移动到的y坐标
            pos_y = int((v_top - v) / (v_top - v_bot) * y_range + y_top) - 7
            for old_y in y_poses:
                if abs(old_y - pos_y) < 5:
                    pos_y += 10
            y_poses.append(pos_y)
            # 创建标签QLabel
            label = QLabel(self.ui.tab_9)
            label.setText(k)
            label.setVisible(True)
            label.move(x_pos, pos_y)
            self.marker_labels.append(label)

        # chart3 = self.ui.chartView_2.chart()
        # axis_x = QLogValueAxis()
        # # axis_x = QValueAxis()
        # axis_y = QValueAxis()
        # axis_x.setTitleText('属性量(单位装分)')
        # axis_y.setTitleText('相对提升')
        # axis_x.setBase(2)
        # axis_x.setMinorTickCount(-1)
        # axis_y.setTickCount(-1)
        # chart3.addAxis(axis_x, Qt.AlignBottom)
        # chart3.addAxis(axis_y, Qt.AlignLeft)
        # top_y = 0
        # for k in ['ParryValue', 'WeaponDamage']:
        #     name = names[k]
        #     v = marker_profits[k]
        #     series = QLineSeries()
        #     chart3.addSeries(series)
        #     series.setName(name)
        #     for index, value in enumerate(v):
        #         if value * 100 > top_y:
        #             top_y = value * 100
        #         series.append(profits[k][index], value * 100)
        #     series.attachAxis(axis_x)
        #     series.attachAxis(axis_y)
        # axis_y.setMax(top_y)






