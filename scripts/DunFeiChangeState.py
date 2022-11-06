# coding: utf-8
# author: LinXin

from scripts.default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '盾飞切换姿态'
tDesc = '盾飞切姿态子技能'
nNeedGcdType = []
nNeedPosState = None


def Apply(player: Player, target: Target):

    # ------------------以下效果要延迟0.375s放到盾飞子技能里实现-------------------
    # 盾飞换姿态
    player.DelBuff(8277, 1)
    player.AddBuff(8278, 1)
    # 盾飞加盾威buff
    target.AddBuff(8397, 1)
    # 盾飞造成伤害
    player.CastSkill(13316, 1)

    return 1




DunFeiChangeState = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)