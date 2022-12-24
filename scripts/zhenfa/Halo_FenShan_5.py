# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '锋凌横绝五阵'
tDesc = '锋凌横绝五阵子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


bJueFan = True

def Apply(player: Player, target: Target):

    player.AddBuff(8403, 1)

    # 绝返判定，用于计算当前应添加多长时间的绝刀cd
    global bJueFan
    if bJueFan:
        player.AddBuff(50019, 1, lasting=1.4375*16)
    else:
        player.AddBuff(50019, 1)
    bJueFan = not bJueFan

    return 1


Halo_FenShan_5 = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)