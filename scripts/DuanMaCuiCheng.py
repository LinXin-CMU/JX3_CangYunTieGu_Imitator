# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=35*16, nMaxStackNum=1),
}

tSkillName = '断马摧城母技能'
tDesc = '断马摧城母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]
nNeedPosState = 0


def Apply(player: Player, target: Target, dwSkillLevel):

    if not player:
        return

    if not player.GetSkillLevel('断马摧城') == 1:
        return

    player.AddPublicCoolDown(1, 1 * 16)
    player.AddSkillCoolDown(25213, 35 * 16)

    nCurrentRage = player.rage

    lv_duanma = nCurrentRage // 10 + 1
    if lv_duanma > 12:
        lv_duanma = 12
    elif lv_duanma < 1:
        lv_duanma = 1

    player.CastSkill(25215, lv_duanma)

    return 1


DuanMaCuiCheng = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)
