# coding: utf-8
# author: LinXin
# 记录战斗中每个伤害技能的状态
# 暂用于计算属性收益和各附魔小吃小药收益
# IO：
# 在程序初始化时初始化自身
# self.StartNewFight：开始记录一份新的战斗记录，返回一个Recorder对象
# Recorder.end：保存当前记录
# Recorder.update：增加一条新记录
# self.GetDamageFromAdvancedAttribute：根据传入的属性增益计算期望DPS
from collections import namedtuple

from player.player_recorder_attribute import RecorderAttribute


class Recorder:

    RecordRow = namedtuple('RecordRow', [
        'nTime', 'dwSkillID',    # 时间
        'nBaseDamage', 'nAttackRate', 'nWeaponDamagePercent',   # 技能基础系数
        'fTargetDefensePercent', 'fLevelDamageParam',
        'fRecipeDamagePercent', 'fRecipeCriticalPercent', 'fAllDamageAddPercent',  # 全局增减益
        'tBuffValues'
    ])

    def __init__(self, parent):
        self._record = None
        self.fight_record = None
        self.base_attributes = None
        self.parent = parent
        self.attrib_slots = {
            'atVitalityBase': 0,
            'atVitalityBasePercentAdd': 0,
            'atAgilityBase': 0,
            'atAgilityBasePercentAdd': 0,
            'atStrengthBase': 0,
            'atStrengthBasePercentAdd': 0,
            'atPhysicsAttackPowerBase': 0,
            'atPhysicsAttackPowerPercent': 0,
            'atVitalityToPhysicsAttackPowerCof': 0,
            'atPhysicsCriticalStrike': 0,
            'atPhysicsCriticalStrikeBaseRate': 0,
            'atAllTypeCriticalStrike': 0,
            'atPhysicsCriticalDamagePowerBase': 0,
            'atPhysicsCriticalDamagePowerBaseKiloNumRate': 0,
            'atAllTypeCriticalDamagePowerBase': 0,
            'atVitalityToPhysicsOverComeCof': 0,
            'atPhysicsOvercomeBase': 0,
            'atPhysicsOvercomePercent': 0,
            'atStrainBase': 0,
            'atStrainRate': 0,
            'atSurplusValueAddPercent': 0,
            'atSurplusValueBase': 0,
            'atParryValueBase': 0,
            'atParryValuePercent': 0,
        }

    def SetBaseAttribute(self, base_attribute):
        self.base_attributes = base_attribute

    def update(self, nTime, *args):
        if self._record is None:
            self._record = [self.RecordRow(nTime, *args)]
        else:
            self._record.append(self.RecordRow(nTime, *args))

    def end(self):
        if self._record is None:
            return

        self.fight_record = self._record
        return self.parent.EndFight()

    def GetFightRecord(self) -> RecordRow:
        return self.fight_record


