# coding: utf-8
# author: LinXin
# 用于计算有内置cd的效果的概率触发事件

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}


tSkillName = '宏_橙武双绝'
tDesc = '橙武双绝宏实际内容'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None



def Apply(player: Player, target: Target, dwSkillLevel):

    buff_zy = player.GetBuff(50025)
    buff_hj = player.GetBuff(8437)

    if player.GetSkillLevel('千山') == 1:
        buff_dd = player.GetBuff(8448)
    else:
        buff_dd = player.GetBuff(8499)

    cd_duanma = player.GetSkillCoolDown(25213)
    cd_juedao = player.GetSkillCoolDown(13055)
    cd_dunfei = player.GetSkillCoolDown(13050)

    if buff_zy.lasting > 0 and cd_juedao > 1*16 and buff_dd.lasting == 0:
        player.CastSkill(13051, 1)
    if buff_zy.lasting == 0 and 1*16 < cd_juedao and player.GetSkillCoolDown(13054) > 1*16:
        player.CastSkill(13051, 1)
    if player.rage < 5:
        player.CastSkill(13051, 1)
    if cd_juedao < 1.5*16 and buff_hj.lasting > 0:
        player.CastSkill(13054, 1)
    if player.IsHaveBuff(24755) and buff_hj.lasting > 0:
        player.CastSkill(13055, 1)
    if cd_juedao >= 1.5*16:
        player.CastSkill(13052, 1)
    if buff_zy.lasting > 0 and buff_dd.lasting > 9.5*16:
        player.CastSkill(13050, 1)
    if player.rage >= 65 and cd_juedao < 1.5*16 and cd_duanma > 3*16:
        player.CastSkill(13050, 1)
    if player.rage >= 110 and (buff_zy.lasting > 0):
        player.CastSkill(13391, 1)
    if (buff_hj.lasting > 0 and player.rage >= 90) or (buff_zy.lasting > 0 and player.rage >= 110):
        player.CastSkill(25213, 1)
    if player.rage < 105:
        player.CastSkill(13045, 1)
    if player.rage <= 95:
        player.CastSkill(13046, 1)
    if player.rage < 105 or cd_dunfei >= 5*16:
        player.CastSkill(13047, 1)
    player.CastSkill(13044, 1)
    if player.rage <= 90 and player.GetSkillCoolDown(13040) <= 25*2*16 and cd_duanma < 2*16:
        player.CastSkill(13040, 1)
    if player.rage <= 70 and player.GetSkillCoolDown(13046) > 8*16:
        player.CastSkill(13040, 1)
    if player.GetSkillLevel("鸿烈"):
        player.CastSkill(26897, 1)


    return 1


cw_shuangjue = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)




