from player.player import Player

player = Player([], [])

for i in range(300 * 16):
    player.Timer(i)
    player.CastSkill(13045, 1)  # /cast 盾压
    player.CastSkill(13047, 1)  # /cast 盾击
    player.CastSkill(13044, 1)  # /cast 盾刀

    if player.rage == 110:
        player.CastSkill(13391, 1)  # /cast [rage>109] 盾挡
    if player.rage > 65 and player.IsHaveBuff(8499) or player.IsHaveBuff(8448):
        player.CastSkill(13050, 1)  # /cast [rage>65&buff:盾挡] 盾飞

    print(player.rage)
    print(player.buffs)

# print(player.casted)
# 导出一个csv
import csv
import datetime

with open(f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv", 'w', encoding='gbk', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=['frame', 'name', 'desc'])
    csv_writer.writeheader()
    csv_writer.writerows(player.casted)
