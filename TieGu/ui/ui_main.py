# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from typing import List, Dict
from functools import reduce

from .ui import Ui_MainWindow
from settings.jx3_collections import recipe
from .modules.ui_selector import TalentSelector
from .modules.ui_setter import UiSetter

HALO_TO_ID = {
    '铁骨阵': 'Halo_TieGu',
    '凌雪阵': 'Halo_LingXue',
}


class MainUI(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)
        self._selector = TalentSelector(self)
        self._setter = UiSetter(self)

        self.skill_data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.groupBox_15.move(90, 260)
        self.groupBox_15.setVisible(False)
        self.groupBox_16.move(90, 300)
        self.groupBox_16.setVisible(False)

    def get_talent(self) -> List[int]:
        return self._selector.talent

    def get_recipe(self) -> List[int]:
        recipes = []
        recipe_index = reduce(lambda i, j: i+j, [i for i in self._selector.recipe.values()])
        for recipe_id in recipe:
            if recipe[recipe_id].index in recipe_index:
                recipes.append(recipe_id)

        return recipes

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








