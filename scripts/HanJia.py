# coding: utf-8
# author: LinXin

from scripts.Default import *
from scripts.slot import _attrib_data

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '寒甲母技能'
tDesc = '寒甲母技能脚本'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    # 招架后加寒甲buff
    if player.IsHaveBuff(8462) and (player.IsHaveBuff(8271) or player.IsHaveBuff(8437) or player.IsHaveBuff(17772)):
        return

    player.DelBuff(8271, all_layer=True)
    player.DelBuff(8437, all_layer=True)
    player.DelBuff(17772, all_layer=True)

    nParryValue = player.ParryValue

    nLayer = nParryValue // 600
    nLargeLayer = min(nLayer // 100, 125)

    if not player.GetSetting('ParryByExpect'):
        if nLargeLayer > 0:
            for _ in range(nLargeLayer):
                player.AddBuff(17772, 1)
            nLayer -= (nLargeLayer * 100)

        if nLayer > 0:
            for _ in range(nLayer):
                player.AddBuff(8271, 1)

        player.AddBuff(8437, 1)
        player.AddBuff(8462, 1)

    else:
        nAttack = nLargeLayer * 30000 + (nLayer - (nLargeLayer * 100)) * 300
        fExpectParry = player.GetCumulativeExpectParry(8*16)
        player.AddBuff(50014, 1, attrib=[_attrib_data('atPhysicsAttackPowerBase', int(nAttack * fExpectParry))])




    return 1


HanJia = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)