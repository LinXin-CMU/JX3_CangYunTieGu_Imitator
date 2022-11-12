# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=47, nDamageRand=0, nAttackRate=max(0.1, 70*1.5*2*2*1.05/1000/2), nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '流血'
tDesc = '流血_无炼狱无割裂子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    if target.IsHaveBuff(8249):
        if target.IsHaveBuff(21308):
            player.AddBuff(50005, 1)
        else:
            player.AddBuff(50007, 1)

    return 1




LiuXueInterval_1 = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)