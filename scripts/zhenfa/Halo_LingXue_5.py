# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '龙皇雪风五阵'
tDesc = '龙皇雪风阵五阵子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    player.AddBuff(50012, 1)
    player.AddBuff(15961, 1)

    return 1


Halo_LingXue_5 = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)