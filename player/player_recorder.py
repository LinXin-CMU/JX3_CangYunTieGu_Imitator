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
from math import ceil

from player.player_recorder_attribute import RecorderAttribute
from db.jx3_stone import stone


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
        self.nBaseDamage = 0
        self.player = None

    def SetPlayer(self, player):
        self.recorder_attribute.SetPlayer(player)
        self.player = player

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
        self.nBaseDamage = self.GetDamageFromAdvancedAttribute({'': 0})

        profits = self.GetAttributeProfit()
        stone_profits = self.GetStoneProfit(profits[0])

        return profits, stone_profits

    def GetDamageFromAdvancedAttribute(self, slots, dwAdvanceBuffAttrib=None):
        """
        根据给定的属性额外数值计算新DPS\n
        dwAdvanceBuffAttrib： 可添加的有效字段在上文\n
        :param dwAdvanceBuffAttrib:
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

            # 额外buff增益
            if dwAdvanceBuffAttrib:
                for slot, value in dwAdvanceBuffAttrib.items():
                    if slot in rd.tBuffValues:
                        rd.tBuffValues[slot] += value

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

            # 清空额外buff增益
            if dwAdvanceBuffAttrib:
                for slot, value in dwAdvanceBuffAttrib.items():
                    if slot in rd.tBuffValues:
                        rd.tBuffValues[slot] -= value

        # 清空体质和拆招额外增益记录
        self.recorder_attribute.set_advanced_parry_value(0)
        self.recorder_attribute.set_advanced_vitality_value(0)


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

        nBaseDamage = self.nBaseDamage

        # 单点收益
        for slot, values in profits.items():
            for value in values:

                if slot == 'ParryValue':
                    self.recorder_attribute.set_advanced_parry_value(value)

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
                elif slot == 'Vitality':
                    self.recorder_attribute.set_advanced_vitality_value(value * markers[slot])

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

        return single_profits, marker_profits, marker_equip_profits

    def GetStoneProfit(self, single_profits):
        """
        计算各五彩石的收益\n
        :return:
        """
        # 1. 读取所有五彩石
        player = self.player

        dwAttrib, dwStoneLevel, dwStoneSlot = player.GetAttributeWithoutStone()
        if not dwStoneLevel:
            dwStoneLevel = 6

        self.current_record.base_attributes = dwAttrib

        nBaseDamage = self.GetDamageFromAdvancedAttribute({'': 0})

        # 精简五彩石的百分比加成是一个buff，不会在上文函数中被移除，因此需要在这里额外判定
        dwBuffSlot = {}
        for slot in {'atVitalityBasePercentAdd', 'atAgilityBasePercentAdd', 'atStrengthBasePercentAdd'}:
            if slot in dwStoneSlot:
                dwBuffSlot[slot] = -1 * dwStoneSlot[slot]


        _Attrs = []
        _Attr_ID = set()
        dwUnEnabledSlots = {'Spunk', 'Spirit', 'Magic', 'Lunar', 'Solar', 'Neutral', 'Poison', 'Decritical', 'Dodge',
                            'Life', 'Mana', 'Tough', 'Therapy', 'Threat', 'Resist', 'Strength', 'Agility',
                            'WeaponDamage', 'AllTypeCritical', 'Haste', 'Parry', 'Vitality'}

        stones = stone.get(dwStoneLevel)
        if not stones:
            return

        for dwID, dwStoneDatas in stones.items():
            attrs = set(i for i in dwStoneDatas['_Attrs'] if i is not None)

            for attr in attrs:
                for other_slot in dwUnEnabledSlots:
                    if other_slot in attr:
                        break

                else:  # 如果没有被break就检查下一个属性，否则会在外层也被break
                    continue

                break

            else:
                _Attr_ID.add(dwID)

                if attrs not in _Attrs:
                    _Attrs.append(attrs)


        # 2. 计算大致属性收益比
        # 强制计算体质精简和体外拆，其他dps五彩石在这里粗略比较

        profits = {
            'atVitalityBase': single_profits['Vitality'][4],
            'atPhysicsAttackPowerBase': single_profits['PhysicsAttackPowerBase'][4],
            'atPhysicsCriticalStrike': single_profits['PhysicsCriticalStrike'][4],
            'atPhysicsCriticalDamagePowerBase': single_profits['PhysicsCriticalDamagePower'][4],
            'atPhysicsOvercomeBase': single_profits['PhysicsOvercome'][4],
            'atStrainBase': single_profits['Strain'][4],
            'atSurplusValueBase': single_profits['SurplusValue'][4],
        }

        stone_profit_check = {}

        for dwID in _Attr_ID:
            dwStoneData = stones.get(dwID)

            fProfit = 0
            dwSlots = {}

            for i in range(1, 4):
                slot = dwStoneData.get(f"Attribute{i}ID")
                if not slot:
                    continue

                value1 = dwStoneData.get(f"Attribute{i}Value1")
                value2 = dwStoneData.get(f"Attribute{i}Value2")
                if not value1 and not value2:
                    continue

                value = max([int(v) for v in {value1, value2} if v is not None])

                if slot in profits:
                    fProfit += value * profits[slot]
                    dwSlots[slot] = value

            stone_profit_check[dwID] = {
                'profit': fProfit,
                'slot': dwSlots,
                'name': dwStoneData['Name']
            }

        # 计算各五彩石收益
        # 取前15名+体质精简+体外拆，再排名取出前十名进行展示

        stone_ids = [i for i in stone_profit_check.keys()]
        stone_ids.sort(key=lambda i: stone_profit_check[i]['profit'], reverse=True)

        if len(stone_ids) > 15:
            stone_ids = stone_ids[:15]

        slot_dict = {
            'atPhysicsAttackPowerBase': {'key': 'PhysicsAttackPowerBase', 'name': '攻击'},
            'atPhysicsCriticalStrike': {'key': 'PhysicsCriticalStrike', 'name': '会心'},
            'atPhysicsCriticalDamagePowerBase': {'key': 'PhysicsCriticalDamagePower', 'name': '会效'},
            'atPhysicsOvercomeBase': {'key': 'PhysicsOvercome', 'name': '破防'},
            'atStrainBase': {'key': 'Strain', 'name': '无双'},
            'atSurplusValueBase': {'key': 'SurplusValue', 'name': '破招'},
        }
        dwStoneAdvancedData = None

        # 先计算前15种dps精简
        for dwID in stone_ids:
            dwSlots = stone_profit_check[dwID]['slot']
            advance_data = {}
            szText = ''

            for slot, value in dwSlots.items():
                slot = slot_dict.get(slot)
                if not slot:
                    return

                st = slot.get('key')
                advance_data[st] = value
                szText += f"{slot.get('name')} "

            nAdvancedDamage = self.GetDamageFromAdvancedAttribute(advance_data, dwBuffSlot)

            if dwStoneAdvancedData is None:
                dwStoneAdvancedData = [(stone_profit_check[dwID]['name'], szText, nAdvancedDamage)]
            else:
                dwStoneAdvancedData.append((stone_profit_check[dwID]['name'], szText, nAdvancedDamage))

        # 再计算体外拆和体质精简
        # 体外拆
        special_stone_id_1 = [4018, 4019, 4020, 4021, 4022, 4023]
        id_TWC = special_stone_id_1[dwStoneLevel-1]
        dwStoneData = stones.get(id_TWC)
        if not dwStoneData:
            return

        slot = {
            'Vitality': int(dwStoneData['Attribute1Value1']),
            'ParryValue': int(dwStoneData['Attribute3Value1'])
        }

        self.recorder_attribute.set_advanced_vitality_value(slot['Vitality'])
        self.recorder_attribute.set_advanced_parry_value(slot['ParryValue'])
        nAdvancedDamage = self.GetDamageFromAdvancedAttribute(slot, dwBuffSlot)

        dwStoneAdvancedData.append((dwStoneData['Name'], '体质 外防/血量 拆招 ', nAdvancedDamage))

        # 体质精简
        special_stone_id_2 = [0, 0, 0, 5597, 5598, 5599]
        id_TZJJ = special_stone_id_2[dwStoneLevel - 1]
        if id_TZJJ:
            dwStoneData = stones.get(id_TZJJ)

            # 体质精简的额外体质要先录入，所以这里可能会有点误差，无伤大雅
            value1 = int(dwStoneData['Attribute1Value1'])
            value2 = int(dwStoneData['Attribute2Value1']) / 1024
            nAdvanceVitality = value1 + int(self.recorder_attribute.Vitality * value2)

            slot = {
                'Vitality': nAdvanceVitality,
                'Agility': value1,
                'Strength': value1,
            }

            self.recorder_attribute.set_advanced_vitality_value(nAdvanceVitality)
            nAdvancedDamage = self.GetDamageFromAdvancedAttribute(slot, dwBuffSlot)

            dwStoneAdvancedData.append((dwStoneData['Name'], '全属性 体质(百分比) ', nAdvancedDamage))

        dwStoneAdvancedData.sort(key=lambda i: i[2], reverse=True)

        # 计算提升率
        ret = None
        for stone_checked_data in dwStoneAdvancedData:
            fAdvance = f"{stone_checked_data[2] / nBaseDamage - 1:.2%}"

            if ret is None:
                ret = [(stone_checked_data[0], stone_checked_data[1], fAdvance)]
            else:
                ret.append((stone_checked_data[0], stone_checked_data[1], fAdvance))

        # print(*[f"{i[0]}: {i[2]}\n" for i in ret])

        return ret






    def GetHaloProfit(self):
        pass


