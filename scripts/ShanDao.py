# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=150, nDamageRand=15, nAttackRate=max(0.1, 160*0.9*1.05*1.05/160), nWeaponDamagePercent=1)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=8*16, nMaxStackNum=1)
}

tSkillName = '闪刀'
tDesc = '闪刀母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]
nNeedMinRage = 15
nNeedPosState = 1


def Apply(player: Player, target: Target):
    if not player:
        return

    player.AddSkillCoolDown(13053, 8*16)
    player.AddPublicCoolDown(0, 1.5*16)
    player.rage -= 15

    # 割裂buff
    if player.GetSkillLevel('割裂') == 1:
        if player.IsHaveBuff(8249):
            player.AddBuff(21308, 1)

    return 1




ShanDao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)