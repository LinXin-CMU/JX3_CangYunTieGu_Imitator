# # coding: utf-8
# # author: LinXin
# from re import compile, match, search
#
# from PyQt5.QtWidgets import QPushButton, QMainWindow, QListView, QTableWidget, QHBoxLayout, QVBoxLayout, QLabel, \
#     QComboBox, QTableWidgetItem, QInputDialog
# from PyQt5.QtCore import Qt
# from PyQt5.Qt import QFontMetrics
# from typing import Union, Dict
#
# from ui.ui import Ui_MainWindow
# from ui.modules.ui_other import ICONS, POSITION_NAME, SLOT_DICT, UI_COLOR, StarLabel, WEAPON_TYPE, ENCHANT_NEED, ENCHANT_DUTY, \
#     STONE_ATTRIB_DICT, ClickableComboBox, POSITION_KEY
# from ui.modules.calc_equip import EquipAttribute
# from ui.modules.calc_equip import get_equip_score
# from settings.config import ConfigSetting
# from db.jx3_equip import equip
# from db.jx3_stone import stone
# from db.jx3_enchant import enchant
# from settings.jx3_types import Player
#
#
# # noinspection PyTypeChecker
# class UiEquip:
#
#     # noinspection PyTypeChecker,PyUnresolvedReferences
#     def __init__(self, ui: Union[Ui_MainWindow, QMainWindow]):
#         self.ui = ui
#         self.config = ConfigSetting()
#
#         self._equip_data: Dict = equip  # 根据subtype分类的装备表
#         self.current_filtrated_equip_list = None  # 当前筛选出的装备序列
#         self.current_filtrated_enhance_list = None  # 当前筛选出的小附魔序列
#         self.current_filtrated_enchant_list = None  # 当前筛选出的大附魔序列
#         self.current_position = 3
#         self.current_position_data = None  # 当前装备所属按钮及控件的数据
#         self.current_embedding_setting_index = None     # 当前要设置的镶嵌是几号位
#         self.current_filtrated_stone_list = None      # 当前筛选出的五彩石序列
#         self.stone_selector = {1: '..', 2: '..', 3: '..'}     # 五彩石指定匹配条件
#
#         self.equip_attribute = EquipAttribute(self.ui)
#
#         self.equip_list = {
#                 "HAT": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                         "embedding": [6, 6], "data": "", "score": None},
#                 "BELT": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                          "embedding": [6, 6], "data": "", "score": None},
#                 "SHOES": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                           "embedding": [6, 6], "data": "", "score": None},
#                 "WRIST": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                           "embedding": [6, 6], "data": "", "score": None},
#                 "JACKET": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                            "embedding": [6, 6], "data": "", "score": None},
#                 "RING_1": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                            "embedding": [], "data": "", "score": None},
#                 "RING_2": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                            "embedding": [], "data": "", "score": None},
#                 "BOTTOMS": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                             "embedding": [6, 6], "data": "", "score": None},
#                 "PENDANT": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                             "embedding": [6], "data": "", "score": None},
#                 "NECKLACE": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                              "embedding": [6], "data": "", "score": None},
#                 "PRIMARY_WEAPON": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                                    "embedding": [6, 6, 6], "data": "", "score": None},
#                 "SECONDARY_WEAPON": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
#                                      "embedding": [6], "data": "", "score": None}
#         }
#
#         self.position_data = {
#             self.ui.pushButton_91: {'position': '3', 'name': '帽子', 'name_label': None, 'strength_label': None,
#                                     'str_key': 'HAT'},
#             self.ui.pushButton_92: {'position': '2', 'name': '上衣', 'name_label': None, 'strength_label': None,
#                                     'str_key': 'JACKET'},
#             self.ui.pushButton_93: {'position': '6', 'name': '腰带', 'name_label': None, 'strength_label': None,
#                                     'str_key': 'BELT'},
#             self.ui.pushButton_94: {'position': '10', 'name': '护腕', 'name_label': None, 'strength_label': None,
#                                     'str_key': 'WRIST'},
#             self.ui.pushButton_95: {'position': '8', 'name': '下装', 'name_label': None, 'strength_label': None,
#                                     'str_key': 'BOTTOMS'},
#             self.ui.pushButton_96: {'position': '9', 'name': '鞋子', 'name_label': None, 'strength_label': None,
#                                     'str_key': 'SHOES'},
#             self.ui.pushButton_97: {'position': '4', 'name': '项链', 'name_label': None, 'strength_label': None,
#                                     'str_key': 'NECKLACE'},
#             self.ui.pushButton_98: {'position': '7', 'name': '腰坠', 'name_label': None, 'strength_label': None,
#                                     'str_key': 'PENDANT'},
#             self.ui.pushButton_99: {'position': '5', 'name': '戒指', 'name_label': None, 'strength_label': None,
#                                     'str_key': 'RING_1'},
#             self.ui.pushButton_100: {'position': '5', 'name': '戒指', 'name_label': None, 'strength_label': None,
#                                      'str_key': 'RING_2'},
#             self.ui.pushButton_101: {'position': '1', 'name': '远程武器', 'name_label': None, 'strength_label': None,
#                                      'str_key': 'SECONDARY_WEAPON'},
#             self.ui.pushButton_102: {'position': '0', 'name': '近身武器', 'name_label': None, 'strength_label': None,
#                                      'str_key': 'PRIMARY_WEAPON'},
#         }
#
#         # 性能优先
#         self._stars_state = [False, False, False, False, False, False, False, False]
#         self._star_labels = {
#             1: self.ui.star_1,
#             2: self.ui.star_2,
#             3: self.ui.star_3,
#             4: self.ui.star_4,
#             5: self.ui.star_5,
#             6: self.ui.star_6,
#             7: self.ui.star_7,
#             8: self.ui.star_8,
#         }
#
#         # 样式
#         self.ui.equip_select_combobox.setView(QListView())
#         self.ui.comboBox.setView(QListView())
#         self.ui.comboBox_2.setView(QListView())
#         self.ui.groupBox_17.move(90, 10)
#
#         for i in range(1, 7):
#             table: QTableWidget = getattr(self.ui, f'tableWidget_{i}')
#             table.setEditTriggers(QTableWidget.NoEditTriggers)
#             table.setColumnCount(3)
#             table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#             table.setColumnHidden(2, True)
#             table.setSelectionBehavior(QTableWidget.SelectRows)
#             table.horizontalHeader().setDefaultSectionSize(189)
#             table.setShowGrid(False)
#             table.setStyleSheet("selection-background-color:lightblue;")
#             table.setFocusPolicy(Qt.NoFocus)
#
#         # 品质筛选
#         nMinimumLevel = self.config['equip_min_level']
#         nMaximumLevel = self.config['equip_max_level']
#         if not nMaximumLevel or not nMinimumLevel:
#             return
#         for i in [self.ui.horizontalSlider, self.ui.horizontalSlider_2]:
#             i.setMinimum(int(nMinimumLevel))
#             i.setMaximum(int(nMaximumLevel))
#             i.setSingleStep(5)
#         del i
#         self.ui.horizontalSlider_2.setValue(int(nMaximumLevel))
#         self.ui.horizontalSlider.valueChanged.connect(
#             lambda: self.ui.label_61.setText(f"{self.ui.horizontalSlider.value()}"))
#         self.ui.horizontalSlider_2.valueChanged.connect(
#             lambda: self.ui.label_62.setText(f"{self.ui.horizontalSlider_2.value()}"))
#
#         # 内置一套默认配装
#         self.import_json_func(data=self.config['default_equips'], _init=True)
#
#         # 其他筛选
#         self.ui.checkBox_8.stateChanged.connect(
#             lambda arg: self.ui.checkBox_9.setEnabled(bool(arg)))
#
#         # 列表装备选择
#         self.ui.equip_select_combobox.clicked.connect(
#             lambda: self.get_equip_list_by_filter(self.get_filter()))
#
#         # 左侧装备选择
#         for btn, value in self.position_data.items():
#             btn_func = self.equip_button_func(btn, value)
#             btn.clicked.connect(btn_func)
#             btn_func(_init=True)
#         self.ui.groupBox_19.setVisible(False)  # 先隐藏装备界面，强制用户点击
#
#         # 选择好装备后
#         self.ui.equip_select_combobox.activated.connect(lambda idx: self.equip_box_select_func(idx))
#
#         # self.get_equip_list_by_filter()   # 测试用
#         # self.get_equip_by_position()    # 只有每次更新装备表时需要调用
#
#         # 镶嵌页面开关
#         self.ui.groupBox_23.setVisible(False)
#         # 初始化时隐藏所有的镶嵌孔
#         self.ui.label_86.setVisible(False)
#         for index, btn in enumerate([self.ui.pushButton_90, self.ui.pushButton_103, self.ui.pushButton_104]):
#             btn.setVisible(False)
#             btn.clicked.connect(self.embedding_button_func(index))
#         # 选择镶嵌等级的按钮
#         for i in range(9):
#             btn: QPushButton = getattr(self.ui, f'pushButton_{108+i}')
#             btn.clicked.connect(self.embedding_set_button_func(i))
#
#         # 选择精炼等级的星星
#         for i in range(1, 9):
#             lb: StarLabel = getattr(self.ui, f'star_{i}')
#             lb.hovered.connect(self.strength_star_hover_func(i))
#             lb.unhovered.connect(self.strength_star_leave_func())
#             lb.clicked.connect(self.strength_star_clicked_func(i))
#
#         self.ui.star_button.clicked.connect(self.strength_star_clear_func)
#
#         # 选择小附魔的下拉菜单
#         self.ui.comboBox.clicked.connect(self.set_enhance_list)
#         # 选择大附魔的下拉菜单
#         self.ui.comboBox_2.clicked.connect(self.set_enchant_list)
#
#         # 选择大小附魔后的填表逻辑
#         self.ui.comboBox.activated.connect(lambda idx: self.enhance_box_select_func(idx))
#         self.ui.comboBox_2.activated.connect(lambda idx: self.enchant_box_select_func(idx))
#
#         # 五彩石选择页面的开关
#         self.ui.groupBox_24.setVisible(False)
#         self.ui.groupBox_24.move(240, 200)
#         self.ui.groupBox_24.raise_()
#         self.ui.pushButton_105.clicked.connect(lambda: self.ui.groupBox_24.setVisible(True))
#         self.ui.pushButton.clicked.connect(lambda: self.ui.groupBox_24.setVisible(False))
#         self.ui.pushButton_117.clicked.connect(lambda: self.ui.groupBox_24.setVisible(False))
#
#         # 五彩石指定筛选器
#         for i in range(1, 4):
#             box: ClickableComboBox = getattr(self.ui, f'comboBox_{i+2}')
#             box.setView(QListView())
#             box.clicked.connect(self.set_stone_selector(i, box))
#             box.currentIndexChanged.connect(self.stone_selector_clicked_func(i, box))
#             clear_btn: QPushButton = getattr(self.ui, f'pushButton_{117+i}')
#             clear_btn.clicked.connect(self.stone_selector_clear_func(i, box))
#         self.set_stone_selector(1, self.ui.comboBox_3)()
#         self.stone_selector_clear_func(1, self.ui.comboBox_3)()
#
#         # 选择好五彩石后
#         self.ui.pushButton.clicked.connect(self.stone_list_select_func)
#         # 取消选择五彩石
#         self.ui.pushButton_107.clicked.connect(self.stone_clear_func)
#
#         # 导出json
#         self.ui.pushButton_121.clicked.connect(self.export_json_func)
#         # 导入json
#         # self.ui.equip_button_3.clicked.connect(self.import_json_func)
#
#
#
#     def export_json_func(self):
#         json_attrib = self.equip_attribute.get_final_attrib()
#         _, _ = QInputDialog.getText(
#             self.ui,
#             "导出",
#             "",
#             text=json_attrib,
#             )
#
#     def import_json_func(self, data=None, _init=False):
#
#         flag = True
#         if not data:
#             data, flag = QInputDialog.getText(
#                 self.ui,
#                 "导入数据",
#                 "请输入jx3box或本工具提供的配装代码",
#                 )
#         if flag:
#             try:
#                 data = eval(data)['EquipList']
#                 for pos in self.equip_list:
#                     # 填表
#                     for key in self.equip_list[pos]:
#                         if key in data[pos]:
#                             if key == 'id':
#                                 self.equip_list[pos][key] = data[pos][key][2:]
#                             else:
#                                 self.equip_list[pos][key] = data[pos][key]
#
#                     idkey = POSITION_KEY[pos]
#                     eq_data = equip[idkey].get(int(self.equip_list[pos]['id']))
#                     if not data:
#                         self.equip_list[pos]['data'] = ""
#                         self.equip_list[pos]['score'] = 0
#                     else:
#                         self.equip_list[pos]['data'] = eq_data
#                         self.equip_list[pos]['score'] = get_equip_score(idkey, self.equip_list[pos])
#                     self.equip_attribute.update(self.equip_list)
#             except:
#                 return
#             finally:
#                 if not _init:
#                     # noinspection PyUnresolvedReferences
#                     self.ui.set_attrib_line_edit()
#
#
#     def equip_button_func(self, btn, value):
#         value = value
#
#         # 装备大图标
#         equip_lb = QLabel()
#         equip_lb.resize(42, 42)
#         equip_lb.setPixmap(ICONS['db'])
#         major_layout = QHBoxLayout()
#         major_layout.addWidget(equip_lb)
#
#         # 右侧下方的名称
#         name_lb = QLabel()
#         name_lb.setText('未知装备')
#         # 右侧上方的位置
#         position_lb = QLabel()
#         position_lb.setText(f"{value['name']: <12}")
#         position_lb.setStyleSheet("color: rgb(85, 85, 85)")
#         # 右侧上方精炼提示
#         strength_lb = QLabel()
#         strength_lb.setText(f"(0/0)")
#         # 上方layout
#         upper_layout = QHBoxLayout()
#         upper_layout.addWidget(position_lb)
#         upper_layout.addWidget(strength_lb)
#         # 右侧layout
#         right_layout = QVBoxLayout()
#         right_layout.addLayout(upper_layout)
#         right_layout.addWidget(name_lb)
#
#         # 设置layout
#         major_layout.addLayout(right_layout)
#         btn.setLayout(major_layout)
#         value['name_label'] = name_lb
#         value['strength_label'] = strength_lb
#
#         def inner(_init=False):
#             self.ui.groupBox_19.setVisible(True)
#             self.current_position = value['position']
#             self.current_position_data = value
#
#             btn.setStyleSheet("""QPushButton{
#                                 border:1px;
#                                 background-color: rgb(174, 199, 225);
#                             }""")
#             for _btn in self.position_data:
#                 if not _btn == btn:
#                     _btn.setStyleSheet("""QPushButton{
#                                             border:1px;
#                                             background-color: rgb(225, 225, 225)
#                                         }
#                                         QPushButton:hover{
#                                             border:1px;
#                                             background-color: rgb(227, 234, 240)
#                             }""")
#
#             # 设置镶嵌按钮
#             equip_data = self.equip_list[value['str_key']]
#             nEmbeddingCount = len(equip_data['embedding'])
#             for index, bt in enumerate([self.ui.pushButton_90, self.ui.pushButton_103, self.ui.pushButton_104]):
#                 if nEmbeddingCount > index:
#                     bt.setVisible(True)
#                     bt.setText(f'{equip_data["embedding"][index]}')
#                 else:
#                     bt.setVisible(False)
#             self.ui.label_86.setVisible(True) if nEmbeddingCount > 0 else self.ui.label_86.setVisible(False)
#
#
#             # 设置装备信息
#             # noinspection PyTypeChecker
#             self.set_equip_info_by_equip_data(equip_data['data'])
#
#             # 设置精炼星数
#             self.strength_star_leave_func()()
#
#             # 设置小附魔
#             self.ui.comboBox.clear()
#
#             # 设置大附魔
#             if self.current_position in {'2', '3', '6', '8', '9', '10'}:
#                 self.ui.label_85.setVisible(True)
#                 self.ui.comboBox_2.setVisible(True)
#                 self.ui.comboBox_2.clear()
#             else:
#                 self.ui.label_85.setVisible(False)
#                 self.ui.comboBox_2.setVisible(False)
#
#             # 设置五彩石
#             if self.current_position == '0':
#                 self.ui.label_87.setVisible(True)
#                 self.ui.label_88.setVisible(True)
#                 self.ui.pushButton_105.setVisible(True)
#                 self.ui.pushButton_106.setVisible(True)
#                 self.ui.pushButton_107.setVisible(True)
#             else:
#                 self.ui.label_87.setVisible(False)
#                 self.ui.label_88.setVisible(False)
#                 self.ui.pushButton_105.setVisible(False)
#                 self.ui.pushButton_106.setVisible(False)
#                 self.ui.pushButton_107.setVisible(False)
#
#             value['name_label'].setText(equip_data['data']['Name'])
#
#
#             if not _init:
#                 # noinspection PyUnresolvedReferences
#                 self.ui.set_attrib_line_edit()
#
#         return inner
#
#     def equip_box_select_func(self, idx, equip_id=None, equip_data=None):
#         """
#         选择装备后的填表逻辑\n
#         :return:
#         """
#         if not self.current_filtrated_equip_list:
#             return
#
#         if equip_id is None and equip_data is None:
#             equip_id = list(self.current_filtrated_equip_list)[idx]
#             equip_data = self.current_filtrated_equip_list[equip_id]['data']
#         # print(equip_id, equip_data)
#         szKey = self.current_position_data['str_key']
#         self.equip_list[szKey]['id'] = equip_id
#         self.equip_list[szKey]['data'] = equip_data
#
#         # 清除大附魔
#         self.equip_list[szKey]['enchant'] = ''
#
#         # 最大精炼等级
#         nMaxStrength = equip_data['MaxStrengthLevel']
#         if nMaxStrength:
#             nMaxStrength = int(nMaxStrength)
#         else:
#             nMaxStrength = 0
#
#         self.equip_list[szKey]['strength'] = min(nMaxStrength, self.equip_list[szKey]['strength'])
#
#         self.set_equip_info_by_equip_data(equip_data)
#         self.set_equip_setting_by_equip_data(equip_data)
#         # noinspection PyUnresolvedReferences
#         self.ui.set_attrib_line_edit()
#
#     def set_enhance_list(self):
#         """
#         获取附魔列表
#         :return:
#         """
#         if not self.current_position_data:
#             return
#
#         ret = {}
#
#         nSubType = self.current_position_data['position']
#         enhance_data = enchant['enhance'][nSubType]
#
#         for enhance_id, _data in enhance_data.items():
#
#             szText = _data['AttriName']
#             _del_start_text = {'护腕', '上衣', '下装', '鞋子', '帽子', '腰带'}
#             for text in _del_start_text:
#                 if szText.startswith(text):
#                     szText = szText[2:]
#                     break
#
#             ret[enhance_id] = {
#                 'string': f'{_data["Name"]} {szText}',
#                 'data': _data
#             }
#
#         self.ui.comboBox.clear()
#         self.ui.comboBox.addItems([ret[enhance_id]['string'] for enhance_id in ret])
#
#         self.current_filtrated_enhance_list = ret
#
#     def set_enchant_list(self):
#         """
#         获取大附魔列表\n
#         :return:
#         """
#
#         if not self.current_position_data:
#             return
#
#         ret = {}
#
#         nSubType = self.current_position_data['position']
#         enchant_data = enchant['enchant'][nSubType]
#
#         for enchant_id, _data in enchant_data.items():
#
#             str_key = _data['Name'][:4]
#             if str_key not in ENCHANT_NEED:
#                 continue
#
#             duty_key: str = _data['Name']
#             duty_key = duty_key[duty_key.find('·')+1]
#
#             enchant_need_level_data = ENCHANT_NEED[str_key]
#
#             equip_data = self.equip_list[self.current_position_data['str_key']]['data']
#             if not equip_data:
#                 return
#
#             # noinspection PyTypeChecker
#             if not equip_data['Level'] in range(enchant_need_level_data['min'], enchant_need_level_data['max']+1):
#                 continue
#
#             # noinspection PyTypeChecker
#             _duty = equip_data['_Duty']
#             if ENCHANT_DUTY[_duty] != duty_key:
#                 continue
#
#             ret[enchant_id] = {
#                 'string': f'{_data["Name"]}',
#                 'data': _data
#             }
#
#         self.ui.comboBox_2.clear()
#         self.ui.comboBox_2.addItems([ret[enhance_id]['string'] for enhance_id in ret])
#
#         self.current_filtrated_enchant_list = ret
#
#     def enhance_box_select_func(self, idx):
#         """
#         选择小附魔后的逻辑\n
#         :return:
#         """
#
#         if not self.current_filtrated_enhance_list:
#             return
#
#         enhance_id = list(self.current_filtrated_enhance_list)[idx]
#         # enhance_data = self.current_filtrated_enhance_list[enhance_id]['data']
#         szKey = self.current_position_data['str_key']
#
#         # 设置小附魔id
#         self.equip_list[szKey]['enhance'] = enhance_id
#         # 设置装备信息
#         self.set_equip_info_by_equip_data(self.equip_list[self.current_position_data['str_key']]['data'])
#         # 更新首页属性
#         self.ui.set_attrib_line_edit()
#
#     def enchant_box_select_func(self, idx):
#         """
#         选择大附魔后的逻辑\n
#         :return:
#         """
#         if not self.current_filtrated_enchant_list:
#             return
#
#         enchant_id = list(self.current_filtrated_enchant_list)[idx]
#         # enchant_data = self.current_filtrated_enchant_list[enchant_id]['data']
#         szKey = self.current_position_data['str_key']
#
#         # 设置小附魔id
#         self.equip_list[szKey]['enchant'] = enchant_id
#         # 设置装备信息
#         self.set_equip_info_by_equip_data(self.equip_list[self.current_position_data['str_key']]['data'])
#         self.ui.set_attrib_line_edit()
#
#     def embedding_button_func(self, idx):
#         state = False
#         def inner():
#             nonlocal state
#             if 40+idx*45 != self.ui.groupBox_23.x() and self.ui.groupBox_23.isVisible():
#                 state = True
#             else:
#                 state = not self.ui.groupBox_23.isVisible()
#             self.current_embedding_setting_index = idx
#             self.ui.groupBox_23.setVisible(state)
#             self.ui.groupBox_23.move(40+idx*45, 190)
#         return inner
#
#     def embedding_set_button_func(self, value):
#         def inner():
#             btn = [self.ui.pushButton_90, self.ui.pushButton_103, self.ui.pushButton_104][self.current_embedding_setting_index]
#             btn.setText(f"{value}")
#             self.equip_list[self.current_position_data['str_key']]['embedding'][self.current_embedding_setting_index] = value
#             # noinspection PyTypeChecker
#             self.set_equip_info_by_equip_data(self.equip_list[self.current_position_data['str_key']]['data'])
#             self.ui.groupBox_23.setVisible(False)
#             self.ui.set_attrib_line_edit()
#         return inner
#
#     def strength_star_hover_func(self, idx):
#         def inner():
#             if self.current_position_data is None:
#                 return
#             print('hover: idx=', idx)
#             for i in range(1, idx+1):
#                 self._set_strength_star(i)
#             for i in range(idx+1, 9):
#                 self._set_strength_star(i, on=False)
#         return inner
#
#     def strength_star_leave_func(self):
#         def inner():
#             if self.current_position_data is None:
#                 return
#             nStrength = self.equip_list[self.current_position_data['str_key']]['strength']
#             if nStrength > 0:
#                 for i in range(1, nStrength+1):
#                     self._set_strength_star(i)
#             for i in range(nStrength+1, 9):
#                 self._set_strength_star(i, on=False)
#         return inner
#
#     def strength_star_clicked_func(self, idx):
#         def inner():
#             if self.current_position_data is None:
#                 return
#             print('hover: idx=', idx)
#             self.equip_list[self.current_position_data['str_key']]['strength'] = idx
#             self.strength_star_leave_func()
#             self.set_equip_info_by_equip_data(self.equip_list[self.current_position_data['str_key']]['data'])
#             self.ui.set_attrib_line_edit()
#         return inner
#
#     def strength_star_clear_func(self):
#         if self.current_position_data is None:
#             return
#         self.equip_list[self.current_position_data['str_key']]['strength'] = 0
#         for i in range(1, 9):
#             self._set_strength_star(i, on=False)
#         self.ui.set_attrib_line_edit()
#
#     def _set_strength_star(self, idx, on=True):
#         if idx not in range(1, 9):
#             return
#
#         print(f'set {idx} to {on}')
#
#         bState = self._stars_state[idx - 1]
#         if bool(bState) == bool(on):
#             return
#
#         lb = self._star_labels[idx]
#
#         if on:
#             lb.setPixmap(ICONS['star'])
#         else:
#             lb.setPixmap(ICONS['star_grey'])
#         self._stars_state[idx - 1] = on
#
#     def set_stone_selector(self, idx, box: QComboBox):
#         def inner():
#             _selector = set()
#             _compile = compile(r'彩·(..)·(..)·(..)')
#
#             if not self.current_filtrated_stone_list:
#                 stone_data = stone[6]
#                 for _stone_data in stone_data.values():
#                     _match = match(_compile, _stone_data['Name'])
#
#                     key = _match.group(1)
#                     if key in {'守护', '击破', '济世'}:
#                         if idx < 3:
#                             _value = _match.group(idx+1)
#                             _selector.add(_value)
#                     else:
#                         _value = _match.group(idx)
#                         _selector.add(_value)
#
#             else:
#                 # 先取消当前进度
#                 self.stone_selector[idx] = '..'
#                 self.current_filtrated_stone_list = self.get_stone_list_by_selector()
#
#                 for _stone_data in self.current_filtrated_stone_list[6]:
#                     _match = match(_compile, _stone_data['Name'])
#
#                     key = _match.group(1)
#                     if key in {'守护', '击破', '济世'}:
#                         if idx < 3:
#                             _value = _match.group(idx+1)
#                             _selector.add(_value)
#                     else:
#                         _value = _match.group(idx)
#                         _selector.add(_value)
#
#             for attrib_data in STONE_ATTRIB_DICT['std']:
#                 key = attrib_data['label']
#                 if key in _selector:
#                     _selector.remove(key)
#                     if self.ui.checkBox_13.isChecked():  # 需要根据心法筛选
#                         if self.ui.mount in attrib_data['mounts']:
#                             _selector.add(f"{key}({attrib_data['remark']})")
#                     else:
#                         _selector.add(f"{key}({attrib_data['remark']})")
#
#             box.clear()
#             box.addItems(_selector)
#
#         return inner
#
#     def stone_selector_clicked_func(self, idx, box: QComboBox):
#         """
#         指定匹配的方法\n
#         :param box:
#         :param idx:
#         :return:
#         """
#         def inner():
#             key = box.currentText()[:2]
#             self.stone_selector[idx] = key
#             # print(self.stone_selector)
#
#             # if idx == 1:
#             #     self.stone_selector_clear_func(2, self.ui.comboBox_4)()
#             #     self.stone_selector_clear_func(3, self.ui.comboBox_5)()
#             # elif idx == 2:
#             #     self.stone_selector_clear_func(3, self.ui.comboBox_5)()
#
#             self.current_filtrated_stone_list = self.get_stone_list_by_selector()
#
#         return inner
#
#     def stone_selector_clear_func(self, idx, box: QComboBox):
#         """
#         清除当前选项的方法\n
#         :param idx:
#         :param box:
#         :return:
#         """
#         def inner():
#             box.clear()
#             self.stone_selector[idx] = '..'
#             self.current_filtrated_stone_list = self.get_stone_list_by_selector()
#         return inner
#
#     def get_stone_list_by_selector(self, disorder_selector=None):
#         """
#         通过五彩石词条筛选出符合条件的五彩石\n
#         :return:
#         """
#         ret = {}
#
#         if disorder_selector is None:
#             str_selector = ['彩·', '彩·守护·', '彩·击破·', '彩·济世·']
#             key = "·".join([i for i in self.stone_selector.values() if i])
#
#             str_selector = [(i+key)[:10] for i in str_selector]
#             for stone_lv, lv_stone_data in stone.items():
#                 for stone_id, id_stone_data in lv_stone_data.items():
#                     _name = id_stone_data.get("Name")
#                     if not _name:
#                         continue
#                     if not any([search(i, _name) for i in str_selector]):
#                         continue
#
#                     stone_attrs = id_stone_data['_Attrs']
#                     _s_a = {}
#                     for stone_slot_data in STONE_ATTRIB_DICT['std']:
#                         if stone_slot_data['value'] in stone_attrs:
#                             _s_a[stone_slot_data['value']] = stone_slot_data['remark']
#                     stone_string = "·".join([_s_a[i] for i in stone_attrs if i is not None])
#
#                     _stone_data = {
#                         'Name': id_stone_data['Name'],
#                         'ID': id_stone_data['ID'],
#                         'String': stone_string,
#                     }
#
#                     if stone_lv not in ret:
#                         ret[stone_lv] = [_stone_data]
#                     else:
#                         ret[stone_lv].append(_stone_data)
#
#         else:
#             pass
#
#         for lv in range(1, 7):
#         # for lv, data in ret.items():
#             table: QTableWidget = getattr(self.ui, f'tableWidget_{lv}')
#             table.clear()
#             if lv not in ret:
#                 table.setRowCount(0)
#                 continue
#             else:
#                 table.setRowCount(len(ret[lv]))
#
#             for idx, value in enumerate(ret[lv]):
#                 table.setItem(idx, 0, QTableWidgetItem(value['Name']))
#                 item = QTableWidgetItem(value['String'])
#                 item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
#                 table.setItem(idx, 1, item)
#                 table.setItem(idx, 2, QTableWidgetItem(f"{value['ID']}"))
#
#         # print(ret[6])
#         return ret
#
#     def stone_list_select_func(self):
#         """
#         选择五彩石后的方法\n
#         :return:
#         """
#         if not self.current_position_data:
#             return
#
#         page_idx = self.ui.tabWidget.currentIndex() + 1
#         table: QTableWidget = getattr(self.ui, f'tableWidget_{page_idx}')
#         stone_id = table.item(table.currentRow(), 2).text()
#         self.equip_list['PRIMARY_WEAPON']['stone'] = int(stone_id)
#         self.set_equip_info_by_equip_data(self.equip_list[self.current_position_data['str_key']]['data'])
#         self.ui.set_attrib_line_edit()
#
#     @staticmethod
#     def _set_length(label: QLabel):
#         """
#         初始化时设定部分控件的自适应宽度\n
#         :return:
#         """
#         metrics = QFontMetrics(label.font())
#         label.resize(metrics.width(label.text())+5, label.height())
#
#     # noinspection PyUnresolvedReferences
#     def set_equip_info_by_equip_data(self, data):
#         """
#         通过装备数据设置装备信息页\n
#         :param data:
#         :return:
#         """
#         if not data:
#             return
#
#         # 类型
#         nSubType = data['SubType']
#
#         advance_data = self.equip_list[self.current_position_data['str_key']]
#
#         # 装分数据
#         self.equip_list[self.current_position_data['str_key']]['score'] = get_equip_score(nSubType, advance_data)
#
#         # 属性数据
#         self.equip_list = self.equip_attribute.update(self.equip_list)
#
#         # 装备名称
#         if data['Quality'] == '5':
#             self.ui.label_68.setStyleSheet(f"color: rgb{UI_COLOR['orange']}")
#         else:
#             self.ui.label_68.setStyleSheet(f"color: rgb{UI_COLOR['magenta']}")
#         self.ui.label_68.setText(data['Name'])
#         self._set_length(self.ui.label_68)
#         # 精炼星星数
#         nStrength = advance_data['strength']
#         if not nStrength:
#             nStrength = 0
#         self.ui.label_69.move(10+self.ui.label_68.width(), self.ui.label_69.y())    # 调整精炼星星位置
#         self.ui.label_69.setText('⭐'*nStrength)
#         # 精炼等级
#         self.ui.label_70.setText(f"精炼等级:{nStrength}/{data['MaxStrengthLevel']}")
#         # 部位名称
#         self.ui.label_71.setText(POSITION_NAME.get(nSubType))
#         # 武器类型 武器攻击速度
#         szWeaponType = ''
#         if nSubType == '1':
#             szWeaponType = '投掷' if '试炼之地' in data['BelongMap'] else '弓弦'
#             self.ui.label_139.setText(f'速度 {max(int(data["Base3Min"]), int(data["Base3Max"])) / 16:.1f}')
#         elif nSubType == '0':
#             szWeaponType = WEAPON_TYPE[data['DetailType']]
#             self.ui.label_139.setText(f'速度 {max(int(data["Base3Min"]), int(data["Base3Max"])) / 16:.1f}')
#         else:
#             self.ui.label_139.setText('')
#         self.ui.label_138.setText(szWeaponType)
#         # 下面填写属性的部分开始需要记录y值
#         # 基础属性部分
#         top_y = 50
#         if nSubType in {'1', '0'}:
#             nWeaponBase = max(int(data["Base1Min"]), int(data["Base1Max"]))
#             nWeaponRand = max(int(data["Base2Min"]), int(data["Base2Max"]))
#             nAttackSpeed = max(int(data["Base3Min"]), int(data["Base3Max"])) / 16
#             self.ui.label_72.setVisible(True)
#             self.ui.label_73.setVisible(True)
#             if nSubType == '1':
#                 self.ui.label_72.setText(
#                     f"""远程伤害提高 {nWeaponBase}-{nWeaponBase+nWeaponRand}""")
#                 self.ui.label_73.setText(f"每秒伤害 {(nWeaponBase+0.5*nWeaponRand) / nAttackSpeed:.1f}")
#             elif nSubType == '0':
#                 self.ui.label_72.setText(
#                     f"""近身伤害提高 {nWeaponBase}-{nWeaponBase+nWeaponRand}""")
#                 self.ui.label_73.setText(f"每秒伤害 {(nWeaponBase+0.5*nWeaponRand) / nAttackSpeed:.1f}")
#             top_y += 40     # 武器伤害行+秒伤行
#         else:
#             for i in range(1, 3):
#                 slot = data[f'Base{i}Type']
#                 lb: QLabel = getattr(self.ui, f"label_{71+i}")
#                 if slot not in SLOT_DICT:
#                     lb.setVisible(False)
#                 else:
#                     value = max(int(data[f"Base{i}Min"]), int(data[f"Base{i}Max"]))
#                     lb.move(lb.x(), top_y)
#                     top_y += 20
#                     lb.setText(f'{SLOT_DICT[slot]}提高{value}')
#                     lb.setVisible(True)
#
#         # 魔法属性部分
#         white = {'atVitalityBase', 'atStrengthBase', 'atAgilityBase'}
#         orange = {'atSetEquipmentRecipe', 'atSkillEventHandler'}
#         strength_value = self.equip_list[self.current_position_data['str_key']]['strength_attr']
#         for i in range(1, 13):
#             slot_data = data[f'_Magic{i}Type']
#             lb: QLabel = getattr(self.ui, f'magic_label_{i}')
#             lb_strength: QLabel = getattr(self.ui, f'magic_strength_label_{i}')
#
#             if not slot_data:
#                 lb.setVisible(False)
#                 lb_strength.setVisible(False)
#                 continue
#             slot = slot_data['attr'][0]
#             value = max(*[int(slot_data['attr'][i]) for i in range(1, 5) if slot_data['attr'][i] is not None])
#
#             lb.resize(352, 16)  # 重置回初始高度
#             if slot in orange:
#                 lb_strength.setVisible(False)   # 橙色词条没有精炼加成
#                 lb.setStyleSheet(f"color: rgb{UI_COLOR['orange']}")
#                 lb.move(lb.x(), top_y)
#                 szText = re.findall(re.compile(r'"(.*?)"'), slot_data['label'])[0]
#                 metrics = QFontMetrics(lb.font())
#                 if metrics.width(szText) > lb.width():
#                     lb.setWordWrap(True)
#                     lb.resize(lb.width(), lb.height()+20)
#                     top_y += 20
#
#                 lb.setText(szText.strip().replace('\\', ''))
#             else:
#                 lb.move(lb.x(), top_y)
#                 lb_strength.setVisible(True)
#                 lb.setText(f"{SLOT_DICT[slot]}提高{value}")
#                 self._set_length(lb)
#                 lb_strength.move(lb.x() + lb.width() + 5, lb_strength.y())
#                 if strength_value is not None and len(strength_value) >= i:
#                     if strength_value[i-1] > 0:
#                         lb_strength.setText(f'(+{strength_value[i-1]})')
#                     else:
#                         lb_strength.setVisible(False)
#
#                 if slot in white:
#                     lb.setStyleSheet(f"color: rgb{UI_COLOR['white']}")
#                 else:
#                     lb.setStyleSheet(f"color: rgb{UI_COLOR['green']}")
#
#             lb.setVisible(True)
#             lb_strength.move(lb_strength.x(), top_y)
#             top_y += 20
#
#         # 镶嵌部分
#         if 'embedding_attr' in self.equip_list[self.current_position_data['str_key']]:
#             embedding_value = self.equip_list[self.current_position_data['str_key']]['embedding_attr']
#             for i in range(1, 4):
#                 diamond_data = data.get(f'_DiamondAttributeID{i}')
#                 embedding_icon_lb: QLabel = getattr(self.ui, f'embedding_{i}')
#                 embedding_text_lb: QLabel = getattr(self.ui, f'embedding_desc_{i}')
#                 if not diamond_data:
#                     embedding_text_lb.setVisible(False)
#                     embedding_icon_lb.setVisible(False)
#                     continue
#                 else:
#                     embedding_text_lb.setVisible(True)
#                     embedding_icon_lb.setVisible(True)
#
#                 embedding_lv = advance_data['embedding'][i-1]
#                 embedding_icon = ICONS.get(f'embedding_{embedding_lv}')
#                 if not embedding_icon:
#                     continue
#                 slot = diamond_data[0]
#                 value = embedding_value[i-1]
#
#                 embedding_icon_lb.setPixmap(embedding_icon)
#                 embedding_icon_lb.move(embedding_icon_lb.x(), top_y)
#                 if not embedding_lv:    # 未插五彩石的情况
#                     value = '？'
#                     embedding_text_lb.setStyleSheet(f"color: rgb{UI_COLOR['grey']}")
#                 else:
#                     embedding_text_lb.setStyleSheet(f"color: rgb{UI_COLOR['green']}")
#
#                 embedding_text_lb.setText(f"{SLOT_DICT[slot]}提高{value}")
#                 embedding_text_lb.move(embedding_text_lb.x(), top_y)
#
#                 top_y += 20
#         else:
#             self.ui.embedding_1.setVisible(False)
#             self.ui.embedding_2.setVisible(False)
#             self.ui.embedding_3.setVisible(False)
#             self.ui.embedding_desc_1.setVisible(False)
#             self.ui.embedding_desc_2.setVisible(False)
#             self.ui.embedding_desc_3.setVisible(False)
#
#         # 五彩石部分
#         if nSubType == '0':
#             top_y = self.set_stone(advance_data['stone'], top_y)
#         else:
#             for i in [self.ui.label_140, self.ui.label_90, self.ui.label_141, self.ui.label_142, self.ui.label_143]:
#                 i.setVisible(False)
#
#
#         # 需要等级
#         self.ui.label_92.move(self.ui.label_92.x(), top_y)
#         self.ui.label_92.setText(f"需要等级{data['Require1Value']}")
#         top_y += 20
#
#         # 耐久度
#         nMaxDurability = int(data['MaxDurability'])
#         if nMaxDurability:
#             self.ui.label_96.setVisible(True)
#             self.ui.label_96.move(self.ui.label_96.x(), top_y)
#             self.ui.label_96.setText(f"耐久度：{nMaxDurability}/{nMaxDurability}")
#             top_y += 20
#         else:
#             self.ui.label_96.setVisible(False)
#
#         # 小附魔
#         nEnhance = advance_data['enhance']  # 图标位
#
#         self.ui.label_145.move(self.ui.label_145.x(), top_y)
#         if not nEnhance:
#             self.ui.label_147.setVisible(False)  # 附魔属性位
#             self.ui.label_76.setVisible(True)  # 无附魔提示位
#             self.ui.label_76.move(self.ui.label_147.x(), top_y)
#         else:
#             self.ui.label_147.setVisible(True)  # 附魔属性位
#             self.ui.label_76.setVisible(False)  # 无附魔提示位
#             self.ui.label_147.move(self.ui.label_147.x(), top_y)
#
#             enhance_data = enchant['enhance'][nSubType][nEnhance]
#             szText = enhance_data['AttriName']
#             _del_start_text = {'护腕', '上衣', '下装', '鞋子', '帽子', '腰带'}
#             for text in _del_start_text:
#                 if szText.startswith(text):
#                     szText = szText[2:]
#                     break
#             self.ui.label_147.setText(szText)
#
#         top_y += 20
#
#         # 大附魔
#         self.ui.label_146.move(self.ui.label_146.x(), top_y)
#         self.ui.label_148.resize(self.ui.label_148.width(), 16)
#
#         if nSubType in {'2', '3', '6', '8', '9', '10'}:
#             self.ui.label_146.setVisible(True)
#             self.ui.label_148.setVisible(True)
#             self.ui.label_77.setVisible(True)
#
#             nEnchant = advance_data['enchant']
#             if not nEnchant:
#                 self.ui.label_77.move(self.ui.label_148.x(), top_y)
#                 self.ui.label_148.setVisible(False)
#             else:
#                 self.ui.label_77.setVisible(False)
#                 enchant_data = enchant['enchant'][nSubType][nEnchant]
#
#                 # 大附魔描述
#                 lb = self.ui.label_148
#                 lb.move(lb.x(), top_y)
#                 szText = re.findall(re.compile(r'"(.*?)"'), enchant_data['_AttriName'])[0]
#                 metrics = QFontMetrics(lb.font())
#                 if metrics.width(szText) > lb.width():
#                     lb.setWordWrap(True)
#                     lb.resize(lb.width(), lb.height() + 20)
#                     top_y += 20
#
#                 lb.setText(szText.strip().replace('\\', ''))
#
#         else:
#             self.ui.label_146.setVisible(False)
#             self.ui.label_148.setVisible(False)
#             self.ui.label_77.setVisible(False)
#
#
#         # 套装
#         self.ui.label_150.setVisible(False)
#         self.ui.label_151.setVisible(False)
#         self.ui.label_152.setVisible(False)
#         self.ui.label_162.setVisible(False)
#
#         # 品质等级
#         score_data = advance_data["score"]
#         self.ui.label_154.setText(f'{data["Level"]}')
#         if nStrength:
#             self.ui.label_155.setText(f"(+{score_data.nQualityScoreAdd})")
#             self.ui.label_155.setVisible(True)
#         else:
#             self.ui.label_155.setVisible(False)
#
#         # 装分
#         self.ui.label_158.setText(f'{score_data.nBaseScore}')
#         szText = '('
#         if nStrength:
#             szText += f"+{score_data.nStrengthScoreAdd}"
#         if score_data.nAdvanceScoreAdd:
#             szText += f"+{score_data.nAdvanceScoreAdd}"
#         szText += ')'
#
#         if szText == '()':
#             self.ui.label_157.setVisible(False)
#         else:
#             self.ui.label_157.setVisible(True)
#             self.ui.label_157.setText(szText)
#
#         self.set_attribute()
#
#     def set_equip_setting_by_equip_data(self, data):
#         """
#         根据装备信息设置装备增强栏\n
#         :param data:
#         :return:
#         """
#
#         # 设置最大镶嵌
#         nMaxStars = data['MaxStrengthLevel']
#         if not nMaxStars:
#             nMaxStars = 0
#         else:
#             nMaxStars = int(nMaxStars)
#
#         for i in range(1, nMaxStars+1):
#             self._star_labels[i].setVisible(True)
#
#         for i in range(nMaxStars+1, 9):
#             self._star_labels[i].setVisible(False)
#
#
#     def set_stone(self, stone_id, top_y=None) -> int:
#         """
#         :param top_y:
#         :param stone_id:
#         :return:
#         """
#         for i in [self.ui.label_140, self.ui.label_90, self.ui.label_141, self.ui.label_142, self.ui.label_143]:
#             i.setVisible(False)
#
#         if top_y is None:
#             top_y = self.ui.label_140.y()
#         else:
#             self.ui.label_140.move(self.ui.label_140.x(), top_y)
#             self.ui.label_140.setVisible(True)
#
#         for stone_data in stone.values():
#             if stone_id in stone_data:
#                 # 获取五彩石数据
#                 stone_data = stone_data.get(stone_id)
#                 for i in range(1, 4):
#                     slot = stone_data[f'Attribute{i}ID']
#                     lb: QLabel = getattr(self.ui, f'label_{140 + i}')
#
#                     if not slot:
#                         lb.setVisible(False)
#                         continue
#
#                     else:
#                         value = max(*[int(stone_data[f"Attribute{i}Value{j}"]) for j in range(1, 3) if
#                                       stone_data[f"Attribute{i}Value{j}"] is not None])
#                         lb.setVisible(True)
#                         # 百分比五彩石
#                         if 'PercentAdd' in slot:
#                             value = f"{value/1024:.0%}"
#
#                         lb.setText(f"{SLOT_DICT[slot]}提高{value}")
#
#                         nNeedCount = int(stone_data[f'DiamondCount{i}'])
#                         nNeedLevel = int(stone_data[f'DiamondIntensity{i}'])
#                         if self.equip_attribute.embedding_data['count'] >= nNeedCount and self.equip_attribute.embedding_data['level'] >= nNeedLevel:
#                             lb.setStyleSheet(f'color: rgb{UI_COLOR["green"]}')
#                         else:
#                             lb.setStyleSheet(f'color: rgb{UI_COLOR["grey"]}')
#
#                         lb.move(self.ui.label_90.x(), top_y)
#                         top_y += 20
#                 # 右侧设置页面的显示
#                 self.ui.label_88.setText(stone_data['Name'])
#                 break
#
#         else:
#             self.ui.label_90.move(self.ui.label_90.x(), top_y)
#             self.ui.label_90.setVisible(True)
#             top_y += 20
#
#
#
#
#         return top_y
#
#     def stone_clear_func(self):
#         self.equip_list['PRIMARY_WEAPON']['stone'] = ""
#         self.ui.label_88.setText("")
#         self.set_equip_info_by_equip_data(self.equip_list[self.current_position_data['str_key']]['data'])
#         self.ui.set_attrib_line_edit()
#
#     def get_equip_list_by_filter(self, equip_filter):
#         # filter = {
#         #     'SubType': '8',
#         #     'attr': ['Parry', 'Surplus'],
#         #     'min_level': 9000,
#         #     'max_level': 12000,
#         #     'BelongSchool': {'通用', '精简', '苍云'},
#         #     'MagicKind': {'体质', '防御'}
#         # }
#         equip_data = self._equip_data.get(equip_filter['SubType'])
#         if not equip_data:
#             return
#
#         ret = {}
#
#         for equip_id, _equip in equip_data.items():
#             # 品级
#             if not (equip_filter['min_level'] <= _equip['Level'] <= equip_filter['max_level']):
#                 continue
#
#             # 从属类型
#             if _equip['MagicKind'] not in equip_filter['MagicKind']:
#                 continue
#
#             # 装备类型
#             if _equip['BelongSchool'] not in equip_filter['BelongSchool']:
#                 continue
#
#             # 属性类型
#             for slot in equip_filter['attr']:
#                 if slot not in _equip['_Attrs']:
#                     break
#
#             else:
#                 # 符合要求的装备
#                 # MagicType特殊处理
#                 _MagicType = _equip['MagicType'].replace('命中', '破招').replace('全能', '外防内防破招无双加速').replace('高级', '')
#                 ret[equip_id] = {
#                     'string': f"{_equip['Name']} ({_MagicType})  {_equip['Level']}品",
#                     'data': _equip
#                 }
#
#         self.ui.equip_select_combobox.clear()
#         self.ui.equip_select_combobox.addItems([ret[equip_id]['string'] for equip_id in ret])
#
#         self.current_filtrated_equip_list = ret
#
#     def get_filter(self):
#         """
#         从选项中读取出筛选条件\n
#         :return:
#         """
#         ret = {
#             'SubType': self.current_position,
#             'attr': set(),
#             'min_level': 0,
#             'max_level': 0,
#             'BelongSchool': set(),
#             'MagicKind': set(),
#         }
#
#         # 属性筛选
#         attr_slot = {
#             self.ui.checkBox: 'Parry',
#             self.ui.checkBox_4: 'Critical',
#             self.ui.checkBox_5: 'Strain',
#             self.ui.checkBox_11: 'Overcome',
#             self.ui.checkBox_12: 'Surplus',
#             self.ui.checkBox_10: 'Haste',
#         }
#         for cb, slot in attr_slot.items():
#             if cb.isChecked():
#                 ret['attr'].add(slot)
#
#         # 品质筛选
#         nMin = int(self.ui.label_61.text())
#         nMax = int(self.ui.label_62.text())
#         ret['min_level'] = min(nMin, nMax)
#         ret['max_level'] = max(nMin, nMax)
#
#         # 其他筛选
#         other_slot = {
#             self.ui.checkBox_6: '通用',
#             self.ui.checkBox_7: '精简',
#             self.ui.checkBox_8: '苍云',
#         }
#         for cb, slot in other_slot.items():
#             if cb.isChecked():
#                 ret['BelongSchool'].add(slot)
#         if self.ui.checkBox_8.isChecked():
#             if not self.ui.checkBox_9.isChecked():
#                 ret['BelongSchool'].add('天策')
#                 ret['BelongSchool'].add('少林')
#                 ret['BelongSchool'].add('明教')
#
#         # MagicKind
#         magic_kind_slot = {
#             self.ui.checkBox: '防御',
#             self.ui.checkBox_2: '力道',
#             self.ui.checkBox_3: '身法',
#         }
#         for cb, slot in magic_kind_slot.items():
#             if cb.isChecked():
#                 ret['MagicKind'].add(slot)
#         if self.ui.checkBox_4.isChecked() or self.ui.checkBox_11.isChecked():
#             ret['MagicKind'].add('力道')
#             ret['MagicKind'].add('身法')
#             ret['MagicKind'].add('外功')
#         if self.ui.checkBox_12.isChecked() or self.ui.checkBox_5.isChecked() or self.ui.checkBox_10.isChecked():
#             ret['MagicKind'].add('力道')
#             ret['MagicKind'].add('身法')
#             ret['MagicKind'].add('防御')
#             ret['MagicKind'].add('外功')
#
#         return ret
#
#
#     def set_attribute(self):
#         """
#         属性展示\n
#         :return:
#         """
#         json_attrib = eval(self.equip_attribute.json_attributes)
#         value_attrib = self.equip_attribute.attributes
#
#         # 装分
#         self.ui.label_93.setText(f"{value_attrib['score']}")
#         # 体质
#         self.ui.label_94.setText(f"{json_attrib['Vitality']}")
#         # 身法
#         self.ui.label_97.setText(f"{json_attrib['Agility']}")
#         # 力道
#         self.ui.label_99.setText(f"{json_attrib['Strength']}")
#         # 攻击力
#         self.ui.label_104.setText(f"{json_attrib['PhysicsAttackPower']}")
#         # 会心
#         self.ui.label_106.setText(f"{json_attrib['PhysicsCriticalStrikeRate']:.2%}")
#         # 会效
#         self.ui.label_108.setText(f"{json_attrib['PhysicsCriticalDamagePowerPercent']:.2%}")
#         # 破防
#         self.ui.label_110.setText(f"{json_attrib['PhysicsOvercomePercent']:.2%}")
#         # 无双
#         self.ui.label_112.setText(f"{json_attrib['StrainPercent']:.2%}")
#         # 加速率
#         self.ui.label_114.setText(f"{json_attrib['HastePercent']:.2%}")
#         # 破招
#         self.ui.label_116.setText(f"{json_attrib['SurplusValue']}")
#
#         # 外防
#         self.ui.label_121.setText(f"{json_attrib['PhysicsShieldPercent']:.2%}")
#         # 内防
#         self.ui.label_123.setText(f"{json_attrib['LunarShieldPercent']:.2%}")
#         # 御劲
#         self.ui.label_125.setText(f"{json_attrib['ToughnessDefCriticalPercent']:.2%}")
#         # 闪躲
#         self.ui.label_129.setText(f"{json_attrib['DodgePercent']:.2%}")
#         # 招架
#         self.ui.label_131.setText(f"{json_attrib['ParryPercent']:.2%}")
#         # 拆招
#         self.ui.label_133.setText(f"{json_attrib['ParryValue']}")
#         # 威胁值
#         # self.ui.label_116.setText(f"{json_attrib['SurplusValue']}")
#
#
#
#
#     @staticmethod
#     def get_equip_by_position():
#         """
#         将以subtype分类的数据改为以position分类\n
#         :return:
#         """
#         ret = {}
#         for _, values in equip.items():
#             for id, value in values.items():
#                 _st = value['SubType']
#                 if _st in ret:
#                     ret[_st][id] = value
#                 else:
#                     ret[_st] = {id: value}
#
#         with open('test.txt', 'w', encoding='u8') as f:
#             f.write(ret.__repr__())
