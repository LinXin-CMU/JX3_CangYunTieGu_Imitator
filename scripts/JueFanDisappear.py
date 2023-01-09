# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '绝返绝刀进cd'
tDesc = '绝返绝刀第二刀未打出时进cd'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = 1


def Apply(player: Player, target: Target, dwSkillLevel):
    if not player:
        return

    # 计算需添加cd
    player.ClearCDTime(13055)
    nRecipeCD = 0
    if player.IsSkillRecipeActive(1895):
        nRecipeCD += 1
    if player.IsSkillRecipeActive(1896):
        nRecipeCD += 2
    buff_jfjd_stack = player.GetBuff(50042).layer
    player.AddSkillCoolDown(13055, max(0, 10 - nRecipeCD * buff_jfjd_stack))
    player.DelBuff(50042, all_layer=True)

    return 1


JueFanDisappear = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)