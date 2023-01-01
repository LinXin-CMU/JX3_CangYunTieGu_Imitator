# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '怒炎增伤buff消失'
tDesc = '怒炎增伤buff消失后删秘籍子技能'
nNeedGcdType = []
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):
    if not player:
        return

    player.SetSkillRecipeActive(1879, isActive=False)
    player.SetSkillRecipeActive(4409, isActive=False)

    return 1






NuYanMajorDisappear = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)