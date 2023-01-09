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


tSkillName = '宏_橙武千血'
tDesc = '橙武千血宏实际内容'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None



def Apply(player: Player, target: Target, dwSkillLevel):

    buff_zy = player.GetBuff(50025)
    buff_gy = player.GetBuff(50043)
    # buff_hj = player.GetBuff(8437)
    buff_gl = target.GetBuff(21308)
    buff_lx = target.GetBuff(8249)

    if player.GetSkillLevel('千山') == 1:
        buff_dd = player.GetBuff(8448)
    else:
        buff_dd = player.GetBuff(8499)

    if player.GetSkillLevel("愤恨") == 1:
        buff_xn = player.GetBuff(8386)
    else:
        buff_xn = player.GetBuff(8245)

    # cd_duanma = player.GetSkillCoolDown(25213)
    cd_juedao = player.GetSkillCoolDown(13055)
    cd_zhandao = player.GetSkillCoolDown(13054)
    # cd_dunfei = player.GetSkillCoolDown(13050)

    if buff_zy.lasting > 0 and buff_dd.lasting < 1*16:
        player.CastSkill(13051, 1)
    if buff_zy.lasting == 0 and cd_zhandao > 1*16 and cd_juedao > 1*16 and (buff_gl.lasting > 1*16 or (player.rage < 15 and buff_gl.lasting == 0)):
        player.CastSkill(13051, 1)
    if buff_zy.lasting == 0 and cd_zhandao > 1*16 and (cd_juedao > 1*16 or player.rage < 10):
        player.CastSkill(13051, 1)
    if buff_zy.lasting == 0 and player.rage < 5:
        player.CastSkill(13051, 1)
    if buff_lx.lasting < 1.5*16:
        player.CastSkill(13054, 1)
    if buff_gy.lasting > 0 and player.rage >= 50:
        player.CastSkill(13055, 1)
    if buff_dd.lasting > 0:
        player.CastSkill(13054, 1)
    if buff_gl.lasting == 0 and buff_dd.lasting > 0:
        player.CastSkill(13053, 1)
    if buff_gl.lasting > 0 and buff_lx.lasting > 1.5*16 and buff_dd.lasting > 0:
        player.CastSkill(13055, 1)
    if buff_zy.lasting > 0 and buff_dd.lasting > 2*16:
        player.CastSkill(13052, 1)
    if buff_zy.lasting > 0 and buff_dd.lasting > 8*16:
        player.CastSkill(13050, 1)
    if player.rage >= 25 and buff_dd.lasting > 0 and not player.IsHaveBuff(8424) and buff_gl.lasting > 0 and cd_zhandao == 0:
        player.CastSkill(13050, 1)
    if player.rage >= 40 and buff_gl.lasting == 0 and not player.IsHaveBuff(8424) and buff_dd.lasting > 0 and cd_zhandao == 0:
        player.CastSkill(13050, 1)
    if buff_gy.lasting > 0 and player.rage >= 50:
        player.CastSkill(13050, 1)
    if player.rage < 105:
        player.CastSkill(13045, 1)
    if player.rage < 105:
        player.CastSkill(13047, 1)
    player.CastSkill(13044, 1)
    if player.rage >= 110 and (buff_zy.lasting > 0 or player.IsHaveBuff(8424)):
        player.CastSkill(13391, 1)
    if player.rage >= 110 and buff_dd.lasting < 1*16:
        player.CastSkill(13391, 1)
    if buff_gy.lasting > 0 and 50 > player.rage >= 40:
        player.CastSkill(13040, 1)
    if buff_dd.lasting >= 9*16 and buff_xn.lasting == 0:
        player.CastSkill(13040, 1)
    if player.GetSkillLevel("鸿烈"):
        player.CastSkill(26897, 1)

    return 1


cw_qianxue = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)




