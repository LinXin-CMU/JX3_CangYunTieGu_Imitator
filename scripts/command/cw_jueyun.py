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


tSkillName = '宏_橙武绝云'
tDesc = '橙武绝云宏实际内容'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None



def Apply(player: Player, target: Target, dwSkillLevel):

    if player.GetSkillLevel("愤恨") == 1:
        buff_xn = player.GetBuff(8385)
    else:
        buff_xn = player.GetBuff(8244)

    buff_cw = False
    buff_xr = target.GetBuff(8248)
    buff_fy = player.GetBuff(17176)

    cd_dunji = player.GetSkillCoolDown(13047)
    if player.GetBuff(14309).lasting > 54*16 or buff_xn.lasting == 0:
        player.CastSkill(13040, 1)
    if buff_cw or 0 < player.GetBuff(8451).lasting < 1*16:
        player.CastSkill(13055, 1)
    if buff_xr.lasting > 0 and not player.IsHaveBuff(22976) and not player.IsHaveBuff(22977):
        player.CastSkill(30769, 1)
    if buff_xr.lasting > 0:
        player.CastSkill(13054, 1)
    if target.IsHaveBuff(8249) and not target.IsHaveBuff(21308) and player.rage >= 25:
        player.CastSkill(13053, 1)
    if player.IsHaveBuff(22976):
        player.CastSkill(30769, 1)
    if player.IsHaveBuff(22977):
        player.CastSkill(30769, 1)
    if player.IsHaveBuff(8451) or buff_fy.lasting > 8*16:
        player.CastSkill(13055, 1)
    player.CastSkill(13052, 1)
    if player.rage >= 25 and buff_cw:
        player.CastSkill(13050, 1)
    if player.rage >= 30 and (buff_fy.lasting < 8*16 or cd_dunji > 4*2*16):
        player.CastSkill(13050, 1)
    if buff_cw or cd_dunji > 4*2*16:
        player.CastSkill(13045, 1)
    player.CastSkill(13047, 1)
    player.CastSkill(13044, 1)
    if player.rage < 10:
        player.CastSkill(13051, 1)

    return 1


cw_jueyun = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)




