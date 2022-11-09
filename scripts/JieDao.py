# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=150, nDamageRand=15, nAttackRate=max(0.1, 160*1.1*1.05*1.1*1.05*1.1*1.05/160), nWeaponDamagePercent=1)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '劫刀'
tDesc = '劫刀母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]
nNeedMinRage = 5
nNeedPosState = 1


def Apply(player: Player, target: Target):
    if not player:
        return

    nCostRage = 10
    # 绝刀减消耗秘籍
    if player.IsSkillRecipeActive('#绝刀减消耗', 1):
        nCostRage -= 5
    if player.rage < nCostRage:
        return

    player.AddPublicCoolDown(0, 1.5 * 16)
    player.rage -= nCostRage

    return 1


JieDao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)