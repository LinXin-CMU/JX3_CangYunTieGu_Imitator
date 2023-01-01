# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=130, nDamageRand=12, nAttackRate=max(0.1,  150*1.05*1.05*1.05/160), nWeaponDamagePercent=1)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=15*16, nMaxStackNum=1)
}

tSkillName = '盾猛'
tDesc = '盾猛母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]
nNeedPosState = 0


def Apply(player: Player, target: Target, dwSkillLevel):

    # 盾飞后0.5s无法施展盾猛
    if player.IsHaveBuff(8873, 1):
        return

    player.AddSkillCoolDown(13046, 15*16)
    player.AddPublicCoolDown(0, 1.5*16)

    # 回怒
    if player.GetSkillLevel('震怒') == 1:
        player.rage += 25
    else:
        player.rage += 15

    if player.GetSkillLevel('猛志') == 1:
        player.rage += 35

    # 激昂
    if player.GetSkillLevel('激昂') == 1:
        player.AddBuff(8418, 1)

    # 盾压重置
    if not player.GetSetting('ParryByExpect'):
        parry = player.ParryPercent
        if not isinstance(parry, float):
            return

        if player.IsSkillRecipeActive(1858):
            parry += 0.05
        if player.IsSkillRecipeActive(1859):
            parry += 0.05

        rand = random.randint(1, 10000)
        if rand/10000 <= parry:
            player.ClearCDTime(13045)
    else:
        player.ClearCDTime(13045)

    # 盾猛延迟0.625s造成击倒
    player.AddBuff(50004, 1)

    return 1




DunMeng = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)