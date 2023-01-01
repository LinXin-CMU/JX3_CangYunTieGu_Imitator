# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=1500, nDamageRand=50, nAttackRate=max(0.1, 250/160), nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '鸿烈'
tDesc = '鸿烈伤害子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    if not player.GetSkillLevel("鸿烈") == 1:
        return

    player.AddSkillCoolDown(26897, 25*16)

    return 1


HongLie = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)