# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '恋战停止叠加buff'
tDesc = '恋战_会心后停止叠buff加内置cd'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    if not player.IsHaveBuff(8320):
        player.AddBuff(8320, 1)

    return 1


LianZhanStop = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)