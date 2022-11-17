# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QApplication
import datetime

from player.player import Player
from target.target import Target
from TieGu.ui.ui_main import MainUI

app = QApplication([])
ui = MainUI()
my_target = Target()
my_player = Player([], [], my_target)
my_target.player = my_player


def run():
    global my_player, my_target, ui
    if globals().get('my_target'):
        del globals()['my_target']
        my_target = Target()
    if globals().get('my_player'):
        del globals()['my_player']
        my_player = Player([], [], my_target)
        my_target.player = my_player
        my_player.talents = ui.get_talent()
        my_player.recipes = ui.get_recipe()
        my_target.level = ui.get_level()
        my_target.SetNpcAttributeValueByLevel()
        my_target.attack_cooldown = 2.25 * 16
        my_target.attack_per_count = 1


    skills = {}

    for i in range(300 * 16):
        my_player.Timer(i)
        my_target.Timer(i)

        my_target.CastSkill(1, 1)

        my_player.CastSkill(13045, 1)  # /cast 盾压

        if not (my_player.IsHaveBuff(8499) or my_player.IsHaveBuff(8448)):
            my_player.CastSkill(13046, 1)  # /cast [nobuff:盾挡] 盾猛

        my_player.CastSkill(13047, 1)  # /cast 盾击
        my_player.CastSkill(13044, 1)  # /cast 盾刀

        if my_player.rage == 110:
            my_player.CastSkill(13391, 1)  # /cast [rage>109] 盾挡
        if my_player.rage >= 65 and (my_player.IsHaveBuff(8499) or my_player.IsHaveBuff(8448)):
            my_player.CastSkill(13050, 1)  # /cast [rage>=65&buff:盾挡] 盾飞
        if 0 < my_player.GetBuff(8391, 1).lasting < 10 * 16:
            my_player.CastSkill(13051, 1)  # /cast [bufftime:盾飞<9] 盾回

        my_player.CastSkill(13054, 1)  # /cast 斩刀

        if my_player.IsHaveBuff(24755):
            my_player.CastSkill(13055, 1)  # /cast [buff:24755] 绝刀

        my_player.CastSkill(13052, 1)  # /cast 劫刀

        # 血怒测试用
        if i in [0, 0.5 * 16, 1.5 * 16]:
            my_player.CastSkill(13040, 1)

        print(my_player.rage)
        print(my_player.buffs)
        print(my_target.buffs)

    for i in my_player.casted:
        if i['name'] not in skills:
            skills[i['name']] = 1
        else:
            skills[i['name']] += 1

    ui.label_info.setText(f"[{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] 模拟完成！")
    print(*[f"{i}: {j}\n" for i, j in skills.items()])
    print(int(my_player.damage / 300))


def get_csv():
    global my_player, ui
    import csv

    with open(f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}-player.csv", 'w', encoding='gbk',
              newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['second', 'frame', 'name', 'desc', 'rage', 'damage', 'critical', 'buff', 'tbuff'])
        csv_writer.writeheader()
        csv_writer.writerows(my_player.casted)

    ui.label_info.setText(f"[{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] 导出成功！")


def main():
    global ui, app

    ui.button_main.clicked.connect(run)
    ui.button_tocsv.clicked.connect(get_csv)
    ui.show()
    app.exec()


main()