# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=12*16, nMaxStackNum=1)
}

tSkillName = '盾压母技能'
tDesc = '盾压母技能'
nNeedGcdType = [0, 1, 2, 3, 4, 5]
nNeedPosState = 0


def Apply(player: Player, target):

    nCoolDown = 12
    if player.IsSkillRecipeActive(1856):
        nCoolDown -= 1
    if player.IsSkillRecipeActive(1857):
        nCoolDown -= 1

    player.AddSkillCoolDown(13045, nCoolDown*16)

    # # 回怒
    # if player.GetSkillLevel('震怒') == 1:
    #     player.rage += 25
    # else:
    #     player.rage += 15
    # 回怒要放到不同的子技能中

    # 严阵
    if player.GetSkillLevel('严阵') == 1:
        player.AddBuff(18222, 1)
    # 雄峦
    if player.GetSkillLevel('雄峦') == 1:
        player.AddBuff(8253, 1)

    player.AddBuff(8738, 1)

    # 回怒
    if player.GetSkillLevel('震怒') == 1:
        nRage = 25
    else:
        nRage = 15
    
    if player.GetSetting('ParryByExpect'):

        # 用盾压重置率计算回怒期望
        fExpect = player.ParryPercent
        if not isinstance(fExpect, float):
            return

        if player.IsSkillRecipeActive(1858):
            fExpect += 0.05
        if player.IsSkillRecipeActive(1859):
            fExpect += 0.05

        nRage *= fExpect

        player.CastSkill(50006, 1, _fExpect=fExpect)
        player.AddPublicCoolDown(0, int(1.5 * 16 * fExpect))

    else:
        player.CastSkill(19409, 1)
        player.AddPublicCoolDown(0, 1.5 * 16)

    player.rage += nRage

    return 1




DunYa = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)