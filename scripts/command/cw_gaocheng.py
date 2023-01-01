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
    buff_yz = player.GetBuff(18222)
    buff_ny = player.GetBuff(8276)

    if player.GetSkillLevel('高城') == 1:
        buff_tg = player.GetBuff(17886)
    else:
        buff_tg = player.GetBuff(17885)

    cd_duanma = player.GetSkillCoolDown(25213)
    cd_juedao = player.GetSkillCoolDown(13055)
    cd_dunfei = player.GetSkillCoolDown(13050)

    if player.rage < 5 or buff_yz.lasting < 2*16 or buff_ny.lasting < 2*16:
        player.CastSkill(13051, 1)
    if cd_juedao < 1.5*16:
        player.CastSkill(13054, 1)
    if player.IsHaveBuff(24755):
        player.CastSkill(13055, 1)
    if cd_juedao > 1.5*16 or buff_zy.lasting == 0 and (player.rage >= 70 or player.rage < 10):
        player.CastSkill(13052, 1)
    if buff_zy.lasting > 0 and buff_yz.layer == 5 and buff_yz.lasting > 2*16:
        player.CastSkill(13052, 1)
    if player.rage >= 90 and buff_tg.layer > 10:
        player.CastSkill(25213, 1)
    if player.rage >= 75 and cd_juedao < 3*16 and buff_yz.lasting > 2*16 and cd_duanma > 3*16:
        player.CastSkill(13050, 1)
    player.CastSkill(13045, 1)
    if player.rage <= 85 and cd_duanma > 15*16:
        player.CastSkill(13046, 1)
    player.CastSkill(13047, 1)
    player.CastSkill(13044, 1)
    if player.rage <= 90 and player.GetSkillCoolDown(13040) <= 25*2*16 and cd_duanma < 2*16:
        player.CastSkill(13040, 1)
    if player.rage <= 70 and player.GetSkillCoolDown(13046) > 8*16:
        player.CastSkill(13040, 1)
    if player.GetSkillLevel("鸿烈"):
        player.CastSkill(26897, 1)

    return 1


cw_gaocheng = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)




