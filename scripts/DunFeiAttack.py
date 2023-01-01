# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=24, nDamageRand=2, nAttackRate=max(0.1, 27/160), nWeaponDamagePercent=1)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾飞'
tDesc = '盾飞伤害子技能'
nNeedGcdType = []
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    # ------------------以下效果要延迟0.375s放到盾飞子技能里实现-------------------
    # 盾飞跳伤害后添加计数buff
    player.AddBuff(50000, 1)
    # 盾飞延迟0.125s刷新虚弱buff
    player.AddBuff(50002, 1)
    # 盾飞刷新盾威
    if target.IsHaveBuff(8397):
        target.AddBuff(8397, 1)

    # 盾飞检查是否满足50次伤害
    b_count = player.IsHaveBuff(50000)
    if not b_count:
        return
    if b_count.layer == 50:
        # 调用收回盾牌的脚本
        player.CastSkill('DunHuiChangeState', 1)
    else:
        if player.IsHaveBuff(8391, 1):
            # 可以有下一跳盾飞, 添加1s间隔
            player.AddBuff(50003, 1)

    return 1




DunFeiAttack = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)