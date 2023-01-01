# coding: utf-8
# author: LinXin

from scripts.Default import *
from scripts.include.slot import attrib_data


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '自身被击子技能'
tDesc = '自身被击后触发效果脚本'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    # 是否招架的判定
    fParry = player.ParryPercent

    if random.randint(1, 10000) <= fParry * 10000:
        nFlag = 1
    else:
        nFlag = 0

    # 招架后加寒甲buff
    if not player.GetSetting('ParryByExpect'):
        if nFlag and player.GetSkillLevel('寒甲') == 1:
            player.CastSkill(13135, 1)
    else:
        # 寒甲在招架之后，因此累计概率会包含自身这次
        player.SetExpectParry(fParry)
        if player.GetSkillLevel('寒甲') == 1:
            player.CastSkill(13135, 1)

    # 坚铁buff判定
    if player.GetSkillLevel('坚铁') == 1:
        if player.GetSetting('ParryByExpect'):
            player.DelBuff(8272)
            fLayerExpect = player.GetJianTieExpectByParry(player.ParryPercent)
            player.AddBuff(8272, 1, attrib=[attrib_data('atParryBaseRate', fLayerExpect * (60 / 1024))])
        else:
            player.CastSkill(13139, 1)
            if nFlag:
                player.CastSkill(13140, 1)

    # 崇云buff判定
    if player.GetSkillLevel('崇云') == 1:
        player.CastSkill(21749, 1)

    # 被击后加铁骨气劲
    if player.GetSetting('QiJin'):
        player.CastSkill(50005, 1)

    return 1



BeAttacked = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)