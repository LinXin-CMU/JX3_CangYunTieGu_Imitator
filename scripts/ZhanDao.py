# coding: utf-8
# author: LinXin

from scripts.default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=10*16, nMaxStackNum=1)
}

tSkillName = '斩刀'
tDesc = '斩刀母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]
nNeedMinRage = 15
nNeedPosState = 1


def Apply(player: Player, target: Target):
    if not player:
        return

    player.AddPublicCoolDown(0, 1.5*16)
    player.AddSkillCoolDown(13054, 10*16)

    # 流血部分
    # 获取加速
    # haste = player.HastePercent
    if player.GetSkillLevel('#炼狱') == 1:
        lx_itv = 1 * 16
    else:
        lx_itv = 2 * 16

    # 怒炎-命中虚弱目标添加怒炎buff
    if target.IsHaveBuff(8248):
        player.AddBuff(24755, 1)
        target.DelBuff(8248)

        if target.IsHaveBuff(8249, 1):
            # 已有流血目标
            b_lxitv = player.GetBuff(50005)
            target.AddBuff(8249, 1, lasting=(24 * lx_itv + b_lxitv.lasting))
        else:
            # 仅有虚弱目标
            target.AddBuff(8249, 1, lasting=(25 * lx_itv))
            # 添加流血间隔技能自身监控
            player.CastSkill(8249, 1)

    elif target.IsHaveBuff(8249):
        # 命中仅有流血buff目标刷新流血效果
        b_lxitv = player.GetBuff(50005)
        target.AddBuff(8249, 1, lasting=(24 * lx_itv + b_lxitv.lasting))

    # 戍卫-斩刀强仇和减伤
    player.AddBuff(13934, 1)

    return 1




ZhanDao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)