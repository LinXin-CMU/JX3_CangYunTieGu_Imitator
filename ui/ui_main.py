# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QListView, QComboBox, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from typing import List, Dict
from functools import reduce

from .ui import Ui_MainWindow
from settings.jx3_collections import recipe
from settings.config import ConfigSetting
from settings.jx3_equip_tab import WEAPON_TYPE, PENDANT_TYPE, EQUIP_POSITION, TALENT_INDEX
from settings.jx3_advance_tab import *
from .modules.ui_selector import TalentSelector
from .modules.ui_setter import UiSetter
# from .modules.ui_equip import UiEquip
from .modules.ui_chart import UiPainter
from .modules.ui_attrib import UiAttrib
from db.jx3_enchant import enchant

HALO_TO_ID = {
    '铁骨阵': 'Halo_TieGu',
    '凌雪阵': 'Halo_LingXue',
    '剑纯阵': 'Halo_JianChun',
    '刀宗阵': 'Halo_DaoZong',
    '霸刀阵': 'Halo_BaDao',
    '藏剑阵': 'Halo_CangJian',
    '蓬莱阵': 'Halo_PengLai',
    '丐帮阵': 'Halo_GaiBang',
    '天罗阵': 'Halo_TianLuo',
    '惊羽阵': 'Halo_JingYu',
    '傲血阵': 'Halo_AoXue',
    '分山阵': 'Halo_FenShan'
}


