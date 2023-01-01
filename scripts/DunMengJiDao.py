# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾猛延迟添加击倒buff'
tDesc = '盾猛击倒子技能'
nNeedGcdType = []
nNeedPosState = 0


def Apply(player: Player, target: Target, dwSkillLevel):

    target.AddBuff(994, 1)

    return 1




DunMengJiDao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)