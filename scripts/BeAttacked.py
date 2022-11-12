# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '自身被击子技能'
tDesc = '自身被击后触发效果脚本'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    # 是否招架的判定
    nParry = player.ParryPercent

    if random.randint(1, 10000) <= nParry * 10000:
        nFlag = 1
    else:
        nFlag = 0

    # 招架后加寒甲buff
    if nFlag and player.GetSkillLevel('寒甲') == 1:
        player.CastSkill(13135, 1)

    # 坚铁buff判定
    if player.GetSkillLevel('坚铁') == 1:
        player.CastSkill(13139, 1)
        if nFlag:
            player.CastSkill(13140, 1)

    # 崇云buff判定
    if player.GetSkillLevel('崇云') == 1:
        player.CastSkill(21749, 1)

    return 1



BeAttacked = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)