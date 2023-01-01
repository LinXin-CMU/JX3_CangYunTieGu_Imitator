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
    '贯鳞/风落秋': 100,
}

tAttributeData = {
    100: attrib_data("atPhysicsOvercomeBase", 6408)
}



tSkillName = '风·斩流'
tDesc = '风斩流加buff子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    nLevel = tWeaponLevelData.get((player.GetSetting('PendantType')))
    if not nLevel:
        return

    player.AddBuff(6360, nLevel, attrib=[tAttributeData[nLevel]])
    player.AddSkillCoolDown(50008, 180*16)

    return 1


Wind_ZhanLiu = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)