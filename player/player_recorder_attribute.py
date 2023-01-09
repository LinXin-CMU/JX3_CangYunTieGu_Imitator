# coding: utf-8
# author: LinXin
# 继承自player_attribute，根据快照数据计算增加收益值后的属性


from typing import Dict


from player.player_attribute import Attribute


class RecorderAttribute(Attribute):

    # noinspection PyMissingConstructor
    def __init__(self):
        self.player = None
        self.base_attributes = None
        self.slots_dict = None
        self.advanced_parry_value = 0
        self.advanced_vitality_value = 0

    def SetPlayer(self, player):
        self.player = player

    def set_base_attribute(self, base_attributes):
        self.base_attributes = {k: v for k, v in base_attributes.items()}

    def update_slots(self, slots_dict):
        self.slots_dict = slots_dict

    def set_advanced_parry_value(self, value):
        self.advanced_parry_value = value

    def set_advanced_vitality_value(self, value):
        self.advanced_vitality_value = value

    def get_buff_attribute_value(self, slots) -> Dict[str, int]:

        if self.slots_dict:
            for slot in slots:
                nSlotValue = self.slots_dict.get(slot)
                if not nSlotValue:
                    nSlotValue = 0
                slots[slot] = nSlotValue

        return slots

    @property
    def PhysicsAttackPower(self):

        # 先计算属性收益的拆招值部分
        slots = {
            'atParryValuePercent': 0,
            'atVitalityBasePercentAdd': 0,
        }
        slots = self.get_buff_attribute_value(slots)
        # 属性收益拆招值部分额外判定
        nAdvancedParry = self.advanced_parry_value
        nAdvancedParry += int(nAdvancedParry * slots['atParryValuePercent'] / 1024)
        # 属性收益体质部分额外判定
        nAdvancedVitality = self.advanced_vitality_value
        nAdvancedVitality += int(nAdvancedParry * slots['atVitalityBasePercentAdd'] / 1024)

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
        # 额外拆招值的寒甲计算
        if self.player is None or self.player.GetSkillLevel('寒甲'):
            # 收益计算的拆招值
            value += int(nAdvancedParry * 0.5)
            # 收益计算的体质
            value += int(nAdvancedVitality * 2.25 * 0.5)
        # 百分比
        value += int(value * slots['atPhysicsAttackPowerPercent'] / 1024)
        # 体质转化
        # 默认铁骨
        nVitality = self.Vitality
        value += int(nVitality * 0.04)
        value += int(nVitality * slots['atVitalityToPhysicsAttackPowerCof'] / 1024)

        return value


