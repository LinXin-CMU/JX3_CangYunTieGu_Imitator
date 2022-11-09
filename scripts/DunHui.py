# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾回'
tDesc = '盾回母技能'
nNeedGcdType = [6]
nNeedPosState = 1


def Apply(player: Player, target):

    player.CastSkill('DunHuiChangeState', 1)
    player.AddBuff(8424, 1)

    return 1




DunHui = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)