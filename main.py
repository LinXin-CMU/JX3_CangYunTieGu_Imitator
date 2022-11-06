from player.player import Player
from target.target import Target

target = Target()
player = Player([], [], target)

for i in range(300 * 16):
    player.Timer(i)
    target.Timer(i)

    player.CastSkill(13045, 1)  # /cast 盾压
    player.CastSkill(13047, 1)  # /cast 盾击
    player.CastSkill(13044, 1)  # /cast 盾刀

    if player.rage == 110:
        player.CastSkill(13391, 1)  # /cast [rage>109] 盾挡
    if player.rage >= 80 and player.IsHaveBuff(8499) or player.IsHaveBuff(8448):
        player.CastSkill(13050, 1)  # /cast [rage>65&buff:盾挡] 盾飞
    if 0 < player.GetBuff(8391, 1).lasting < 5*16:
        player.CastSkill(13051, 1)  # /cast [bufftime:盾飞<10] 盾回

    player.CastSkill(13054, 1)  # /cast 斩刀

    if player.IsHaveBuff(24755):
        player.CastSkill(13055, 1)  # /cast [buff:24755] 绝刀

    player.CastSkill(13052, 1)  # /cast 劫刀

    print(player.rage)
    print(player.buffs)
    print(target.buffs)



# print(player.casted)
# 导出一个csv
import csv
import datetime

with open(f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}-player.csv", 'w', encoding='gbk', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=['second', 'frame', 'name', 'desc', 'rage', 'buff', 'tbuff'])
    csv_writer.writeheader()
    csv_writer.writerows(player.casted)

# with open(f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}-target.csv", 'w', encoding='gbk', newline='') as f:
#     csv_writer = csv.DictWriter(f, fieldnames=['frame', 'name', 'desc'])
#     csv_writer.writeheader()
#     csv_writer.writerows(target.casted)
