# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}


tSkillName = '分山橙武触发'
tDesc = '分山橙武触发子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    player.AddBuff(50043, 1)    # 橙武特效表现buff
    player.AddBuff(2584, 1)     # 橙武特效内置cd

    # 清绝刀和盾压的cd
    player.ClearCDTime(13045)
    player.ClearCDTime(13055)

    return 1


ChengWu_Dps = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)