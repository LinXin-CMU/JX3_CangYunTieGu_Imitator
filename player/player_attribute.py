# coding: utf-8
# author: LinXin
# 负责属性计算

from settings.jx3_types import Player
from settings.jx3_collections import LEVEL_CONST, LEVEL_RATE, global_params, special_stones
from scripts.include.slot import attribute_value, attrib_data
from db.jx3_stone import stone

from typing import Dict
from math import ceil


class Attribute:

    def __init__(self, player: Player, origin_data: Dict):
        # 这里要先做一步转换成基础值
        self.base_attributes = {
            'Vitality': 0,
            'Agility': 0,
            'Strength': 0,
            'PhysicsAttackPowerBase': 0,
            'PhysicsCriticalStrike': 0,
            'PhysicsCriticalDamagePower': 0,
            'PhysicsOvercome': 0,
            'Strain': 0,
            'SurplusValue': 0,
            'Haste': 0,
            'Parry': 0,
            'ParryValue': 0,
            'WeaponDamage': 0,
        }

        self.origin_data = origin_data

        self._player = player
        self._get_origin_attributes_value()

    def GetBaseAttributes(self):
        return self.base_attributes


    def _get_origin_attributes_value(self):
        """
        将配装器json转化为各类基础属性用于计算\n
        :param origin_data:
        :return:
        """
        # ---------------------------检查属性规范----------------------------
        slots = ['EquipList']
        for slot in slots:
            if slot not in self.origin_data:
                return

        tEquipList = self.origin_data['EquipList']
        # -----------------------------基础体质-----------------------------
        nVitalityBase = self.origin_data['Vitality']
        # 配装器活血 pass

        # -----------------------------基础身法-----------------------------
        # 配装器活脉 pass
        nAgilityBase = self.origin_data['Agility']
        # -----------------------------基础力道-----------------------------
        nStrengthBase = self.origin_data['Strength']
        # ----------------------------主属性五彩石---------------------------
        # 五彩石
        if not tEquipList['PRIMARY_WEAPON']:
            return
        stone_id = tEquipList['PRIMARY_WEAPON']['stone']
        if stone_id in special_stones:
            slot, value = special_stones.get(stone_id)
            match slot:
                case 'atVitalityBasePercentAdd':
                    nVitalityBase = ceil(nVitalityBase / (1 + (value / 1024)))
                case 'atStrengthBasePercentAdd':
                    nStrengthBase = ceil(nStrengthBase / (1 + (value / 1024)))
                case 'atAgilityBasePercentAdd':
                    nAgilityBase = ceil(nAgilityBase / (1 + (value / 1024)))

        # -----------------------------基础攻击-----------------------------
        nPhysicsAttackPowerBase = self.origin_data['PhysicsAttackPowerBase']
        # 不包含力道转化
        # 这里注意要用面板力道去减！
        nPhysicsAttackPowerBase -= int(self.origin_data['Strength'] * 0.15)
        # -----------------------------基础会心-----------------------------
        fPhysicsCriticalStrike = self.origin_data['PhysicsCriticalStrikeRate']
        nCriticalRate = global_params['fCriticalStrikeParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        nPhysicsCriticalStrikeBase = int(fPhysicsCriticalStrike * nCriticalRate + 0.5)
        # 不包含身法转化
        nPhysicsCriticalStrikeBase -= int(self.origin_data['Agility'] * 0.64)
        # -----------------------------基础会效-----------------------------
        fPhysicsCriticalDamagePower = self.origin_data['PhysicsCriticalDamagePowerPercent'] - 1.75
        nCriticalPowerRate = global_params['fCriticalStrikePowerParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        nPhysicsCriticalDamagePowerBase = int(fPhysicsCriticalDamagePower * nCriticalPowerRate + 0.5)
        # -----------------------------基础破防-----------------------------
        fPhysicsOvercome = self.origin_data['PhysicsOvercomePercent']
        nOvercomeRate = global_params['fOvercomeParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        nPhysicsOvercomeBase = int(fPhysicsOvercome * nOvercomeRate + 0.5)
        # 不包含力道转化
        nPhysicsOvercomeBase -= int(self.origin_data['Strength'] * 0.3)
        # -----------------------------基础无双-----------------------------
        fStrain = self.origin_data['StrainPercent']
        nStrainRate = global_params['fInsightParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        nStrainBase = int(fStrain * nStrainRate + 0.5)
        # -----------------------------基础破招-----------------------------
        nSurplusValueBase = self.origin_data['SurplusValue']
        # -----------------------------基础加速-----------------------------
        fHaste = self.origin_data['HastePercent']
        nHasteRate = global_params['fHasteRate'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        nHasteBase = int(fHaste * nHasteRate + 0.5)
        # -----------------------------基础招架-----------------------------
        fParry = self.origin_data['ParryPercent'] - 0.03
        nParryRate = global_params['fParryParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        nParryBase = int((nParryRate * fParry / (1 - fParry)) + 0.5)
        # 默认铁骨, 后续再改
        # 不包含体质转化
        nParryBase -= int(self.origin_data['Vitality'] * 0.15)
        # -----------------------------基础拆招-----------------------------
        nParryValueBase = self.origin_data['ParryValue']
        # 默认铁骨, 后续再改
        # 不包含体质转化
        nParryValueBase -= int(self.origin_data['Vitality'] * 2.25)
        # -----------------------------武器伤害-----------------------------
        nWeaponDamage = self.origin_data['MeleeWeaponDamage'] + int(0.5 * (self.origin_data['MeleeWeaponDamageRand']))

        self.base_attributes = {
            'Vitality': nVitalityBase,
            'Agility': nAgilityBase,
            'Strength': nStrengthBase,
            'PhysicsAttackPowerBase': nPhysicsAttackPowerBase,
            'PhysicsCriticalStrike': nPhysicsCriticalStrikeBase,
            'PhysicsCriticalDamagePower': nPhysicsCriticalDamagePowerBase,
            'PhysicsOvercome': nPhysicsOvercomeBase,
            'Strain': nStrainBase,
            'SurplusValue': nSurplusValueBase,
            'Haste': nHasteBase,
            'Parry': nParryBase,
            'ParryValue': nParryValueBase,
            'WeaponDamage': nWeaponDamage,
        }

        # print()

    def get_buff_attribute_value(self, slots) -> Dict[str, int]:

        tSlots = {k: v for k, v in slots.items()}

        for buff in self._player.buffs.values():
            if not buff.attrib:
                continue
            for _attrib_data in buff.attrib:
                if isinstance(_attrib_data, attrib_data):
                    pass  # 如果是给定属性字段和值，那么不作查找
                else:
                    _attrib_data = attribute_value[_attrib_data]
                if _attrib_data.slot in tSlots:
                    tSlots[_attrib_data.slot] += _attrib_data.value * buff.layer

        return tSlots

    @property
    def Vitality(self):
        slots = {
            'atVitalityBase': 0,
            'atVitalityBasePercentAdd': 0,
            'atBasePotentialAdd': 0,
        }
        slots = self.get_buff_attribute_value(slots)

        # 以下注释内容已设置为buff

        # # 活血
        # if self._player.GetSkillLevel('活血') == 1:
        #     slots['atVitalityBasePercentAdd'] += 102

        # # 五彩石
        # tEquipList = self.origin_data['EquipList']
        # if not ['PRIMARY_WEAPON']:
        #     return
        # stone_id = tEquipList['PRIMARY_WEAPON']['stone']
        # if stone_id in special_stones:
        #     slot, value = special_stones.get(stone_id)
        #     if slot == 'atVitalityBasePercentAdd':
        #         slots['atVitalityBasePercentAdd'] += value

        value = self.base_attributes['Vitality']
        value += slots['atVitalityBase']
        value += slots['atBasePotentialAdd']
        value += int(value * (slots['atVitalityBasePercentAdd'] / 1024))

        return value

    @property
    def Agility(self):
        slots = {
            'atAgilityBase': 0,
            'atAgilityBasePercentAdd': 0,
            'atBasePotentialAdd': 0,
        }
        slots = self.get_buff_attribute_value(slots)

        # 以下注释内容已设置为buff

        # # 活脉
        # if self._player.GetSkillLevel('活脉') == 1:
        #     slots['atAgilityBasePercentAdd'] += 102

        # # 五彩石
        # tEquipList = self.origin_data['EquipList']
        # if not ['PRIMARY_WEAPON']:
        #     return
        # stone_id = tEquipList['PRIMARY_WEAPON']['stone']
        # if stone_id in special_stones:
        #     slot, value = special_stones.get(stone_id)
        #     if slot == 'atAgilityBasePercentAdd':
        #         slots['atAgilityBasePercentAdd'] += value

        value = self.base_attributes['Agility']
        value += slots['atAgilityBase']
        value += slots['atBasePotentialAdd']
        value += int(value * (slots['atAgilityBasePercentAdd'] / 1024))

        return value

    @property
    def Strength(self):
        slots = {
            'atStrengthBase': 0,
            'atStrengthBasePercentAdd': 0,
            'atBasePotentialAdd': 0,
        }
        slots = self.get_buff_attribute_value(slots)

        # 以下注释内容已设置为buff

        # # 五彩石
        # tEquipList = self.origin_data['EquipList']
        # if not ['PRIMARY_WEAPON']:
        #     return
        # stone_id = tEquipList['PRIMARY_WEAPON']['stone']
        # if stone_id in special_stones:
        #     slot, value = special_stones.get(stone_id)
        #     if slot == 'atStrengthBasePercentAdd':
        #         slots['atStrengthBasePercentAdd'] += value

        value = self.base_attributes['Strength']
        value += slots['atStrengthBase']
        value += slots['atBasePotentialAdd']
        value += int(value * (slots['atStrengthBasePercentAdd'] / 1024))

        return value

    @property
    def PhysicsAttackPower(self):
        slots = {
            'atPhysicsAttackPowerBase': 0,
            'atPhysicsAttackPowerPercent': 0,
            'atVitalityToPhysicsAttackPowerCof': 0,
        }
        slots = self.get_buff_attribute_value(slots)

        value = self.base_attributes['PhysicsAttackPowerBase']
        value += slots['atPhysicsAttackPowerBase']
        # 力道转化
        value += int(self.Strength * 0.15)
        # 百分比
        value += int(value * slots['atPhysicsAttackPowerPercent'] / 1024)
        # 体质转化
        # 默认铁骨
        nVitality = self.Vitality
        value += int(nVitality * 0.04)
        value += int(nVitality * slots['atVitalityToPhysicsAttackPowerCof'] / 1024)

        return value

    @property
    def PhysicsCriticalPercent(self):
        slots = {
            'atPhysicsCriticalStrike': 0,
            'atPhysicsCriticalStrikeBaseRate': 0,
            'atAllTypeCriticalStrike': 0,
        }

        slots = self.get_buff_attribute_value(slots)

        value = self.base_attributes['PhysicsCriticalStrike']
        value += slots['atPhysicsCriticalStrike']
        value += slots['atAllTypeCriticalStrike']
        # 身法转化
        value += int(self.Agility * 0.64)

        # 转化为百分比
        value /= global_params['fCriticalStrikeParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        value += slots['atPhysicsCriticalStrikeBaseRate']

        return value

    @property
    def PhysicsCriticalDamagePowerPercent(self):
        slots = {
            'atPhysicsCriticalDamagePowerBase': 0,
            'atPhysicsCriticalDamagePowerBaseKiloNumRate': 0,
            'atAllTypeCriticalDamagePowerBase': 0,
        }
        slots = self.get_buff_attribute_value(slots)
        value = self.base_attributes['PhysicsCriticalDamagePower']
        value += slots['atPhysicsCriticalDamagePowerBase']
        value += slots['atAllTypeCriticalDamagePowerBase']

        # 转化为百分比
        value /= global_params['fCriticalStrikePowerParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        value += slots['atPhysicsCriticalDamagePowerBaseKiloNumRate']
        value += 1.75
        return value

    @property
    def PhysicsOvercomePercent(self):
        slots = {
            'atVitalityToPhysicsOverComeCof': 0,
            'atPhysicsOvercomeBase': 0,
            'atPhysicsOvercomePercent': 0,
        }
        slots = self.get_buff_attribute_value(slots)
        value = self.base_attributes['PhysicsOvercome']
        # 力道转化
        value += int(self.Strength * 0.3)
        # 固定值增益
        value += slots['atPhysicsOvercomeBase']
        # 百分比增益
        value += int(value * slots['atPhysicsOvercomePercent'] / 1024)

        # 体质转化
        value += int(self.Vitality * slots['atVitalityToPhysicsOverComeCof'] / 1024)

        # 转化为百分比
        value /= global_params['fOvercomeParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        return value

    @property
    def StrainPercent(self):
        slots = {
            'atStrainBase': 0,
            'atStrainRate': 0,
        }
        slots = self.get_buff_attribute_value(slots)
        value = self.base_attributes['Strain']
        value += slots['atStrainBase']
        # 转化为百分比
        value /= global_params['fInsightParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        # 百分比固定增益
        value += slots['atStrainRate'] / 1024

        return value

    @property
    def SurplusValue(self):
        slots = {
            'atSurplusValueAddPercent': 0,
            'atSurplusValueBase': 0,
        }
        slots = self.get_buff_attribute_value(slots)
        value = self.base_attributes['SurplusValue']
        # 固定值
        value += slots['atSurplusValueBase']

        value += int(value * slots['atSurplusValueAddPercent'] / 1024)

        return value

    @property
    def HastePercent(self):
        slots = {
        }
        slots = self.get_buff_attribute_value(slots)
        value = self.base_attributes['Haste']

        # 转化为百分比
        value /= global_params['fHasteRate'] * (LEVEL_RATE * 120 - LEVEL_CONST)
        return value

    @property
    def HasteValueGuo(self):
        slot = {
            'atHasteBasePercentAdd': 0,
        }
        # 取郭氏值
        value = int(
            (self.base_attributes['Haste'] * 1024) / (global_params['fHasteRate'] * (LEVEL_RATE * 120 - LEVEL_CONST)))
        # 增益
        value += slot['atHasteBasePercentAdd']
        return value

    @property
    def ParryPercent(self):
        # atParryBaseRate
        slots = {
            'atParryBaseRate': 0,
        }

        slots = self.get_buff_attribute_value(slots)
        value = self.ParryPercentValue

        # 转化为百分比
        value = value / (value + (global_params['fParryParam'] * (LEVEL_RATE * 120 - LEVEL_CONST)))
        # 百分比增益
        value += slots['atParryBaseRate']
        # 心法默认
        value += 0.03

        return value

    @property
    def ParryPercentValue(self):
        slots = {
            'atParryPercent': 0,
        }
        slots = self.get_buff_attribute_value(slots)
        value = self.base_attributes['Parry']

        # 增益值
        value += int(value * slots['atParryPercent'] / 1024)
        # 体质转化
        value += int(self.Vitality * 0.15)

        return value

    @property
    def ParryValue(self):
        slots = {
            'atParryValueBase': 0,
            'atParryValuePercent': 0,
        }
        slots = self.get_buff_attribute_value(slots)
        value = self.base_attributes['ParryValue']
        value += slots['atParryValueBase']
        # 增益值
        value += int(value * slots['atParryValuePercent'] / 1024)

        # 体质转化
        value += int(self.Vitality * 2.25)

        return value

    @property
    def WeaponDamage(self):
        slots = {
        }
        slots = self.get_buff_attribute_value(slots)
        value = self.base_attributes['WeaponDamage']

        return value

    @property
    def WeaponAttackSpeed(self):
        value = self.origin_data['MeleeWeaponAttackSpeed']
        return value

    @property
    def AllDamageAddPercent(self):
        slots = {
            'atAllDamageAddPercent': 0,
            'atAllPhysicsDamageAddPercent': 0,
        }
        slots = self.get_buff_attribute_value(slots)
        value = 1
        value *= (1 + slots['atAllDamageAddPercent'] / 1024)
        value *= (1 + slots['atAllPhysicsDamageAddPercent'] / 1024)
        return value

    def GetAttributeWithoutStone(self):
        """
        获取不含五彩石的基础属性\n
        :return:
        """
        tEquipList = self.origin_data.get('EquipList')
        if not tEquipList:
            return self.base_attributes, 0, {}

        dwWeaponData = tEquipList.get('PRIMARY_WEAPON')
        if not dwWeaponData:
            return self.base_attributes, 0, {}

        dwStoneID = dwWeaponData.get("stone")
        if not dwStoneID:
            return self.base_attributes, 0, {}

        for dwLevel, stone_db in stone.items():
            if dwStoneID in stone_db:
                dwStoneData = stone_db[dwStoneID]
                break

        else:
            return self.base_attributes, 0, {}

        slots = {}
        for i in range(1, 4):
            slot = dwStoneData.get(f"Attribute{i}ID")
            if not slot:
                continue

            value1 = dwStoneData.get(f"Attribute{i}Value1")
            value2 = dwStoneData.get(f"Attribute{i}Value2")
            if not value1 and not value2:
                continue

            value = max([int(v) for v in {value1, value2} if v is not None])

            slots[slot] = value

        ret = {k: v for k, v in self.base_attributes.items()}

        for k, v in slots.items():
            match k:
                case 'atVitalityBase':
                    ret['Vitality'] -= v
                case 'atAgilityBase':
                    ret['Agility'] -= v
                case 'atStrengthBase':
                    ret['Strength'] -= v
                case 'atBasePotentialAdd':
                    ret['Vitality'] -= v
                    ret['Agility'] -= v
                    ret['Strength'] -= v

                case 'atPhysicsAttackPowerBase':
                    ret['PhysicsAttackPowerBase'] -= v
                case 'atPhysicsCriticalStrike' | 'atAllTypeCriticalStrike':
                    ret['PhysicsCriticalStrike'] -= v
                case 'atPhysicsCriticalDamagePowerBase' | 'atAllTypeCriticalDamagePowerBase':
                    ret['PhysicsCriticalDamagePower'] -= v
                case 'atPhysicsOvercomeBase':
                    ret['PhysicsOvercome'] -= v
                case 'atStrainBase':
                    ret['Strain'] -= v
                case 'atSurplusValueBase':
                    ret['SurplusValue'] -= v
                case 'atHasteBase':
                    ret['atHasteBase'] -= v
                case 'atParryBase':
                    ret['Parry'] -= v
                case 'atParryValueBase':
                    ret['ParryValue'] -= v
                case 'atMeleeWeaponDamageBase':
                    ret['WeaponDamage'] -= v

                case 'atVitalityBasePercentAdd':
                    nVitality = int(self.base_attributes['Vitality'] * v / 1024)
                    ret['PhysicsAttackPowerBase'] -= int(nVitality * 2.25 * 0.5)

        return ret, dwLevel, slots







