# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=150*2/5, nDamageRand=50 * 0.1*2/5, nAttackRate=300 * ((1 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    2: damage_data(nDamageBase=160*2/5, nDamageRand=60 * 0.1*2/5, nAttackRate=300 * ((2 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    3: damage_data(nDamageBase=170*2/5, nDamageRand=70 * 0.1*2/5, nAttackRate=300 * ((3 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    4: damage_data(nDamageBase=180*2/5, nDamageRand=80 * 0.1*2/5, nAttackRate=300 * ((4 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    5: damage_data(nDamageBase=200*2/5, nDamageRand=90 * 0.1*2/5, nAttackRate=300 * ((5 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    6: damage_data(nDamageBase=220*2/5, nDamageRand=100 * 0.1*2/5, nAttackRate=300 * ((6 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    7: damage_data(nDamageBase=240*2/5, nDamageRand=110 * 0.1*2/5, nAttackRate=300 * ((7 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    8: damage_data(nDamageBase=260*2/5, nDamageRand=120 * 0.1*2/5, nAttackRate=300 * ((8 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    9: damage_data(nDamageBase=270*2/5, nDamageRand=130 * 0.1*2/5, nAttackRate=300 * ((9 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    10: damage_data(nDamageBase=280*2/5, nDamageRand=140 * 0.1*2/5, nAttackRate=300 * ((10 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    11: damage_data(nDamageBase=290*2/5, nDamageRand=150 * 0.1*2/5, nAttackRate=300 * ((11 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
    12: damage_data(nDamageBase=300*2/5, nDamageRand=155 * 0.1*2/5, nAttackRate=300 * ((12 - 1) * 0.075 + 1) * 1.3 / 160, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    2: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    3: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    4: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    5: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    6: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    7: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    8: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    9: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    10: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    11: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    12: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '断马摧城'
tDesc = '断马摧城伤害子技能'
nNeedGcdType = []
nNeedPosState = 0


def Apply(player: Player, target: Target, dwSkillLevel):

    return 1


DuanMaCuiChengDamage = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)
