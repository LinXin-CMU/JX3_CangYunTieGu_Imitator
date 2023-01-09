# coding: utf-8
# author: LinXin

from scripts.Default import *

tSkillData = {
    1: damage_data(nDamageBase=0, nDamageRand=0, nAttackRate=0, nWeaponDamagePercent=0),
}

tSkillCoolDown = {
    1: cooldown_data(nSingleCoolDown=0, nMaxStackNum=1),
}

tSkillName = '初始化团队增益'
tDesc = '团队增益初始化母技能'
nNeedGcdType = []
nNeedMinRage = 0
nNeedPosState = None


def Apply(player: Player, target: Target, dwSkillLevel):

    # 破风
    if player.GetTeamMateTalent(18872):
        target.AddBuff(12717, 1)
    elif player.GetTeamMateTalent(403):
        target.AddBuff(661, 1)

    # 撼如雷
    if player.GetTeamMateTalent(404):
        player.AddBuff(362, 1)

    # 鼓
    if player.GetTeamMateTalent(15115):
        player.CastSkill(15115, 1)

    # 乘龙箭
    if player.GetTeamMateTalent(2603):
        player.CastSkill(2603, 1)

    # 舍身弘法
    if player.GetTeamMateTalent(15195):
        player.AddBuff(50029, 1)

    # 朝圣言
    if player.GetTeamMateTalent(3985):
        player.CastSkill(3985, 1)

    # 戒火斩
    if player.GetTeamMateTalent(3980):
        target.AddBuff(4058, 1)

    # 振奋
    if player.GetTeamMateTalent(50012):
        player.CastSkill(50012, 1)

    # 寒啸千军
    if player.GetTeamMateTalent(50013):
        player.CastSkill(50013, 1)

    # 虚弱
    if player.GetTeamMateTalent(50014):
        target.AddBuff(50034, 1)

    # 秋肃
    if player.GetTeamMateTalent(31208):
        target.AddBuff(23305, 1)
        target.DelBuff(4058)

    # 袖气
    if player.GetTeamMateTalent(545):
        player.AddBuff(673, 1)

    # 左旋右转
    if player.GetTeamMateTalent(567):
        player.AddBuff(20938, 1)

    # 泠风解怀
    if player.GetTeamMateTalent(30850):
        player.CastSkill(30850, 1)

    # 仙王蛊鼎
    if player.GetTeamMateTalent(2234):
        player.CastSkill(2234, 1)

    # 梅花三弄
    if player.GetTeamMateTalent(14071) or player.GetTeamMateTalent(23826):
        player.CastSkill(14071, 1)

    # 香稠
    if player.GetTeamMateTalent(28650):
        player.AddBuff(20841, 1)

    # 配伍
    if player.GetTeamMateTalent(28772) and not player.GetTeamMateTalent(28650):
        for _ in range(5):
            player.AddBuff(20877, 1)

    # 飘黄
    if player.GetTeamMateTalent(28678):
        player.CastSkill(28678, 1)

    # 落子无悔
    if player.GetTeamMateTalent(32381):
        player.CastSkill(32381, 1)


    return 1


AdvanceInit = skill_script(tSkillData, tSkillCoolDown, tSkillName, tDesc, nNeedGcdType, nNeedMinRage, nNeedPosState,
                          Apply)