# coding: utf-8
# author: LinXin
from PyQt5.QtWidgets import QComboBox, QLabel, QApplication
from PyQt5.QtCore import pyqtSignal, QEvent
# from PyQt5.Qt import QColor
from PyQt5.QtGui import QMouseEvent
from PIL import Image

app = QApplication([])


# noinspection PyUnresolvedReferences
class ClickableComboBox(QComboBox):
    clicked = pyqtSignal()

    def showPopup(self) -> None:
        self.clicked.emit()
        super(ClickableComboBox, self).showPopup()


# noinspection PyUnresolvedReferences
class StarLabel(QLabel):
    hovered = pyqtSignal()
    unhovered = pyqtSignal()
    clicked = pyqtSignal()

    def enterEvent(self, a0: QEvent) -> None:
        self.hovered.emit()
        print('MouseEnter')
        super(StarLabel, self).enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        self.unhovered.emit()
        print('MouseLeave')
        super(StarLabel, self).leaveEvent(a0)

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.clicked.emit()
        print('Click')
        super(StarLabel, self).mouseReleaseEvent(ev)


ICONS = {
    'equip_max': Image.open(r'ui/source/border_max.png').toqpixmap(),
    'db': Image.open(r'ui/source/border_min.png').toqpixmap(),
    # 'embedding_0': Image.open(r'ui/source/embedding_0.png').resize((16, 16)).toqpixmap(),
    # 'embedding_1': Image.open(r'ui/source/embedding_1.png').resize((16, 16)).toqpixmap(),
    # 'embedding_2': Image.open(r'ui/source/embedding_2.png').resize((16, 16)).toqpixmap(),
    # 'embedding_3': Image.open(r'ui/source/embedding_3.png').resize((16, 16)).toqpixmap(),
    # 'embedding_4': Image.open(r'ui/source/embedding_4.png').resize((16, 16)).toqpixmap(),
    # 'embedding_5': Image.open(r'ui/source/embedding_5.png').resize((16, 16)).toqpixmap(),
    # 'embedding_6': Image.open(r'ui/source/embedding_6.png').resize((16, 16)).toqpixmap(),
    # 'embedding_7': Image.open(r'ui/source/embedding_7.png').resize((16, 16)).toqpixmap(),
    # 'embedding_8': Image.open(r'ui/source/embedding_8.png').resize((16, 16)).toqpixmap(),
    # 'star': Image.open(r'ui/source/star.png').resize((16, 16)).toqpixmap(),
    # 'star_grey': Image.open(r'ui/source/star_grey.png').resize((16, 16)).toqpixmap(),

}

POSITION_NAME = {
    '3': '帽子',
    '2': '上衣',
    '6': '腰带',
    '10': '护腕',
    '8': '下装',
    '9': '鞋子',
    '4': '项链',
    '7': '腰坠',
    '5': '戒指',
    '1': '远程武器',
    '0': '近身武器',
}

POSITION_KEY = {
    'HAT': '3',
    'JACKET': '2',
    'BELT': '6',
    'WRIST': '10',
    'BOTTOMS': '8',
    'SHOES': '9',
    'NECKLACE': '4',
    'PENDANT': '7',
    'RING_1': '5',
    'RING_2': '5',
    'SECONDARY_WEAPON': '1',
    'PRIMARY_WEAPON': '0',
}

