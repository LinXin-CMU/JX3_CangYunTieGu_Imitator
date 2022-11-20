# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '通用_Npc普攻子技能'
tDesc = 'Npc普攻子技能脚本'
nNeedGcdType = [0]
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    target.AddPublicCoolDown(0, target.GetSetting('AttackFreq'))

    for i in range(target.GetSetting('AttackCount')):
        player.CastSkill(50000, 1)

    return 1



NpcAttack = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)