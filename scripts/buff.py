# coding: utf-8
# author: LinXin
from collections import namedtuple


_buff_data = namedtuple('buff_data', ['dwID', 'nMaxTime', 'nMaxStackNum', 'Desc'])


buff_data = {
    8232: _buff_data(8232, 16*3, 1, '盾刀二段标记buff'),
    8253: _buff_data(8253, 8*16, 1, '雄峦'),
    8262: _buff_data(8262, 16*4, 1, '盾刀三段标记buff'),
    8263: _buff_data(8263, 16*3, 1, '盾刀四段标记buff'),
    8398: _buff_data(8398, 16*6, 1, '卷云'),
    8418: _buff_data(8418, 6*16, 1, '激昂'),
    8448: _buff_data(8448, 11*16, 1, '盾挡（千山）'),
    8499: _buff_data(8499, 11*16, 1, '盾挡'),
    8504: _buff_data(8504, 10*16, 125, '振奋'),
    8738: _buff_data(8738, 16*12, 1, '缓深'),
    18222: _buff_data(18222, 12*16, 5, '严阵'),
}