SLOT_DICT = {
    'atPhysicsShieldBase': '外功防御等级'
    , 'atMagicShield': '内功防御等级'
    , 'atMeleeWeaponDamageBase': '近战武器伤害'
    , 'atMeleeWeaponDamageRand': '近战武器伤害浮动'
    , 'atMeleeWeaponAttackSpeedBase': '近战攻击速度'
    , 'atRangeWeaponDamageBase': '远程伤害'
    , 'atRangeWeaponDamageRand': '远程伤害浮动'
    , 'atRangeWeaponAttackSpeedBase': '远程攻击速度'
    , 'atVitalityBase': '体质'
    , 'atAgilityBase': '身法'
    , 'atAgilityBasePercentAdd': '身法'
    , 'atSpunkBase': '元气'
    , 'atSpunkBasePercentAdd': '元气'
    , 'atStrengthBase': '力道'
    , 'atStrengthBasePercentAdd': '力道'
    , 'atSpiritBase': '根骨'
    , 'atSpiritBasePercentAdd': '根骨'
    , 'atVitalityBasePercentAdd': '体质'
    , 'atDecriticalDamagePowerBase': '化劲等级'
    , 'atDecriticalDamagePowerPercent': '化劲率'
    , 'atParryBase': '招架等级'
    , 'atParryPercent': '招架率'
    , 'atParryValueBase': '拆招值'
    , 'atParryValuePercent': '拆招值'
    , 'atDodge': '闪避等级'
    , 'atToughnessBase': '御劲等级'
    , 'atToughnessPercent': '御劲率'
    , 'atGlobalResistPercent': '减伤'
    , 'atDropDefence': '抗摔系数'
    , 'atHasteBase': '加速等级'
    , 'atStrainBase': '无双等级'
    , 'atStrainPercent': '无双率'
    , 'atSurplusValueBase': '破招值'
    , 'atBasePotentialAdd': '全属性'
    , 'atAllTypeHitValue': '全命中'
    , 'atAllTypeCriticalStrike': '全会心等级'
    , 'atAddSprintPowerCost': '气力值'
    , 'atAddSprintPowerMax': '气力值上限'
    , 'atAddSprintPowerRevive': '气力值每秒恢复速度'
    , 'atActiveThreatCoefficient': '威胁值'
    , 'atLunarAttackPowerBase': '阴性内功攻击'
    , 'atMagicAttackPowerBase': '内功攻击'
    , 'atNeutralAttackPowerBase': '混元性内功攻击'
    , 'atPoisonAttackPowerBase': '毒性内功攻击'
    , 'atSolarAndLunarAttackPowerBase': '阴阳内功攻击'
    , 'atSolarAttackPowerBase': '阳性内功攻击'
    , 'atLunarCriticalStrike': '阴性内功会心等级'
    , 'atLunarCriticalStrikeBaseRate': '阴性内功会心'
    , 'atMagicCriticalStrike': '内功会心等级'
    , 'atNeutralCriticalStrike': '混元性内功会心等级'
    , 'atNeutralCriticalStrikeBaseRate': '混元性内功会心'
    , 'atPoisonCriticalStrike': '毒性内功会心等级'
    , 'atPoisonCriticalStrikeBaseRate': '毒性内功会心'
    , 'atSolarAndLunarCriticalStrike': '阴阳内功会心等级'
    , 'atSolarCriticalStrike': '阳性内功会心等级'
    , 'atSolarCriticalStrikeBaseRate': '阳性内功会心'
    , 'atLunarHitValue': '阴性内功命中'
    , 'atMagicHitValue': '内功命中'
    , 'atNeutralHitValue': '混元性内功命中'
    , 'atPoisonHitValue': '毒性内功命中'
    , 'atSolarAndLunarHitValue': '阴阳内功命中'
    , 'atSolarHitValue': '阳性内功命中'
    , 'atLunarOvercomeBase': '阴性内功破防等级'
    , 'atMagicOvercome': '内功破防等级'
    , 'atNeutralOvercomeBase': '混元性内功破防等级'
    , 'atNeutralOvercomePercent': '混元性内功破防'
    , 'atPoisonOvercomeBase': '毒性内功破防等级'
    , 'atSolarAndLunarOvercomeBase': '阴阳内功破防等级'
    , 'atSolarOvercomeBase': '阳性内功破防等级'
    , 'atManaReplenishExt': '内力恢复'
    , 'atManaReplenishPercent': '内力恢复'
    , 'atMaxManaAdditional': '内力上限'
    , 'atMaxManaBase': '内力上限'
    , 'atMaxManaPercentAdd': '内力上限'
    , 'atDamageToManaForSelf': '内力偷取'
    , 'atModifyCostManaPercent': '内力消耗'
    , 'atPhysicsAttackPowerBase': '外功攻击'
    , 'atPhysicsAttackPower': '外功攻击'
    , 'atPhysicsCriticalStrike': '外功会心等级'
    , 'atPhysicsHitValue': '外功命中'
    , 'atPhysicsOvercomeBase': '外功破防等级'
    , 'atLifeReplenishExt': '气血恢复'
    , 'atLifeReplenishPercent': '气血恢复'
    , 'atMaxLifeAdditional': '气血上限'
    , 'atMaxLifeBase': '气血上限'
    , 'atMaxLifePercentAdd': '气血上限'
    , 'atLunarMagicShieldBase': '阴性内功防御等级'
    , 'atNeutralMagicShieldBase': '混元性内功防御等级'
    , 'atPoisonMagicShieldBase': '毒性内功防御等级'
    , 'atSolarMagicShieldBase': '阳性内功防御等级'
    , 'atPhysicsDefenceAdd': '外功防御'
    , 'atPhysicsShieldAdditional': '外功防御'
    , 'atPhysicsShieldPercent': '外功防御'
    , 'atDamageToLifeForSelf': '生命偷取'
    , 'atDivingFrameBase': '水下呼吸'
    , 'atMoveSpeedPercent': '移动速度'
    , 'atTherapyCoefficient': '治疗成效'
    , 'atTherapyPowerBase': '治疗成效'
    , 'atBeTherapyCoefficient': '被治疗成效'
    , 'atAddHorseSprintPowerCost': '马术气力值'
    , 'atAddHorseSprintPowerMax': '马术气力值'
    , 'atAddHorseSprintPowerRevive': '马术气力值'
    , 'atAllTypeCriticalDamagePowerBase': '全会心效果等级'
    , 'atLunarCriticalDamagePowerPercent': '阴性内功会心效果'
    , 'atMagicCriticalDamagePowerBase': '内功会心效果等级'
    , 'atMagicCriticalDamagePowerPercent': '内功会心效果'
    , 'atNeutralCriticalDamagePowerBase': '混元性内功会心效果等级'
    , 'atNeutralCriticalDamagePowerPercent': '混元性内功会心效果'
    , 'atPoisonCriticalDamagePowerBase': '毒性内功会心效果等级'
    , 'atPoisonCriticalDamagePowerPercent': '毒性内功会心效果'
    , 'atSolarAndLunarCriticalDamagePowerBase': '阴阳内功会心效果等级'
    , 'atSolarCriticalDamagePowerBase': '阳性内功会心效果等级'
    , 'atSolarCriticalDamagePowerPercent': '阳性内功会心效果'
    , 'atPhysicsCriticalDamagePowerBase': '外功会心效果等级'
    , 'atPhysicsCriticalDamagePowerPercent': '外功会心效果'
    , 'atSetEquipmentRecipe': '套装效果秘籍'
}

UI_COLOR = {
    'orange': (255, 150, 0),
    'green': (0, 200, 72),
    'white': (255, 255, 255),
    'grey': (173, 173, 173),
    'magenta': (227, 44, 229),
}

ENCHANT_NEED = {"天堑奇珂": {"min": 10600, "max": 11300}, "天堑奇琨": {"min": 9800, "max": 10300},
                "山市鬼洲": {"min": 6500, "max": 7200}, "山市鬼域": {"min": 5850, "max": 6450},
                "山市鬼船": {"min": 5250, "max": 5800}, "山市鬼冢": {"min": 4750, "max": 5200},
                "山市鬼楼": {"min": 4400, "max": 4700}, "昆吾焰珩": {"min": 2900, "max": 3300},
                "昆吾焰珀": {"min": 2750, "max": 2950}, "昆吾焰砂": {"min": 2300, "max": 2450},
                "昆吾焰晶": {"min": 2500, "max": 2700}}

