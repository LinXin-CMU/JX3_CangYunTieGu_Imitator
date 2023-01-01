# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=max(0.1, 0.12), nWeaponDamagePercent=1.2)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '卷雪刀'
tDesc = '卷雪刀子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):
    if not player:
        return

    nAttackSpeed = player.WeaponAttackSpeed
    # 先计算实际帧数
    nHasteGuo = player.GetSnapShot(13054)['HasteValueGuo']
    nAttackSpeed = int(1024 * nAttackSpeed / (1024 + nHasteGuo))

    player.AddBuff(50011, 1, lasting=nAttackSpeed)

    return 1


JuanXueDao = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)