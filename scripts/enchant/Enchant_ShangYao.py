# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '输出腰带大附魔'
tDesc = '输出腰带大附魔子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    if not player:
        return

    if player.IsHaveBuff(15456):
        return

    if random.random() < 0.3:
        player.AddBuff(15455, 1, attrib=[59])
    else:
        player.AddBuff(15455, 1, attrib=[60])

    player.AddBuff(15456, 1)

    return 1


ShangYao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)