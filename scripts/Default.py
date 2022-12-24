# coding: utf-8
# author: LinXin

from settings.jx3_types import skill_script, damage_data, cooldown_data, Player, Target
import random
from scripts.include.buff import buff_data
from scripts.include.slot import _attrib_data

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '默认技能'
tDesc = '默认的技能脚本'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    return 1



Default = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)