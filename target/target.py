# coding: utf-8
# author: LinXin

from settings.jx3_types import *
from .target_attribute import Attribute
from .target_skill import skill_id_to_script
from scripts.include.buff import buff_data
import scripts

from typing import Dict, Union


class Target:

    def __init__(self):
        # ————————————————————怒气部分————————————————————
        self._rage = 0

        self.casted = None
        self._damage = 0
        # ————————————————————属性部分————————————————————
        self._attribute = Attribute(self)

        # ————————————————————气劲部分————————————————————
        self.buffs: Dict[int, buff] = {
        }
        # ————————————————————技能部分————————————————————
        # self.talents = talents
        # self.recipes = recipes
        # ————————————————————技能cd部分————————————————————
        self._cooldown = {
        }
        self.gcd_list = {
            0: 0,  # 'normal_24',  # 常规1.5s
            1: 0,  # 'normal_16',  # 常规1s
            2: 0,  # 'dundang_8',  # 盾挡进入的0.5s
            3: 0,  # 'hanxiao_0',  # 寒啸进入的0s
            4: 0,  # 'dundao_0',  # 盾刀234段进入的0s
            5: 0,  # 'xuedao_8',  # 血刀进入的0.5s
            6: 0,  # 'dunfei_16',  # 盾飞自身1s
            7: 0,  # 'xuenu_8',  # 血怒自身0.5s
        }
        # 当前时间
        self._timer = -1

        # ————————————————————体态部分————————————————————
        self.level = None
        #
        self.player = None

        # ————————————————————环境部分————————————————————
        self.settings = {
            'QiJin': 0,
            'CriticalByExpect': 0,
            'AttackFreq': 0,
            'AttackCount': 0,
            'Halo': None,
        }

    # ————————————————————怒气部分————————————————————

    # @property
    # def rage(self):
    #     return self._rage
    #
    # @rage.setter
    # def rage(self, value):
    #     assert False

    # ————————————————————属性部分————————————————————
    # @property
    # def Vitality(self):
    #     return self._attribute.Vitality
    #
    # @property
    # def PhysicsAttackPower(self):
    #     return self._attribute.PhysicsAttackPower
    #
    # @property
    # def PhysicsCriticalPercent(self):
    #     return self._attribute.PhysicsCriticalPercent
    #
    # @property
    # def PhysicsCriticalDamagePowerPercent(self):
    #     return self._attribute.PhysicsCriticalDamagePowerPercent
    #
    # @property
    # def OvercomePercent(self):
    #     return self._attribute.OvercomePercent
    #
    # @property
    # def StrainPercent(self):
    #     return self._attribute.StrainPercent
    #
    # @property
    # def SurplusValue(self):
    #     return self._attribute.SurplusValue
    #
    # @property
    # def HastePercent(self):
    #     return self._attribute.HastePercent
    #
    # @property
    # def ParryPercent(self):
    #     return self._attribute.ParryPercent
    #
    # @property
    # def ParryPercentValue(self):
    #     return self._attribute.ParryPercentValue
    #
    # @property
    # def ParryValue(self):
    #     return self._attribute.ParryValue

    @property
    def PhysicsShieldValue(self):
        return self._attribute.PhysicsShieldValue

    @property
    def PhysicsDamageCoefficient(self):
        return self._attribute.PhysicsDamageCoefficient

    def GetPhysicsShieldPercent(self, value):
        return self._attribute.GetPhysicsShieldPercent(value)

    def SetNpcAttributeValueByLevel(self):
        self._attribute.SetNpcAttributeValueByLevel()


    # ————————————————————技能部分————————————————————

    def CastSkill(self, skill_id, skill_level):
        # 1. 获取到对应脚本
        # 2. 执行对应脚本的Apply方法
        # 3. 检查释放结果，记录释放信息

        # 技能效果
        if skill_id in skill_id_to_script:
            _skill = skill_id_to_script[skill_id]
        elif isinstance(skill_id, str):
            if hasattr(scripts, skill_id):
                _skill = getattr(scripts, skill_id)
                if not _skill:
                    return
            else:
                return
        else:
            return

        # 检查gcd
        gcd_type_list = _skill.nNeedGcdType
        for gcd_type in gcd_type_list:
            if gcd_type not in self.gcd_list:
                return
            if self.gcd_list[gcd_type] > 0:
                return

        # 检查cd
        cd_data: cooldown_data = _skill.tSkillCoolDown
        if skill_level not in cd_data:
            return
        cd_data = cd_data[skill_level]

        if skill_id in self._cooldown:
            max_cd = cd_data.nMaxStackNum * cd_data.nSingleCoolDown
            if not max_cd:
                return
            # 检查现有cd+一层cd是否大于总cd, 若为否则可以施展
            if self._cooldown[skill_id] + cd_data.nSingleCoolDown > max_cd:
                return

        # 检查怒气需求
        # if self._rage < _skill.nNeedMinRage:
        #     return

        # 检查体态
        # if self.IsHaveBuff(8277):
        #     n_state = 0
        # else:
        #     n_state = 1
        # if _skill.nNeedPosState != n_state:
        #     return

        if not self.player:
            return
        state = _skill.Apply(self.player, self, skill_level)
        # 技能伤害
        if state:
            self._damage += state
            # 记录技能
            if self.casted is None:
                self.casted = [{'frame': self._timer, 'name': _skill.tSkillName, 'desc': _skill.tDesc}]
            else:
                self.casted.append({'frame': self._timer, 'name': _skill.tSkillName, 'desc': _skill.tDesc})

    def GetSkillLevel(self, skill_id):
        """
        :param skill_id:
        :return:
        """
        pass

    def IsSkillRecipeActive(self, recipe_id, recipe_level):
        """
        :param recipe_id:
        :param recipe_level:
        :return:
        """
        pass

    # ————————————————————气劲部分————————————————————

    def AddBuff(self, buff_id, level, desc=None, lasting=None, attrib=None):
        """
        :param attrib:
        :param buff_id:
        :param level:
        :param desc:
        :param lasting:
        :return:
        """
        if not buff_id:
            return
        if buff_id not in buff_data:
            return
        else:
            _buff_data = buff_data[buff_id]

        if lasting is None:
            lasting = _buff_data.nMaxTime
        if desc is None:
            desc = _buff_data.Desc
        if attrib is None:
            attrib = _buff_data.Attrib

        if buff_id in self.buffs:
            _buff: buff = self.buffs.get(buff_id)
            if level < _buff.level:
                return
            if level == _buff.level:
                layer = _buff.layer + 1
                self.buffs[buff_id] = buff(buff_id, level, min(_buff_data.nMaxStackNum, layer), desc, lasting, _buff.script, _buff.attrib)
                return
            # 等级大于的情况
            self.buffs[buff_id] = buff(buff_id, level, 1, desc, lasting, _buff.script, _buff.attrib)

        else:
            self.buffs[buff_id] = buff(buff_id, level, 1, desc, lasting, _buff_data.Script, attrib)


    def IsHaveBuff(self, buff_id, buff_level=None) -> Union[buff, None]:
        """
        :param buff_id:
        :param buff_level:
        :return:
        """
        if not buff_id:
            return
        if buff_id not in self.buffs:
            return

        _buff = self.buffs[buff_id]
        if buff_level is not None:
            if _buff.level == buff_level:
                return _buff
            else:
                return
        else:
            return _buff

    def GetBuff(self, buff_id, buff_level=None) -> buff:
        """
        :param buff_id:
        :param buff_level:
        :return:
        """
        if not buff_id:
            return buff(0, 0, 0, '', 0, None, None)
        if buff_id not in self.buffs:
            return buff(0, 0, 0, '', 0, None, None)

        _buff = self.buffs[buff_id]
        if buff_level is not None:
            if _buff.level == buff_level:
                return _buff
            else:
                return buff(0, 0, 0, '', 0, None, None)
        else:
            return _buff

    def DelBuff(self, buff_id, buff_level=None, all_layer=False):
        """
        :param all_layer:
        :param buff_id:
        :param buff_level:
        :return:
        """
        if not buff_id:
            return
        if buff_id not in self.buffs:
            return

        _buff = self.buffs[buff_id]
        if buff_level is not None and _buff.level == buff_level or buff_level is None:
            if all_layer:
                new_layer = 0
            else:
                new_layer = max(0, _buff.layer - 1)
            if not new_layer:
                del self.buffs[buff_id]
                return 1
            else:
                self.buffs[buff_id] = buff(_buff.id, _buff.level, new_layer, _buff.desc, _buff.lasting, _buff.script, _buff.attrib)
                return 1
        else:
            return

    # ————————————————————时间部分————————————————————

    def Timer(self, value: int):
        """
        :return:
        """
        # 更新时间，记录用
        nPassedTime = 0
        if value > self._timer:
            nPassedTime = value - self._timer
            self._timer = value
        else:
            return

        # 减cd
        _del = []
        for skill_id, skill_cd in self._cooldown.items():
            skill_cd -= nPassedTime
            if skill_cd > 0:
                self._cooldown[skill_id] = skill_cd
            else:
                _del.append(skill_id)
        for skill_id in _del:
            del self._cooldown[skill_id]

        # 减gcd
        for gcd_type, gcd_value in self.gcd_list.items():
            gcd_value -= nPassedTime
            if gcd_value > 0:
                self.gcd_list[gcd_type] = gcd_value
            else:
                self.gcd_list[gcd_type] = 0

        # 减buff持续时间
        _del = []
        for buff_id, _buff_data in self.buffs.items():
            new_lasting = max(_buff_data.lasting - nPassedTime, 0)
            if not new_lasting:
                _del.append(buff_id)
            else:
                self.buffs[buff_id] = buff(*_buff_data[:-3], new_lasting, *_buff_data[-2:])
        for buff_id in _del:
            _script = self.buffs[buff_id].script
            if _script is not None:
                self.CastSkill(_script, 1)
            # 技能脚本可能会删除buff, 这里再检查一次
            if buff_id in self.buffs:
                del self.buffs[buff_id]


    def AddSkillCoolDown(self, skill_id, period):
        """
        :param skill_id:
        :param period:
        :return:
        """
        if not period:
            return
        if not skill_id:
            return
        if skill_id not in self._cooldown:
            self._cooldown[skill_id] = period
        else:
            self._cooldown[skill_id] += period

    def AddPublicCoolDown(self, cooldown_type, period):
        """
        :param cooldown_type:
        :param period:
        :return:
        """
        if not period:
            return
        if cooldown_type not in GCD_TYPE:
            return
        self.gcd_list[cooldown_type] = period

    def ClearCDTime(self, skill_id, period=None):
        """
        :param skill_id:
        :param period:
        :return:
        """
        if not skill_id:
            return
        if skill_id not in self._cooldown:
            return
        else:
            cd = self._cooldown[skill_id]
            if period is None or cd <= period:
                del self._cooldown[skill_id]
            else:
                self._cooldown[skill_id] = cd - period

    # ————————————————————环境部分————————————————————
    def GetSetting(self, slot):
        """
        :param slot:
        :return:
        """
        if slot in self.settings:
            return self.settings[slot]
        else:
            return 0
