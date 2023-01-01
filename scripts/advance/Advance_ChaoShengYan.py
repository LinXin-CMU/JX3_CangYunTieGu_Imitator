# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '朝圣言'
tDesc = '朝圣言子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None



def Apply(player: Player, target: Target, dwSkillLevel):

    if player.IsHaveBuff(50030):
        return

    nStackNum = player.GetTeamMateAdvanceStackNum(3985)
    if not nStackNum:
        return

    for _ in range(nStackNum):
        player.AddBuff(4246, 1)
    player.AddBuff(50030, 1)

    return 1



Advance_ChaoShengYan = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)