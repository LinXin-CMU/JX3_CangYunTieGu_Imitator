# coding: utf-8
# author: LinXin
from collections import namedtuple
from typing import List, Dict, Union


skill_script = namedtuple('skill_script', ['tSkillData', 'tSkillCoolDown', 'tSkillName', 'tDesc', 'nNeedGcdType', 'nNeedMinRage', 'nNeedPosState', 'Apply'])

damage_data = namedtuple('skill_damage', ['nDamageBase', 'nDamageRand', 'nAttackRate', 'nWeaponDamagePercent'])

cooldown_data = namedtuple('cooldown_data', ['nSingleCoolDown', 'nMaxStackNum'])

buff = namedtuple('buff', ['id', 'level', 'layer', 'desc', 'lasting', 'script', 'attrib'])

GCD_TYPE = {
    0: 'normal_24',     # 常规1.5s
    1: 'normal_16',     # 常规1s
    2: 'dundang_8',     # 盾挡进入的0.5s
    3: 'hanxiao_0',     # 寒啸进入的0s
    4: 'dundao_0',      # 盾刀234段进入的0s
    5: 'xuedao_8',      # 血刀进入的0.5s
    6: 'dunfei_16',     # 盾飞自身1s
    7: 'xuenu_8',       # 血怒自身0.5s
}


class Target:
    casted: List
    buffs: Dict[int, buff]
    talents: List
    recipes: List
    level: int
    # 攻击频率
    attack_cooldown: int
    attack_per_count: int
    def __init__(self, talents: list, recipes: list): ...
    # ————————————————————怒气部分————————————————————
    @property
    def rage(self): return ...
    @rage.setter
    def rage(self, value): ...
    # ————————————————————属性部分————————————————————
    @property
    def PhysicsShieldValue(self): ...
    def GetPhysicsShieldPercent(self, value): ...

    # ————————————————————技能部分————————————————————

    def CastSkill(self, skill_id, skill_level):
        """
        :param skill_id:
        :param skill_level:
        :return:
        """

    def GetSkillLevel(self, skill_id):
        """
        :param skill_id:
        :return:
        """

    def IsSkillRecipeActive(self, recipe_id, recipe_level):
        """
        :param recipe_id:
        :param recipe_level:
        :return:
        """
        pass

    # ————————————————————气劲部分————————————————————
    def AddBuff(self, buff_id, level, desc=None, lasting=None):
        """
        :param buff_id:
        :param level:
        :param desc:
        :param lasting:
        :return:
        """

    def IsHaveBuff(self, buff_id, buff_level=None) -> Union[buff, None]:
        """
        :param buff_id:
        :param buff_level:
        :return:
        """

    def GetBuff(self, buff_id, buff_level=None) -> buff:
        """
        :param buff_id:
        :param buff_level:
        :return:
        """

    def DelBuff(self, buff_id, buff_level=None, all_layer=False):
        """
        :param all_layer:
        :param buff_id:
        :param buff_level:
        :return:
        """
    # ————————————————————时间部分————————————————————

    def Timer(self):
        """
        :return:
        """

    def AddSkillCoolDown(self, skill_id, period):
        """
        :param skill_id:
        :param period:
        :return:
        """

    def AddPublicCoolDown(self, cooldown_type, period):
        """
        GCD_TYPE = {\n
        0: 'normal_24',     # 常规1.5s\n
        1: 'normal_16',     # 常规1s\n
        2: 'dundang_8',     # 盾挡进入的0.5s\n
        3: 'hanxiao_0',     # 寒啸进入的0s\n
        4: 'dundao_0',      # 盾刀234段进入的0s\n
        5: 'xuedao_8',      # 血刀进入的0.5s\n
        6: 'dunfei_16',     # 盾飞自身1s\n
        7: 'xuenu_8',       # 血怒自身0.5s\n
    }\n
        :param cooldown_type:
        :param period:
        :return:
        """

    def ClearCDTime(self, skill_id, period=None):
        """
        :param skill_id:
        :param period:
        :return:
        """


