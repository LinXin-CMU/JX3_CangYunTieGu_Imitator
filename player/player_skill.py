# coding: utf-8
# author: LinXin

from settings.jx3_types import *
import scripts


# ————————————————————技能部分————————————————————
# 建立变量名和技能脚本的关系

skill_id_to_script: Dict[int, skill_script[Union[damage_data, cooldown_data, int, str]]] = {
    13039: scripts.JuanXueDao,
    13040: scripts.XueNu,
    13044: scripts.DunDao,
    13045: scripts.DunYa,
    13046: scripts.DunMeng,
    13047: scripts.DunJi,
    13050: scripts.DunFei,
    13051: scripts.DunHui,
    13052: scripts.JieDao,
    13053: scripts.ShanDao,
    13054: scripts.ZhanDao,
    13055: scripts.JueDao,
    13059: scripts.DunDao_2,
    13060: scripts.DunDao_3,
    13119: scripts.DunDao_4,
    13127: scripts.LianZhan,
    13128: scripts.LianZhanStop,
    13135: scripts.HanJia,
    13139: scripts.JianTie,
    13140: scripts.JianTieStop,
    13164: scripts.DunDao_ChuChen,
    13316: scripts.DunFeiAttack,
    13352: scripts.DunFeiChangeState,
    13391: scripts.DunDang,
    13540: scripts.DunFeiAddXuRuo,
    21749: scripts.ChongYun,
    25213: scripts.DuanMaCuiCheng,
    25215: scripts.DuanMaCuiChengDamage,
    32745: scripts.PoZhao,

    # 以下是自定义技能
    50000: scripts.BeAttacked,
    50001: scripts.LiuXueInterval_1,
    50002: scripts.LiuXueInterval_2,
    50003: scripts.LiuXueInterval_3,
    50004: scripts.LiuXueInterval_4,
    50005: scripts.TieGu,
}
