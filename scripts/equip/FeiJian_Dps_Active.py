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
    3: [attrib_data("atAllTypeCriticalStrike", 3400), attrib_data("atAllTypeCriticalDamagePowerBase", 1620)]
}



tSkillName = '飞剑绝意·锋'
tDesc = '龙门飞剑输出武器主动效果'
nNeedGcdType = [0]
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    nLevel = 3

    buff_fj = player.GetBuff(18781)
    if buff_fj.layer < 5:
        return

    player.AddPublicCoolDown(0, 1.5*16)

    player.AddBuff(18792, nLevel, attrib=tAttributeData[nLevel])
    player.DelBuff(18781, all_layer=True)

    return 1


FeiJian_Dps_Active = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)