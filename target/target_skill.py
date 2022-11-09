# coding: utf-8
# author: LinXin

from settings.jx3_types import *

# ————————————————————技能部分————————————————————
# 建立变量名和技能脚本的关系

skill_id_to_script: Dict[int, skill_script[Union[damage_data, cooldown_data, int, str]]] = {
}