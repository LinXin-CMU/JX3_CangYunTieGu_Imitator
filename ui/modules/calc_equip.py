# coding: utf-8
# author: LinXin
from typing import Dict, List, Union
from collections import namedtuple
from re import compile
from json import dumps

from db.jx3_stone import stone
from db.jx3_enchant import enchant
from settings.jx3_types import Player

score_data = namedtuple('score_data', ['nBaseScore', 'nQualityScoreAdd', 'nStrengthScoreAdd', 'nAdvanceScoreAdd'])


def _get_equip_base_score(position, level, quality):
    position_rate = {
        '0': 1.2,
        '1': .6,
        '2': 1,
        '3': .9,
        '4': .5,
        '5': .5,
        '6': .7,
        '7': .5,
        '8': 1,
        '9': .7,
        '10': .7
    }
    quality_rate = {
        '1': .8,
        '2': 1.4,
        '3': 1.6,
        '4': 1.8,
        '5': 2.5
    }

    return round(level * quality_rate[quality] * position_rate[position])


def _get_strength_score(level, strength):
    if not strength:
        strength = 0
    return int(0.5 * level * strength * (0.003 * strength + 0.007) + 0.5)


def _get_embedding_score(embedding: List):
    fScore = 0
    if not embedding:
        return 0

    for em in embedding:
        if em < 6:
            fScore += 8.8 * 16 * 1.3 * (0.65 * em - 3.2)
        else:
            fScore += 0.195 * 8.8 * 16 * em
    return fScore


def _get_stone_score(stone_id):
    if not stone_id:
        return 0

    for lv, lv_data in stone.items():
        if stone_id in lv_data:
            return 3.5 * 8.8 * 20 * lv
    return 0


def _get_enchant_score(position, enhance_id, enchant_id):
    nScore = 0
    enhance_data = enchant['enhance'][position].get(enhance_id)
    if enhance_data:
        nScore += enhance_data['Score']
    if position in {'2', '3', '6', '8', '9', '10'}:
        enchant_data = enchant['enchant'][position].get(enchant_id)
        if enchant_data:
            nScore += enchant_data['Score']

    return nScore


def get_equip_score(position: str, equip_data: Dict):
    """
    "HAT": {"id": "", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                        "embedding": [6, 6], "data": ""},
    :param position:
    :param equip_data:
    :return:
    """
    # to_position = {"HAT": '3',
    #                "BELT": '6',
    #                "SHOES": '9',
    #                "WRIST": '10',
    #                "JACKET": '2',
    #                "RING_1": '5',
    #                "RING_2": '5',
    #                "BOTTOMS": '8',
    #                "PENDANT": '7',
    #                "NECKLACE": '4',
    #                "PRIMARY_WEAPON": '0',
    #                "SECONDARY_WEAPON": '1'}

    nBaseScore = _get_equip_base_score(position, equip_data['data']['Level'], equip_data['data']['Quality'])
    nStrengthLevelScore = _get_strength_score(equip_data['data']['Level'], equip_data['strength'])
    nStrengthEquipScore = _get_strength_score(nBaseScore, equip_data['strength'])

    fEmbeddingScore = _get_embedding_score(equip_data['embedding'])
    fStoneScore = _get_stone_score(equip_data['stone'])
    nEnchantScore = _get_enchant_score(position, equip_data['enhance'], equip_data['enchant'])
    nAdvanceScore = int(fEmbeddingScore + fStoneScore + nEnchantScore + 0.5)

    return score_data(nBaseScore, nStrengthLevelScore, nStrengthEquipScore, nAdvanceScore)


from PyQt5.QtWidgets import QMainWindow
from ui.ui import Ui_MainWindow

to_position = {"HAT": '3', "BELT": '6', "SHOES": '9', "WRIST": '10', "JACKET": '2', "RING_1": '5', "RING_2": '5',
               "BOTTOMS": '8', "PENDANT": '7', "NECKLACE": '4', "PRIMARY_WEAPON": '0', "SECONDARY_WEAPON": '1'}


