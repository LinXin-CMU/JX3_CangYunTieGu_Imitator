# coding: utf-8
# author: LinXin

from scripts.default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0.4, nWeaponDamagePercent=0),
    2: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0.55*0.66, nWeaponDamagePercent=0),
    3: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0.7, nWeaponDamagePercent=0),
    4: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0.8*0.66, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    2: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    3: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    4: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '破招'
tDesc = '苍云破招子技能'
nNeedGcdType = []
nNeedPosState = None


def Apply(player: Player, target: Target):
    return 1



PoZhao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)