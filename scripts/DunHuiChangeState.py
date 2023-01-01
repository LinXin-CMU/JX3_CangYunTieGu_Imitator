# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾回切换姿态'
tDesc = '盾回切姿态子技能'
nNeedGcdType = [6]
nNeedPosState = 1


def Apply(player: Player, target: Target, dwSkillLevel):

    # 盾回换姿态
    player.DelBuff(8278, 1)
    player.AddBuff(8277, 1)

    # 清除盾飞buff
    player.DelBuff(8391, 1, all_layer=True)
    player.DelBuff(13352, 1, all_layer=True)
    player.DelBuff(50000, 1, all_layer=True)
    player.DelBuff(50001, 1, all_layer=True)
    player.DelBuff(50002, 1, all_layer=True)
    player.DelBuff(50003, 1, all_layer=True)

    # 盾飞保护gcd
    player.AddPublicCoolDown(6, 1*16)

    return 1




DunHuiChangeState = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)