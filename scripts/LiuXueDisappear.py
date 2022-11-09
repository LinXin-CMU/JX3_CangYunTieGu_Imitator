# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '流血结束移除割裂'
tDesc = '流血_消失后移除割裂子技能'
nNeedGcdType = []
nNeedPosState = None


def Apply(player: Player, target: Target):

    target.DelBuff(21308, all_layer=True)

    return 1




LiuXueDisappear = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)