# coding: utf-8
# author: LinXin
from scripts.default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾刀母技能'
tDesc = '盾刀母技能脚本'
nNeedGcdType = [0, 1, 2, 3, 4, 5]


def Apply(player: Player, target):
    # print('这是盾刀母技能脚本')
    if not player:
        return

    # 盾刀段数判定
    dundao_b_2 = player.IsHaveBuff(8232, 1)
    dundao_b_3 = player.IsHaveBuff(8262, 1)
    dundao_b_4 = player.IsHaveBuff(8263, 1)

    if player.GetSkillLevel('强袭') == 1 and dundao_b_4:
        # 四段盾刀
        player.DelBuff(8263)
        player.CastSkill(13119, 1)
        player.rage += 15
        player.AddPublicCoolDown(4, 1*16)

    elif dundao_b_3:
        # 三段盾刀
        player.DelBuff(8262)
        player.CastSkill(13060, 1)
        if player.GetSkillLevel('强袭') == 1:
            player.AddBuff(8263, 1)
        if player.IsSkillRecipeActive('盾刀加怒气', 1):
            player.rage += 10
        else:
            player.rage += 5
        player.AddPublicCoolDown(4, 1*16)

    elif dundao_b_2:
        # 二段盾刀
        player.DelBuff(8232)
        player.CastSkill(13059, 1)
        player.AddBuff(8262, 1)
        player.rage += 5
        player.AddPublicCoolDown(4, 1*16)

    else:
        # 一段盾刀
        player.CastSkill('DunDao_1', 1)
        player.AddBuff(8232, 1)
        player.rage += 5
        player.AddPublicCoolDown(1, 1*16)

    # target.AddBuff(8398, 1)   # 卷云
    # 盾压重置
    parry = player.ParryPercent
    if not isinstance(parry, float):
        return
    rand = random.randint(1, 10000)
    if rand/10000 <= parry:
        player.ClearCDTime(13045)

    return 1




DunDao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)