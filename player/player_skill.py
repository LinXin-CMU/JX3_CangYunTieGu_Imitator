# coding: utf-8
# author: LinXin

from settings.jx3_types import *
import scripts


# ————————————————————技能部分————————————————————
# 建立变量名和技能脚本的关系

skill_id_to_script: Dict[int, skill_script[Union[damage_data, cooldown_data, int, str]]] = {
    2234: scripts.Advance_XianWangGuDing,
    2603: scripts.Advance_ChengLongJian,
    3985: scripts.Advance_ChaoShengYan,
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
    14071: scripts.Advance_MeiHuaSanNong,
    15115: scripts.Advance_HaoLingSanJun,
    15195: scripts.Advance_SheShenHongFa,
    19409: scripts.DunYaDamage,
    21749: scripts.ChongYun,
    22122: scripts.Enchant_YuMao,
    22166: scripts.Enchant_ShangWan,
    22169: scripts.Enchant_ShangYao,
    25213: scripts.DuanMaCuiCheng,
    25215: scripts.DuanMaCuiChengDamage,
    26060: scripts.FeiJian_Dps_Active,
    26140: scripts.FeiJian_MT_Passive,
    26141: scripts.FeiJian_MT_Active,
    28678: scripts.Advance_PiaoHuang,
    29541: scripts.Advance_PiaoHuangDmg,
    29919: scripts.FeiJian_Dps_Passive,
    30850: scripts.Advance_LingFengJieHuai,
    32381: scripts.Advance_LuoZiWuHui,
    32745: scripts.PoZhao,
    33249: scripts.Enchant_YuWan,
    33257: scripts.Enchant_ShangXie,
    # 以下是自定义技能
    50000: scripts.BeAttacked,
    50001: scripts.LiuXueInterval_1,
    50002: scripts.LiuXueInterval_2,
    50003: scripts.LiuXueInterval_3,
    50004: scripts.LiuXueInterval_4,
    50005: scripts.TieGu,
    50006: scripts.DunYaDamageExcept,
    50007: scripts.Water_ZhanLiu,
    50008: scripts.Wind_ZhanLiu,
    50009: scripts.ChengWu_MT,
    50010: scripts.ChengWu_MT_Step,
    50011: scripts.PercentageEventTrigger,
    50012: scripts.Advance_ZhenFen,
    50013: scripts.Advance_HanXiaoQianJun,
    # 50014 友方虚弱占位
    50015: scripts.AdvanceInit,


    # 以下是宏
    60000: scripts.cw_nujue,
    60001: scripts.nujue,
    60002: scripts.cw_shuangjue,
    60003: scripts.cw_gaocheng,
}
