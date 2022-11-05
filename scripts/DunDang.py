# coding: utf-8
# author: LinXin

from scripts.default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾挡'
tDesc = '盾挡'
nNeedGcdType = [0, 2, 5]
nNeedMinRage = 10


def Apply(player: Player, target):
    player.AddPublicCoolDown(0, 1.5*16)

    rage = player.rage
    lv_dundang = rage // 10

    # 千山奇穴下效果
    if player.GetSkillLevel('千山') == 1:
        player.AddBuff(8448, lv_dundang)
    else:
        player.AddBuff(8499, lv_dundang)

    # 振奋
    if player.GetSkillLevel('振奋') == 1:
        n_zhenfen = min(player.ParryPercentValue // 1500, 125)
        player.AddBuff(8504, n_zhenfen)

    player.rage -= (lv_dundang * 10)



    return 1




DunDang = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)