class FightRecorder:

    def __init__(self):
        self.records = None
        self.recorder_attribute = RecorderAttribute()
        self.current_record: Recorder | None = None

    def SetPlayer(self, player):
        self.recorder_attribute.SetPlayer(player)

    def StartNewFight(self):
        self.current_record = Recorder(self)
        return self.current_record

    def EndFight(self):
        if self.records is None:
            self.records = [self.current_record.GetFightRecord()]
        else:
            self.records.append(self.current_record.GetFightRecord())

        # print(self.current_record.GetFightRecord())
        # print(self.GetDamageFromAdvancedAttribute(
        #     {'atPhysicsAttackPower': 0}
        # ))
        return self.GetAttributeProfit()

    def GetDamageFromAdvancedAttribute(self, slots):
        """
        根据给定的属性额外数值计算新DPS\n
        :param slots:
        :return:
        """
        record = self.current_record.GetFightRecord()
        if not record:
            return 0
        if not slots:
            return 0

        # 设置基础属性
        base_attr = {k: v for k, v in self.current_record.base_attributes.items()}
        for slot, value in slots.items():
            if slot in base_attr:
                base_attr[slot] += value
            else:
                base_attr[slot] = value
        self.recorder_attribute.set_base_attribute(base_attr)

        tSnapShot = {}

        # 计算伤害
        nDamage = 0
        for rd in record:
            self.recorder_attribute.update_slots(rd.tBuffValues)

            # 计算各属性
            if rd.dwSkillID == 32745:
                nPhysicsAttackPower = self.recorder_attribute.SurplusValue
            else:
                nPhysicsAttackPower = self.recorder_attribute.PhysicsAttackPower
            nWeaponDamage = self.recorder_attribute.WeaponDamage
            fStrainPercent = self.recorder_attribute.StrainPercent
            fPhysicsOvercomePercent = self.recorder_attribute.PhysicsOvercomePercent
            fCritical = self.recorder_attribute.PhysicsCriticalPercent + rd.fRecipeCriticalPercent
            fCriticalPower = self.recorder_attribute.PhysicsCriticalDamagePowerPercent

            # 设置流血快照
            if rd.dwSkillID in {13053, 13054}:
                tSnapShot[13054] = {
                    'PhysicsAttackPower': nPhysicsAttackPower,
                    'PhysicsCriticalPercent': fCritical,
                    'PhysicsCriticalDamagePowerPercent': fCriticalPower,
                    'StrainPercent': fStrainPercent,
                    'AllDamageAddPercent': rd.fAllDamageAddPercent,
                }
            if rd.dwSkillID in {50001, 50002, 50003, 50004, 'LiuXueInterval_1', 'LiuXueInterval_2', 'LiuXueInterval_3', 'LiuXueInterval_4'} and 13054 in tSnapShot:
                nPhysicsAttackPower, fPhysicsCriticalPercent, fPhysicsCriticalDamagePowerPercent, \
                    fStrainPercent, fAllDamageAddPercent = tSnapShot[13054].values()

            # 计算伤害
            nBaseDamage = rd.nBaseDamage + rd.nAttackRate * nPhysicsAttackPower + rd.nWeaponDamagePercent * nWeaponDamage
            nBaseDamage *= (1 + fPhysicsOvercomePercent) * (1 + fStrainPercent) * (1 + rd.fRecipeDamagePercent) * (1 - rd.fTargetDefensePercent)
            nBaseDamage *= (1 + rd.fLevelDamageParam) * rd.fAllDamageAddPercent
            nBaseDamage = int(nBaseDamage * fCritical * fCriticalPower + nBaseDamage * (1 - fCritical))
            nDamage += nBaseDamage

        return int(nDamage / 300)

    def GetAttributeProfit(self):
        """
        计算属性收益\n
        这里会使用一个默认配置，包括需要计算收益的属性字段和属性值
        :return:
        """
        # 属性收益的具体计算用数值
        # 修改时要同时修改ui_chart中的同名表格
        profits = {
            'Vitality': [1, 2, 5, 10, 20],
            'Agility': [1, 2, 5, 10, 20],
            'Strength': [1, 2, 5, 10, 20],
            'PhysicsAttackPowerBase': [1, 2, 5, 10, 20],
            'PhysicsCriticalStrike': [1, 2, 5, 10, 20],
            'PhysicsCriticalDamagePower': [1, 2, 5, 10, 20],
            'PhysicsOvercome': [1, 2, 5, 10, 20],
            'Strain': [1, 2, 5, 10, 20],
            'SurplusValue': [1, 2, 5, 10, 20],
            'ParryValue': [1, 2, 5, 10, 20],
            'WeaponDamage': [1, 2, 5, 10, 20],
        }

        single_profits = {}
        marker_profits = {}

        # 基准DPS
        nBaseDamage = self.GetDamageFromAdvancedAttribute({'': 0})

        # 单点收益
        for slot, values in profits.items():
            for value in values:

                if slot == 'ParryValue':
                    self.recorder_attribute.set_advanced_parry_value(value)
                else:
                    self.recorder_attribute.set_advanced_parry_value(0)

                nDamage = self.GetDamageFromAdvancedAttribute({slot: value*100})
                fAdvanced = (nDamage / nBaseDamage) - 1

                if slot in single_profits:
                    single_profits[slot].append(fAdvanced)
                else:
                    single_profits[slot] = [fAdvanced]

        # 单分收益
        markers = {
            'Vitality': 147,
            'Agility': 66,
            'Strength': 66,
            'PhysicsAttackPowerBase': 131,
            'PhysicsCriticalStrike': 293,
            'PhysicsCriticalDamagePower': 293,
            'PhysicsOvercome': 293,
            'Strain': 293,
            'SurplusValue': 293,
            'ParryValue': 847,
            'WeaponDamage': 197,
        }
        for slot, values in profits.items():
            for value in values:

                if slot == 'ParryValue':
                    self.recorder_attribute.set_advanced_parry_value(value * markers[slot])
                    self.recorder_attribute.set_advanced_vitality_value(0)
                elif slot == 'Vitality':
                    self.recorder_attribute.set_advanced_vitality_value(value * markers[slot])
                    self.recorder_attribute.set_advanced_parry_value(0)
                else:
                    self.recorder_attribute.set_advanced_parry_value(0)
                    self.recorder_attribute.set_advanced_vitality_value(0)

                nDamage = self.GetDamageFromAdvancedAttribute({slot: value * markers[slot]})
                fAdvanced = (nDamage / nBaseDamage) - 1

                if slot in marker_profits:
                    marker_profits[slot].append(fAdvanced)
                else:
                    marker_profits[slot] = [fAdvanced]

        # 装备拆招值单分收益
        marker_equip_profits = {k: v for k, v in marker_profits.items()}
        marker_equip_profits['ParryValue'] = []
        for value in profits['ParryValue']:
            nAdvancedParryValue = value * markers['ParryValue'] * 0.4
            self.recorder_attribute.set_advanced_parry_value(nAdvancedParryValue)
            nDamage = self.GetDamageFromAdvancedAttribute({'ParryValue': nAdvancedParryValue})
            fAdvanced = (nDamage / nBaseDamage) - 1
            marker_equip_profits['ParryValue'].append(fAdvanced)
        self.recorder_attribute.set_advanced_parry_value(0)


        return single_profits, marker_profits, marker_equip_profits




