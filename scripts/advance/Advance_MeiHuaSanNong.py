# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '梅花三弄'
tDesc = '梅花三弄总控母技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None



def Apply(player: Player, target: Target, dwSkillLevel):

    # 先检查风雷盾
    if player.GetTeamMateTalent(23826):
        if not player.IsHaveBuff(50037):
            fNongMeiCov = player.GetTeamMateAdvanceStackNum(23826)
            player.DelBuff(9334, 1)
            player.AddBuff(16911, 1, lasting=int(120*16*fNongMeiCov))
            player.AddBuff(50037, 1)

    if player.GetTeamMateTalent(14071):
        if not player.IsHaveBuff(16911) and not player.IsHaveBuff(9335):
            fMeiHuaCov = player.GetTeamMateAdvanceStackNum(14071)
            player.AddBuff(9334, 1, lasting=int(15*16*fMeiHuaCov))
            player.AddBuff(9335, 1)

    return 1



Advance_MeiHuaSanNong = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)