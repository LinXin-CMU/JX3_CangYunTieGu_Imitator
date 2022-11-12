# coding: utf-8
# author: LinXin
# 负责属性计算

from settings.jx3_types import Player
from scripts.buff import buff_data
from scripts.slot import attribute_value

from typing import Dict



class Attribute:

    def __init__(self, player: Player):
        # 这里要先做一步转换成基础值
        self._attributes = {
            'Vitality': 41,
            'Agility': 41,
            'Strength': 41,
            'PhysicsAttackPowerBase': 0,
            'PhysicsCriticalStrike': 0,
            'PhysicsCriticalDamagePower': 0,
            'PhysicsOvercome': 0,
            'Strain': 0,
            'SurplusValue': 0,
            'Haste': 0,
            'Parry': 40000,
            'ParryValue': 160000,
        }

        self._player = player

    def _get_buff_attribute_value(self, slots) -> Dict[str, int]:

        for buff in self._player.buffs.values():
            if not buff.attrib:
                continue
            for attrib_data in buff.attrib:
                attrib_data = attribute_value[attrib_data]
                if attrib_data.slot in slots:
                    slots[attrib_data.slot] += attrib_data.value * buff.layer

        return slots


    @property
    def Vitality(self):
        return

    @property
    def PhysicsAttackPower(self):
        slots = {
            'atPhysicsAttackPowerBase': 0,
        }

        slots = self._get_buff_attribute_value(slots)

        value = self._attributes['PhysicsAttackPowerBase']
        value += slots['atPhysicsAttackPowerBase']

        return value

    @property
    def PhysicsCriticalPercent(self):
        slots = {
            'atPhysicsCriticalStrikeBaseRate': 0
        }

        slots = self._get_buff_attribute_value(slots)

        value = self._attributes['PhysicsCriticalStrike']
        value += slots['atPhysicsCriticalStrikeBaseRate']

        return value

    @property
    def PhysicsCriticalDamagePowerPercent(self):
        return

    @property
    def OvercomePercent(self):
        return

    @property
    def StrainPercent(self):
        return

    @property
    def SurplusValue(self):
        return 10000

    @property
    def HastePercent(self):
        return

    @property
    def ParryPercent(self):
        nBaseValue = 35846.25
        # atParryBaseRate
        slots = {
            'atParryBaseRate': 0,
        }

        slots = self._get_buff_attribute_value(slots)

        value = self.ParryPercentValue
        value = value / (value + nBaseValue)
        value += slots['atParryBaseRate']
        value += 0.03

        return value

    @property
    def ParryPercentValue(self):
        slots = {
            'atParryPercent': 0,
        }
        slots = self._get_buff_attribute_value(slots)

        value = int(self._attributes['Parry'] * (1 + slots['atParryPercent']))

        return value

    @property
    def ParryValue(self):
        return self._attributes['ParryValue']