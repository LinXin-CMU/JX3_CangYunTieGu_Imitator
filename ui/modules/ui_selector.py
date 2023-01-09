# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QGroupBox, QPushButton, QLabel, QInputDialog, QMainWindow, QLineEdit
from PyQt5.QtCore import Qt
from typing import Union

from ui.ui import Ui_MainWindow
from settings.config import ConfigSetting
from settings.jx3_collections import talent


def set_index(index, func):
    index = index

    def inner():
        func(index)

    return inner


def set_qx_index(pos, idx, func):
    pos = pos
    idx = idx

    def inner():
        func(pos, idx)

    return inner


class TalentSelector:

    def __init__(self, ui: Union[Ui_MainWindow, QMainWindow]):
        self.ui = ui
        # self.qx_index = {}
        self.config = ConfigSetting()

        self.talent = {}
        self.recipe = {}

        for i in range(1, 13):
            gb: QGroupBox = getattr(self.ui, f'groupBox_{i}')
            gb.setVisible(False)
            gb.move(8+60*i, 420)
            btn: QPushButton = getattr(self.ui, f'pushButton_{i}')
            btn.clicked.connect(set_index(i, self._talent_clicked))

        for i in range(1, 10):
            gb: QGroupBox = getattr(self.ui, f'groupBox_skill_{i}')
            gb.move(6+60*i, 370)
            gb.setVisible(False)
            btn: QPushButton = getattr(self.ui, f'skill_button_{i}')
            btn.clicked.connect(set_index(i, self._skill_clicked))

        for i in range(13, 80):
            btn: QPushButton = getattr(self.ui, f'pushButton_{i}')
            btn.clicked.connect(set_index(i, self._recipe_icon_clicked))

        self.ui.button_ImportJsonTalent.clicked.connect(self.get_data_by_json)

        self.talent_frames = None
        self.set_basic_data()

        if self.ui.mount == 10389:
            dwDefaultTalent = self.config['default_talent_tiegu']
        elif self.ui.mount == 10390:
            dwDefaultTalent = self.config['default_talent_fenshan']
        else:
            dwDefaultTalent = ""
        self.set_data_by_json(dwDefaultTalent, self.config['default_recipe'])

    def set_basic_data(self):
        """
        读取并设置奇穴初始数据\n
        :return:
        """

        if self.ui.mount not in talent:
            return

        if self.talent_frames is not None:
            for frame in self.talent_frames:
                frame.deleteLater()

        frames = None

        for qx_position in talent[self.ui.mount]:
            gb = getattr(self.ui, f"groupBox_{qx_position}")
            for idx, qx in enumerate(talent[self.ui.mount][qx_position].values()):
                # 生成一个QPushButton
                btn = QPushButton(gb)
                btn.resize(40, 40)
                btn.move(10, 10 + 60 * idx)
                btn.clicked.connect(set_qx_index(qx_position, f"{idx + 1}", self._qx_icon_clicked))
                # 生成一个QLabel
                lb = QLabel(gb)
                lb.resize(60, 20)
                lb.setText(f'{qx.get("name")}')
                lb.move(0, 50 + 60 * idx)
                lb.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                # 记录奇穴控件
                if frames is None:
                    frames = [btn, lb]
                else:
                    frames += [btn, lb]

        self.talent_frames = frames

    def get_data_by_json(self):
        """
        弹出对话框以获取json数据\n
        :return:
        """
        data, ok = QInputDialog.getText(self.ui, "苍云循环模拟器", "请输入jx3box奇穴模拟器提供的奇穴编码", QLineEdit.Normal, "")
        if not ok:
            return
        self.set_data_by_json(data)

    def set_data_by_json(self, qx_data, rc_data=None):
        """
        通过config中的默认值设置奇穴和秘籍\n
        :param rc_data:
        :param qx_data:
        :return:
        """
        # ---------------------奇穴部分---------------------
        # noinspection PyBroadException
        try:
            if not isinstance(qx_data, dict):
                data = eval(qx_data)
            else:
                data = qx_data
        except:
            return

        if 'xf' not in data:
            return
        if 'sq' not in data:
            return

        xf = {
            10389: '铁骨衣',
            10390: '分山劲',
        }
        if data.get('xf') == xf.get(self.ui.mount):
            for pos, idx in enumerate(data.get('sq').split(",")):
                self._set_qx_data(pos + 1, idx)

            # 记录当前奇穴
            qx_setting = data.get('sq').split(",")
            for index, qx in enumerate(qx_setting):
                self.talent[str(index + 1)] = talent[self.ui.mount][str(index + 1)][qx]["name"]

        # ---------------------秘籍部分---------------------
        # noinspection PyBroadException
        try:
            self.recipe = eval(rc_data)
        except:
            return
        # noinspection PyBroadException
        try:
            for values in self.recipe.values():
                for btn_value in values:
                    btn: QPushButton = getattr(self.ui, f"pushButton_{btn_value}")
                    self._set_recipe_select_data(btn, 1)
        except:
            print("config有误")

    def _set_qx_data(self, pos, idx):
        """
        设置选择奇穴后奇穴栏的图标和名称\n
        :return:
        """
        lb: QLabel = getattr(self.ui, f'label_{pos}')

        if not isinstance(pos, str):
            pos = str(pos)
        if not isinstance(idx, str):
            idx = str(idx)

        data = talent
        for k in [self.ui.mount, pos, idx]:
            data = data.get(k)
            if not data:
                return
        lb.setText(data.get('name'))

        # 记录当前奇穴
        self.talent[pos] = data.get('name')


    def _talent_clicked(self, index):
        """
        展开和关闭奇穴选择框\n
        :param index:
        :return:
        """
        gb: QGroupBox = getattr(self.ui, f'groupBox_{index}')
        if not gb:
            return
        gb.setVisible(not gb.isVisible())
        gb.raise_()

        for idx in [i for i in range(1, 13) if i != index]:
            gb = getattr(self.ui, f'groupBox_{idx}')
            gb.setVisible(False)

    def _qx_icon_clicked(self, pos, idx):
        """
        设置选择的奇穴\n
        :param pos:
        :param idx:
        :return:
        """
        # 做一个接口，方便通过json导入奇穴时的方法复用
        self._set_qx_data(pos, idx)
        # 隐藏奇穴页
        gb: QGroupBox = getattr(self.ui, f'groupBox_{pos}')
        if not gb:
            return
        gb.setVisible(False)


    def _skill_clicked(self, index):
        """
        展开和关闭奇穴选择框\n
        :param index:
        :return:
        """
        gb: QGroupBox = getattr(self.ui, f'groupBox_skill_{index}')
        if not gb:
            return
        gb.setVisible(not gb.isVisible())
        gb.raise_()

        for idx in [i for i in range(1, 10) if i != index]:
            gb = getattr(self.ui, f'groupBox_skill_{idx}')
            gb.setVisible(False)

    def _recipe_icon_clicked(self, index):
        """
        设置秘籍选择后的样式\n
        :return:
        """
        btn: QPushButton = getattr(self.ui, f'pushButton_{index}')
        parent = btn.parent().objectName()

        if parent in self.recipe:
            if index in self.recipe[parent]:
                # 取消选择
                self.recipe[parent] = [i for i in self.recipe[parent] if i != index]
                nFlag = 0
            else:
                if len(self.recipe[parent]) < 4:
                    self.recipe[parent].append(index)
                    nFlag = 1
                else:
                    nFlag = 0
        else:
            self.recipe[parent] = [index]
            nFlag = 1

        self._set_recipe_select_data(btn, nFlag)

    # @staticmethod
    def _set_recipe_select_data(self, btn, nFlag):

        if nFlag:
            btn.setStyleSheet("""
            QPushButton{
                background-color: rgb(186, 52, 26);
                color: rgb(225, 225, 225);
            }
            QPushButton:hover{
                background-color: rgb(214, 60, 29);
            }
            """)

        else:
            btn.setStyleSheet("")

        print(self.recipe)
