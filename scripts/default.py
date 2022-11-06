# coding: utf-8
# author: LinXin

from jx3_types import skill_script, damage_data, cooldown_data, Player, Target
from scripts.buff import buff_data
import random


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=max(0.1, 0/160), nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '默认技能'
tDesc = '默认的技能脚本'
nNeedGcdType = 0
nNeedMinRage = 0
nNeedPosState = 0   # 盾姿态


def Apply(player: Player, target: Target):
    return 1




default = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)