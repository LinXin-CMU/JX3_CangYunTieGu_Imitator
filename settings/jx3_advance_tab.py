# coding: utf-8
# author: LinXin
from scripts.include.slot import attrib_data


TABLES = {
    "断浪·水晶芙蓉宴": {
        'attr': [attrib_data("atVitalityBase", 536)],
        'desc': "使用：摆出一桌宴席，食用后提升当前内功最受增益的基础属性324点（体质为536点），效果持续一个小时。"
    },
    "断浪·玉笛谁家听落梅": {
        'attr': [attrib_data("atPhysicsAttackPowerBase", 326), attrib_data("atAllTypeCriticalStrike", 723), attrib_data("atAllTypeCriticalStrike", 723)],
        'desc': "使用：摆出一桌宴席，团队成员均可食用。外功攻击提高326点，全会心提高723点，破招提高723点，持续60分钟。"
    },
    "断浪·鸳鸯烩珍宴": {
        'attr': [attrib_data("atAllTypeCriticalStrike", 723), attrib_data("atHasteBase", 723)],
        'desc': "使用：摆出一桌宴席，团队成员均可食用。疗伤提高351点，全会心提高723点，急速值提高723点，持续60分钟。"
    },
    "断浪·蜀味烘焙宴": {
        'attr': [attrib_data("atVitalityBase", 268), attrib_data("atMaxLifeAdditional", 3616), attrib_data("atActiveThreatCoefficient", 829)],
        'desc': "使用：摆出一桌宴席，团队成员均可食用。体质提高268点，仇恨值提高45%，最大气血提高3616点，持续60分钟。"
    },
    "断浪·鸿门宴": {
        'attr': [attrib_data("atVitalityBase", 268), attrib_data("atDecriticalDamagePowerBase", 362), attrib_data("atToughnessBase", 362)],
        'desc': "使用：摆出一桌宴席，团队成员均可食用。体质提高268点，化劲提高362点，御劲提高362点，持续60分钟。"
    },
    "同泽宴": {
        'attr': [attrib_data("atSurplusValueBase", 192), attrib_data("atStrainBase", 192)],
        'desc': "使用：无双值提升192点，破招值提升192点。持续一个小时，可以和其他宴席效果同时存在。"
    },
    "炼狱水煮鱼": {
        'attr': [attrib_data("atStrainBase", 100), attrib_data("atSurplusValueBase", 100)],
        'desc': "由炼狱厨神创制的水煮鱼，堪称人间美味，功效不同凡响。无双增加100点，破招增加100点。可以和其他宴席效果叠加。"
    },
    "蒸鱼菜盘": {
        'attr': [attrib_data("atStrainBase", 517)],
        'desc': "无双值提高517点，持续60分钟。"
    }
}

ADVANCE_MEDICINE = {
    "断浪·上品破秽散(破防)": {
        'attr': [attrib_data("atPhysicsOvercomeBase", 1627), attrib_data("atMagicOvercome", 1627)],
        'desc': "使用：全破防提高1627点，持续30分钟。"
    },
    "断浪·上品玉璃散(会心)": {
        'attr': [attrib_data("atAllTypeCriticalStrike", 1627)],
        'desc': "使用：全会心提高1627点，持续30分钟。"
    },
    "断浪·上品凝神散(破招)": {
        'attr': [attrib_data("atSurplusValueBase", 1627)],
        'desc': "使用：破招提高1627点，持续30分钟。"
    },
    "断浪·上品活气散(加速)": {
        'attr': [attrib_data("atHasteBase", 1627)],
        'desc': "使用：急速值提高1627点，持续30分钟。"
    },
    "断浪·上品亢龙散(攻击)": {
        'attr': [attrib_data("atPhysicsAttackPowerBase", 733)],
        'desc': "使用：外功攻击提高733点，持续30分钟。"
    },
}

ADVANCE_FOOD = {
    "断浪·红烧排骨(破防)": {
        'attr': [attrib_data("atPhysicsOvercomeBase", 1266), attrib_data("atMagicOvercome", 1266)],
        'desc': "使用：全破防提高1266点，持续30分钟。"
    },
    "断浪·酸菜鱼(会心)": {
        'attr': [attrib_data("atAllTypeCriticalStrike", 1266)],
        'desc': "使用：全会心提高1266点，持续30分钟。"
    },
    "断浪·白肉血肠(破招)": {
        'attr': [attrib_data("atSurplusValueBase", 1266)],
        'desc': "使用：破招提高1266点，持续30分钟。"
    },
    "断浪·红烧扣肉(加速)": {
        'attr': [attrib_data("atHasteBase", 1266)],
        'desc': "使用：急速值提高1266点，持续30分钟。"
    },
    "断浪·太后饼(攻击)": {
        'attr': [attrib_data("atPhysicsAttackPowerBase", 570)],
        'desc': "使用：外功攻击提高570点，持续30分钟。"
    },
}

ASSIST_MEDICINE = {
    "断浪·上品健体丸(体质)": {
        'attr': [attrib_data("atVitalityBase", 603)],
        'desc': "使用：体质提高603点，持续30分钟。"
    },
    "断浪·上品轻身丹(身法)": {
        'attr': [attrib_data("atAgilityBase", 365)],
        'desc': "使用：身法提高365点，持续30分钟。"
    },
    "断浪·上品大力丸(力道)": {
        'attr': [attrib_data("atStrengthBase", 365)],
        'desc': "使用：力道提高365点，持续30分钟。"
    },
}

