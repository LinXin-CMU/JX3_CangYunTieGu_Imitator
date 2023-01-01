# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=116, nDamageRand=11, nAttackRate=max(0.1, 120*1.05/160), nWeaponDamagePercent=1),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '盾刀'
tDesc = '出尘伤害子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = 0


def Apply(player: Player, target: Target, dwSkillLevel):

    return 1



DunDao_ChuChen = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)