# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=104, nDamageRand=10, nAttackRate=max(0.1, (100 * 1.05 * 1.05 * 1.1)/160), nWeaponDamagePercent=1)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=4*16, nMaxStackNum=3)
}

tSkillName = '盾击'
tDesc = '盾击母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]


def Apply(player: Player, target):
    player.AddPublicCoolDown(1, 1*16)
    player.AddPublicCoolDown(2, 0.5*16)

    player.AddSkillCoolDown(13047, 4*16)

    player.rage += 10

    # 盾压重置
    parry = player.ParryPercent
    if not isinstance(parry, float):
        return
    rand = random.randint(1, 10000)
    if rand/10000 <= parry:
        player.ClearCDTime(13045)

    return 1




DunJi = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)