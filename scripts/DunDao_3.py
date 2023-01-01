# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=130, nDamageRand=15, nAttackRate=max(0.1, (120 * 1.05 * 1.05 * 1.1)/160), nWeaponDamagePercent=1)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾刀'
tDesc = '盾刀三段伤害子技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]
nNeedPosState = 0


def Apply(player: Player, target: Target, dwSkillLevel):
    return 1




DunDao_3 = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)