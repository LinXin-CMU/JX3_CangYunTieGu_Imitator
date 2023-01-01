# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '舍身弘法'
tDesc = '舍身弘法子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None



def Apply(player: Player, target: Target, dwSkillLevel):

    if player.IsHaveBuff(50029):
        return

    nStackNum = player.GetTeamMateAdvanceStackNum(15195)
    if not nStackNum:
        return

    for _ in range(nStackNum):
        player.AddBuff(10208, 1)

    player.AddBuff(50029, 1)


    return 1



Advance_SheShenHongFa = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)