class MainUI(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)
        self.mount = 10389

        self.config = ConfigSetting()
        self._selector = TalentSelector(self)
        self._setter = UiSetter(self)
        self._painter = UiPainter(self)
        self._attrib = UiAttrib(self)
        # self._equipsetter = UiEquip(self)
        # self._equipsetter.import_json_func(data=self.config['default_equips'])

        self.skill_data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.cellClicked.connect(lambda i, _: self.read_history(i))

        self.resize(1246, 849)
        self.setMinimumSize(1246, 849)
        self.setMaximumSize(1246, 849)

        self.profit_data = {
            '单点收益': {},
            '同分收益(装备)': {},
            '同分收益(其他增益)': {},
        }
        self.history_record = None

        self.comboBox_6.setView(QListView())
        self.comboBox_6.currentTextChanged.connect(self.draw_attribute_profits)

        self.tabWidget_2.setCurrentIndex(0)
        self.comboBox_12.setView(QListView())
        self.comboBox_13.setView(QListView())
        self.comboBox_14.setView(QListView())

        self.comboBox_14.addItems(eval(self.config['commands']))
        self.comboBox_14.currentTextChanged.connect(self.set_talent_by_command)

        self.set_special_equip_selector()
        self.set_enchant_select_box()
        for i in range(7, 12):
            box: QComboBox = getattr(self, f"comboBox_{i}")
            box.currentTextChanged.connect(self.set_enchant_select_box_text_color(box))

        self.set_self_advance_select_box()

        for i in range(35, 38):
            box: QCheckBox = getattr(self, f"checkBox_{i}")
            box.clicked.connect(self.self_advance_check_clicked(box))
        self.qijin_checkBox.clicked.connect(self.self_advance_check_clicked(self.qijin_checkBox))

        self.pushButton_126.clicked.connect(self.self_advance_clear_button)

        for i in range(38, 47):
            box: QCheckBox = getattr(self, f"checkBox_{i}")
            box.clicked.connect(self.other_advance_major_box_clicked(box))

        self.pushButton_127.clicked.connect(self.other_advance_clear_button)

        self.pushButton_128.clicked.connect(self.self_advance_text_func)
        self.pushButton_129.clicked.connect(self.other_advance_text_func)
        self.other_advance_explain_func()

        self.set_attrib_line_edit()


    def get_talent(self) -> Dict[int, str]:
        return self._selector.talent

    def get_recipe(self) -> List[int]:
        recipes = []
        recipe_index = reduce(lambda i, j: i + j, [i for i in self._selector.recipe.values()])
        for recipe_id in recipe:
            if recipe[recipe_id].index in recipe_index:
                recipes.append(recipe_id)

        return recipes

    def get_attribute(self) -> Dict:
        json_attrib = self._attrib.attribute
        json_attrib['Vitality'] = int(self.lineEdit_3.text()) if self.lineEdit_3.text() != "" else json_attrib[
            'Vitality']
        json_attrib['Agility'] = int(self.lineEdit_4.text()) if self.lineEdit_4.text() != "" else json_attrib['Agility']
        json_attrib['Strength'] = int(self.lineEdit_5.text()) if self.lineEdit_5.text() != "" else json_attrib[
            'Strength']
        json_attrib['PhysicsAttackPower'] = int(self.lineEdit_6.text()) if self.lineEdit_6.text() != "" else \
        json_attrib['PhysicsAttackPower']
        json_attrib['PhysicsCriticalStrikeRate'] = float(
            self.lineEdit_7.text().strip("%")) / 100 if self.lineEdit_7.text() != "" else json_attrib[
            'PhysicsCriticalStrikeRate']
        json_attrib['PhysicsCriticalDamagePowerPercent'] = float(
            self.lineEdit_8.text().strip("%")) / 100 if self.lineEdit_8.text() != "" else json_attrib[
            'PhysicsCriticalDamagePowerPercent']
        json_attrib['PhysicsOvercomePercent'] = float(
            self.lineEdit_9.text().strip("%")) / 100 if self.lineEdit_9.text() != "" else json_attrib[
            'PhysicsOvercomePercent']
        json_attrib['StrainPercent'] = float(
            self.lineEdit_10.text().strip("%")) / 100 if self.lineEdit_10.text() != "" else json_attrib['StrainPercent']
        json_attrib['HastePercent'] = float(
            self.lineEdit_11.text().strip("%")) / 100 if self.lineEdit_11.text() != "" else json_attrib['HastePercent']
        json_attrib['SurplusValue'] = int(self.lineEdit_12.text()) if self.lineEdit_12.text() != "" else json_attrib[
            'SurplusValue']
        json_attrib['ParryPercent'] = float(
            self.lineEdit_13.text().strip("%")) / 100 if self.lineEdit_13.text() != "" else json_attrib['ParryPercent']
        json_attrib['ParryValue'] = int(self.lineEdit_14.text()) if self.lineEdit_14.text() != "" else json_attrib[
            'ParryValue']

        return json_attrib

    def get_attribute_with_set(self) -> Dict:
        """
        获取带套装字段的属性信息（内部用）\n
        :return:
        """
        json_attrib = self.get_attribute()
        ret = {
            'json': json_attrib,
            'recipe': json_attrib.get('atSetEquipmentRecipe'),
            'event': json_attrib.get('atSkillEventHandler')
        }

        # 首页的装备特殊信息设置
        # 手动的设置是最高优先级判定
        if not self.checkBox_29.isChecked():
            if ret['recipe']:
                ret['recipe'] = [i for i in ret['recipe'] if i != 1923]
        elif ret['recipe']:
            if 1923 not in ret['recipe']:
                ret['recipe'].append(1923)
        else:
            ret['recipe'] = [1923]

        if not self.checkBox_33.isChecked():
            if ret['event']:
                ret['event'] = [i for i in ret['event'] if i != 1222]
        elif ret['event']:
            if 1222 not in ret['event']:
                ret['event'].append(1222)
        else:
            ret['event'] = [1222]

        if not self.checkBox_34.isChecked():
            if ret['recipe']:
                ret['recipe'] = [i for i in ret['recipe'] if i not in {1932, 1933}]
        elif ret['recipe']:
            if 1932 not in ret['recipe']:
                ret['recipe'] += [1932]
            if 1933 not in ret['recipe']:
                ret['recipe'] += [1933]
        else:
            ret['recipe'] = [1932, 1933]

        return ret

    def get_level(self) -> int:
        return self.Level_spinBox.value()

    def get_settings(self) -> Dict:
        # 这里改设置条目的时候要同步到player
        ret = {
            'QiJin': 0,
            'CriticalByExpect': 0,
            'AttackFreq': 0,
            'AttackCount': 0,
            'Halo': None,
            'ParryByExpect': 0,
            'WeaponType': None,
            'PendantType': None,
            'Enchants': None,
        }
        item_to_key = {
            self.qijin_checkBox: 'QiJin',
            self.setting_critical_checkbox: 'CriticalByExpect',
            self.setting_parry_checkbox: 'ParryByExpect',
        }
        for box, key in item_to_key.items():
            if box.isChecked():
                ret[key] = 1
        match self.envior_button.text():
            case '副本':
                ret['AttackFreq'] = int(2.25 * 16)
                ret['AttackCount'] = 1
            case '地鼠门':
                ret['AttackFreq'] = int(2.25 * 16)
                ret['AttackCount'] = 6
            case '木桩':
                ret['AttackFreq'] = 1 * 16
                ret['AttackCount'] = 1

        if self.halo_button.text() in HALO_TO_ID:
            ret['Halo'] = HALO_TO_ID[self.halo_button.text()]

        ret['WeaponType'] = self.comboBox_12.currentText()
        ret['PendantType'] = self.comboBox_13.currentText()
        ret['Enchants'] = [self.comboBox_7.currentIndex(), self.comboBox_8.currentIndex(), self.comboBox_9.currentIndex(),
                           self.comboBox_10.currentIndex(), self.comboBox_11.currentIndex()]


        return ret

    def set_attrib_line_edit(self):

        # 装备属性部分
        json_attrib = self._attrib.attribute
        # 体质
        self.lineEdit_3.setText(f"{json_attrib['Vitality']}")
        # 身法
        self.lineEdit_4.setText(f"{json_attrib['Agility']}")
        # 力道
        self.lineEdit_5.setText(f"{json_attrib['Strength']}")
        # 攻击力
        self.lineEdit_6.setText(f"{json_attrib['PhysicsAttackPower']}")
        # 会心
        self.lineEdit_7.setText(f"{json_attrib['PhysicsCriticalStrikeRate']:.2%}")
        # 会效
        self.lineEdit_8.setText(f"{json_attrib['PhysicsCriticalDamagePowerPercent']:.2%}")
        # 破防
        self.lineEdit_9.setText(f"{json_attrib['PhysicsOvercomePercent']:.2%}")
        # 无双
        self.lineEdit_10.setText(f"{json_attrib['StrainPercent']:.2%}")
        # 加速率
        self.lineEdit_11.setText(f"{json_attrib['HastePercent']:.2%}")
        # 破招
        self.lineEdit_12.setText(f"{json_attrib['SurplusValue']}")
        # 招架
        self.lineEdit_13.setText(f"{json_attrib['ParryPercent']:.2%}")
        # 拆招
        self.lineEdit_14.setText(f"{json_attrib['ParryValue']}")

        # 装备效果部分
        equip_effect_id = {
            1932: self.checkBox_34,
            1222: self.checkBox_33,
            1923: self.checkBox_29,
        }
        recipes = json_attrib.get('atSetEquipmentRecipe')
        if recipes:
            if 1932 in recipes:
                equip_effect_id[1932].setChecked(True)
            else:
                equip_effect_id[1932].setChecked(False)
        events = json_attrib.get('atSkillEventHandler')
        if events:
            if 1222 in events:
                equip_effect_id[1222].setChecked(True)
            else:
                equip_effect_id[1222].setChecked(False)
            if 1923 in events:
                equip_effect_id[1923].setChecked(True)
            else:
                equip_effect_id[1923].setChecked(False)

        dwEquipData = json_attrib.get('EquipList')
        if not dwEquipData:
            return

        # 武器类型
        dwWeaponID = 0
        dwWeaponData = dwEquipData.get('PRIMARY_WEAPON')
        if dwWeaponData:
            dwWeaponID = dwWeaponData.get('id')

        if dwWeaponID:
            for index, ids in WEAPON_TYPE.items():
                if dwWeaponID in ids:
                    self.comboBox_12.setCurrentIndex(index)
                    break
            else:
                self.comboBox_12.setCurrentIndex(0)
        else:
            self.comboBox_12.setCurrentIndex(0)

        # 腰坠类型
        dwPendantID = 0
        dwPendantData = dwEquipData.get('PENDANT')
        if dwPendantData:
            dwPendantID = dwPendantData.get('id')

        if dwPendantID:
            for index, ids in PENDANT_TYPE.items():
                if dwPendantID in ids:
                    self.comboBox_13.setCurrentIndex(index)
                    break
            else:
                self.comboBox_13.setCurrentIndex(0)
        else:
            self.comboBox_13.setCurrentIndex(0)

        # 大附魔
        boxes = {
            'HAT': self.comboBox_7,
            'JACKET': self.comboBox_8,
            'BELT': self.comboBox_9,
            'WRIST': self.comboBox_10,
            'SHOES': self.comboBox_11,
        }
        for str_key, pos_id in EQUIP_POSITION.items():
            box: QComboBox = boxes[str_key]
            dwPositionData = dwEquipData.get(str_key)
            if not dwPositionData:
                continue

            dwEnchantID = dwPositionData.get('enchant')
            if not dwEnchantID:
                nIndex = 0
            else:
                szEnchantName = enchant['enchant'][pos_id].get(dwEnchantID)
                if not szEnchantName:
                    nIndex = 0
                else:
                    szEnchantName = szEnchantName['Name']
                    for nIndex in range(5):
                        if box.itemText(nIndex) == szEnchantName:
                            break
                    else:
                        nIndex = 0

            box.setCurrentIndex(nIndex)

        # 奇穴
        dwTalentData = json_attrib.get("TalentCode")
        if not dwTalentData:
            return

        szTalentCode = {"version": "v20221202", "xf": "铁骨衣", "sq": ""}
        for dwTalent in dwTalentData:
            szName = dwTalent["name"]
            nIndex = [TALENT_INDEX[i] for i in TALENT_INDEX if szName in i]
            if not nIndex:
                nIndex = 1
            else:
                nIndex = nIndex[0]
            szTalentCode["sq"] += f"{nIndex},"
        szTalentCode["sq"] = szTalentCode["sq"][:-1]
        self._selector.set_data_by_json(szTalentCode)


    def set_skill_data_table(self, data: Dict, nFightTime=None, nDps=None):
        """
        设置输出统计表格\n
        :param data:
        :return:
        """

        # 先遍历一遍，排序并算百分比
        nTotalDamage = 0
        list_data = []

        for skill_name, skill_data in data.items():
            list_data.append({
                'name': skill_name,
                'count': int(skill_data['count']),
                'damage': skill_data['damage'],
                'percent': '',
                'critical': f"{skill_data['critical'] / skill_data['count']:.2%}",
            })
            nTotalDamage += skill_data['damage']

        for index, item in enumerate(list_data):
            list_data[index]['percent'] = f'{item["damage"] / nTotalDamage:.2%}'
        list_data.sort(key=lambda i: i['damage'], reverse=True)

        self.skill_data_table.setRowCount(len([i for i in list_data if i['damage'] > 0]))

        if nFightTime:
            self.dps_label.setText(f'{int(nTotalDamage / (nFightTime / 16))}')
        if nDps:
            self.dps_label.setText(f"{nDps}")

        for index, item in enumerate(list_data):
            self.skill_data_table.setItem(index, 0, QTableWidgetItem(f'{item["name"]}'))
            self.skill_data_table.setItem(index, 1, QTableWidgetItem(f'{item["count"]}'))
            self.skill_data_table.setItem(index, 2, QTableWidgetItem(f'{item["damage"]}'))
            self.skill_data_table.setItem(index, 3, QTableWidgetItem(f'{item["percent"]}'))
            self.skill_data_table.setItem(index, 4, QTableWidgetItem(f'{item["critical"]}'))

    def set_attribute_profits(self, *args):
        self.profit_data = {
            '单点收益': args[0],
            '同分收益(装备)': args[2],
            '同分收益(其他增益)': args[1],
        }
        # 设置数据时是初次调用，默认展示单分收益
        self.comboBox_6.setCurrentIndex(2)

    def draw_attribute_profits(self, text):
        marker_profits = self.profit_data[text]
        self._painter.DrawAttributeProfits(marker_profits, text)

    def set_special_equip_selector(self):
        """
        设置武器类型和腰坠类型的选择\n
        :return:
        """
        try:
            dwWeaponList = eval(self.config['weapon_type'])
            dwPendantList = eval(self.config['pendant_type'])

            self.comboBox_12.addItems(dwWeaponList)
            self.comboBox_13.addItems(dwPendantList)

        except:
            return

    def get_command_id(self):
        commands_id = {
            "怒绝": 60000,
            "双绝": 60002,
            "高城": 60003,
        }
        szText = self.comboBox_14.currentText()
        nID = commands_id.get(szText)
        if not nID:
            return 0
        else:
            return nID

    def set_talent_by_command(self, command):
        commands_id = {
            "怒绝": {"version": "v20221202", "xf": "铁骨衣", "sq": "2,1,4,3,3,2,4,4,1,4,5,5"},
            "双绝": {"version": "v20221202", "xf": "铁骨衣", "sq": "2,1,4,3,3,2,4,4,1,4,5,5"},
            "怒血": {"version": "v20221202", "xf": "铁骨衣", "sq": "2,1,4,3,3,1,4,4,1,4,5,5"},
            "千血": {"version": "v20221202", "xf": "铁骨衣", "sq": "2,1,4,3,1,1,4,4,1,4,5,5"},
            "高城": {"version": "v20221202", "xf": "铁骨衣", "sq": "2,1,4,3,3,2,4,4,1,1,5,5"},
        }
        dwTalentData = commands_id.get(command)
        if not dwTalentData:
            return

        self._selector.set_data_by_json(dwTalentData)

        if command == '高城':
            self.qijin_checkBox.setChecked(True)

    def add_history(self, data, command, dps, halo, qijin, attr="None"):
        if halo == '无阵眼':
            halo = '无'
        else:
            halo = halo[:-1]

        if qijin:
            qijin = '是'
        else:
            qijin = '否'

        tb = self.tableWidget
        nNewRow = tb.rowCount()
        tb.setRowCount(nNewRow+1)
        for index, item in enumerate([command, dps, halo, qijin, attr]):
            tb_item = QTableWidgetItem(f"{item}")
            tb_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tb.setItem(nNewRow, index, tb_item)

        # 历史记录设置
        if self.history_record is None:
            self.history_record = [data]
        else:
            self.history_record.append(data)

    def read_history(self, index):
        if self.history_record is None:
            return

        try:
            dwHistory = self.history_record[index]
        except IndexError:
            return

        nDps = self.tableWidget.item(index, 1).text()

        self.set_skill_data_table(dwHistory, nDps=nDps)

    def set_enchant_select_box(self):
        try:
            enchants = eval(self.config['enchants'])
            if len(enchants) != 2:
                return
        except:
            return

        slot1 = ['·御·', '·伤·']
        slot2 = {
            '帽': self.comboBox_7,
            '衣': self.comboBox_8,
            '腰': self.comboBox_9,
            '腕': self.comboBox_10,
            '鞋': self.comboBox_11,
        }
        for box in slot2.values():
            box.setView(QListView())
            box.addItem('无附魔')

        for index, enchant_type in enumerate(slot1):
            # 蓝色
            str1 = enchants[0] + enchant_type
            # 紫色
            str2 = enchants[1] + enchant_type
            # 部位
            for str_pos, box in slot2.items():
                str_pos_1 = str1 + str_pos
                str_pos_2 = str2 + str_pos
                box.addItem(str_pos_1)
                box.setItemData(index*2+1, QColor('blue'), Qt.ForegroundRole)
                box.addItem(str_pos_2)
                box.setItemData(index*2+2, QColor('purple'), Qt.ForegroundRole)

    def set_enchant_select_box_text_color(self, box: QComboBox):
        enchants = eval(self.config['enchants'])
        def inner():
            szText = box.currentText()
            if enchants[0] in szText:
                color = "#69a2eb"
            elif enchants[1] in szText:
                color = "#9a479a"
            else:
                color = "#000000"
            box.setStyleSheet(f"color: {color};")
        return inner

    def set_self_advance_select_box(self):
        # 宴席
        self.comboBox_15.setView(QListView())
        self.comboBox_15.addItem("无")
        self.comboBox_15.addItems([i for i in TABLES.keys() if i.startswith("断浪·")])
        self.comboBox_15.currentTextChanged.connect(self.self_advance_box_clicked(self.comboBox_15))
        # 其他内容
        links = {
            self.comboBox_19: ADVANCE_MEDICINE,
            self.comboBox_20: ASSIST_MEDICINE,
            self.comboBox_21: ADVANCE_FOOD,
            self.comboBox_22: ASSIST_FOOD,
            self.comboBox_23: WEAPON_ENCHANT,
            self.comboBox_24: HOME_FOOD,
            self.comboBox_25: HOME_WINE,
        }
        for k, v in links.items():
            k.setView(QListView())
            k.addItem("无")
            k.addItems(v.keys())
            k.currentTextChanged.connect(self.self_advance_box_clicked(k))

    def self_advance_box_clicked(self, box: QComboBox):
        links = {
            self.comboBox_15: TABLES,
            self.comboBox_19: ADVANCE_MEDICINE,
            self.comboBox_20: ASSIST_MEDICINE,
            self.comboBox_21: ADVANCE_FOOD,
            self.comboBox_22: ASSIST_FOOD,
            self.comboBox_23: WEAPON_ENCHANT,
            self.comboBox_24: HOME_FOOD,
            self.comboBox_25: HOME_WINE,
        }
        links2 = {
            self.comboBox_15: "宴席",
            self.comboBox_19: "增强类药品",
            self.comboBox_20: "辅助类药品",
            self.comboBox_21: "增强类食品",
            self.comboBox_22: "辅助类食品",
            self.comboBox_23: "武器限时附魔",
            self.comboBox_24: "家园烹饪",
            self.comboBox_25: "家园酿造",
        }
        def inner(text):
            data_table = links.get(box)
            if not data_table:
                return

            if text == '无':
                szText = ""
            else:
                szText = data_table.get(text)
                if not szText:
                    return

                szText = szText['desc']
                self.plainTextEdit.setPlainText(f"[{text}]\n\n 类型：{links2[box]}\n\n {szText}")

        return inner

    def self_advance_check_clicked(self, box: QCheckBox):
        link = {
            self.qijin_checkBox: "铁骨气劲",
            self.checkBox_35: "同泽宴",
            self.checkBox_36: "炼狱水煮鱼",
            self.checkBox_37: "蒸鱼菜盘",
        }
        def inner():

            text = link.get(box)
            if not text:
                return

            if text != "铁骨气劲":
                szText = TABLES.get(text)
                if not szText:
                    return

                szText = szText['desc']
                self.plainTextEdit.setPlainText(f"[{text}]\n\n 类型：宴席\n\n {szText}")
            else:
                szText = "秘境中若自身周围30尺存在4个及以上的友方目标，自身受到攻击且为其第一仇恨时获得“铁骨”气劲：每点体质提高0.04点外功攻击力，0.02点破防等级，威胁值大体不变，最大叠加15层，持续12秒。"
                self.plainTextEdit.setPlainText(f"[{text}]\n\n {szText}")

        return inner

    def get_self_advance_attribute(self) -> List[attrib_data]:
        """
        读取所有小吃小药并返回属性序列\n
        :return:
        """
        dwAttribs = []
        links = {
            self.comboBox_15: TABLES,
            self.comboBox_19: ADVANCE_MEDICINE,
            self.comboBox_20: ASSIST_MEDICINE,
            self.comboBox_21: ADVANCE_FOOD,
            self.comboBox_22: ASSIST_FOOD,
            self.comboBox_23: WEAPON_ENCHANT,
            self.comboBox_24: HOME_FOOD,
            self.comboBox_25: HOME_WINE,
        }

        for box, table in links.items():
            szText = box.currentText()
            if szText in table:
                dwAttribs += table.get(szText)['attr']

        link = {
            self.checkBox_35: "同泽宴",
            self.checkBox_36: "炼狱水煮鱼",
            self.checkBox_37: "蒸鱼菜盘",
        }
        for box, key in link.items():
            if box.isChecked():
                dwAttribs += TABLES.get(key)['attr']

        return dwAttribs

    def self_advance_clear_button(self):
        cb = {
            self.qijin_checkBox,
            self.checkBox_35,
            self.checkBox_36,
            self.checkBox_37,
        }
        for i in cb:
            i.setChecked(False)

        bx = {
            self.comboBox_15,
            self.comboBox_19,
            self.comboBox_20,
            self.comboBox_21,
            self.comboBox_22,
            self.comboBox_23,
            self.comboBox_24,
            self.comboBox_25,
        }
        for i in bx:
            i.setCurrentIndex(0)

    def self_advance_text_func(self):
        """
        自身增益的说明\n
        :return:
        """
        szText = "[单体增益]\n\n 指自身可以提供的增益内容，包括T气劲和各类小吃小药，详细效果可以通过选择对应选项查看。\n\n 依副本实际情况勾选即可。"
        self.plainTextEdit.setPlainText(szText)


    def other_advance_major_box_clicked(self, box: QCheckBox):
        link = {
            self.checkBox_38: [self.groupBox_28, "[铁牢律]\n\n 团本常见\n\n 常见增益：号令三军、劲风(破风)\n\n 乘龙箭使用者较少。\n\n 号令三军选项框右侧为填写层数的位置，一般默认即可。"],
            self.checkBox_39: [self.groupBox_29, "[洗髓经]\n\n 团本较少\n\n 舍身弘法为单体增益，一般情况下铁骨享受不到。\n\n 舍身弘法选项框右侧为填写层数的位置，一般默认即可。"],
            self.checkBox_40: [self.groupBox_30, "[明尊琉璃体]\n\n 团本常见\n\n 常见增益：朝圣言(铁骨较难利用)、戒火斩\n\n 额外注意：戒火斩会被秋肃顶替。\n\n 朝圣言选项框右侧为填写层数的位置，一般默认即可。"],
            self.checkBox_41: [self.groupBox_31, "[铁骨衣]\n\n  双铁骨在团本中较少见\n\n 常见增益：振奋、寒啸千军\n\n 会补虚弱的人数比例较少\n\n 这里指的是给自己提供增益的副T铁骨，非自身。\n\n 振奋选项框右侧为填写层数的位置，一般默认即可。"],
            self.checkBox_42: [self.groupBox_32, "[离经易道]\n\n 团本常见\n\n 常见增益：秋肃\n\n 落子无悔为爆发治疗技能，一般不会作为增益使用。\n\n 秋肃会顶替掉戒火斩的效果。"],
            self.checkBox_43: [self.groupBox_33, "[云裳心经]\n\n 团本常见\n\n 常见增益：左旋右转\n\n 泠风解怀收益很低，一般不会点出。"],
            self.checkBox_44: [self.groupBox_34, "[补天诀]\n\n 团本常见\n\n 常见增益：仙王蛊鼎"],
            self.checkBox_45: [self.groupBox_35, "[相知]\n\n 团本常见\n\n 常见增益：梅花三弄\n\n 梅花三弄的覆盖率取决于铁骨自身奇穴和相知奇穴，有雄峦或天音知脉的情况下覆盖率会变高，请依照实际情况填写覆盖率\n\n 弄梅(风雷瑶琴剑梅花盾)对于铁骨覆盖率较低。\n\n 梅花三弄及弄梅右侧为填写覆盖率的位置，一般默认即可，也可按照实际情况填写。"],
            self.checkBox_46: [self.groupBox_36, "[灵素]\n\n 团本常见\n\n 常见增益：配伍、飘黄\n\n 香稠对于输出主T收益很高，对于团队总DPS也是正提升，但对治疗量有影响，一般情况下灵素不会默认选择此奇穴。"],
        }

        def inner(checked):
            gb = link.get(box)
            if not gb:
                return

            gb[0].setEnabled(checked)
            self.plainTextEdit.setPlainText(gb[1])

        return inner

    def get_other_advance_data(self):
        ret = {
            'Mates': None,
            'Talents': None,
            'Stacks': None
        }
        # all_mates = {
        #     "铁牢律": None,
        #     "洗髓经": None,
        #     "明尊琉璃体": None,
        #     "铁骨衣": None,
        #     "离经易道": None,
        #     "云裳心经": None,
        #     "补天诀": None,
        #     "相知": None,
        #     "灵素": None,
        # }
        talents = {
            self.checkBox_47: 15115,
            self.checkBox_48: 18872,
            self.checkBox_49: 2603,
            self.checkBox_50: 15195,
            self.checkBox_51: 3985,
            self.checkBox_52: 3980,
            self.checkBox_53: 50012,
            self.checkBox_54: 50013,
            self.checkBox_55: 50014,
            self.checkBox_56: 31208,
            self.checkBox_57: 567,
            self.checkBox_58: 30850,
            self.checkBox_59: 2234,
            self.checkBox_60: 14071,
            self.checkBox_67: 23826,
            self.checkBox_61: 28650,
            self.checkBox_63: 28722,
            self.checkBox_62: 28678,
            self.checkBox_68: 32381,
            }
        bx = {
            self.checkBox_38: "铁牢律",
            self.checkBox_39: "洗髓经",
            self.checkBox_40: "明尊琉璃体",
            self.checkBox_41: "铁骨衣",
            self.checkBox_42: "离经易道",
            self.checkBox_43: "云裳心经",
            self.checkBox_44: "补天诀",
            self.checkBox_45: "相知",
            self.checkBox_46: "灵素",
        }

        for box, origin in bx.items():
            # if not box.isEnabled():
            #     continue
            if not box.isChecked():
                continue

            if ret['Mates'] is None:
                ret['Mates'] = [origin]
            else:
                ret['Mates'].append(origin)

        # 破风特殊处理
        if ret['Mates']:
            if "铁牢律" in ret['Mates']:
                ret['Talents'] = [403]

        for box, talent_id in talents.items():
            if not box.isEnabled():
                continue
            if not box.isChecked():
                continue

            if ret['Talents'] is None:
                ret['Talents'] = [talent_id]
            else:
                ret['Talents'].append(talent_id)



        ret['Stacks'] = {
            15115: self.spinBox.value(),
            15195: self.spinBox_2.value(),
            3985: self.spinBox_3.value(),
            50012: self.spinBox_4.value(),
            14071: self.spinBox_7.value() / 100,
            23826: self.spinBox_8.value() / 100,
        }

        return ret



    def other_advance_clear_button(self):
        bx = {
            self.checkBox_38: self.groupBox_28,
            self.checkBox_39: self.groupBox_29,
            self.checkBox_40: self.groupBox_30,
            self.checkBox_41: self.groupBox_31,
            self.checkBox_42: self.groupBox_32,
            self.checkBox_43: self.groupBox_33,
            self.checkBox_44: self.groupBox_34,
            self.checkBox_45: self.groupBox_35,
            self.checkBox_46: self.groupBox_36,
        }
        for k, v in bx.items():
            k.setChecked(False)
            v.setEnabled(False)

    def other_advance_text_func(self):
        szText = "[团队增益]\n\n 指团队内其他成员提供给自身的增益，详细效果可以通过选择对应选项查看。\n\n 部分团队增益并不常见或是个人增益，非固定团时也不要强求。"
        self.plainTextEdit.setPlainText(szText)

    def other_advance_explain_func(self):
        talents = {
            self.checkBox_47: "[号令三军]\n\n 一鼓，自身每1125点基础体质使团队成员无双等级提高400点，最多48层，持续30秒；二鼓，团队成员的无双提高层数衰减一半，持续30秒；三鼓，团队成员受到的所有伤害提高10%，持续至战斗结束，该招式每场战斗只能施展一次。",
            self.checkBox_48: "[龙吟]\n\n 对目标造成100%的武器伤害外加外功伤害并使自身获得2点战意，使目标同时附带“流血”和“破风”效果，“流血”效果使目标每2秒受到外功伤害且可叠加2层。“破风”效果使目标外功防御等级降低1150点，持续14秒。\n\n [劲风]\n\n 奇穴效果，“龙吟”附带的“破风”效果提高33%。\n\n 激活铁牢律后默认存在破风效果，勾选此项后会变为劲风奇穴效果",
            self.checkBox_49: "[乘龙箭]\n\n 运功0.5秒，打断目标运功，对目标造成外功伤害，并使其外功防御等级降低10%，持续10秒，自身将获得一点“战意”，命中超过地面8尺以上的目标会将其击落倒地2秒，马上方可施展。",
            self.checkBox_50: "[舍身弘法]\n\n 可对团队成员施展，每950点基础体质使目标无双等级提高240点、基础疗伤成效提高250点，最多36层。承担其受到的所有伤害，且期间目标造成的仇恨值全部转移到自身，并使自身气血最大值提高20%，持续20秒。",
            self.checkBox_51: "[朝圣言]\n\n 需持续运功。8秒内强迫自身周围12尺范围内所有敌对目标攻击自身，并使范围内所有团队成员每秒回复5%气血上限，自身每2250点基础体质使团队成员无双等级提高400点，最多24层。持续运功时自身受到的伤害降低60%，不受移动限制，无法被打断，完整施展后立刻击飞自身周围12尺内的15个敌对目标。\n\n 若激活奇穴[圣浴明心]，则仅需将层数×1.5后重新填写即可。",
            self.checkBox_52: "[戒火斩]\n\n 对目标造成阳性内功伤害，并使其受到的伤害提高2%，持续15秒。该招式附带额外威胁值。",
            self.checkBox_53: "[振奋]\n\n 施展“盾挡”后，自身每1500点招架等级使得自身20尺范围内最多25个团队成员外功、内功破防等级提高60点，持续10秒。",
            self.checkBox_54: "[寒啸千军]\n\n 消耗20点格挡值，鼓舞团队士气，使自身半径20尺内最多25名团队成员内外功破防等级提高20%，持续15秒。",
            self.checkBox_55: "[虚弱]\n\n 使目标外功防御等级降低5%。\n\n 主T的虚弱由于输出循环中的斩刀，覆盖率较低。副T铁骨的虚弱可以达到100%覆盖率。",
            self.checkBox_56: "[秋肃]\n\n 商阳指”调息时间增加15秒，施展“商阳指”，使目标40秒内受到的伤害提高6%，不可与同类效果叠加。\n\n 会移除[戒火]易伤效果",
            self.checkBox_57: "[左旋右转]\n\n 需“名动四方”触发的剑舞状态，持续运功5秒，期间每秒使自身12尺内所有团队成员气血值回复，且破招值提高4500点，持续12秒，该气劲时间可叠加，最多60秒。若周围15尺友方目标数量少于等于10人，则造成的治疗效果提升100%。",
            self.checkBox_58: "[泠风解怀]\n\n 需要“名动四方”触发的剑舞状态，链接自身与友方目标，使目标气血值回复，链接持续5秒，若双方距离超过25尺则提前结束链接状态。链接期间友方目标的伤害、治疗成效提高10%，且每0.5秒减少自身“风袖低昂”调息时间0.5秒，使友方目标气血值回复，并减少其0.5秒“梦冧”不利气劲。链接效果期间，自身施展“帝骖龙翔”后产生的控制效果会延迟1秒在链接的友方目标位置生效。",
            self.checkBox_59: "[仙王蛊鼎]\n\n 在地面放置一个仙王蛊鼎，使周围15尺内所有团队成员造成的伤害提高12%，仙王蛊鼎消失后结束。你所属的小队或团队成员可以点击它，每人每15秒只能使用一次，最多可被使用20次。使用后恢复30%气血值和20%内力值。仙王蛊鼎在25秒之后消失。",
            self.checkBox_60: "[庄周梦]\n\n “梅花三弄”持续期间，目标伤害招式无视目标15%内外功防御等级。",
            self.checkBox_67: "[弄梅]\n\n 由长歌特殊武器·风雷瑶琴剑(相知心法)产生，吸收大量伤害，使自身伤害招式无视目标20%内外功防御等级并提升自身700点破防等级，吸收值可通过过量治疗效果填充，持续时间结束时若在战斗中且护盾值为最大，会刷新护盾持续时间。",
            self.checkBox_61: "[香稠]\n\n “赤芍寒香”治疗量提高10%，施展“赤芍寒香”使得目标体质提高20%，相同该效果不能共存。",
            self.checkBox_63: "[配伍]\n\n “灵素中和”治疗量提高13%，命中目标使其提高1%的力道、身法、元气和根骨，最多叠加5层，持续10秒。",
            self.checkBox_62: "[飘黄]\n\n “逐云寒蕊”不再产生隐匿效果，使得“逐云寒蕊”10尺范围的团队成员施展伤害招式附带一段额外伤害，该伤害无视目标100%的防御，最多每1.5秒触发一次，持续10秒，该效果在60秒内只能享受一次。",
            self.checkBox_68: "[落子无悔]\n\n 主动技能，引爆所有棋子，对自身15尺范围内团队成员造成169-186(+1.63*治疗量)治疗效果。若场上黑子多于白子，将使受到治疗的成员受到“落墨”效果，使受到的伤害降低20%，持续5秒，不可与其他减伤效果叠加。若白子多于黑子，则将使受到治疗的成员受到“皎素”效果，提高5%的会心效果，持续10秒。\n\n 默认每次落子无悔都触发[皎素]效果。",
            }

        def set_text(text):
            def inner():
                self.plainTextEdit.setPlainText(text)
            return inner

        for k, v in talents.items():
            k.clicked.connect(set_text(v))


    def get_fight_time(self) -> int:
        nFightTime = self.spinBox_6.text()
        try:
            nFightTime = int(nFightTime)
            nFightTime *= 60 * 16

        except:
            nFightTime = 300*16

        return nFightTime













