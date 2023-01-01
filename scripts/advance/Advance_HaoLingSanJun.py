# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '号令三军'
tDesc = '号令三军子技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


nGuCount = 1
bCanCast = True


def Apply(player: Player, target: Target, dwSkillLevel):

    nStackNum = player.GetTeamMateAdvanceStackNum(15115)
    if not nStackNum:
        return

    global nGuCount, bCanCast

    if nGuCount == 1:
        for _ in range(nStackNum):
            player.AddBuff(23107, 1)
        nGuCount = 2
        bCanCast = False

    elif nGuCount == 2:
        for _ in range(nStackNum // 2):
            player.AddBuff(23107, 1)
        nGuCount = 3

    elif nGuCount == 3:
        player.AddBuff(10175, 1)
        nGuCount = 1

    return 1


def ResetState():
    global nGuCount, bCanCast
    nGuCount = 1
    bCanCast = True


Advance_HaoLingSanJun = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)