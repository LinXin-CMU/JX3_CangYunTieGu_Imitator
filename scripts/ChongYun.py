# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '崇云删buff'
tDesc = '崇云_被击加血怒时间子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target):

    if player.IsHaveBuff(50009):
        # 删一层崇云buff
        player.DelBuff(50009)

        # 加血怒持续时间
        if player.GetSkillLevel('#愤恨') == 1:
            buff_xn = player.GetBuff(8386)
            buff_xn_id = 8386
        else:
            buff_xn = player.GetBuff(8245)
            buff_xn_id = 8245

        player.DelBuff(buff_xn_id)
        for _ in range(buff_xn.layer):
            player.AddBuff(buff_xn_id, buff_xn.level, lasting=buff_xn.lasting)

    return 1


ChongYun = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)