class Player:
    casted: List
    damage: int
    buffs: Dict[int, buff]
    talents: List
    recipes: List
    life: float
    level: int
    settings: Dict[str, int]
    def __init__(self, talents: list, recipes: list, target: Target): ...
    # ————————————————————怒气部分————————————————————
    @property
    def rage(self): return ...
    @rage.setter
    def rage(self, value): ...
    # ————————————————————属性部分————————————————————
    @property
    def Vitality(self): return ...
    @property
    def PhysicsAttackPower(self): return ...
    @property
    def PhysicsCriticalPercent(self): return ...
    @property
    def PhysicsCriticalDamagePowerPercent(self): return ...
    @property
    def OvercomePercent(self): return ...
    @property
    def StrainPercent(self): return ...
    @property
    def SurplusValue(self): return ...
    @property
    def HastePercent(self): return ...
    @property
    def HasteValueGuo(self): return ...
    @property
    def ParryPercent(self): return ...
    @property
    def ParryPercentValue(self): return ...
    @property
    def ParryValue(self): return ...
    @property
    def WeaponDamage(self): return ...
    @property
    def WeaponAttackSpeed(self): return ...

    def SetSnapShot(self, skill_id):
        """
        # 记录攻击，会心，会效，无双，增伤
        :param skill_id:
        :return:
        """

    def GetSnapShot(self, skill_id): ...
    # ————————————————————技能部分————————————————————

    def CastSkill(self, skill_id, skill_level):
        """
        :param skill_id:
        :param skill_level:
        :return:
        """

    def GetSkillLevel(self, skill_id):
        """
        :param skill_id:
        :return:
        """

    def SetSkillRecipeActive(self, recipe_id, isActive=True):
        """
        :param recipe_id:
        :param isActive:
        :return:
        """

    def IsSkillRecipeActive(self, recipe_id):
        """
        :param recipe_id:
        :return:
        """
        pass

    # ————————————————————气劲部分————————————————————
    def AddBuff(self, buff_id, level, desc=None, lasting=None, attrib=None):
        """
        :param buff_id:
        :param level:
        :param desc:
        :param lasting:
        :param attrib:
        :return:
        """

    def IsHaveBuff(self, buff_id, buff_level=None) -> Union[buff, None]:
        """
        :param buff_id:
        :param buff_level:
        :return:
        """

    def GetBuff(self, buff_id, buff_level=None) -> buff:
        """
        :param buff_id:
        :param buff_level:
        :return:
        """

    def DelBuff(self, buff_id, buff_level=None, all_layer=False):
        """
        :param all_layer:
        :param buff_id:
        :param buff_level:
        :return:
        """
    # ————————————————————时间部分————————————————————

    def Timer(self):
        """
        :return:
        """

    def AddSkillCoolDown(self, skill_id, period):
        """
        :param skill_id:
        :param period:
        :return:
        """

    def GetSkillCoolDown(self, skill_id) -> Union[int, None]:
        """
        :param skill_id:
        :return:
        """

    def AddPublicCoolDown(self, cooldown_type, period):
        """
        GCD_TYPE = {\n
        0: 'normal_24',     # 常规1.5s\n
        1: 'normal_16',     # 常规1s\n
        2: 'dundang_8',     # 盾挡进入的0.5s\n
        3: 'hanxiao_0',     # 寒啸进入的0s\n
        4: 'dundao_0',      # 盾刀234段进入的0s\n
        5: 'xuedao_8',      # 血刀进入的0.5s\n
        6: 'dunfei_16',     # 盾飞自身1s\n
        7: 'xuenu_8',       # 血怒自身0.5s\n
    }\n
        :param cooldown_type:
        :param period:
        :return:
        """

    def ClearCDTime(self, skill_id, period=None):
        """
        :param skill_id:
        :param period:
        :return:
        """

    def GetSetting(self, slot):
        """
        :param slot:
        :return:
        """

