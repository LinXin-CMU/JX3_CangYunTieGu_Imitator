# coding: utf-8
# author: LinXin

from scripts.default import *


tSkillData = {
    1: damage_data(nDamageBase=202, nDamageRand=18, nAttackRate=max(0.1,  190 * 1.05*1.05*1.05*1.1/160), nWeaponDamagePercent=1)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=12*16, nMaxStackNum=1)
}

tSkillName = '盾压'
tDesc = '盾压母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]


def Apply(player: Player, target):
    player.AddSkillCoolDown(13045, 12*16)
    player.AddPublicCoolDown(0, 1.5*16)

    # 回怒
    if player.GetSkillLevel('震怒') == 1:
        player.rage += 25
    else:
        player.rage += 15
    # 严阵
    if player.GetSkillLevel('严阵') == 1:
        player.AddBuff(18222, 1)
    # 雄峦
    if player.GetSkillLevel('雄峦') == 1:
        player.AddBuff(8253, 1)

    player.AddBuff(8738, 1)
    return 1




DunYa = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)