# coding: utf-8
# author: LinXin

from scripts.default import *


tSkillData = {
    1: damage_data(nDamageBase=47, nDamageRand=0, nAttackRate=max(0.1, 70*1.5*2*2*1.05*1.9/160), nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '流血'
tDesc = '流血_有炼狱有割裂子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    if target.IsHaveBuff(8249):
        player.AddBuff(50008, 1)

    return 1




LiuXueInterval_4 = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)