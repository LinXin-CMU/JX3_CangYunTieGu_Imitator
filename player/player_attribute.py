# coding: utf-8
# author: LinXin
# 负责属性计算

class Attribute:

    def __init__(self, player):
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
        return 0.4

    @property
    def ParryPercentValue(self):
        return self._attributes['Parry']

    @property
    def ParryValue(self):
        return self._attributes['ParryValue']