# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=202, nDamageRand=18, nAttackRate=max(0.1,  190 * 1.05*1.05*1.05*1.1/160), nWeaponDamagePercent=1)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=12*16, nMaxStackNum=1)
}

tSkillName = '盾压'
tDesc = '盾压伤害子技能'
nNeedGcdType = []
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    return 1


DunYaDamage = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)