ENCHANT_DUTY = {
    '1': '伤',
    '2': '伤',
    '3': '御',
    '4': '疗',
}

WEAPON_TYPE = {"0": "棍类", "1": "长兵类", "2": "短兵类", "4": "双兵类", "5": "笔类", "6": "投掷", "7": "弓弦", "9": "重兵类", "10": "笛类",
               "11": "千机匣", "12": "弯刀", "13": "短棒", "14": "刀盾", "15": "琴", "16": "傲霜刀", "17": "伞", "18": "链刃",
               "19": "魂灯", "20": "百草卷", "21": "横刀"}

ATTRIBUTE_DICT = {"Vitality": {"name": "体质", "isPercent": 0, "default": 0},
                  "Agility": {"name": "身法", "isPercent": 0, "default": 0},
                  "Spirit": {"name": "根骨", "isPercent": 0, "default": 0},
                  "Spunk": {"name": "元气", "isPercent": 0, "default": 0},
                  "Strength": {"name": "力道", "isPercent": 0, "default": 0},
                  "PhysicsAttackPowerBase": {"name": "基础攻击", "popname": "基础外功攻击", "isPercent": 0, "default": 1},
                  "PhysicsAttackPower": {"name": "攻击力", "popname": "最终外功攻击", "isPercent": 0, "default": 1},
                  "LunarAttackPowerBase": {"name": "基础攻击", "popname": "基础阴性内功攻击", "isPercent": 0, "default": 1},
                  "LunarAttackPower": {"name": "攻击力", "popname": "最终阴性内功攻击", "isPercent": 0, "default": 1},
                  "SolarAttackPowerBase": {"name": "基础攻击", "popname": "基础阳性内功攻击", "isPercent": 0, "default": 1},
                  "SolarAttackPower": {"name": "攻击力", "popname": "最终阳性内功攻击", "isPercent": 0, "default": 1},
                  "NeutralAttackPowerBase": {"name": "基础攻击", "popname": "基础混元内功攻击", "isPercent": 0, "default": 1},
                  "NeutralAttackPower": {"name": "攻击力", "popname": "最终混元内功攻击", "isPercent": 0, "default": 1},
                  "PoisonAttackPowerBase": {"name": "基础攻击", "popname": "基础毒性内功攻击", "isPercent": 0, "default": 1},
                  "PoisonAttackPower": {"name": "攻击力", "popname": "最终毒性内功攻击", "isPercent": 0, "default": 1},
                  "TherapyPowerBase": {"name": "基础治疗", "isPercent": 0, "default": 0},
                  "TherapyPower": {"name": "治疗量", "isPercent": 0, "default": 1},
                  "PhysicsHit": {"name": "外功命中等级", "popname": "外功命中等级", "isPercent": 0, "default": 1},
                  "PhysicsHitPercent": {"name": "命中", "popname": "对同等级目标命中几率", "isPercent": 1, "default": 1},
                  "LunarHit": {"name": "阴性命中等级", "popname": "阴性命中等级", "isPercent": 0, "default": 1},
                  "LunarHitPercent": {"name": "命中", "popname": "对同等级目标命中几率", "isPercent": 1, "default": 1},
                  "SolarHit": {"name": "阳性命中等级", "popname": "阳性命中等级", "isPercent": 0, "default": 1},
                  "SolarHitPercent": {"name": "命中", "popname": "对同等级目标命中几率", "isPercent": 1, "default": 1},
                  "NeutralHit": {"name": "混元命中等级", "popname": "混元命中等级", "isPercent": 0, "default": 1},
                  "NeutralHitPercent": {"name": "命中", "popname": "对同等级目标命中几率", "isPercent": 1, "default": 1},
                  "PoisonHit": {"name": "毒性命中等级", "popname": "毒性命中等级", "isPercent": 0, "default": 1},
                  "PoisonHitPercent": {"name": "命中", "popname": "对同等级目标命中几率", "isPercent": 1, "default": 1},
                  "PhysicsCriticalStrike": {"name": "外功会心等级", "popname": "外功会心等级", "isPercent": 0, "default": 0},
                  "PhysicsCriticalStrikeRate": {"name": "会心", "popname": "提高对同等级目标会心几率", "isPercent": 1, "default": 1},
                  "LunarCriticalStrike": {"name": "阴性会心等级", "popname": "阴性会心等级", "isPercent": 0, "default": 0},
                  "LunarCriticalStrikeRate": {"name": "会心", "popname": "提高对同等级目标会心几率", "isPercent": 1, "default": 1},
                  "SolarCriticalStrike": {"name": "阳性会心等级", "popname": "阳性会心等级", "isPercent": 0, "default": 0},
                  "SolarCriticalStrikeRate": {"name": "会心", "popname": "提高对同等级目标会心几率", "isPercent": 1, "default": 1},
                  "NeutralCriticalStrike": {"name": "混元会心等级", "popname": "混元会心等级", "isPercent": 0, "default": 0},
                  "NeutralCriticalStrikeRate": {"name": "会心", "popname": "提高对同等级目标会心几率", "isPercent": 1, "default": 1},
                  "PoisonCriticalStrike": {"name": "毒性会心等级", "popname": "毒性会心等级", "isPercent": 0, "default": 0},
                  "PoisonCriticalStrikeRate": {"name": "会心", "popname": "提高对同等级目标会心几率", "isPercent": 1, "default": 1},
                  "PhysicsCriticalDamagePower": {"name": "外功", "isPercent": 0, "default": 0},
                  "PhysicsCriticalDamagePowerPercent": {"name": "会心效果", "popname": "最终外功内功会心效果", "isPercent": 1,
                                                        "default": 1},
                  "LunarCriticalDamagePower": {"name": "阴性", "isPercent": 0, "default": 0},
                  "LunarCriticalDamagePowerPercent": {"name": "会心效果", "popname": "最终阴性内功会心效果", "isPercent": 1,
                                                      "default": 1},
                  "SolarCriticalDamagePower": {"name": "阳性", "isPercent": 0, "default": 0},
                  "SolarCriticalDamagePowerPercent": {"name": "会心效果", "popname": "最终阳性内功会心效果", "isPercent": 1,
                                                      "default": 1},
                  "NeutralCriticalDamagePower": {"name": "混元", "isPercent": 0, "default": 0},
                  "NeutralCriticalDamagePowerPercent": {"name": "会心效果", "popname": "最终混元内功会心效果", "isPercent": 1,
                                                        "default": 1},
                  "PoisonCriticalDamagePower": {"name": "毒性", "isPercent": 0, "default": 0},
                  "PoisonCriticalDamagePowerPercent": {"name": "会心效果", "popname": "最终毒性内功会心效果", "isPercent": 1,
                                                       "default": 1},
                  "PhysicsOvercome": {"name": "外功破防等级", "popname": "最终外功破防", "isPercent": 0, "default": 1},
                  "PhysicsOvercomeBase": {"name": "外功破防等级", "popname": "基础外功破防", "isPercent": 0, "default": 0},
                  "PhysicsOvercomePercent": {"name": "破防", "popname": "自身对同等级目标外功伤害提升", "isPercent": 1, "default": 1},
                  "LunarOvercome": {"name": "阴性破防等级", "popname": "最终阴性内功破防", "isPercent": 0, "default": 1},
                  "LunarOvercomeBase": {"name": "阴性破防等级", "popname": "基础阴性内功破防", "isPercent": 0, "default": 0},
                  "LunarOvercomePercent": {"name": "破防", "popname": "自身对同等级目标阴性内功伤害提升", "isPercent": 1, "default": 1},
                  "SolarOvercome": {"name": "阳性破防等级", "popname": "最终阳性内功破防", "isPercent": 0, "default": 1},
                  "SolarOvercomeBase": {"name": "阳性破防等级", "popname": "基础阳性内功破防", "isPercent": 0, "default": 0},
                  "SolarOvercomePercent": {"name": "破防", "popname": "自身对同等级目标阳性内功伤害提升", "isPercent": 1, "default": 1},
                  "NeutralOvercome": {"name": "混元破防等级", "popname": "最终混元内功破防", "isPercent": 0, "default": 1},
                  "NeutralOvercomeBase": {"name": "混元破防等级", "popname": "基础混元内功破防", "isPercent": 0, "default": 0},
                  "NeutralOvercomePercent": {"name": "破防", "popname": "自身对同等级目标混元内功伤害提升", "isPercent": 1, "default": 1},
                  "PoisonOvercome": {"name": "毒性破防等级", "popname": "最终毒性内功破防", "isPercent": 0, "default": 1},
                  "PoisonOvercomeBase": {"name": "毒性破防等级", "popname": "基础毒性内功破防", "isPercent": 0, "default": 0},
                  "PoisonOvercomePercent": {"name": "破防", "popname": "自身对同等级目标毒性内功伤害提升", "isPercent": 1, "default": 1},
                  "Haste": {"name": "加速", "popname": "加速等级", "isPercent": 0, "default": 1},
                  "HastePercent": {"name": "加速率", "isPercent": 1, "default": 1},
                  "Strain": {"name": "无双等级", "isPercent": 0, "default": 1},
                  "StrainPercent": {"name": "无双", "popname": "对同等级秘境首领伤害提高", "isPercent": 1, "default": 1},
                  "SurplusValue": {"name": "破招", "isPercent": 0, "default": 1},
                  "SurplusValuePercent": {"name": "破招", "popname": "破招值", "isPercent": 1, "default": 0},
                  "PhysicsShieldBase": {"name": "基础外功防御等级", "isPercent": 0, "default": 0},
                  "PhysicsShield": {"name": "外防等级", "popname": "最终外功防御等级", "isPercent": 0, "default": 0},
                  "PhysicsShieldPercent": {"name": "外功防御", "popname": "同等级目标对你的外功伤害降低", "isPercent": 1, "default": 1},
                  "LunarShieldBase": {"name": "基础阴性内防等级", "isPercent": 0, "default": 0},
                  "LunarShield": {"name": "阴性内防等级", "popname": "最终阴性内功防御等级", "isPercent": 0, "default": 0},
                  "LunarShieldPercent": {"name": "内功防御", "popname": "同等级目标对你的阴性内功伤害降低", "isPercent": 1, "default": 1},
                  "SolarShieldBase": {"name": "基础阳性内防等级", "isPercent": 0, "default": 0},
                  "SolarShield": {"name": "阳性内防等级", "popname": "最终阳性内功防御等级", "isPercent": 0, "default": 0},
                  "SolarShieldPercent": {"name": "内功防御", "popname": "同等级目标对你的阳性内功伤害降低", "isPercent": 1, "default": 1},
                  "NeutralShieldBase": {"name": "基础混元内防等级", "isPercent": 0, "default": 0},
                  "NeutralShield": {"name": "混元内防等级", "popname": "最终混元内功防御等级", "isPercent": 0, "default": 0},
                  "NeutralShieldPercent": {"name": "内功防御", "popname": "同等级目标对你的混元性内功伤害降低", "isPercent": 1,
                                           "default": 1},
                  "PoisonShieldBase": {"name": "基础毒性内防等级", "isPercent": 0, "default": 0},
                  "PoisonShield": {"name": "毒性内防等级", "popname": "最终毒性内功防御等级", "isPercent": 0, "default": 0},
                  "PoisonShieldPercent": {"name": "内功防御", "popname": "同等级目标对你的毒性内功伤害降低", "isPercent": 1, "default": 1},
                  "Dodge": {"name": "闪躲等级", "isPercent": 0, "default": 0},
                  "DodgePercent": {"name": "闪躲", "isPercent": 1, "default": 1},
                  "Parry": {"name": "招架等级", "isPercent": 0, "default": 0},
                  "ParryPercent": {"name": "招架", "isPercent": 1, "default": 1},
                  "ParryValue": {"name": "拆招", "isPercent": 0, "default": 1},
                  "Toughness": {"name": "御劲等级", "popname": "御劲等级提高", "isPercent": 0, "default": 0},
                  "ToughnessDefCriticalPercent": {"name": "御劲", "popname": "被同等级目标会心攻击的几率降低", "isPercent": 1,
                                                  "default": 1},
                  "ToughnessDecirDamagePercent": {"name": "御劲减会伤", "popname": "被同等级目标会心攻击时受到的额外伤害降低", "isPercent": 1,
                                                  "default": 0},
                  "DecriticalDamage": {"name": "化劲等级", "isPercent": 0, "default": 0},
                  "DecriticalDamagePercent": {"name": "化劲", "isPercent": 1, "default": 1},
                  "MaxHealth": {"name": "最大气血值", "isPercent": 0, "default": 1},
                  "ActiveThreatCoefficient": {"name": "招式威胁值", "isPercent": 0, "default": 0}}

