# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QPushButton, QMainWindow, QInputDialog
from typing import Union

from ui.ui import Ui_MainWindow
from settings.config import ConfigSetting
from settings.jx3_equip_tab import EQUIP_SET_DATA, SET_ATTR, ATTRS


class UiAttrib:

    def __init__(self, ui: Union[Ui_MainWindow, QMainWindow]):
        self.ui = ui
        self.config = ConfigSetting()

        self.attribute = None
        self.SetAttribByJson(json_data=self.config["default_equips"], _init=True)

        self.ui.equip_button_3.clicked.connect(self.SetAttribByJson)

    def SetAttribByJson(self, json_data=None, _init=False):
        flag = True
        if not json_data:
            json_data, flag = QInputDialog.getText(
                self.ui,
                "导入数据",
                "请输入jx3box提供的配装代码",
            )
        if flag:
            try:
                if not isinstance(json_data, dict):
                    data = eval(json_data)
            except:
                return

            # 查找套装效果
            dwEquipList = data.get("EquipList")
            if not dwEquipList:
                return

            dwSetCount = {}

            for position, position_data in dwEquipList.items():
                dwID = position_data.get("id")
                if not dwID:
                    continue

                for dwSetIDs in EQUIP_SET_DATA:
                    if dwID in dwSetIDs:
                        nSetID = EQUIP_SET_DATA[dwSetIDs]
                        if nSetID in dwSetCount:
                            dwSetCount[nSetID] += 1
                        else:
                            dwSetCount[nSetID] = 1

            dwAttr = {
                "atSetEquipmentRecipe": None,
                "atSkillEventHandler": None,
            }

            for nSetID, nSetCount in dwSetCount.items():
                if nSetID not in SET_ATTR:
                    continue

                dwSetAttr = SET_ATTR[nSetID]
                for nCount in dwSetAttr:
                    if nSetCount >= nCount:
                        for dwSetAttrID in dwSetAttr[nCount]:
                            slot, value = ATTRS[dwSetAttrID]
                            if slot not in dwAttr:
                                continue

                            if dwAttr[slot] is None:
                                dwAttr[slot] = [value]
                            else:
                                if value not in dwAttr[slot]:
                                    dwAttr[slot].append(value)
            data.update(dwAttr)

            # 查找大附魔

            # 导入奇穴

            self.attribute = data
            if not _init:
                # noinspection PyUnresolvedReferences
                self.ui.set_attrib_line_edit()

