# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QMainWindow
from typing import List, Dict

from .ui import Ui_MainWindow
from .modules.ui_selector import TalentSelector



class MainUI(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)

        self._selector = TalentSelector(self)

    def get_talent(self) -> List[int]:
        return self._selector.talent

    def get_recipe(self) -> Dict[str, List[int]]:
        return self._selector.recipe








