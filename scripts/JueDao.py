# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=180, nDamageRand=12, nAttackRate=max(0.1, 250*0.75*0.9*1.1*1.05*1.05*1.05*1.22*1.05*1.05*1.1/160), nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=10*16, nMaxStackNum=1)
}

tSkillName = '绝刀'
tDesc = '绝刀母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]
nNeedMinRage = 10
nNeedPosState = 1


def Apply(player: Player, target: Target, dwSkillLevel):
    if not player:
        return

    # 检查怒气需求
    if player.IsSkillRecipeActive(1850):
        nRageCost = 10
    else:
        nRageCost = 25

    # # 调试用！
    # nRageCost = 10

    if player.rage < nRageCost:
        return

    # 绝刀cd
    cd_juedao = 10
    if player.IsSkillRecipeActive(1895):
        cd_juedao -= 1
    if player.IsSkillRecipeActive(1896):
        cd_juedao -= 2
    player.AddPublicCoolDown(0, 1.5*16)
    player.AddSkillCoolDown(13055, cd_juedao*16)

    # 绝刀消耗怒气加伤害
    current_rage = player.rage
    lv_juedao = min((current_rage - nRageCost) // 10, 4)

    if lv_juedao:
        player.AddBuff(9052, lv_juedao)
        for i in range(5):
            if i == lv_juedao:
                player.SetSkillRecipeActive(4917+i)
            else:
                player.SetSkillRecipeActive(4917+i, isActive=False)


    nRageCost += lv_juedao * 10

    # 优先触发橙武特效
    if player.IsHaveBuff(50043):
        player.ClearCDTime(13055)
        nRageCost = 0
    else:
        # 绝返
        if player.GetSkillLevel("绝返") == 1:
            # 第一刀未打出的情况
            if player.IsHaveBuff(8451):
                player.DelBuff(8451)
                player.AddBuff(8453, 1)     # 绝刀第二刀倒计时
                player.AddBuff(50042, 1)    # 绝返绝刀施展次数计数
                player.ClearCDTime(13055)
                nRageCost = 0
            # 第二刀的情况
            elif player.IsHaveBuff(8453):
                player.DelBuff(8453)
                player.AddBuff(50042, 1)    # 绝返绝刀施展次数计数

                # 计算需添加cd
                player.ClearCDTime(13055)
                nRecipeCD = 0
                if player.IsSkillRecipeActive(1895):
                    nRecipeCD += 1
                if player.IsSkillRecipeActive(1896):
                    nRecipeCD += 2
                buff_jfjd_stack = player.GetBuff(50042).layer
                player.AddSkillCoolDown(13055, max(0, (10-nRecipeCD*buff_jfjd_stack)*16))
                player.DelBuff(50042, all_layer=True)


        # 怒炎重置cd
        if player.IsHaveBuff(24756):
            player.DelBuff(24756)
            player.ClearCDTime(13055)
            nRageCost = 0

    # 绝刀破招，铁骨3级
    if player.mount == 10389:
        player.CastSkill(32745, 3)
    elif player.mount == 10390:
        player.CastSkill(32745, 4)

    player.rage -= nRageCost

    # 阵云结晦
    if player.GetSkillLevel("阵云结晦") == 1:
        player.AddBuff(22993, 1)
        player.CastSkill(30859, 1)  # 阵云绝

    # 分野
    if player.GetSkillLevel("分野") == 1:
        player.AddBuff(17176, 1)
        player.AddBuff(50041, 1)    # 分野会心会效，这一句后面不能再有player.CastSkill方法

    return 1






JueDao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)