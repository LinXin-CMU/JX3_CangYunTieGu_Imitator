# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=40, nDamageRand=17, nAttackRate=max(0.1, 75/160), nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '昆吾·弦刃'
tDesc = '输出护腕大附魔子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    if not player:
        return

    if player.IsHaveBuff(15453):
        return

    player.AddBuff(15453, 1)

    return 1


ShangWan = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)