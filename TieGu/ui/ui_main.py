# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QMainWindow
from typing import List, Dict
from functools import reduce

from .ui import Ui_MainWindow
from settings.jx3_collections import recipe
from .modules.ui_selector import TalentSelector



class MainUI(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)

        self._selector = TalentSelector(self)

    def get_talent(self) -> List[int]:
        return self._selector.talent

    def get_recipe(self) -> List[int]:
        recipes = []
        recipe_index = reduce(lambda i, j: i+j, [i for i in self._selector.recipe.values()])
        for recipe_id in recipe:
            if recipe[recipe_id].index in recipe_index:
                recipes.append(recipe_id)

        return recipes

    def get_level(self) -> int:
        return self.Level_spinBox.value()








