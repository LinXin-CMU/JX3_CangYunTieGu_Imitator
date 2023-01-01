# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}


tAttributeData = {
    3: attrib_data("atVitalityBase", 64)
}



tSkillName = '龙门飞剑防御被动'
tDesc = '龙门飞剑防御武器被动效果'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    nLevel = 3
    player.AddBuff(18783, nLevel, attrib=[tAttributeData[nLevel]])
    player.AddSkillCoolDown(26140, 6*16)

    # if player.GetBuff(18783, 1).layer == 5:
    #     player.CastSkill(26141, 1)

    return 1


FeiJian_MT_Passive = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)