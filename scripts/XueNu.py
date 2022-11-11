# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=25*16, nMaxStackNum=3),
}

tSkillName = '血怒'
tDesc = '血怒母技能'
nNeedGcdType = [7]
nNeedPosState = None


def Apply(player: Player, target: Target):

    player.AddPublicCoolDown(7, 0.5*16)
    player.AddSkillCoolDown(13040, 25*16)

    nAddRage = 10
    if player.IsSkillRecipeActive(1870):
        nAddRage += 5
    if player.IsSkillRecipeActive(1871):
        nAddRage += 5
    if player.IsSkillRecipeActive(1872):
        nAddRage += 5

    if player.GetSkillLevel('愤恨') == 1:
        nPeriod = 25
    else:
        nPeriod = 10
    if player.IsSkillRecipeActive(1867):
        nPeriod += 1
    if player.IsSkillRecipeActive(1868):
        nPeriod += 1
    if player.IsSkillRecipeActive(1869):
        nPeriod += 1
    nPeriod *= 16

    if player.GetSkillLevel('愤恨') == 1:
        buff_xn_id = 8386
    else:
        buff_xn_id = 8245

    # 血怒连按处理
    if player.IsHaveBuff(8384):
        # 在连按条件内
        if player.IsHaveBuff(8383):
            # 第三层需求buff
            if player.GetBuff(buff_xn_id).layer == 2:
                player.AddBuff(buff_xn_id, 1, lasting=nPeriod)
                player.DelBuff(8382)
                player.DelBuff(8383)

        elif player.IsHaveBuff(8382):
            # 第二层需求buff
            if player.GetBuff(buff_xn_id).layer == 1:
                player.AddBuff(buff_xn_id, 1, lasting=nPeriod)
                player.DelBuff(8382)
                player.AddBuff(8383, 1)

        else:
            # ？
            player.AddBuff(buff_xn_id, 1, lasting=nPeriod)
            player.DelBuff(8383)
            player.AddBuff(8382, 1)

    else:
        player.DelBuff(buff_xn_id, all_layer=True)
        player.AddBuff(buff_xn_id, 1, lasting=nPeriod)
        player.AddBuff(8382, 1)

    # 任何情况都添加连按需求buff
    player.AddBuff(8384, 1)

    # 崇云buff
    player.AddBuff(14964, 1)
    # 崇云次数检测buff
    for i in range(3):
        player.AddBuff(50009, 1)




    player.rage += nAddRage

    return 1



XueNu = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)