ASSIST_FOOD = {
    "断浪·皮蛋瘦肉粥(体质)": {
        'attr': [attrib_data("atVitalityBase", 469)],
        'desc': "使用：体质提高469点，持续30分钟。"
    },
    "断浪·杂锦鱼球粥(身法)": {
        'attr': [attrib_data("atAgilityBase", 284)],
        'desc': "使用：身法提高284点，持续30分钟。"
    },
    "断浪·三鲜粥(力道)": {
        'attr': [attrib_data("atStrengthBase", 284)],
        'desc': "使用：力道提高284点，持续30分钟。"
    },
}

WEAPON_ENCHANT = {
    "断浪·瀑沙熔锭(外攻)": {
        'attr': [attrib_data("atPhysicsAttackPowerBase", 489)],
        'desc': "使用：外功攻击提升489点，持续30分钟。"
    },
}

HOME_FOOD = {
    "创意料理·盛·破防": {
        'attr': [attrib_data("atMaxLifeAdditional", -10562), attrib_data("atPhysicsOvercomeBase", 1584), attrib_data("atMagicOvercome", 1584)],
        'desc': "气血值降低10562点，全破防等级提高1584点"
    },
    "创意料理·盛·会心": {
        'attr': [attrib_data("atMaxLifeAdditional", -10562), attrib_data("atAllTypeCriticalStrike", 1584)],
        'desc': "气血值降低10562点，会心等级提高1584点"
    },
    "创意料理·盛·攻击": {
        'attr': [attrib_data("atMaxLifeAdditional", -10562), attrib_data("atPhysicsAttackPowerBase", 708)],
        'desc': "气血值降低10562点，外功攻击提高708点"
    },
    "创意料理·盛·无双": {
        'attr': [attrib_data("atMaxLifeAdditional", -10562), attrib_data("atStrainBase", 1584)],
        'desc': "气血值降低10562点，无双提高1584点"
    },
    "创意料理·盛·破招": {
        'attr': [attrib_data("atStrainBase", -704), attrib_data("atSurplusValueBase", 1584)],
        'desc': "无双降低704点，破招提高1584点"
    },
    "葫芦叫花鸡(攻击)": {
        'attr': [attrib_data("atPhysicsAttackPowerBase", 262)],
        'desc': "外功攻击提高262点"
    },
    "清蒸鲈鱼(破防)": {
        'attr': [attrib_data("atPhysicsOvercomeBase", 586), attrib_data("atMagicOvercome", 586)],
        'desc': "全破防提高586点"
    },
    "炖豆腐(无双)": {
        'attr': [attrib_data("atStrainBase", 586)],
        'desc': "无双提高586点"
    },
    "炸鱼干(会心)": {
        'attr': [attrib_data("atAllTypeCriticalStrike", 586)],
        'desc': "全会心提高586点"
    },
    "煎豆腐(破招)": {
        'attr': [attrib_data("atSurplusValueBase", 586)],
        'desc': "破招提高586点"
    },
}

HOME_WINE = {
    "女儿红(加速)": {
        'attr': [attrib_data("atHasteBase", 234)],
        'desc': "使用：急速等级提高234点，持续30分钟。"
    },
    "女儿红·今朝醉(加速)": {
        'attr': [attrib_data("atHasteBase", 468)],
        'desc': "使用：急速等级提高468点，持续30分钟。"
    },
    "女儿红·六日醉(加速)": {
        'attr': [attrib_data("atHasteBase", 702)],
        'desc': "使用：急速等级提高702点，持续30分钟。"
    },
    "女儿红·旬又三(加速)": {
        'attr': [attrib_data("atHasteBase", 936)],
        'desc': "使用：急速等级提高936点，持续30分钟。"
    },
    "关外白酒(身法)": {
        'attr': [attrib_data("atAgilityBase", 52)],
        'desc': "使用：身法提高52点，持续30分钟。"
    },
    "关外白酒·今朝醉(身法)": {
        'attr': [attrib_data("atAgilityBase", 104)],
        'desc': "使用：身法提高104点，持续30分钟。"
    },
    "关外白酒·六日醉(身法)": {
        'attr': [attrib_data("atAgilityBase", 156)],
        'desc': "使用：身法提高156点，持续30分钟。"
    },
    "关外白酒·旬又三(身法)": {
        'attr': [attrib_data("atAgilityBase", 208)],
        'desc': "使用：身法提高208点，持续30分钟。"
    },
    "汾酒(力道)": {
        'attr': [attrib_data("atStrengthBase", 52)],
        'desc': "使用：力道提高52点，持续30分钟。"
    },
    "汾酒·今朝醉(力道)": {
        'attr': [attrib_data("atStrengthBase", 104)],
        'desc': "使用：力道提高104点，持续30分钟。"
    },
    "汾酒·六日醉(力道)": {
        'attr': [attrib_data("atStrengthBase", 156)],
        'desc': "使用：力道提高156点，持续30分钟。"
    },
    "汾酒·旬又三(力道)": {
        'attr': [attrib_data("atStrengthBase", 208)],
        'desc': "使用：力道提高208点，持续30分钟。"
    },
}

SKILL_NOT_BELONGS_TO_SELF = {
    # 所有队友技能的id，用于导出战斗记录时筛选出不属于自身的技能
    15115: "号令三军",
    18872: "劲风",
    2603: "乘龙箭",
    403: "破风",
    15195: "舍身弘法",
    3985: "朝圣言",
    3980: "戒火斩",
    50012: "振奋",
    50013: "寒啸千军",
    50014: "虚弱",
    31208: "秋肃",
    32381: "落子无悔",
    567: "左旋右转",
    30850: "泠风解怀",
    2234: "仙王蛊鼎",
    14071: "梅花三弄",
    23826: "弄梅",
    28650: "香稠",
    28722: "配伍",
    28678: "飘黄",
}





