# coding: utf-8
# author: LinXin

from scripts.Default import *


tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0)
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1)
}

tSkillName = '怒炎消失绝刀走cd'
tDesc = '怒炎消失子技能'
nNeedGcdType = []
nNeedPosState = None


def Apply(player: Player, target: Target):
    if not player:
        return

    if player.GetSkillLevel('#怒炎') == 1 and not player.IsHaveBuff(24756):
        # 怒炎重置绝刀被消耗时，要检测绝刀是否进cd，若未进cd则要手动添加cd
        if not player.GetSkillCoolDown(13055):
            # 绝刀进cd
            cd_juedao = 10
            if player.IsSkillRecipeActive('#绝刀减cd1s', 1):
                cd_juedao -= 1
            if player.IsSkillRecipeActive('#绝刀减cd2s', 1):
                cd_juedao -= 2
            player.AddSkillCoolDown(13055, cd_juedao)

    return 1






NuYanDisappear = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState, Apply)