# noinspection PyBroadException
class EquipAttribute:

    def __init__(self, parent):
        self.parent = parent
        self.equip_list = None
        self.attributes = {}
        self.json_attributes = {}
        self.embedding_data = {'count': 0, 'level': 0}
        self.set_data = {}
        self.read_mount_attr()
        self.read_talent_attr()
        self.calc_base_attr()
        self.read_system_transform_attr()
        self.calc_percent_attr()
        self.read_mount_transform_attr()
        self.get_final_attrib()

        self.strength_const = [0, 0.005, 0.013, 0.024, 0.038, 0.055, 0.075, 0.098, 0.124]
        self.embedding_const = [0, 0.195, 0.39, 0.585, 0.78, 0.975, 1.17, 1.755, 2.6]

    def update(self, equip_list: Dict) -> Dict:
        self.attributes = {}
        self.equip_list = equip_list
        self.read_equip_base_attr()
        self.read_stone_attr()
        self.read_set_attr()
        self.read_mount_attr()
        self.read_talent_attr()
        self.calc_base_attr()
        self.read_system_transform_attr()
        self.calc_percent_attr()
        self.read_mount_transform_attr()
        self.get_final_attrib()

        print(self.attributes)
        print(self.json_attributes)

        return self.equip_list

    def read_equip_base_attr(self):

        nDiamondCount = 0
        nDiamondLevel = 0

        for pos, eq in self.equip_list.items():
            szPosition = to_position[pos]
            equip_data = eq['data']
            if not equip_data:
                continue

            # 装分部分
            if 'score' in eq:
                if 'score' in self.attributes:
                    self.attributes['score'] += sum(eq['score']) - eq['score'].nQualityScoreAdd
                else:
                    self.attributes['score'] = sum(eq['score']) - eq['score'].nQualityScoreAdd

            # 基础属性部分
            for i in range(1, 7):
                szBaseAttrSlot = equip_data[f'Base{i}Type']
                nBaseAttrValue = equip_data[f'Base{i}Max']
                if nBaseAttrValue is not None:
                    try:
                        nBaseAttrValue = int(nBaseAttrValue)
                    except:
                        continue

                    if szBaseAttrSlot not in self.attributes:
                        self.attributes[szBaseAttrSlot] = nBaseAttrValue
                    else:
                        self.attributes[szBaseAttrSlot] += nBaseAttrValue

            # 魔法属性部分
            strength_value = None

            for i in range(1, 13):
                data = equip_data[f'_Magic{i}Type']
                if data is None:
                    continue
                else:
                    data = data['attr']

                szMagicAttrSlot = data[0]
                nMagicAttrValue = max([int(data[i]) for i in range(1, 5) if data[i] is not None])
                if nMagicAttrValue is not None:
                    try:
                        nMagicAttrValue = int(nMagicAttrValue)
                    except:
                        continue

                    if szMagicAttrSlot not in self.attributes:
                        self.attributes[szMagicAttrSlot] = nMagicAttrValue
                    else:
                        self.attributes[szMagicAttrSlot] += nMagicAttrValue
                else:
                    continue

                # 精炼部分
                if eq['strength'] > 0 and szMagicAttrSlot not in {'atActiveThreatCoefficient'}:
                    nStrengthAttr = int(nMagicAttrValue * self.strength_const[eq['strength']] + 0.5)
                else:
                    nStrengthAttr = 0

                if strength_value is None:
                    strength_value = [nStrengthAttr]
                else:
                    strength_value.append(nStrengthAttr)

                if szMagicAttrSlot not in self.attributes:
                    self.attributes[szMagicAttrSlot] = nStrengthAttr
                else:
                    self.attributes[szMagicAttrSlot] += nStrengthAttr

            self.equip_list[pos]['strength_attr'] = strength_value

            # 镶嵌部分
            embedding_value = None
            for i in range(1, 4):
                data = equip_data[f'_DiamondAttributeID{i}']
                if data is None:
                    continue

                szDiamondAttrSlot = data[0]
                nDiamondAttrValue = data[1]
                nCurrentDiamondLevel = eq['embedding'][i - 1]
                if nDiamondAttrValue is not None:
                    try:
                        nDiamondAttrValue = int(int(nDiamondAttrValue) * self.embedding_const[nCurrentDiamondLevel])
                    except:
                        continue

                    if szDiamondAttrSlot not in self.attributes:
                        self.attributes[szDiamondAttrSlot] = nDiamondAttrValue
                    else:
                        self.attributes[szDiamondAttrSlot] += nDiamondAttrValue

                    if embedding_value is None:
                        embedding_value = [nDiamondAttrValue]
                    else:
                        embedding_value.append(nDiamondAttrValue)

                    if nCurrentDiamondLevel > 0:
                        nDiamondCount += 1
                        nDiamondLevel += nCurrentDiamondLevel
                self.equip_list[pos]['embedding_attr'] = embedding_value

            # 小附魔部分
            if eq['enhance']:
                enhance_data = enchant['enhance'][szPosition].get(eq['enhance'])
                if enhance_data is not None:
                    for i in range(1, 5):
                        szEnhanceSlot = enhance_data[f'Attribute{i}ID']
                        if szEnhanceSlot is None:
                            continue
                        try:
                            nEnhanceValue = max(int(enhance_data[f'Attribute{i}Value1']),
                                                int(enhance_data[f'Attribute{i}Value2']))
                        except:
                            continue

                        if szEnhanceSlot not in self.attributes:
                            self.attributes[szEnhanceSlot] = nEnhanceValue
                        else:
                            self.attributes[szEnhanceSlot] += nEnhanceValue

            # 大附魔部分
            if eq['enchant']:
                enchant_data = enchant['enchant'][szPosition].get(eq['enchant'])

                if enchant_data is not None:
                    enchant_attr = enchant_data['_Attrs']
                    if enchant_attr is not None:
                        for attr in enchant_attr:
                            szEnchantSlot = attr[0]
                            if not szEnchantSlot:
                                continue
                            nEnchantValue = max([int(attr[i]) for i in range(1, 3) if attr[i] is not None])

                            if szEnchantSlot not in self.attributes:
                                self.attributes[szEnchantSlot] = nEnchantValue
                            else:
                                self.attributes[szEnchantSlot] += nEnchantValue

            # 套装部分
            set_attrs = equip_data.get('_SetAttrbs')
            if set_attrs:
                set_id = set_attrs['ID']
                # 储存套装数据
                if set_id not in self.set_data:
                    self.set_data[set_id] = {
                        'count': 1,
                        'data': equip_data.get('_SetData')
                    }
                else:
                    self.set_data[set_id]['count'] += 1



        self.embedding_data = {
            'count': nDiamondCount,
            'level': nDiamondLevel
        }

    def read_stone_attr(self):
        stone_id = self.equip_list['PRIMARY_WEAPON']['stone']
        if not stone_id:
            return

        for lv, stone_data in stone.items():
            if stone_id in stone_data:
                stone_data = stone_data[stone_id]
                break
        else:
            return

        for i in range(1, 4):
            nNeedCount = int(stone_data[f'DiamondCount{i}'])
            nNeedLevel = int(stone_data[f'DiamondIntensity{i}'])
            if self.embedding_data['count'] >= nNeedCount and self.embedding_data['level'] >= nNeedLevel:
                szStoneSlot = stone_data[f'Attribute{i}ID']
                if szStoneSlot is None:
                    continue
                nStoneValue = max([int(stone_data[f'Attribute{i}Value{j}']) for j in range(1, 3) if
                                   stone_data[f'Attribute{i}Value{j}'] is not None])
                if szStoneSlot not in self.attributes:
                    self.attributes[szStoneSlot] = nStoneValue
                else:
                    self.attributes[szStoneSlot] += nStoneValue


    def read_set_attr(self):
        for set_id, set_data in self.set_data.items():
            nCount = set_data['count']
            if nCount < 2:
                continue

            for key, attrs in set_data['data'].items():
                if not attrs:
                    continue
                if int(key[0]) <= nCount:
                    szSetSlot = attrs['attr'][0]
                    nSetValue = max([int(attrs['attr'][j]) for j in range(1, 5) if attrs['attr'][j] is not None])
                    if szSetSlot not in self.attributes:
                        self.attributes[szSetSlot] = nSetValue
                    else:
                        self.attributes[szSetSlot] += nSetValue
                    # 将套装数据写入EquipList


    def read_mount_attr(self):
        mount_attrib = {
            10390: {
                'atPhysicsAttackPowerBase': 1526,
                'atPhysicsOvercomeBase': 694,
                'atVitalityBase': 41,
                'atAgilityBase': 41,
                'atStrengthBase': 41,
                'atParryBase': 554,
                'atPhysicsShieldBase': 400,
                'atMagicShield': 400,
            },
            10389: {
                'atVitalityBase': 41,
                'atAgilityBase': 41,
                'atStrengthBase': 41,
                'atParryBase': 914,
                'atParryValueBase': 2114,
                'atPhysicsShieldBase': 948,
                'atMagicShield': 400,
            }
        }
        if self.parent.mount not in mount_attrib:
            return

        for slot, value in mount_attrib[self.parent.mount].items():
            if slot in self.attributes:
                self.attributes[slot] += value
            else:
                self.attributes[slot] = value

    # noinspection PyUnresolvedReferences
    def read_talent_attr(self):
        # 奇穴到属性值的映射
        talent_add_mapping: dict[str: dict] = {
            "活脉": {"atVitalityBasePercentAdd": 102, "atAgilityBasePercentAdd": 102},
            "活血": {"atVitalityBasePercentAdd": 102},
            "用御": {"atHasteBasePercentAdd": 102},
            "从容": {"atPhysicsAttackPowerPercent": 205},
        }
        talents = self._get_talent()
        for talent in talent_add_mapping:
            if talent in talents.values():
                # 添加对应属性
                for slot, value in talent_add_mapping[talent].items():
                    if slot in self.attributes:
                        self.attributes[slot] += value
                    else:
                        self.attributes[slot] = value

    def calc_base_attr(self):
        for slot in self.attributes:
            if 'atAllType' in slot:
                # 全属性类型
                new_slot = slot.replace("AllType", "Physics")
                if new_slot in self.attributes:
                    self.attributes[new_slot] = self.attributes[slot]
            elif 'BasePotentialAdd' in slot:
                # 全主属性
                value = self.attributes[slot]
                for new_slot in ['atVitalityBase', 'atAgilityBase', 'atStrengthBase']:
                    self.attributes[new_slot] += value
            elif 'BasePercentAdd' in slot:
                # 主属性加成
                slot_name = \
                    [match.group('attrtype') for match in compile(r'at(?P<attrtype>.+?)BasePercentAdd').finditer(slot)][
                        0]
                # 这一步只能加成主属性
                if slot_name in ['Vitality', 'Agility', 'Strength', 'Spunk', 'Spirit']:
                    new_slot = f"at{slot_name}Base"
                    value = self.attributes[slot]
                    if new_slot in self.attributes:
                        self.attributes[new_slot] += int(self.attributes[new_slot] * (value / 1024))
        if 'atPhysicsShieldAdditional' in self.attributes:
            self.attributes['atPhysicsShieldBase'] += self.attributes['atPhysicsShieldAdditional']

    def read_system_transform_attr(self):
        # 这里的值为其准确的小数值再向下取整
        # 身法
        # 对会心加成
        if 'atPhysicsCriticalStrike' in self.attributes:
            self.attributes['atPhysicsCriticalStrike'] += int(self.attributes['atAgilityBase'] * 0.64)
        else:
            self.attributes['atPhysicsCriticalStrike'] = int(self.attributes['atAgilityBase'] * 0.64)
        # 力道
        # 对攻击加成
        # 铁骨适配
        if 'atPhysicsAttackPowerBase' in self.attributes:
            self.attributes['atPhysicsAttackPowerBase'] += int(self.attributes['atStrengthBase'] * 0.15)
        else:
            self.attributes['atPhysicsAttackPowerBase'] = int(self.attributes['atStrengthBase'] * 0.15)
        # 对破防加成
        if 'atPhysicsOvercomeBase' in self.attributes:
            self.attributes['atPhysicsOvercomeBase'] += int(self.attributes['atStrengthBase'] * 0.3)
        else:
            self.attributes['atPhysicsOvercomeBase'] = int(self.attributes['atStrengthBase'] * 0.3)

    def calc_percent_attr(self):
        if 'atPhysicsAttackPowerPercent' in self.attributes:
            self.attributes['atPhysicsAttackPower'] = int(self.attributes['atPhysicsAttackPowerBase'] * (
                    self.attributes['atPhysicsAttackPowerPercent'] / 1024))

    def read_mount_transform_attr(self):
        # 分山劲
        if self.parent.mount == 10390:
            # 1.71攻击
            if 'atPhysicsAttackPower' in self.attributes:
                self.attributes['atPhysicsAttackPower'] += int(self.attributes['atAgilityBase'] * (1751 / 1024))
            else:
                self.attributes['atPhysicsAttackPower'] = int(self.attributes['atAgilityBase'] * (1751 / 1024))
            # 0.1招架
            self.attributes['atParryBase'] += int(self.attributes['atAgilityBase'] * (102 / 1024))
            # 1拆招值
            if 'atParryValueBase' in self.attributes:
                self.attributes['atParryValueBase'] += self.attributes['atAgilityBase'] * 1
            else:
                self.attributes['atParryValueBase'] = self.attributes['atAgilityBase'] * 1
        elif self.parent.mount == 10389:
            # 0.15招架
            self.attributes['atParryBase'] += int(self.attributes['atVitalityBase'] * (154 / 1024))
            # 2.25拆招
            self.attributes['atParryValueBase'] += int(self.attributes['atVitalityBase'] * (2304 / 1024))
            # 0.04攻击
            if 'atPhysicsAttackPower' in self.attributes:
                self.attributes['atPhysicsAttackPower'] += int(self.attributes['atVitalityBase'] * (41 / 1024))
            else:
                self.attributes['atPhysicsAttackPower'] = int(self.attributes['atVitalityBase'] * (41 / 1024))

    def get_final_attrib(self):
        json_data = {
            "Vitality": 0, "Agility": 0, "Spirit": 0, "Spunk": 0, "Strength": 0, "PhysicsAttackPowerBase": 0,
            "PhysicsAttackPower": 0, "PhysicsCriticalStrikeRate": 0.0,
            "PhysicsCriticalDamagePowerPercent": 0, "PhysicsOvercomePercent": 0, "StrainPercent": 0,
            "HastePercent": 0, "SurplusValue": 0, "MaxHealth": 0,
            "PhysicsShieldPercent": 0, "LunarShieldPercent": 0,
            "ToughnessDefCriticalPercent": 0, "DecriticalDamagePercent": 0, "DodgePercent": 0, "ParryPercent": 0,
            "ParryValue": 0, "ActiveThreatCoefficient": 0, "MeleeWeaponAttackSpeed": 0, "MeleeWeaponDamage": 0, "MeleeWeaponDamageRand": 0,
            'EquipList': {
                "HAT": {"id": "7_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                        "embedding": [6, 6]},
                "BELT": {"id": "7_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                         "embedding": [6, 6]},
                "SHOES": {"id": "7_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                          "embedding": [6, 6]},
                "WRIST": {"id": "7_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                          "embedding": [6, 6]},
                "JACKET": {"id": "7_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                           "embedding": [6, 6]},
                "RING_1": {"id": "8_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                           "embedding": []},
                "RING_2": {"id": "8_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                           "embedding": []},
                "BOTTOMS": {"id": "7_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                            "embedding": [6, 6]},
                "PENDANT": {"id": "8_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                            "embedding": [6]},
                "NECKLACE": {"id": "8_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                             "embedding": [6]},
                "PRIMARY_WEAPON": {"id": "6_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                                   "embedding": [6, 6, 6]},
                "SECONDARY_WEAPON": {"id": "6_", "stone": "", "enchant": "", "enhance": "", "strength": 6,
                                     "embedding": [6]}
                        }
                    }

        # 体质, 身法, 力道, 基础攻击, 破招, 拆招值, 武器系列
        numeric_attr_mapping = {
            "Vitality": "atVitalityBase",
            "Agility": "atAgilityBase",
            "Strength": "atStrengthBase",
            "PhysicsAttackPowerBase": "atPhysicsAttackPowerBase",
            "SurplusValue": "atSurplusValueBase",
            "ParryValue": "atParryValueBase",
            "MeleeWeaponAttackSpeed": "atMeleeWeaponAttackSpeedBase",
            "MeleeWeaponDamage": "atMeleeWeaponDamageBase",
            "MeleeWeaponDamageRand": "atMeleeWeaponDamageRand"
        }
        percentage_attr_mapping = {
            "PhysicsCriticalStrikeRate": ("atPhysicsCriticalStrike", 78622.5),
            "PhysicsCriticalDamagePowerPercent": ("atPhysicsCriticalDamagePowerBase", 27513.75),
            "PhysicsOvercomePercent": ("atPhysicsOvercomeBase", 78622.5),
            "StrainPercent": ("atStrainBase", 75809.75),
            "ToughnessDefCriticalPercent": ("atToughnessBase", 78622.5)
        }
        non_linear_percentage_mapping = {
            "PhysicsShieldPercent": ("atPhysicsShieldBase", 42000.75),
            "LunarShieldPercent": ("atMagicShield", 42000.75),
            "ParryPercent": ("atParryBase", 35846.25),
            "DodgePercent": ("atDodge", 30549.75),
        }
        for slot in numeric_attr_mapping:
            if numeric_attr_mapping[slot] in self.attributes:
                json_data[slot] = self.attributes[numeric_attr_mapping[slot]]
        # 最终攻击
        json_data["PhysicsAttackPower"] = self.attributes['atPhysicsAttackPower'] + self.attributes['atPhysicsAttackPowerBase']
        # 线性百分比属性：会心，会效，破防，无双, 御劲
        for slot in percentage_attr_mapping:
            if percentage_attr_mapping[slot][0] in self.attributes:
                json_data[slot] = self.attributes[percentage_attr_mapping[slot][0]] / percentage_attr_mapping[slot][1]
            if slot == 'PhysicsCriticalDamagePowerPercent':
                json_data[slot] = min(3, 1.75 + json_data[slot])
        # 加速
        if 'atHasteBase' in self.attributes:
            _haste_add = 0
            if 'atHasteBasePercentAdd' in self.attributes:
                _haste_add = self.attributes['atHasteBasePercentAdd']
            json_data["HastePercent"] = min(0.25, (self.attributes['atHasteBase'] / 96483.75) + (_haste_add / 1024))
        # 非线性百分比属性：外防，内防，招架, 闪避
        for slot in non_linear_percentage_mapping:
            if non_linear_percentage_mapping[slot][0] in self.attributes:
                _value = self.attributes[non_linear_percentage_mapping[slot][0]]
                json_data[slot] = _value / (_value + non_linear_percentage_mapping[slot][1])
            # 不同属性特殊处理
            if slot in {"PhysicsShieldPercent", "LunarShieldPercent"}:
                json_data[slot] = min(0.75, json_data[slot])
            elif slot == "ParryPercent":
                json_data[slot] += 0.03

        # 装备
        if self.equip_list is not None:
            for pos, eq in self.equip_list.items():
                for key in eq:
                    if key in json_data['EquipList'][pos]:
                        if key == 'id':
                            json_data['EquipList'][pos][key] += str(eq[key])
                        else:
                            json_data['EquipList'][pos][key] = eq[key]
        # 删除不存在的装备id
        for key, eq in json_data['EquipList'].items():
            if len(eq["id"]) == 2:
                json_data['EquipList'][key]['id'] = ""

        try:
            del self.attributes['atPhysicsAttackPowerPercent']
        except KeyError:
            pass
        try:
            del self.attributes['atSkillEventHandler']
        except KeyError:
            pass

        self.json_attributes = dumps(json_data)
        return self.json_attributes

    def _get_strength_value(self, ori_value, strength_lv) -> int:
        return int(ori_value * self.strength_const[strength_lv] + 0.5)

    def _get_talent(self):
        return self.parent.get_talent()
