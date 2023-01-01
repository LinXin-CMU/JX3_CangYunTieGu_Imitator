# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾挡'
tDesc = '盾挡'
nNeedGcdType = [0, 2, 5]
nNeedMinRage = 10
nNeedPosState = 0


attrib_value = {
    1: [13, 35],
    2: [14, 36],
    3: [15, 37],
    4: [16, 38],
    5: [17, 39],
    6: [18, 40],
    7: [19, 41],
    8: [20, 42],
    9: [21, 43],
    10: [22, 44],
    11: [23, 45],
    12: [2, 24],
    13: [3, 25],
    14: [4, 26],
    15: [5, 27],
    16: [6, 28],
    17: [7, 29],
    18: [8, 30],
    19: [9, 31],
    20: [10, 32],
    21: [11, 33],
    22: [12, 34],
}


def Apply(player: Player, target: Target, dwSkillLevel):
    player.AddPublicCoolDown(0, 1.5*16)

    rage = player.rage
    lv_dundang = rage // 10

    # 千山奇穴下效果
    if player.GetSkillLevel('千山') == 1:
    # if True:
        player.AddBuff(8448, lv_dundang, attrib=attrib_value[lv_dundang+11])
    else:
        player.AddBuff(8499, lv_dundang, attrib=attrib_value[lv_dundang])

    # 振奋
    if player.GetSkillLevel('振奋') == 1:
        n_zhenfen = min(player.ParryPercentValue // 1500, 125)
        player.AddBuff(8504, n_zhenfen)

    player.rage -= (lv_dundang * 10)

    return 1




DunDang = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)