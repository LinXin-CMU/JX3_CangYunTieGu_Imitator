# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from typing import List, Dict
from functools import reduce

from .ui import Ui_MainWindow
from settings.jx3_collections import recipe
from settings.config import ConfigSetting
from .modules.ui_selector import TalentSelector
from .modules.ui_setter import UiSetter
from .modules.ui_equip import UiEquip

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
        self._equipsetter = UiEquip(self)
        self._equipsetter.import_json_func(data=self.config['default_equips'])

        self.skill_data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.resize(1246, 849)
        self.setMinimumSize(1246, 849)
        self.setMaximumSize(1246, 849)

    def get_talent(self) -> Dict[int, str]:
        return self._selector.talent

    def get_recipe(self) -> List[int]:
        recipes = []
        recipe_index = reduce(lambda i, j: i+j, [i for i in self._selector.recipe.values()])
        for recipe_id in recipe:
            if recipe[recipe_id].index in recipe_index:
                recipes.append(recipe_id)

        return recipes

    def get_attribute(self) -> Dict:
        json_attrib = eval(self._equipsetter.equip_attribute.json_attributes)
        json_attrib['Vitality'] = int(self.lineEdit_3.text()) if self.lineEdit_3.text() != "" else json_attrib['Vitality']
        json_attrib['Agility'] = int(self.lineEdit_4.text()) if self.lineEdit_4.text() != "" else json_attrib['Agility']
        json_attrib['Strength'] = int(self.lineEdit_5.text()) if self.lineEdit_5.text() != "" else json_attrib['Strength']
        json_attrib['PhysicsAttackPower'] = int(self.lineEdit_6.text()) if self.lineEdit_6.text() != "" else json_attrib['PhysicsAttackPower']
        json_attrib['PhysicsCriticalStrikeRate'] = float(self.lineEdit_7.text().strip("%"))/100 if self.lineEdit_7.text() != "" else json_attrib['PhysicsCriticalStrikeRate']
        json_attrib['PhysicsCriticalDamagePowerPercent'] = float(self.lineEdit_8.text().strip("%"))/100 if self.lineEdit_8.text() != "" else json_attrib['PhysicsCriticalDamagePowerPercent']
        json_attrib['PhysicsOvercomePercent'] = float(self.lineEdit_9.text().strip("%"))/100 if self.lineEdit_9.text() != "" else json_attrib['PhysicsOvercomePercent']
        json_attrib['StrainPercent'] = float(self.lineEdit_10.text().strip("%"))/100 if self.lineEdit_10.text() != "" else json_attrib['StrainPercent']
        json_attrib['HastePercent'] = float(self.lineEdit_11.text().strip("%"))/100 if self.lineEdit_11.text() != "" else json_attrib['HastePercent']
        json_attrib['SurplusValue'] = int(self.lineEdit_12.text()) if self.lineEdit_12.text() != "" else json_attrib['SurplusValue']
        json_attrib['ParryPercent'] = float(self.lineEdit_13.text().strip("%"))/100 if self.lineEdit_13.text() != "" else json_attrib['ParryPercent']
        json_attrib['ParryValue'] = int(self.lineEdit_14.text()) if self.lineEdit_14.text() != "" else json_attrib['ParryValue']
        
        return json_attrib

    def get_level(self) -> int:
        return self.Level_spinBox.value()

    def get_settings(self) -> Dict:
        ret = {
            'QiJin': 0,
            'CriticalByExpect': 0,
            'AttackFreq': 0,
            'AttackCount': 0,
            'Halo': None,
            'ParryByExpect': 0,
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
                ret['AttackFreq'] = 2.25 * 16
                ret['AttackCount'] = 1
            case '地鼠门':
                ret['AttackFreq'] = 2.25 * 16
                ret['AttackCount'] = 6
            case '木桩':
                ret['AttackFreq'] = 1 * 16
                ret['AttackCount'] = 1

        if self.halo_button.text() in HALO_TO_ID:
            ret['Halo'] = HALO_TO_ID[self.halo_button.text()]

        return ret

    def set_attrib_line_edit(self):
        json_attrib = eval(self._equipsetter.equip_attribute.json_attributes)
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


    def set_skill_data_table(self, data: Dict):
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
        self.dps_label.setText(f'{int(nTotalDamage/300)}')
        for index, item in enumerate(list_data):
            self.skill_data_table.setItem(index, 0, QTableWidgetItem(f'{item["name"]}'))
            self.skill_data_table.setItem(index, 1, QTableWidgetItem(f'{item["count"]}'))
            self.skill_data_table.setItem(index, 2, QTableWidgetItem(f'{item["damage"]}'))
            self.skill_data_table.setItem(index, 3, QTableWidgetItem(f'{item["percent"]}'))
            self.skill_data_table.setItem(index, 4, QTableWidgetItem(f'{item["critical"]}'))








