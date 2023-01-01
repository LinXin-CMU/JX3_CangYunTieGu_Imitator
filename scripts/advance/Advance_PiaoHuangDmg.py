# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=417, nDamageRand=15, nAttackRate=max(0.1, 250 * 1.3 * 1.25 * 0.85 * 0.9 * 0.9 * 0.9 * 0.9 * 0.9/160), nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '飘黄'
tDesc = '飘黄伤害子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None



def Apply(player: Player, target: Target, dwSkillLevel):

    if player.IsHaveBuff(21637):
        return

    if not player.IsHaveBuff(20854):
        return

    player.AddBuff(21637, 1)
    target.AddBuff(50039, 1)

    return 1



Advance_PiaoHuangDmg = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)