# coding: utf-8
# author: LinXin
# 这一堆大部分都是测试代码~
# from time

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication, Qt
from datetime import datetime
from PIL import Image

from player.player import Player
from player.player_recorder import FightRecorder
from target.target import Target
from ui.ui_main import MainUI


# print("main.py row55 测试用！！记得打包时注释掉！！")


class Main:

    def __init__(self, ui: MainUI):
        self.target = None
        self.player = None
        self.recorder = FightRecorder()
        self.ui = ui

    def run(self):
        # nTime = time.time()
        nFightTime = self.ui.get_fight_time()
        self.ui.set_progress_bar_by_time(nFightTime)

        recorder = self.recorder.StartNewFight()

        self.target = Target()
        self.player = Player(self.ui.get_talent(), self.ui.get_recipe(), self.target, self.ui.get_attribute_with_set())
        self.recorder.SetPlayer(self.player)
        self.target.player = self.player
        self.target.level = self.ui.get_level()
        self.player.SetMount(self.ui.get_mount_id())
        self.player.settings = self.ui.get_settings()
        self.target.settings = self.player.settings
        self.target.SetNpcAttributeValueByLevel()
        self.player.ActiveHaloByID()
        self.player.SetFightRecorder(recorder)
        self.player.ResetEventCount()
        self.player.SetAdvanceEffect(self.ui.get_self_advance_attribute())
        self.player.SetTeamMateData(self.ui.get_other_advance_data())
        self.player.SetDelay(self.ui.get_delay_msec())
        recorder.SetBaseAttribute(self.player.BaseAttributes)

        nCommand = self.ui.get_command_id()
        if not nCommand:
            return

        # nCommand = 60004

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
            self.ui.progressBar.setValue(i//16)

            # 判断延迟时间
            nDelay = self.player.GetCumulativeDelayFrame()
            if i + nDelay >= nFightTime:
                break
            else:
                i += int(self.player.GetLatestStep())



        for i in self.player.casted:
            if i['name'] not in skills:
                skills[i['name']] = {'count': i['fExpect'], 'damage': i['damage'], 'critical': i['critical']}
            else:
                skills[i['name']]['count'] += i['fExpect']
                skills[i['name']]['damage'] += i['damage']
                skills[i['name']]['critical'] += i['critical']
    
        self.ui.label_info.setText(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] 模拟完成！")
        self.ui.set_skill_data_table(skills, nFightTime)
        self.ui.progressBar.setValue(self.ui.progressBar.maximum())

        profits = recorder.end()
        self.ui.set_attribute_profits(*profits[0])
        self.ui.set_stone_profit_table(profits[1])
        self.ui.tabWidget_2.setCurrentIndex(1)

        # print(time.time() - nTime)
        nDps = int(self.player.damage / (nFightTime / 16))
        self.ui.add_history(skills, self.ui.comboBox_14.currentText(), nDps, self.ui.halo_button.text(), self.ui.qijin_checkBox.checkState())

        print(self.player.BaseAttributes)
        print(self.player.GetAttributeWithoutStone())

        return nDps

    def get_csv(self):
        import csv

        if not self.player:
            return

        with open(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}-player.csv", 'w', encoding='gbk',
                  newline='') as f:
            csv_writer = csv.DictWriter(f, fieldnames=['second', 'frame', 'name', 'desc', 'rage', 'damage', 'critical',
                                                       'buff', 'tbuff', 'fExpect', 'cd_盾飞', 'cd_斩刀'])
            csv_writer.writeheader()
            csv_writer.writerows(self.player.casted)

        self.ui.label_info.setText(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] 导出成功！")


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
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    ui = MainUI()
    main = Main(ui)
    ui.button_main.clicked.connect(main.run)
    ui.button_tocsv.clicked.connect(main.get_csv)
    ui.show()
    app.exec()


main()