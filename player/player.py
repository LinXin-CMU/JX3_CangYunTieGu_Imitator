# coding: utf-8
# author: LinXin

from main import buff
from .player_attribute import Attribute

from typing import Dict


class Player:

    def __init__(self):
        # ————————————————————怒气部分————————————————————
        self._rage = 0

        self._casted = None
        self._damage = 0
        # ————————————————————属性部分————————————————————
        self._attribute = Attribute(self)
        # ————————————————————气劲部分————————————————————
        self._buffs: Dict[int, buff] = {
        }

    # ————————————————————怒气部分————————————————————

    @property
    def rage(self):
        return self._rage

    @rage.setter
    def rage(self, value):
        assert isinstance(value, int), '怒气必须为整数'
        self._rage = min(110, value)

    # ————————————————————属性部分————————————————————
    @property
    def Vitality(self):
        return self._attribute.Vitality

    @property
    def PhysicsAttackPower(self):
        return self._attribute.PhysicsAttackPower

    @property
    def PhysicsCriticalPercent(self):
        return self._attribute.PhysicsCriticalPercent

    @property
    def PhysicsCriticalDamagePowerPercent(self):
        return self._attribute.PhysicsCriticalDamagePowerPercent

    @property
    def OvercomePercent(self):
        return self._attribute.OvercomePercent

    @property
    def StrainPercent(self):
        return self._attribute.StrainPercent

    @property
    def SurplusValue(self):
        return self._attribute.SurplusValue

    @property
    def HastePercent(self):
        return self._attribute.HastePercent

    @property
    def ParryPercent(self):
        return self._attribute.ParryPercent

    @property
    def ParryValue(self):
        return self._attribute.ParryValue


    # ————————————————————技能部分————————————————————

    def CastSkill(self):
        # 1. 获取到对应脚本
        # 2. 执行对应脚本的Apply方法
        # 3. 检查释放结果，记录释放信息
        pass

    # ————————————————————气劲部分————————————————————

    def AddBuff(self):
        pass

    def GetBuff(self):
        pass


