# coding: utf-8
# author: LinXin

from typing import Dict, Union

from jx3_types import *
import scripts


# ————————————————————技能部分————————————————————
# 建立变量名和技能脚本的关系

skill_id_to_script: Dict[int, skill_script[Union[damage_data, cooldown_data, int, str]]] = {
}