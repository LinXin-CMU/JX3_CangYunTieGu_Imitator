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


def Apply(player: Player, target: Target):
    if not player:
        return

    # 检查怒气需求
    if player.IsSkillRecipeActive(1850):
        nCostRage = 10
    else:
        nCostRage = 25

    # # 调试用！
    # nCostRage = 10

    if player.rage < nCostRage:
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
    lv_juedao = min((current_rage - nCostRage) // 10, 4)

    if lv_juedao:
        player.AddBuff(9052, lv_juedao)
        for i in range(5):
            if i == lv_juedao:
                player.SetSkillRecipeActive(4917+i)
            else:
                player.SetSkillRecipeActive(4917+i, isActive=False)


    nCostRage += lv_juedao * 10

    # 怒炎重置cd
    if player.IsHaveBuff(24756):
        player.DelBuff(24756)
        player.ClearCDTime(13055)
        nCostRage = 0

    # 绝刀破招，铁骨3级
    player.CastSkill(32745, 3)

    player.rage -= nCostRage

    return 1






JueDao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)