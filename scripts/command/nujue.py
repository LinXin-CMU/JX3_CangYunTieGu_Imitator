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


tSkillName = '宏_怒绝'
tDesc = '怒绝宏实际内容'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None



def Apply(player: Player, target: Target, dwSkillLevel):
    
    player.CastSkill(13045, 1)  # /cast 盾压

    if not (player.IsHaveBuff(8499) or player.IsHaveBuff(8448)):
        player.CastSkill(13046, 1)  # /cast [nobuff:盾挡] 盾猛

    if player.rage > 80 and True:
        player.CastSkill(25213, 1)  # /cast 断马摧城

    player.CastSkill(13047, 1)  # /cast 盾击
    player.CastSkill(13044, 1)  # /cast 盾刀

    if player.rage == 110:
        player.CastSkill(13391, 1)  # /cast [rage>109] 盾挡

    if player.rage >= 65 and (player.IsHaveBuff(8499) or player.IsHaveBuff(8448)):
        player.CastSkill(13050, 1)  # /cast [rage>=65&buff:盾挡] 盾飞

    if player.GetSkillCoolDown(13054) > 0 and player.GetSkillCoolDown(13055) > 0:
        player.CastSkill(13051, 1)  # /cast [bufftime:盾飞<9] 盾回

    player.CastSkill(13054, 1)  # /cast 斩刀

    if player.IsHaveBuff(24755):
        player.CastSkill(13055, 1)  # /cast [buff:24755] 绝刀

    player.CastSkill(13052, 1)  # /cast 劫刀

    if not player.IsHaveBuff(8245) and (
            player.IsHaveBuff(8499) or player.IsHaveBuff(8448)) and player.rage < 50:
        player.CastSkill(13040, 1)
   
    return 1


nujue = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)




