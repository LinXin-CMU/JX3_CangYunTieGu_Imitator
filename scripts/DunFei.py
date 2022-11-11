# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=18, nMaxStackNum=3)
}

tSkillName = '盾飞'
tDesc = '盾飞母技能'
nNeedGcdType = [6]
nNeedPosState = 0


def Apply(player: Player, target: Target):

    # 盾飞加buff
    nTime = buff_data.get(8391)
    if not nTime:
        return
    nTime = nTime.nMaxTime
    if player.IsSkillRecipeActive(1957):
        nTime += 5
    if player.IsSkillRecipeActive(1958):
        nTime += 5
    player.AddBuff(8391, 1, lasting=nTime)

    # 盾飞延迟换姿态
    player.AddBuff(13352, 1)

    # 盾飞进gcd
    player.AddPublicCoolDown(6, 1*16)

    # 盾飞立即加虚弱buff
    target.AddBuff(8248, 1)

    # 怒炎
    if player.GetSkillLevel('怒炎') == 1:
        # 加怒炎buff
        player.AddBuff(8276, 1)
        player.ClearCDTime(13054, 5*16)

    # 0.5s内无法施展盾猛
    player.AddBuff(8873, 1)

    # ------------------以下效果要延迟0.375s放到盾飞子技能里实现-------------------
    # 盾飞换姿态
    # 盾飞加盾威buff

    return 1




DunFei = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)