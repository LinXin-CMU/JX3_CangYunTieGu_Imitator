# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=40, nDamageRand=17, nAttackRate=max(0.1, 100/160), nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '刃凌'
tDesc = '输出鞋子大附魔子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    if not player:
        return

    if player.IsHaveBuff(24774):
        return

    player.AddBuff(24774, 1)

    return 1


Enchant_ShangXie = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)