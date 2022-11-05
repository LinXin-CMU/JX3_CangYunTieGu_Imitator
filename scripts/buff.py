# coding: utf-8
# author: LinXin
from collections import namedtuple


_buff_data = namedtuple('buff_data', ['dwID', 'nMaxTime', 'nMaxStackNum', 'Desc', 'Script'])


buff_data = {
    8232: _buff_data(8232, 16*3, 1, '盾刀二段标记buff', None),
    8248: _buff_data(8248, 25*16, 1, '虚弱', None),
    8253: _buff_data(8253, 8*16, 1, '雄峦', None),
    8262: _buff_data(8262, 16*4, 1, '盾刀三段标记buff', None),
    8263: _buff_data(8263, 16*3, 1, '盾刀四段标记buff', None),
    8276: _buff_data(8276, 15*16, 1, '怒炎', None),
    8277: _buff_data(8277, 999999*16, 1, '切换至盾姿态', None),
    8278: _buff_data(8278, 999999*16, 1, '切换至刀姿态', None),
    8391: _buff_data(8391, 15*16, 1, '盾飞', None),
    8397: _buff_data(8397, 15*16, 1, '盾威', None),
    8398: _buff_data(8398, 16*6, 1, '卷云', None),
    8418: _buff_data(8418, 6*16, 1, '激昂', None),
    8448: _buff_data(8448, 11*16, 1, '盾挡（千山）', None),
    8499: _buff_data(8499, 11*16, 1, '盾挡', None),
    8504: _buff_data(8504, 10*16, 125, '振奋', None),
    8738: _buff_data(8738, 16*12, 1, '缓深', None),
    13352: _buff_data(13352, 0.375*16, 1, '盾飞延迟切姿态', 'DunFeiChangeState'),
    18222: _buff_data(18222, 12*16, 5, '严阵', None),
    # 以下是自定义功能的buff
    50000: _buff_data(50000, 25*16, 50, '盾飞跳数监控', None),
    50001: _buff_data(50001, 25*16, 1, '盾飞后监控虚弱是否被流血覆盖', None),
    50002: _buff_data(50002, 0.125*16, 1, '盾飞延迟获得虚弱', 'DunFeiAddXuRuo'),
    50003: _buff_data(50003, 1*16, 1, '盾飞伤害子技能1秒cd', 'DunFeiAttack'),
}


