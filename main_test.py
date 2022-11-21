# coding: utf-8
# author: LinXin
# 这一堆大部分都是测试代码~
import time

from PyQt5.QtWidgets import QApplication
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime

from player.player import Player
from target.target import Target
from TieGu.ui.ui_main import MainUI


app = QApplication([])
ui = MainUI()


class Main:

    def __init__(self):
        self.target = None
        self.player = None

    def run(self):
        nTime = time.time()

        self.target = Target()
        self.player = Player([], [], self.target)
        self.target.player = self.player
        self.player.talents = ui.get_talent()
        self.player.recipes = ui.get_recipe()
        self.target.level = ui.get_level()
        self.player.settings = ui.get_settings()
        self.target.settings = self.player.settings
        self.target.SetNpcAttributeValueByLevel()
        self.player.ActiveHaloByID()

        skills = {}
        i = 0
        while i < 300*16:

            self.player.Timer(i)
            self.target.Timer(i)

            self.player.CastSkill(13045, 1)  # /cast 盾压
    
            if not (self.player.IsHaveBuff(8499) or self.player.IsHaveBuff(8448)):
                self.player.CastSkill(13046, 1)  # /cast [nobuff:盾挡] 盾猛
    
            if self.player.rage > 80 and True:
                self.player.CastSkill(25213, 1) # /cast 断马摧城
    
            self.player.CastSkill(13047, 1)  # /cast 盾击
            self.player.CastSkill(13044, 1)  # /cast 盾刀
    
            if self.player.rage == 110:
                self.player.CastSkill(13391, 1)  # /cast [rage>109] 盾挡
            if self.player.rage >= 65 and (self.player.IsHaveBuff(8499) or self.player.IsHaveBuff(8448)):
                self.player.CastSkill(13050, 1)  # /cast [rage>=65&buff:盾挡] 盾飞
            if 0 < self.player.GetBuff(8391, 1).lasting < 10 * 16:
                self.player.CastSkill(13051, 1)  # /cast [bufftime:盾飞<9] 盾回
    
            self.player.CastSkill(13054, 1)  # /cast 斩刀
    
            if self.player.IsHaveBuff(24755):
                self.player.CastSkill(13055, 1)  # /cast [buff:24755] 绝刀
    
            self.player.CastSkill(13052, 1)  # /cast 劫刀
    
            # 血怒测试用
            if i in [0, 0.5 * 16, 1.5 * 16]:
                self.player.CastSkill(13040, 1)
    
            print(self.player.rage)
            print(self.player.buffs)
            print(self.target.buffs)
    
            # 设置进度条
            ui.progressBar.setValue(i//16)

            i += int(self.player.GetLatestStep())

        for i in self.player.casted:
            if i['name'] not in skills:
                skills[i['name']] = {'count': 1, 'damage': i['damage'], 'critical': i['critical']}
            else:
                skills[i['name']]['count'] += 1
                skills[i['name']]['damage'] += i['damage']
                skills[i['name']]['critical'] += i['critical']
    
        ui.label_info.setText(f"[{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] 模拟完成！")
        ui.set_skill_data_table(skills)
        print(int(self.player.damage / 300))
        ui.progressBar.setValue(300)

        print(time.time() - nTime)
        return int(self.player.damage / 300)

    def get_csv(self):
        import csv

        with open(f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}-player.csv", 'w', encoding='gbk',
                  newline='') as f:
            csv_writer = csv.DictWriter(f, fieldnames=['second', 'frame', 'name', 'desc', 'rage', 'damage', 'critical',
                                                       'buff', 'tbuff'])
            csv_writer.writeheader()
            csv_writer.writerows(self.player.casted)

        ui.label_info.setText(f"[{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] 导出成功！")


# def multiThread_run():
#     nTime = time.time()
#     nDamage = 0
#     pool = ThreadPoolExecutor(5)
#     tasks = [pool.submit(Main().run) for _ in range(5)]
#     for future in as_completed(tasks):
#         nDamage += future.result()
#
#     print(int(nDamage / 5))
#     print(time.time() - nTime)


def main():
    global ui, app
    main = Main()
    ui.button_main.clicked.connect(main.run)
    ui.button_tocsv.clicked.connect(main.get_csv)
    ui.show()
    app.exec()


main()