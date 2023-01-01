# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tWeaponLevelData = {
    '烽烟黯': 95,
}

tAttributeData = {
    95: attrib_data("atPhysicsAttackPowerBase", 67)
}



tSkillName = '水·斩流'
tDesc = '水斩流加buff子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    nLevel = tWeaponLevelData.get((player.GetSetting('WeaponType')))
    if not nLevel:
        return

    player.AddBuff(4761, nLevel, attrib=[tAttributeData[nLevel]])

    return 1


Water_ZhanLiu = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)