# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
    2: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
    2: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

# 部分大附魔的属性标记
# 1/3代表当前版本普通装备对应品级等级附魔，2/4代表英雄装备
tSkillLevelData = {
    1: [61, 62],
    2: [63, 64]
}

tSkillName = '防御帽子大附魔'
tDesc = '防御帽子大附魔子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None




def Apply(player: Player, target: Target, dwSkillLevel):

    if not player:
        return

    if player.IsHaveBuff(15414):
        return


    player.AddBuff(15413, 1, attrib=tSkillLevelData[dwSkillLevel])
    player.AddBuff(15414, 1)

    return 1


Enchant_YuMao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)