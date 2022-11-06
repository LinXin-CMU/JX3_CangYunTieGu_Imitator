# coding: utf-8
# author: LinXin

from scripts.default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾飞添加虚弱buff'
tDesc = '盾飞添加虚弱buff子技能'
nNeedGcdType = []
nNeedPosState = None


def Apply(player: Player, target: Target):

    # 延迟0.125s刷新虚弱buff
    if player.IsHaveBuff(50001) and player.IsHaveBuff(8278):
        target.AddBuff(8248, 1)
        pass

    return 1


DunFeiAddXuRuo = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)

