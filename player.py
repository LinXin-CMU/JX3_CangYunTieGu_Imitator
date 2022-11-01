# coding: utf-8
# author: LinXin

from main import buff

from typing import Dict


class Player:

    def __init__(self):
        # ————————————————————怒气部分————————————————————
        self._rage = 0

        self._casted = None
        self._damage = 0
        # ————————————————————属性部分————————————————————
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
            'Parry': 0,
            'ParryValue': 0,
        }
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
    # ————————————————————这里明天可以单独写一个class加载进来————————————————————

    @property
    def Vitality(self):
        return

    @property
    def PhysicsAttackPower(self):
        return

    @property
    def PhysicsCriticalPercent(self):
        return

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
        return

    @property
    def HastePercent(self):
        return

    @property
    def ParryPercent(self):
        return

    @property
    def ParryValue(self):
        return





