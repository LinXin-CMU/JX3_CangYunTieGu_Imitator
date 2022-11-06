# coding: utf-8
# author: LinXin

from scripts.default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=10*16, nMaxStackNum=1)
}

tSkillName = '流血'
tDesc = '流血伤害子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    if target.IsHaveBuff(8249):
        player.AddBuff(50005, 1)

    return 1




LiuXueInterval = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)