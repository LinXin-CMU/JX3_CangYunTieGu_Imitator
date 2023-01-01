# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}


tSkillName = '铁骨橙武触发'
tDesc = '铁骨橙武触发子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    player.AddBuff(50025, 1)    # 橙武特效表现buff
    player.AddBuff(2584, 1)     # 橙武特效内置cd
    player.AddBuff(50023, 1)    # 铁骨橙武特效加内外防
    player.AddBuff(50024, 1, lasting=1)    # 铁骨橙武特效回血量怒气，首跳立即生效

    return 1


ChengWu_MT = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)