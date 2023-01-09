# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=max(0.1, 0/160), nWeaponDamagePercent=1)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '阵云结晦'
tDesc = '阵云结晦一段伤害子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = 1


def Apply(player: Player, target: Target, dwSkillLevel):
    if not player:
        return

    if not player.GetSkillLevel("阵云结晦") == 1:
        return

    return 1




ZhenYunJieHui_1_dmg = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)