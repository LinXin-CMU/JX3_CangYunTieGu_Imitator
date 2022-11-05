# coding: utf-8
# author: LinXin

from typing import Dict, Union

from jx3_types import *
import scripts


# ————————————————————技能部分————————————————————
# 建立变量名和技能脚本的关系

skill_id_to_script: Dict[int, skill_script[Union[damage_data, cooldown_data, int, str]]] = {
    13044: scripts.DunDao,
    13045: scripts.DunYa,
    13046: scripts.DunMeng,
    13047: scripts.DunJi,
    13059: scripts.DunDao_2,
    13060: scripts.DunDao_3,
    13119: scripts.DunDao_4,
    13316: scripts.DunFeiAttack,
    13352: scripts.DunFeiChangeState,
    13391: scripts.DunDang,
    13540: scripts.DunFeiAddXuRuo,
}