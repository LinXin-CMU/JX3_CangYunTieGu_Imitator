# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=1500, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
    2: damage_data(nDamageBase=1690, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
    3: damage_data(nDamageBase=3040, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=6*16, nMaxStackNum=1),
    2: cooldown_data(nSingleCoolDown=6*16, nMaxStackNum=1),
    3: cooldown_data(nSingleCoolDown=6*16, nMaxStackNum=1),

}


tSkillName = '剑风'
tDesc = '龙门飞剑输出武器被动效果'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    player.AddBuff(18781, 1)
    player.AddSkillCoolDown(29919, 6*16)

    return 1


FeiJian_Dps_Passive = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)