# coding: utf-8
# author: LinXin
# 这一堆大部分都是测试代码~
# from time

from PyQt5.QtWidgets import QApplication
from PyQt5.QtChart import QChartView
from datetime import datetime

from player.player import Player
from player.player_recorder import FightRecorder
from target.target import Target
from ui.ui_main import MainUI

QChartView()

app = QApplication([])
ui = MainUI()


class Main:

    def __init__(self):
        self.target = None
        self.player = None
        self.recorder = FightRecorder()

    def run(self):
        # nTime = time.time()
        nFightTime = ui.get_fight_time()
        recorder = self.recorder.StartNewFight()

        self.target = Target()
        self.player = Player(ui.get_talent(), ui.get_recipe(), self.target, ui.get_attribute_with_set())
        self.recorder.SetPlayer(self.player)
        self.target.player = self.player
        self.target.level = ui.get_level()
        self.player.settings = ui.get_settings()
        self.target.settings = self.player.settings
        self.target.SetNpcAttributeValueByLevel()
        self.player.ActiveHaloByID()
        self.player.SetFightRecorder(recorder)
        self.player.ResetEventCount()
        self.player.SetAdvanceEffect(ui.get_self_advance_attribute())
        self.player.SetTeamMateData(ui.get_other_advance_data())
        recorder.SetBaseAttribute(self.player.BaseAttributes)

        nCommand = ui.get_command_id()
        if not nCommand:
            return

        skills = {}
        self.player.CastSkill(50015, 1)     # 增益初始化
        i = 0
        while i < nFightTime:

            self.player.Timer(i)
            self.target.Timer(i)

            self.player.CastSkill(nCommand, 1)

            # if self.player.GetBuff(18783, 1).layer == 5:
            #     self.player.CastSkill(26141, 1)     # /use 龙门飞剑
            if self.player.GetBuff(8391).lasting > 14.5 * 16:
                self.player.CastSkill(26060, 1)
                self.player.CastSkill(50008, 1)

    
            print(self.player.rage)
            print(self.player.buffs)
            print(self.target.buffs)
    
            # 设置进度条
            ui.progressBar.setValue(i//16)

            i += int(self.player.GetLatestStep())

        for i in self.player.casted:
            if i['name'] not in skills:
                skills[i['name']] = {'count': i['fExpect'], 'damage': i['damage'], 'critical': i['critical']}
            else:
                skills[i['name']]['count'] += i['fExpect']
                skills[i['name']]['damage'] += i['damage']
                skills[i['name']]['critical'] += i['critical']
    
        ui.label_info.setText(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] 模拟完成！")
        ui.set_skill_data_table(skills, nFightTime)
        ui.progressBar.setValue(300)
        ui.set_attribute_profits(*recorder.end())
        ui.tabWidget_2.setCurrentIndex(1)

        # print(time.time() - nTime)
        nDps = int(self.player.damage / (nFightTime / 16))
        ui.add_history(skills, ui.comboBox_14.currentText(), nDps, ui.halo_button.text(), ui.qijin_checkBox.checkState())
        return nDps

    def get_csv(self):
        import csv

        if not self.player:
            return

        with open(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}-player.csv", 'w', encoding='gbk',
                  newline='') as f:
            csv_writer = csv.DictWriter(f, fieldnames=['second', 'frame', 'name', 'desc', 'rage', 'damage', 'critical',
                                                       'buff', 'tbuff', 'fExpect', 'cd_盾飞'])
            csv_writer.writeheader()
            csv_writer.writerows(self.player.casted)

        ui.label_info.setText(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] 导出成功！")


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