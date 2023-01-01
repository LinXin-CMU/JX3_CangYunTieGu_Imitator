# coding: utf-8
# author: LinXin
# 用于计算有内置cd的效果的概率触发事件
# import random

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}


tSkillName = '概率触发事件监控器'
tDesc = '概率触发事件监控器'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None

# 橙武
nChengWuCount = 0

# 大附魔
nShangWanCount = 0  # 伤腕
nShangYaoCount = 0  # 伤腰
nShangXieCount = 0  # 伤鞋
nYuWanCount = 0     # 御腕

# 部分大附魔的属性标记
# 1/3代表当前版本普通装备对应品级等级附魔，2/4代表英雄装备
dwShangYiAttrib = {
    3: [61, 62],
    4: [63, 64],
}
dwShangMaoAttrib = {
    3: [99, 100],
    4: [101, 102],
}

def Apply(player: Player, target: Target, dwSkillLevel):

    # 橙武
    szWeaponType = player.GetSetting('WeaponType')
    if szWeaponType in {'铁骨橙武'}:
        if not player.IsHaveBuff(2584):
            global nChengWuCount
            nChengWuCount += 1
            if nChengWuCount > 32:
                nChengWuCount = 0
                player.CastSkill(50009, 1)

    # 大附魔
    # 设置结构: [0-帽, 1-衣, 2-腰, 3-腕, 4-鞋]
    # 0-无对应附魔; 1,2-T附魔; 3,4-dps附魔
    dwEnchantSetting = player.GetSetting('Enchants')
    # 腕
    if dwEnchantSetting[3] in {3, 4}:
        if not player.IsHaveBuff(15453):
            global nShangWanCount
            nShangWanCount += 1
            if nShangWanCount > 9:
                nShangWanCount = 0
                player.CastSkill(22166, 1)
    elif dwEnchantSetting[3] in {1, 2}:
        if not player.IsHaveBuff(24791):
            global nYuWanCount
            nYuWanCount += 1
            if nYuWanCount > 9:
                nYuWanCount = 0
                player.CastSkill(33249, 1)

    # 腰
    if dwEnchantSetting[2] in {3, 4}:
        if not player.IsHaveBuff(15456):
            global nShangYaoCount
            nShangYaoCount += 1
            if nShangYaoCount > 5:
                nShangYaoCount = 0
                player.CastSkill(22169, 1)
    # 御腰省略

    # 鞋
    if dwEnchantSetting[4] in {3, 4}:
        if not player.IsHaveBuff(24774):
            global nShangXieCount
            nShangXieCount += player.PhysicsCriticalPercent
            if nShangXieCount >= 1:
                nShangXieCount = 0
                player.CastSkill(33257, 1)
    # 御鞋省略

    # 衣
    if dwEnchantSetting[1] in {3, 4}:
        if not player.IsHaveBuff(50026):
            player.AddBuff(50026, 1, attrib=dwShangYiAttrib[dwEnchantSetting[1]])
    # 御衣省略

    # 帽
    if dwEnchantSetting[0] in {3, 4}:
        if not player.IsHaveBuff(15436):
            player.AddBuff(15436, 1, attrib=dwShangMaoAttrib[dwEnchantSetting[0]])
    elif dwEnchantSetting[0] in {1, 2}:
        if not player.IsHaveBuff(15414):
            player.CastSkill(22122, dwEnchantSetting[0])


    return 1


def ResetEventCount():
    global nChengWuCount, nShangWanCount, nShangYaoCount, nShangXieCount, nYuWanCount
    nChengWuCount = 4
    nShangWanCount = 0
    nShangYaoCount = 0
    nShangXieCount = 0
    nYuWanCount = 0


PercentageEventTrigger = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)




