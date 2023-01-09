   # coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '阵云结晦母技能'
tDesc = '阵云结晦母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]
nNeedMinRage = 0
nNeedPosState = 1


def Apply(player: Player, target: Target, dwSkillLevel):
    if not player:
        return

    if not player.GetSkillLevel("阵云结晦") == 1:
        return

    buff_zy = player.GetBuff(22993)
    if not buff_zy.layer >= 4:
        if not player.IsHaveBuff(22976) and not player.IsHaveBuff(22977):
            return

    player.AddPublicCoolDown(0, 1.5*16)

    if player.IsHaveBuff(22977):    # 雁门迢递
        player.CastSkill(30857, 1)
        player.DelBuff(22977)   # 删三段标记buff
        # 五次绝国伤害
        for _ in range(5):
            player.CastSkill(30858, 1)

    elif player.IsHaveBuff(22976):  # 月照连营
        player.CastSkill(30926, 1)
        player.DelBuff(22976)
        player.AddBuff(22977, 1)

    else:
        # 删4层阵云buff
        for _ in range(4):
            player.DelBuff(22993)

        player.CastSkill(30925, 1)  # 阵云结晦
        player.AddBuff(22976, 1)    # 加二段标记buff
        player.DelBuff(22977, 1)    # 删可能存在的三段标记buff


    return 1




ZhenYunJieHui_major = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)