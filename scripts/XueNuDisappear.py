# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '血怒消失后删buff'
tDesc = '血怒消失后子技能'
nNeedGcdType = []
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    player.DelBuff(8244)
    player.DelBuff(8245)
    player.DelBuff(8382)
    player.DelBuff(8383)
    player.DelBuff(8384)
    player.DelBuff(8385)
    player.DelBuff(8386)
    player.DelBuff(14309)
    player.DelBuff(14964)
    player.DelBuff(50009)

    return 1



XueNuDisappear = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)