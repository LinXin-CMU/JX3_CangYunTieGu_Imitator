# coding: utf-8
# author: LinXin
from collections import namedtuple


_buff_data = namedtuple('buff_data', ['dwID', 'nMaxTime', 'nMaxStackNum', 'Desc', 'Script'])


buff_data = {
    994: _buff_data(994, 1*16, 1, '倒地', None),
    8232: _buff_data(8232, 16*3, 1, '盾刀二段标记buff', None),
    8245: _buff_data(8245, 10*16, 3, '血怒防御buff', 'XueNuDisappear'),
    8248: _buff_data(8248, 25*16, 1, '虚弱', None),
    8249: _buff_data(8249, 25*16, 1, '流血', 'LiuXueDisappear'),
    8253: _buff_data(8253, 8*16, 1, '雄峦', None),
    8262: _buff_data(8262, 16*4, 1, '盾刀三段标记buff', None),
    8263: _buff_data(8263, 16*3, 1, '盾刀四段标记buff', None),
    8271: _buff_data(8271, 8*16, 125, '寒甲_300AP', None),
    8272: _buff_data(8272, 8*16, 5, '坚铁', 'JianTieDisappear'),
    8276: _buff_data(8276, 15*16, 1, '怒炎', None),
    8277: _buff_data(8277, 999999*16, 1, '切换至盾姿态', None),
    8278: _buff_data(8278, 999999*16, 1, '切换至刀姿态', None),
    8321: _buff_data(8321, 8.25*16, 1, '坚铁_招架后停止叠加cd', None),
    8382: _buff_data(8382, 1*16, 1, '血怒连按第二层需求buff', None),
    8383: _buff_data(8383, 1*16, 1, '血怒连按第三层需求buff', None),
    8384: _buff_data(8384, 1*16, 1, '血怒连按需求buff', None),
    8386: _buff_data(8386, 10*16, 3, '血怒加强后防御buff', 'XueNuDisappear'),
    8391: _buff_data(8391, 15*16, 1, '盾飞', 'DunHuiChangeState'),
    8397: _buff_data(8397, 15*16, 1, '盾威', None),
    8398: _buff_data(8398, 16*6, 1, '卷云', None),
    8418: _buff_data(8418, 6*16, 1, '激昂', None),
    8424: _buff_data(8424, 8*16, 1, '坚定', None),
    8437: _buff_data(8437, 8*16, 1, '寒甲', 'HanJiaDisappear'),
    8448: _buff_data(8448, 11*16, 1, '盾挡（千山）', None),
    8462: _buff_data(8462, 2*16, 1, '招架后寒甲内置cd', None),
    8499: _buff_data(8499, 11*16, 1, '盾挡', None),
    8504: _buff_data(8504, 10*16, 125, '振奋', None),
    8738: _buff_data(8738, 16*12, 1, '缓深', None),
    8873: _buff_data(8873, 0.5*16, 1, '盾飞0.5s内无法施展盾猛', None),
    9052: _buff_data(9052, 999999*16, 1, '绝刀耗怒增伤标记buff', None),
    13352: _buff_data(13352, 0.375*16, 1, '盾飞延迟切姿态', 'DunFeiChangeState'),
    13934: _buff_data(13934, 3*16, 1, '戍卫', None),
    14964: _buff_data(14964, 999999*16, 1, '崇云', None),
    17772: _buff_data(17772, 8*16, 125, '寒甲_3万AP', None),
    18222: _buff_data(18222, 12*16, 5, '严阵', None),
    21308: _buff_data(21308, 999999*16, 1, '割裂', None),
    24755: _buff_data(24755, 4*16, 1, '怒炎标记buff', 'NuYanDisappear'),
    24756: _buff_data(24756, 4*16, 1, '怒炎重置绝刀标记', None),
    # 以下是自定义功能的buff
    50000: _buff_data(50000, 25*16, 50, '盾飞跳数监控', None),
    50001: _buff_data(50001, 25*16, 1, '盾飞后监控虚弱是否被流血覆盖', None),
    50002: _buff_data(50002, 0.125*16, 1, '盾飞延迟获得虚弱', 'DunFeiAddXuRuo'),
    50003: _buff_data(50003, 1*16, 1, '盾飞伤害子技能1秒cd', 'DunFeiAttack'),
    50004: _buff_data(50004, 0.625*16, 1, '盾猛延迟造成击倒', 'DunMengJiDao'),
    50005: _buff_data(50005, 2*16, 1, '流血_无炼狱无割裂', 'LiuXueInterval_1'),
    50006: _buff_data(50006, 1*16, 1, '流血_有炼狱无割裂', 'LiuXueInterval_2'),
    50007: _buff_data(50007, 2*16, 1, '流血_无炼狱有割裂', 'LiuXueInterval_3'),
    50008: _buff_data(50008, 1*16, 1, '流血_有炼狱有割裂', 'LiuXueInterval_4'),
    50009: _buff_data(50009, 999999*16, 3, '崇云_次数检测', None),
}