STONE_ATTRIB_DICT = {"std": [{"value": "atPhysicsAttackPowerBase", "label": "锐刃", "remark": "外功攻击",
                              "mounts": [10015, 10026, 10144, 10145, 10224, 10268, 10390, 10464, 10533, 10585]},
                             {"value": "atPhysicsOvercomeBase", "label": "斩铁", "remark": "外功破防",
                              "mounts": [10015, 10026, 10144, 10145, 10224, 10268, 10390, 10464, 10698, 10533, 10585]},
                             {"value": "atPhysicsCriticalStrike", "label": "见切", "remark": "外功会心",
                              "mounts": [10015, 10026, 10144, 10145, 10224, 10268, 10390, 10464, 10698, 10533, 10585,
                                         10225]},
                             {"value": "atPhysicsCriticalDamagePowerBase", "label": "痛击", "remark": "外功会效",
                              "mounts": [10015, 10026, 10144, 10145, 10224, 10268, 10390, 10464, 10698, 10533, 10585,
                                         10225]}, {"value": "atMeleeWeaponDamageBase", "label": "狂攻", "remark": "武器伤害",
                                                   "mounts": [10015, 10026, 10144, 10145, 10224, 10268, 10390, 10464,
                                                              10698, 10533, 10585]},
                             {"value": "atMagicAttackPowerBase", "label": "激流", "remark": "内功攻击",
                              "mounts": [10003, 10014, 10021, 10081, 10175, 10225, 10242, 10243, 10447, 10615, 10627]},
                             {"value": "atMagicOvercome", "label": "灭气", "remark": "内功破防",
                              "mounts": [10003, 10014, 10021, 10081, 10175, 10225, 10242, 10243, 10447, 10615, 10627]},
                             {"value": "atMagicCriticalStrike", "label": "星见", "remark": "内功会心",
                              "mounts": [10003, 10014, 10021, 10028, 10080, 10081, 10175, 10176, 10242, 10243, 10447,
                                         10448, 10615, 10626, 10627]},
                             {"value": "atMagicCriticalDamagePowerBase", "label": "月华", "remark": "内功会效",
                              "mounts": [10003, 10014, 10021, 10028, 10080, 10081, 10175, 10176, 10242, 10243, 10447,
                                         10448, 10615, 10626, 10627]},
                             {"value": "atMagicShield", "label": "耐受", "remark": "内功防御",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atPhysicsShieldAdditional", "label": "守御", "remark": "外功防御",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atMaxLifeAdditional", "label": "血魂", "remark": "最大气血",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atActiveThreatCoefficient", "label": "忘我", "remark": "威胁值",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atTherapyPowerBase", "label": "海纳", "remark": "治疗",
                              "mounts": [10028, 10080, 10176, 10448, 10626]},
                             {"value": "atTherapyCoefficient", "label": "妙手", "remark": "治疗（百分比）",
                              "mounts": [10028, 10080, 10176, 10448, 10626]}, {"value": "placeholder", "label": "分割线"},
                             {"value": "atStrainBase", "label": "无双", "remark": "无双",
                              "mounts": [10003, 10014, 10015, 10021, 10026, 10062, 10081, 10144, 10145, 10175, 10224,
                                         10225, 10242, 10243, 10268, 10390, 10447, 10464, 10698, 10533, 10585, 10615,
                                         10627]}, {"value": "atSurplusValueBase", "label": "破招", "remark": "破招",
                                                   "mounts": [10003, 10014, 10015, 10021, 10026, 10062, 10081, 10144,
                                                              10145, 10175, 10224, 10225, 10242, 10243, 10268, 10389,
                                                              10390, 10447, 10464, 10698, 10533, 10585, 10615, 10627]},
                             {"value": "atHasteBase", "label": "急速", "remark": "加速",
                              "mounts": [10002, 10003, 10014, 10015, 10021, 10026, 10028, 10062, 10080, 10081, 10144,
                                         10145, 10175, 10176, 10224, 10225, 10242, 10243, 10268, 10389, 10390, 10447,
                                         10448, 10464, 10698, 10533, 10585, 10615, 10626, 10627]},
                             {"value": "atToughnessBase", "label": "大御", "remark": "御劲", "mounts": []},
                             {"value": "atDecriticalDamagePowerBase", "label": "大化", "remark": "化劲",
                              "mounts": [10003, 10014, 10021, 10028, 10080, 10081, 10175, 10176, 10242, 10447, 10448,
                                         10615, 10626, 10627]}, {"value": "atParryBase", "label": "不屈", "remark": "招架",
                                                                 "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atParryValueBase", "label": "破势", "remark": "拆招",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atDodge", "label": "灵动", "remark": "闪避",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atLifeReplenishExt", "label": "回春", "remark": "气血恢复",
                              "mounts": [10002, 10062, 10243, 10389]}, {"value": "placeholder", "label": "分割线"},
                             {"value": "atSolarAttackPowerBase", "label": "烈阳", "remark": "阳性攻击", "mounts": [10003]},
                             {"value": "atSolarOvercomeBase", "label": "日炎", "remark": "阳性破防", "mounts": [10003]},
                             {"value": "atSolarCriticalStrike", "label": "燎原", "remark": "阳性会心", "mounts": [10003]},
                             {"value": "atSolarCriticalDamagePowerBase", "label": "浴火", "remark": "阳性会效",
                              "mounts": [10003]}, {"value": "atNeutralAttackPowerBase", "label": "雷鸣", "remark": "混元攻击",
                                                   "mounts": [10014, 10021, 10615]},
                             {"value": "atNeutralOvercomeBase", "label": "混沌", "remark": "混元破防",
                              "mounts": [10014, 10021, 10615]},
                             {"value": "atNeutralCriticalStrike", "label": "融天", "remark": "混元会心",
                              "mounts": [10014, 10021, 10028, 10615]},
                             {"value": "atNeutralCriticalDamagePowerBase", "label": "霹雳", "remark": "混元会效",
                              "mounts": [10014, 10021, 10028, 10615]},
                             {"value": "atLunarAttackPowerBase", "label": "霜冷", "remark": "阴性攻击",
                              "mounts": [10081, 10447]},
                             {"value": "atLunarOvercomeBase", "label": "冻髓", "remark": "阴性破防",
                              "mounts": [10081, 10447]},
                             {"value": "atLunarCriticalStrike", "label": "化雪", "remark": "阴性会心",
                              "mounts": [10080, 10081, 10447, 10448]},
                             {"value": "atLunarCriticalDamagePowerBase", "label": "杯雪", "remark": "阴性会效",
                              "mounts": [10080, 10081, 10447, 10448]},
                             {"value": "atPoisonAttackPowerBase", "label": "鹤顶", "remark": "毒性攻击",
                              "mounts": [10175, 10225, 10627]},
                             {"value": "atPoisonOvercomeBase", "label": "腐心", "remark": "毒性破防",
                              "mounts": [10175, 10225, 10627]},
                             {"value": "atPoisonCriticalStrike", "label": "蚀骨", "remark": "毒性会心",
                              "mounts": [10175, 10176, 10626, 10627]},
                             {"value": "atPoisonCriticalDamagePowerBase", "label": "穿石", "remark": "毒性会效",
                              "mounts": [10175, 10176, 10626, 10627]},
                             {"value": "atSolarAndLunarAttackPowerBase", "label": "琉璃", "remark": "阴阳攻击",
                              "mounts": [10242, 10243]},
                             {"value": "atSolarAndLunarOvercomeBase", "label": "焚虚", "remark": "阴阳破防",
                              "mounts": [10242, 10243]},
                             {"value": "atSolarAndLunarCriticalStrike", "label": "虹卷", "remark": "阴阳会心",
                              "mounts": [10242, 10243]},
                             {"value": "atSolarAndLunarCriticalDamagePowerBase", "label": "界影", "remark": "阴阳会效",
                              "mounts": [10242, 10243]}, {"value": "placeholder", "label": "分割线"},
                             {"value": "atAllTypeCriticalStrike", "label": "强击", "remark": "全会心",
                              "mounts": [10003, 10014, 10015, 10021, 10026, 10028, 10080, 10081, 10144, 10145, 10175,
                                         10176, 10224, 10225, 10242, 10243, 10268, 10390, 10447, 10448, 10464, 10698,
                                         10533, 10585, 10615, 10626, 10627]},
                             {"value": "atAllTypeCriticalDamagePowerBase", "label": "刚烈", "remark": "全会效",
                              "mounts": [10003, 10014, 10015, 10021, 10026, 10028, 10080, 10081, 10144, 10145, 10175,
                                         10176, 10224, 10225, 10242, 10243, 10268, 10390, 10447, 10448, 10464, 10698,
                                         10533, 10585, 10615, 10626, 10627]}, {"value": "placeholder", "label": "分割线"},
                             {"value": "atBasePotentialAdd", "label": "固本", "remark": "全属性",
                              "mounts": [10002, 10003, 10014, 10015, 10021, 10026, 10028, 10062, 10080, 10081, 10144,
                                         10145, 10175, 10176, 10224, 10225, 10242, 10243, 10268, 10389, 10390, 10447,
                                         10448, 10464, 10698, 10533, 10585, 10615, 10626, 10627]},
                             {"value": "atVitalityBase", "label": "霸体", "remark": "体质",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atVitalityBasePercentAdd", "label": "健体", "remark": "体质（百分比）",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atStrengthBase", "label": "真刚", "remark": "力道",
                              "mounts": [10026, 10224, 10268, 10464, 10698]},
                             {"value": "atStrengthBasePercentAdd", "label": "聚力", "remark": "力道（百分比）",
                              "mounts": [10026, 10224, 10268, 10464, 10698]},
                             {"value": "atAgilityBase", "label": "瞬影", "remark": "身法",
                              "mounts": [10015, 10144, 10145, 10390, 10533, 10585]},
                             {"value": "atAgilityBasePercentAdd", "label": "强身", "remark": "身法（百分比）",
                              "mounts": [10015, 10144, 10145, 10390, 10533, 10585]},
                             {"value": "atSpiritBase", "label": "灵根", "remark": "根骨",
                              "mounts": [10014, 10028, 10080, 10081, 10175, 10176, 10447, 10448, 10626, 10627]},
                             {"value": "atSpiritBasePercentAdd", "label": "固筋", "remark": "根骨（百分比）",
                              "mounts": [10014, 10028, 10080, 10081, 10175, 10176, 10447, 10448, 10626, 10627]},
                             {"value": "atSpunkBase", "label": "真元", "remark": "元气",
                              "mounts": [10003, 10014, 10021, 10615]},
                             {"value": "atSpunkBasePercentAdd", "label": "聚魂", "remark": "元气（百分比）",
                              "mounts": [10003, 10014, 10021, 10615]}, {"value": "placeholder", "label": "分割线"},
                             {"value": "atGlobalResistPercent", "label": "铁壁", "remark": "通用减伤",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atBeTherapyCoefficient", "label": "清源", "remark": "承疗提升",
                              "mounts": [10002, 10062, 10243, 10389]},
                             {"value": "atManaReplenishExt", "label": "潮生", "remark": "内力恢复", "mounts": [0]},
                             {"value": "atMoveSpeedPercent", "label": "迅疾", "remark": "移动速度", "mounts": [0]},
                             {"value": "atModifyCostManaPercent", "label": "延绵", "remark": "内力消耗降低（百分比）",
                              "mounts": [0]},
                             {"value": "atDamageToLifeForSelf", "label": "嗜血", "remark": "生命偷取", "mounts": [0]}],
                     "origin": [{"value": "atPhysicsAttackPowerBase", "label": "锐刃", "remark": "外功攻击",
                                 "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atPhysicsHitValue", "label": "心眼", "remark": "外功命中",
                                 "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atPhysicsOvercomeBase", "label": "斩铁", "remark": "外功破防",
                                 "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atPhysicsCriticalStrike", "label": "见切", "remark": "外功会心",
                                 "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atPhysicsCriticalDamagePowerBase", "label": "痛击", "remark": "外功会效",
                                 "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atMeleeWeaponDamageBase", "label": "狂攻", "remark": "武器伤害",
                                 "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atMagicAttackPowerBase", "label": "激流", "remark": "内功攻击",
                                 "mounts": [10003, 10014, 10021, 10081, 10175]},
                                {"value": "atMagicHitValue", "label": "灵识", "remark": "内功命中",
                                 "mounts": [10003, 10014, 10021, 10081, 10175]},
                                {"value": "atMagicOvercome", "label": "灭气", "remark": "内功破防",
                                 "mounts": [10003, 10014, 10021, 10081, 10175]},
                                {"value": "atMagicCriticalStrike", "label": "星见", "remark": "内功会心",
                                 "mounts": [10003, 10014, 10021, 10028, 10080, 10081, 10175, 10176]},
                                {"value": "atMagicCriticalDamagePowerBase", "label": "月华", "remark": "内功会效",
                                 "mounts": [10003, 10014, 10021, 10028, 10080, 10081, 10175, 10176]},
                                {"value": "atPhysicsShieldAdditional", "label": "守御", "remark": "外功防御",
                                 "mounts": [10002, 10062]},
                                {"value": "atMagicShield", "label": "耐受", "remark": "内功防御", "mounts": [10002, 10062]},
                                {"value": "atMaxLifeAdditional", "label": "血魂", "remark": "最大气血",
                                 "mounts": [10002, 10062]},
                                {"value": "atActiveThreatCoefficient", "label": "忘我", "remark": "威胁值",
                                 "mounts": [10002, 10062]},
                                {"value": "atTherapyPowerBase", "label": "海纳", "remark": "治疗",
                                 "mounts": [10028, 10080, 10176]},
                                {"value": "atTherapyCoefficient", "label": "妙手", "remark": "治疗（百分比）",
                                 "mounts": [10028, 10080, 10176]}, {"value": "placeholder", "label": "分割线"},
                                {"value": "atStrainBase", "label": "无双", "remark": "无双",
                                 "mounts": [10002, 10003, 10014, 10015, 10021, 10026, 10062, 10081, 10144, 10145,
                                            10175]},
                                {"value": "atToughnessBase", "label": "大御", "remark": "御劲", "mounts": []},
                                {"value": "atDecriticalDamagePowerBase", "label": "大化", "remark": "化劲", "mounts": []},
                                {"value": "atParryBase", "label": "不屈", "remark": "招架", "mounts": [10002, 10062]},
                                {"value": "atParryValueBase", "label": "破势", "remark": "拆招", "mounts": [10002, 10062]},
                                {"value": "atDodge", "label": "灵动", "remark": "闪避", "mounts": [10002, 10062]},
                                {"value": "atLifeReplenishExt", "label": "回春", "remark": "气血恢复",
                                 "mounts": [10002, 10062]}, {"value": "placeholder", "label": "分割线"},
                                {"value": "atSolarAttackPowerBase", "label": "烈阳", "remark": "阳性攻击", "mounts": [10003]},
                                {"value": "atSolarHitValue", "label": "灼筋", "remark": "阳性命中", "mounts": [10003]},
                                {"value": "atSolarOvercomeBase", "label": "日炎", "remark": "阳性破防", "mounts": [10003]},
                                {"value": "atSolarCriticalStrike", "label": "燎原", "remark": "阳性会心", "mounts": [10003]},
                                {"value": "atSolarCriticalDamagePowerBase", "label": "浴火", "remark": "阳性会效",
                                 "mounts": [10003]},
                                {"value": "atNeutralAttackPowerBase", "label": "雷鸣", "remark": "混元攻击",
                                 "mounts": [10014, 10021]},
                                {"value": "atNeutralHitValue", "label": "裂激", "remark": "混元命中",
                                 "mounts": [10014, 10021]},
                                {"value": "atNeutralOvercomeBase", "label": "混沌", "remark": "混元破防",
                                 "mounts": [10014, 10021]},
                                {"value": "atNeutralCriticalStrike", "label": "融天", "remark": "混元会心",
                                 "mounts": [10014, 10021, 10028]},
                                {"value": "atNeutralCriticalDamagePowerBase", "label": "霹雳", "remark": "混元会效",
                                 "mounts": [10014, 10021, 10028]},
                                {"value": "atLunarAttackPowerBase", "label": "霜冷", "remark": "阴性攻击", "mounts": [10081]},
                                {"value": "atLunarHitValue", "label": "碎冰", "remark": "阴性命中", "mounts": [10081]},
                                {"value": "atLunarOvercomeBase", "label": "冻髓", "remark": "阴性破防", "mounts": [10081]},
                                {"value": "atLunarCriticalStrike", "label": "化雪", "remark": "阴性会心",
                                 "mounts": [10081, 10080]},
                                {"value": "atLunarCriticalDamagePowerBase", "label": "杯雪", "remark": "阴性会效",
                                 "mounts": [10080, 10081]},
                                {"value": "atPoisonAttackPowerBase", "label": "鹤顶", "remark": "毒性攻击",
                                 "mounts": [10175]},
                                {"value": "atPoisonHitValue", "label": "化玉", "remark": "毒性命中", "mounts": [10175]},
                                {"value": "atPoisonOvercomeBase", "label": "腐心", "remark": "毒性破防", "mounts": [10175]},
                                {"value": "atPoisonCriticalStrike", "label": "蚀骨", "remark": "毒性会心",
                                 "mounts": [10175, 10176]},
                                {"value": "atPoisonCriticalDamagePowerBase", "label": "穿石", "remark": "毒性会效",
                                 "mounts": [10175, 10176]},
                                {"value": "atSolarAndLunarAttackPowerBase", "label": "琉璃", "remark": "阴阳攻击",
                                 "mounts": [0]},
                                {"value": "atSolarAndLunarHitValue", "label": "点睛", "remark": "阴阳命中", "mounts": [0]},
                                {"value": "atSolarAndLunarOvercomeBase", "label": "焚虚", "remark": "阴阳破防",
                                 "mounts": [0]},
                                {"value": "atSolarAndLunarCriticalStrike", "label": "虹卷", "remark": "阴阳会心",
                                 "mounts": [0]},
                                {"value": "atSolarAndLunarCriticalDamagePowerBase", "label": "界影", "remark": "阴阳会效",
                                 "mounts": [0]}, {"value": "placeholder", "label": "分割线"},
                                {"value": "atAllTypeCriticalStrike", "label": "强击", "remark": "全会心",
                                 "mounts": [10015, 10026, 10003, 10014, 10021, 10028, 10080, 10081, 10175, 10176]},
                                {"value": "atAllTypeCriticalDamagePowerBase", "label": "刚烈", "remark": "全会效",
                                 "mounts": [10003, 10014, 10015, 10021, 10026, 10028, 10080, 10081, 10175, 10176]},
                                {"value": "placeholder", "label": "分割线"},
                                {"value": "atBasePotentialAdd", "label": "固本", "remark": "全属性", "mounts": []},
                                {"value": "atVitalityBase", "label": "霸体", "remark": "体质", "mounts": [10002, 10062]},
                                {"value": "atVitalityBasePercentAdd", "label": "健体", "remark": "体质（百分比）",
                                 "mounts": [10002, 10062]}, {"value": "atStrengthBase", "label": "真刚", "remark": "力道",
                                                             "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atStrengthBasePercentAdd", "label": "聚力", "remark": "力道（百分比）",
                                 "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atAgilityBase", "label": "瞬影", "remark": "身法",
                                 "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atAgilityBasePercentAdd", "label": "强身", "remark": "身法（百分比）",
                                 "mounts": [10015, 10026, 10144, 10145]},
                                {"value": "atSpiritBase", "label": "灵根", "remark": "根骨",
                                 "mounts": [10015, 10003, 10021, 10014, 10028, 10080, 10081, 10175, 10176]},
                                {"value": "atSpiritBasePercentAdd", "label": "固筋", "remark": "根骨（百分比）",
                                 "mounts": [10003, 10014, 10021, 10081, 10028, 10080, 10175, 10176]},
                                {"value": "atSpunkBase", "label": "真元", "remark": "元气",
                                 "mounts": [10003, 10014, 10021, 10081]},
                                {"value": "atSpunkBasePercentAdd", "label": "聚魂", "remark": "元气（百分比）",
                                 "mounts": [10003, 10014, 10021, 10081]}, {"value": "placeholder", "label": "分割线"},
                                {"value": "atGlobalResistPercent", "label": "铁壁", "remark": "通用减伤（百分比）",
                                 "mounts": [10002, 10062]},
                                {"value": "atBeTherapyCoefficient", "label": "清源", "remark": "承疗提升",
                                 "mounts": [10002, 10062]},
                                {"value": "atManaReplenishExt", "label": "潮生", "remark": "内力恢复",
                                 "mounts": [10002, 10003, 10014, 10015, 10021, 10026, 10028, 10062, 10080, 10081, 10175,
                                            10176]},
                                {"value": "atMoveSpeedPercent", "label": "迅疾", "remark": "移动速度", "mounts": []},
                                {"value": "atModifyCostManaPercent", "label": "延绵", "remark": "内力消耗降低（百分比）",
                                 "mounts": [10002, 10003, 10014, 10015, 10021, 10026, 10028, 10062, 10080, 10081, 10175,
                                            10176]}, {"value": "atDamageToManaForSelf", "label": "吸星", "remark": "内力偷取",
                                                      "mounts": [10002, 10003, 10014, 10015, 10021, 10026, 10028, 10062,
                                                                 10080, 10081, 10175, 10176]},
                                {"value": "atDamageToLifeForSelf", "label": "固本", "remark": "生命偷取", "mounts": []}]}




