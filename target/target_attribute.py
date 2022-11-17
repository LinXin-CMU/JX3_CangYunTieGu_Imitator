# coding: utf-8
# author: LinXin
# 负责属性计算
from typing import Dict

from settings.jx3_types import Target
from settings.jx3_collections import npc_attribute_data, LEVEL_CONST, LEVEL_RATE, global_params
from scripts.slot import attribute_value


class Attribute:

    def __init__(self, target: Target):
        self._attributes = {
            'PhysicsShieldValue': 0,
            'AllTypeCriticalStrikeValue': 0
        }

        self._target = target

    def SetNpcAttributeValueByLevel(self):
        level = self._target.level
        if not level:
            return
        if level not in range(120, 125):
            return

        data = npc_attribute_data[level]
        self._attributes['PhysicsShieldValue'] = data.defense
        self._attributes['AllTypeCriticalStrikeValue'] = data.critical

    def _get_buff_attribute_value(self, slots) -> Dict[str, int]:

        for buff in self._target.buffs.values():
            if not buff.attrib:
                continue
            for attrib_data in buff.attrib:
                attrib_data = attribute_value[attrib_data]
                if attrib_data.slot in slots:
                    slots[attrib_data.slot] += attrib_data.value * buff.layer

        return slots

    # @property
    # def Vitality(self):
    #     return
    #
    # @property
    # def PhysicsAttackPower(self):
    #     return
    #
    # @property
    # def PhysicsCriticalPercent(self):
    #     return
    #
    # @property
    # def PhysicsCriticalDamagePowerPercent(self):
    #     return
    #
    # @property
    # def OvercomePercent(self):
    #     return
    #
    # @property
    # def StrainPercent(self):
    #     return
    #
    # @property
    # def SurplusValue(self):
    #     return
    #
    # @property
    # def HastePercent(self):
    #     return
    #
    # @property
    # def ParryPercent(self):
    #     return 0.4
    #
    # @property
    # def ParryPercentValue(self):
    #     return self._attributes['Parry']
    #
    # @property
    # def ParryValue(self):
    #     return self._attributes['ParryValue']

    @property
    def PhysicsShieldValue(self):
        slots = {
            'atPhysicsShieldPercent': 0
        }
        slots = self._get_buff_attribute_value(slots)
        value = self._attributes['PhysicsShieldValue']

        value += int(value * slots['atPhysicsShieldPercent'] / 1024)
        return value

    def GetPhysicsShieldPercent(self, value):
        nTargetLevel = self._target.level
        if not nTargetLevel:
            return

        nDefenseConst = global_params['fPhysicsShieldParam'] * (nTargetLevel * LEVEL_RATE - LEVEL_CONST)

        return value / (value + nDefenseConst)
