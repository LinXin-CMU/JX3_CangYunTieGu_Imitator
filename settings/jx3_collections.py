# coding: utf-8
# author: LinXin

talent = {
    "铁骨衣": {
        "1": {
            "1": {"name": "狂刀", "icon": 6439, "desc": "盾刀造成的威胁值提高30%。", "order": "1", "pos": 1, "is_skill": 0, "meta": None,
                  "extend": None, "id": "13338"},
            "2": {"name": "盾威", "icon": 6285, "desc": "“盾飞”命中目标使目标所有伤害输出降低5%，持续15秒。", "order": "1", "pos": 2, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13320"},
            "3": {"name": "权门", "icon": 6328, "desc": "“盾飞”伤害降低20%，可对击中的目标周围10尺的其他敌对目标进行弹射。", "order": "1", "pos": 3,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13318"}},
        "2": {
            "1": {"name": "炼狱", "icon": 6320, "desc": "流血效果作用时间间隔缩短1秒，总持续时间保持不变。", "order": "2", "pos": 1, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13089"},
            "2": {"name": "出尘", "icon": 6329, "desc": "受自身招架率影响有%的几率触发，使“盾刀”第三段攻击追加一次伤害。", "order": "2", "pos": 2,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13121"},
            "3": {"name": "激昂", "icon": 6352, "desc": "施展“盾猛”后使自身基础招架等级提高10%，基础拆招值提高10%，持续6秒。", "order": "2", "pos": 3,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13356"}},
        "3": {
            "1": {"name": "慑服", "icon": 6321, "desc": "施展“无惧”使自身御劲率提高5%，持续8秒。", "order": "3", "pos": 1, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13122"},
            "2": {"name": "戍卫", "icon": 6318, "desc": "施展“斩刀”使自身受到伤害降低20%，持续3秒，且强制目标攻击自身。", "order": "3", "pos": 2,
                  "is_skill": 0, "meta": None, "extend": None, "id": "20509"},
            "3": {"name": "勇决", "icon": 11869, "desc": "“血怒”状态下，每1点拆招值为自己添加0.06点内功防御等级。", "order": "3", "pos": 3, "is_skill": 0,
                  "meta": None, "extend": None, "id": "23929"},
            "4": {"name": "铿锵", "icon": 6438, "desc": "怒气上限提高10点，成功招架后回复自身5%气血最大值，该效果最多每6秒触发一次。", "order": "3", "pos": 4,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13136"}},
        "4": {
            "1": {"name": "强袭", "icon": 6330, "desc": "“盾刀”第三段攻击命中有自身虚弱或流血效果的目标后可触发第四段攻击，第四段攻击额外回复10点怒气。", "order": "4",
                  "pos": 1, "is_skill": 0, "meta": None, "extend": None, "id": "13120"},
            "2": {"name": "潜心", "icon": 6341, "desc": "“盾舞”作用目标提高2个，造成的威胁值提高50%。", "order": "4", "pos": 2, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13360"},
            "3": {"name": "坚铁", "icon": 6353, "desc": "受到任何技能伤害都使自身招架率提高6%，最多可叠加5层，成功招架后该效果不再叠加，8秒后效果消失。", "order": "4",
                  "pos": 3, "is_skill": 0, "meta": None, "extend": None, "id": "13138"},
            "4": {"name": "卷云", "icon": 6316, "desc": "“盾刀”每一段招式伤害逐步递增，施展第三段时将卸除目标混元、阳性、阴性、毒性有益气劲各一个。", "order": "4", "pos": 4,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13321"}},
        "5": {
            "1": {"name": "千山", "icon": 6342, "desc": "施展“盾挡”后获得的招架率、拆招值提升效果提高30%。", "order": "5", "pos": 1, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13421"},
            "2": {"name": "振奋", "icon": 6436, "desc": "施展“盾挡”后，自身每1500点招架等级使得自身20尺范围内最多25个团队成员外功、内功破防等级提高60点，持续10秒。",
                  "order": "5", "pos": 2, "is_skill": 0, "meta": None, "extend": None, "id": "13422"},
            "3": {"name": "震怒", "icon": 6310, "desc": "“盾压”“盾猛”额外回复10点怒气。", "order": "5", "pos": 3, "is_skill": 0, "meta": None,
                  "extend": None, "id": "13361"},
            "4": {"name": "胜前", "icon": 6423, "desc": "盾击充能时间延长至20秒，每1%的招架率回复自身0.5%的气血最大值。", "order": "5", "pos": 4,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13113"}},
        "6": {
            "1": {"name": "割裂", "icon": 6294, "desc": "“闪刀”命中有自身流血效果的目标使流血效果的剩余伤害提高90%。", "order": "6", "pos": 1, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13132"},
            "2": {"name": "怒炎", "icon": 6348, "desc": "施展“盾飞”，“斩刀”调息时间降低5秒，且使“绝刀”“斩刀”伤害增加30%，持续15秒。若施展“斩刀”命中虚弱非侠士目标，则获得持续4秒的“怒炎”效果：施展“绝刀”可返还所消耗的怒气，并额外获得一次在“怒炎”效果期间施展“绝刀”的机会。",
                  "order": "6", "pos": 2, "is_skill": 0, "meta": None, "extend": None, "id": "13133"},
            "3": {"name": "当关", "icon": 6313, "desc": "“盾飞”附带嘲讽效果，强制目标攻击自身3秒，10秒内此目标不会再被嘲讽。", "order": "6", "pos": 3,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13368"},
            "4": {"name": "活血", "icon": 6433, "desc": "体质和被疗伤效果提高10%。", "order": "6", "pos": 4, "is_skill": 0, "meta": None,
                  "extend": None, "id": "13124"}},
        "7": {
            "1": {"name": "雷云", "icon": 6287, "desc": "“盾飞”命中的第一个目标若正在运功，则使该目标2秒内无法运功。", "order": "7", "pos": 1, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13397"},
            "2": {"name": "坚韧", "icon": 6335, "desc": "格挡值最大值增加100点，“盾墙”调息时间降低5秒，持续期间自身气血最大值提高30%。", "order": "7", "pos": 2,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13363"},
            "3": {"name": "肆意", "icon": 6430, "desc": "盾墙效果消失后，使自身团队成员获得无威胁气劲，持续6秒。", "order": "7", "pos": 3, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13364"},
            "4": {"name": "蔑视", "icon": 7248, "desc": "施展伤害招式命中目标，若自身气血百分比高于目标气血百分比，则使下一招式无视目标50%外功防御等级，且对击倒、被击僵直目标伤害提高15%。",
                  "order": "7", "pos": 4, "is_skill": 0, "meta": None, "extend": None, "id": "14838"}},
        "8": {
            "1": {"name": "雄峦", "icon": 6481, "desc": "施展“盾压”使自身获得雄峦效果，效果期间使自身化解相当于自身拆招值的伤害量，持续8秒。", "order": "8", "pos": 1,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13098"},
            "2": {"name": "盾反", "icon": 6333,"desc": "“盾壁”效果消失4秒内可施展，期间造成的威胁值提高30%，施展后将盾壁化解伤害的80%施放出来造成半径8尺的群体伤害效果，每额外命中一个目标，“盾壁”调息时间降低7秒，“无惧”调息时间降低1秒，伤害提高20%，最多可命中5个目标。",
                  "order": "8", "pos": 2, "is_skill": 1, "meta": "兵来将挡，绝处逢生。", "extend": "攻击技，攻击目标越多，造成的伤害效果越高。", "id": "13071"},
            "3": {"name": "返生", "icon": 6334, "desc": "施展“盾壁”使自身立即回复自身10%气血最大值，并回复自身30%格挡值。", "order": "8", "pos": 3,
                  "is_skill": 0, "meta": None, "extend": None, "id": "18723"},
            "4": {"name": "恋战", "icon": 6303, "desc": "施展任何伤害技能都使自身会心率提高3%，最多可叠加10层，技能会心后该效果不再叠加，8秒后效果消失。", "order": "8",
                  "pos": 4, "is_skill": 0, "meta": None, "extend": None, "id": "13126"},
            "5": {"name": "坚固", "icon": 14085, "desc": "成功招架后自身回复1.5%的气血值，此效果每秒最多触发5次。", "order": "8", "pos": 5, "is_skill": 0,
                  "meta": None, "extend": None, "id": "25216"}},
        "9": {
            "1": {"name": "从容", "icon": 6432, "desc": "当自身血量高于60%，则外功基础攻击提高20%。", "order": "9", "pos": 1, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13366"},
            "2": {"name": "赤心", "icon": 6305, "desc": "“血怒”效果期间每消耗或回复1点怒气为自身回复0.1%气血最大值。", "order": "9", "pos": 2,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13073"},
            "3": {"name": "百炼", "icon": 6338, "desc": "“盾壁”变为2层充能招式，充能时间1分20秒，伤害吸收效果提升至100%。", "order": "9", "pos": 3,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13367"},
            "4": {"name": "捍卫", "icon": 6300, "desc": "“盾墙”效果期间自身半径8尺范围内最多5个友方目标受到的伤害降低40%，免疫所有控制效果（被拉除外）。", "order": "9",
                  "pos": 4, "is_skill": 0, "meta": None, "extend": None, "id": "13418"},
            "5": {"name": "愤恨", "icon": 6437, "desc": "消耗5%气血，“血怒”效果提高30%，持续时间增加至25秒。", "order": "9", "pos": 5, "is_skill": 0,
                  "meta": None, "extend": None, "id": "13304"}},
        "10": {
            "1": {"name": "高城", "icon": 13375, "desc": "“铁骨”气劲效果提高60%，可以额外叠加5层。", "order": "10", "pos": 1, "is_skill": 0,
                  "meta": None, "extend": None, "id": "25715"},
            "2": {"name": "战毅", "icon": 6297, "desc": "施展“盾壁”立刻回复自身20%气血最大值，招式效果期间每秒回复自身3%的气血。", "order": "10", "pos": 2,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13171"},
            "3": {"name": "戒备", "icon": 6311, "desc": "自身血量每下降10%，基础招架等级提高10%，拆招值提高800点。", "order": "10", "pos": 3,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13420"},
            "4": {"name": "寒甲", "icon": 6309, "desc": "成功招架后使自身基础外功攻击力获得提升，提升量相当于自身当前拆招值的50%。", "order": "10", "pos": 4,
                  "is_skill": 0, "meta": None, "extend": None, "id": "13134"},
            "5": {"name": "猛志", "icon": 6324, "desc": "“盾猛”施展后自身获得额外35点怒气和3点格挡值。", "order": "10", "pos": 5, "is_skill": 0,
                  "meta": None, "extend": None, "id": "25219"}},
        "11": {
            "1": {"name": "肃列", "icon": 6325, "desc": "“盾墙”调息时间提高15秒，在“盾墙”下持续超过2秒时，使得自身周围20尺25个团队成员获得“盾壁”效果，可以化解等同于其20%最大气血值的伤害，持续10秒。",
                  "order": "11", "pos": 1, "is_skill": 0, "meta": None, "extend": None, "id": "26729"},
            "2": {"name": "鸿烈", "icon": 6427, "desc": "“无惧”调息时间降低5秒，施展“无惧”对周围8尺范围最多6个目标造成外功伤害，使其强制攻击自身，并使得周围20尺团队成员获得无威胁气劲，持续5秒。",
                  "order": "11", "pos": 2, "is_skill": 0, "meta": None, "extend": None, "id": "26897"},
            "3": {"name": "肃驾", "icon": 7245, "desc": "每消耗15点怒气，回复自身1点格挡值，“分山劲”心法下降低自身“盾立”0.5秒的调息时间。",
                  "order": "11", "pos": 3, "is_skill": 0, "meta": None, "extend": None, "id": "14840"},
            "4": {"name": "石虎", "icon": 7452, "desc": "受到任何伤害攻击导致自身气血值低于40%则立刻重置“盾壁”调息时间，该效果最多每3分钟触发一次。",
                  "order": "11", "pos": 4, "is_skill": 0,"meta": None, "extend": None, "id": "14841"},
            "5": {"name": "严阵", "icon": 6332, "desc": "对敌对目标施展“盾压”使得自身“破招”提高10%，此效果持续15秒，最多叠加5层。",
                  "order": "11", "pos": 5, "is_skill": 0, "meta": None, "extend": None, "id": "25356"}},
        "12": {
            "1": {"name": "崇云", "icon": 6432, "desc": "“血怒”效果期间自身基础拆招值提升15%。受到攻击则使得血怒时间延长2秒，最多触发3次。",
                  "order": "12", "pos": 1, "is_skill": 0, "meta": None, "extend": None, "id": "21749"},
            "2": {"name": "澄生", "icon": 6429, "desc": "“血怒”施展后为自身回复10%气血最大值。", "order": "12", "pos": 2,
                  "is_skill": 0, "meta": None, "extend": None, "id": "14848"},
            "3": {"name": "亮节", "icon": 7223, "desc": "“盾舞”调息时间增加至30秒，强制目标攻击自身并使自身受到的所有伤害降低30%。",
                  "order": "12", "pos": 3, "is_skill": 0, "meta": None, "extend": None, "id": "14849"},
            "4": {"name": "寒啸千军", "icon": 7514, "desc": "消耗20点格挡值，鼓舞友方士气，使自身半径20尺内最多25名友方目标内外功破防等级提高20%，持续15秒。",
                  "order": "12", "pos": 4, "is_skill": 1, "meta": "闻鼓则进，闻金则止，无有不胜。", "extend": "辅助技，有效增加友方近战成员的伤害能力。", "id": "15072"},
            "5": {"name": "断马摧城", "icon": 14087, "desc": "举盾对自身8尺范围最多5个目标造成一次锤击，造成外功伤害并使其眩晕3秒。当前每拥有10点怒气此次伤害提高7.5%，并使其眩晕时长增加0.25秒。被命中的目标受到惊吓，攻击力下降50%，并在5秒内逐渐恢复。外功伤害>",
                  "order": "12", "pos": 5, "is_skill": 1, "meta": "高城楼橹数千重，一追击地勇摧之。", "extend": "攻击技，擎盾状态下方可施展，造成自身范围的高额伤害，怒气高时施展最佳。", "id": "25213"}}},
    "分山劲": {
        "1": {
             "1": {"name": "刀魂", "icon": 6291, "desc": "擎刀姿态下自身基础外功攻击力提高15%。", "order": "1", "pos": 1, "is_skill": 0,
                   "meta": None, "extend": None, "id": "13317"},
             "2": {"name": "难行", "icon": 6345, "desc": "“盾飞”的最大充能次数提升至5层，且目标被盾牌首次击中时移动速度降低60%，持续6秒。", "order": "1",
                   "pos": 2, "is_skill": 0, "meta": None, "extend": None, "id": "13374"},
             "3": {"name": "权门", "icon": 6328, "desc": "“盾飞”伤害降低20%，可对击中的目标周围10尺的其他敌对目标进行弹射。", "order": "1", "pos": 3,
                   "is_skill": 0, "meta": None, "extend": None, "id": "13318"}}, "2": {
             "1": {"name": "炼狱", "icon": 6320, "desc": "流血效果作用时间间隔缩短1秒，总持续时间保持不变。", "order": "2", "pos": 1,
                   "is_skill": 0, "meta": None, "extend": None, "id": "13089"},
             "2": {"name": "鸣金", "icon": 6315, "desc": "“盾墙”调息时间降低5秒，格挡值最大值增加100点。", "order": "2", "pos": 2,
                   "is_skill": 0, "meta": None, "extend": None, "id": "18354"}, "3": {"name": "绝返", "icon": 6295,
                                                                                      "desc": "“斩刀”伤害提高20%，命中虚弱目标后获得持续6秒的“狂绝”效果：若施展“绝刀”未成功击杀目标，则返还消耗的怒气，并额外获得一次在6秒内施展“绝刀”的机会。",
                                                                                      "order": "2", "pos": 3,
                                                                                      "is_skill": 0, "meta": None,
                                                                                      "extend": None, "id": "13090"}},
                 "3": {"1": {"name": "分野", "icon": 6288, "desc": "“绝刀”会心几率提高15%，会心效果提高20%，施展“绝刀”使得自身伤害提高5%，持续12秒。",
                             "order": "3", "pos": 1, "is_skill": 0, "meta": None, "extend": None, "id": "13087"},
                       "2": {"name": "怒涌", "icon": 13374, "desc": "“擎刀”姿态下，首次降低怒气到10及以下时，使自身接下来6秒内施展招式不再消耗怒气。",
                             "order": "3", "pos": 2, "is_skill": 0, "meta": None, "extend": None, "id": "28514"},
                       "3": {"name": "万仞", "icon": 6308, "desc": "施展“绝刀”后，会对目标周围6尺范围内额外5个目标造成外功伤害。", "order": "3",
                             "pos": 3, "is_skill": 0, "meta": None, "extend": None, "id": "13088"},
                       "4": {"name": "飞瀑", "icon": 6331, "desc": "“盾飞”会心几率提高15%，击中目标后自身回复5点怒气，最多回复25点。", "order": "3",
                             "pos": 4, "is_skill": 0, "meta": None, "extend": None, "id": "13372"}}, "4": {
                 "1": {"name": "战骨", "icon": 12719, "desc": "“盾毅”调息时间降低10秒，伤害提高40%，可以在擎盾状态下直接施展。", "order": "4",
                       "pos": 1, "is_skill": 0, "meta": None, "extend": None, "id": "24098"},
                 "2": {"name": "血魄", "icon": 6341, "desc": "施展“血怒”，清空自身“斩刀”、“绝刀”调息时间，并获得25点怒气。", "order": "4", "pos": 2,
                       "is_skill": 0, "meta": None, "extend": None, "id": "21281"},
                 "3": {"name": "劫生", "icon": 6441, "desc": "“劫刀”施展距离提高2尺，会心几率提高15%，会心效果提高15%。", "order": "4", "pos": 3,
                       "is_skill": 0, "meta": None, "extend": None, "id": "18978"},
                 "4": {"name": "北漠", "icon": 6283, "desc": "“盾击”伤害提高70%，施展“盾击”对自身6尺120度扇形范围的额外5个目标也造成伤害。", "order": "4",
                       "pos": 4, "is_skill": 0, "meta": None, "extend": None, "id": "13109"}}, "5": {
                 "1": {"name": "锋鸣", "icon": 6326, "desc": "“血怒”效果期间自身外功破防等级提高15%，期间外功伤害招式会心，使其持续时间延长6秒，最多触发4次。",
                       "order": "5", "pos": 1, "is_skill": 0, "meta": None, "extend": None, "id": "22897"},
                 "2": {"name": "残裂", "icon": 6434, "desc": "“盾猛”可将目标击退8尺并撞击沿途最多5个其他目标，使其眩晕3秒。", "order": "5", "pos": 2,
                       "is_skill": 0, "meta": None, "extend": None, "id": "13414"},
                 "3": {"name": "叱威", "icon": 6306, "desc": "“盾舞”在盾墙姿态下施展时，可触发二段技能，施展“盾舞·强化”击退周围8尺内最多6个目标。",
                       "order": "5", "pos": 3, "is_skill": 0, "meta": None, "extend": None, "id": "13278"},
                 "4": {"name": "步临", "icon": 6284,
                       "desc": "“盾击”使目标被疗伤成效降低30%，此效果最多可叠加2层，持续12秒。2层时，受到苍云“苍雪刀”套路招式伤害提高5%。", "order": "5", "pos": 4,
                       "is_skill": 0, "meta": None, "extend": None, "id": "13111"}}, "6": {
                 "1": {"name": "割裂", "icon": 6294, "desc": "“闪刀”命中有自身流血效果的目标使流血效果的剩余伤害提高90%。", "order": "6", "pos": 1,
                       "is_skill": 0, "meta": None, "extend": None, "id": "13132"},
                 "2": {"name": "残楼", "icon": 6289, "desc": "自身气血值每降低10%，“劫刀”“绝刀”“斩刀”的伤害提高7%。", "order": "6", "pos": 2,
                       "is_skill": 0, "meta": None, "extend": None, "id": "13086"}, "3": {"name": "血誓", "icon": 18272,
                                                                                          "desc": "若自身气血值高于20%，在“血怒”状态下每次施展“苍雪刀”套路下招式，将消耗自身5%的最大气血值。连续两次对同一目标施展“苍雪刀”套路下招式后，第三次命中该目标的“苍雪刀”套路下招式消耗40%的自身当前气血值，将对目标造成一次外功伤害并附带一层“血誓”效果，持续3秒，效果期间被疗伤成效额外降低30%，可与其他减疗效果叠加。",
                                                                                          "order": "6", "pos": 3,
                                                                                          "is_skill": 0, "meta": None,
                                                                                          "extend": None,
                                                                                          "id": "32618"},
                 "4": {"name": "雷云", "icon": 6287, "desc": "“盾飞”命中的第一个目标若正在运功，则使该目标2秒内无法运功。", "order": "6", "pos": 4,
                       "is_skill": 0, "meta": None, "extend": None, "id": "13397"}}, "7": {
                 "1": {"name": "活脉", "icon": 6433, "desc": "体质和身法提高10%。", "order": "7", "pos": 1, "is_skill": 0,
                       "meta": None, "extend": None, "id": "14903"}, "2": {"name": "隐刀", "icon": 6355,
                                                                           "desc": "最少消耗5点怒气，最多消耗15点怒气，消耗逐渐增加，闪刀命中附带自身虚弱或流血效果的目标后10秒内可连续施展，隐刀命中附带自身虚弱或流血效果的目标可对其造成100%的武器伤害外加点外功伤害，并冲刺穿过目标，期间自身免疫伤害和控制效果，持续1秒，施展次数越多，怒气消耗越高。",
                                                                           "order": "7", "pos": 2, "is_skill": 1,
                                                                           "meta": "无影无踪刀光现，风驰绝尘斩立决。",
                                                                           "extend": "攻击技，穿越目标身体造成中等外功伤害效果。",
                                                                           "id": "13152"},
                 "3": {"name": "血刀", "icon": 6440,
                       "desc": "消耗10点怒气，“闪刀”命中目标后方可施展，可对15尺范围内最多5个目标造成100%的武器伤害外加点外功伤害，若当前目标附带自身的流血效果，则血刀命中的所有目标都将附带一层流血效果。",
                       "order": "7", "pos": 3, "is_skill": 1, "meta": "刀锋锐刃血光溅，修罗身前胆锋芒。",
                       "extend": "攻击技，擎刀状态下方可施展，可对多个目标同时造成伤害效果。", "id": "13153"},
                 "4": {"name": "卷云", "icon": 6316, "desc": "“盾刀”每一段招式伤害逐步递增，施展第三段时将卸除目标混元、阳性、阴性、毒性有益气劲各一个。",
                       "order": "7", "pos": 4, "is_skill": 0, "meta": None, "extend": None, "id": "13321"}}, "8": {
                 "1": {"name": "吓魂", "icon": 6429, "desc": "“绝刀”附带8尺冲刺效果，命中自身流血目标，直接造成最大怒气对应的伤害。", "order": "8",
                       "pos": 1, "is_skill": 0, "meta": None, "extend": None, "id": "21282"},
                 "2": {"name": "过涯", "icon": 16189,
                       "desc": "“盾壁”调息时间降低20秒，持续时间延长4秒。“盾壁”伤害吸收盾效果降低至最大生命值的30%，效果期间提高自身100%最大生命值上限，受到的贯体治疗不生效，非贯体治疗效果在盾壁结束时作用于自身。",
                       "order": "8", "pos": 2, "is_skill": 0, "meta": None, "extend": None, "id": "28490"},
                 "3": {"name": "肃驾", "icon": 7245, "desc": "每消耗15点怒气，回复自身1点格挡值，“分山劲”心法下降低自身“盾立”0.5秒的调息时间。",
                       "order": "8", "pos": 3, "is_skill": 0, "meta": None, "extend": None, "id": "14840"},
                 "4": {"name": "恋战", "icon": 6303, "desc": "施展任何伤害技能都使自身会心率提高3%，最多可叠加10层，技能会心后该效果不再叠加，8秒后效果消失。",
                       "order": "8", "pos": 4, "is_skill": 0, "meta": None, "extend": None, "id": "13126"},
                 "5": {"name": "扶阵", "icon": 14088,
                       "desc": "“盾墙”调息时间降低5秒，“盾墙”状态下，可以施展“盾猛”和“盾击”，施展“盾猛”举盾向前快速冲刺15尺。击晕路径上最多5个目标并造成外功伤害。对终点6尺范围最多5个目标造成100%武器伤害外加外功伤害并且击倒5秒，随后解除自身盾墙状态。",
                       "order": "8", "pos": 5, "is_skill": 0, "meta": None, "extend": None, "id": "25203"}}, "9": {
                 "1": {"name": "从容", "icon": 6432, "desc": "当自身血量高于60%，则外功基础攻击提高20%。", "order": "9", "pos": 1,
                       "is_skill": 0, "meta": None, "extend": None, "id": "13366"},
                 "2": {"name": "赤心", "icon": 6305, "desc": "“血怒”效果期间每消耗或回复1点怒气为自身回复0.1%气血最大值。", "order": "9", "pos": 2,
                       "is_skill": 0, "meta": None, "extend": None, "id": "13073"}, "3": {"name": "千险", "icon": 6435,
                                                                                          "desc": "战斗状态下，自身气血低于35%时解除自身所有控制效果并使自身免疫所有控制效果(被拉除外)并使受到的伤害降低10%，气血高于35%后该效果消失。",
                                                                                          "order": "9", "pos": 3,
                                                                                          "is_skill": 0, "meta": None,
                                                                                          "extend": None,
                                                                                          "id": "13172"},
                 "4": {"name": "卧沙", "icon": 7488, "desc": "“撼地”眩晕效果提高1秒，变为2层充能技能，充能时间为18秒。", "order": "9", "pos": 4,
                       "is_skill": 0, "meta": None, "extend": None, "id": "14839"},
                 "5": {"name": "用御", "icon": 14084, "desc": "擎盾姿态下自身加速率提高10%，每连续施展三次 “云城盾”套路招式技能攻击同一目标，造成外功伤害。",
                       "order": "9", "pos": 5, "is_skill": 0, "meta": None, "extend": None, "id": "26723"}}, "10": {
                 "1": {"name": "愤恨", "icon": 6437, "desc": "消耗5%气血，“血怒”效果提高30%，持续时间增加至25秒。", "order": "10", "pos": 1,
                       "is_skill": 0, "meta": None, "extend": None, "id": "13304"},
                 "2": {"name": "劫化生", "icon": 6346, "desc": "施展“血怒”后获得的“劫化”效果期间每点身法提高自身2点招架等级，持续时间提升至8秒，调息时间提高至38秒。",
                       "order": "10", "pos": 2, "is_skill": 0, "meta": None, "extend": None, "id": "13395"},
                 "3": {"name": "激奋", "icon": 6322,
                       "desc": "施展“盾壁”将会触发10尺范围“振奋军阵”，处于“军阵”中的5个友方目标不会受到重伤，受到伤害提高10%，基础攻击力提高20%，“振奋军阵”持续8秒。此效果不会在秘境中生效。",
                       "order": "10", "pos": 3, "is_skill": 0, "meta": None, "extend": None, "id": "20984"},
                 "4": {"name": "盾抛", "icon": 6296,
                       "desc": "盾墙状态下，施展“盾压”后可施展，震碎自身周围刀气障碍，造成外功伤害并将目标及其周围4尺内3个目标抛至自己身后15尺，并使其眩晕2秒。 盾墙状态下施展盾压会使目标锁足2秒。",
                       "order": "10", "pos": 4, "is_skill": 1, "meta": "力拔山兮，游刃有余。", "extend": "控制技，能有效的配合队友打乱对方阵型。",
                       "id": "13386"},
                 "5": {"name": "入阵", "icon": 11866, "desc": "施展“盾击”命中气血值百分比低于自身的目标，每相差25%追加一段外功伤害，并额外回复2点怒气值。",
                       "order": "10", "pos": 5, "is_skill": 0, "meta": None, "extend": None, "id": "25210"}}, "11": {
                 "1": {"name": "蔑视", "icon": 7248,
                       "desc": "施展伤害招式命中目标，若自身气血百分比高于目标气血百分比，则使下一招式无视目标50%外功防御等级，且对击倒、被击僵直目标伤害提高15%。", "order": "11",
                       "pos": 1, "is_skill": 0, "meta": None, "extend": None, "id": "14838"},
                 "2": {"name": "捍卫", "icon": 6300, "desc": "“盾墙”效果期间自身半径8尺范围内最多5个友方目标受到的伤害降低40%，免疫所有控制效果（被拉除外）。",
                       "order": "11", "pos": 2, "is_skill": 0, "meta": None, "extend": None, "id": "13418"},
                 "3": {"name": "返生", "icon": 6334, "desc": "施展“盾壁”使自身立即回复自身10%气血最大值，并回复自身30%格挡值。", "order": "11",
                       "pos": 3, "is_skill": 0, "meta": None, "extend": None, "id": "18723"},
                 "4": {"name": "石虎", "icon": 7452, "desc": "受到任何伤害攻击导致自身气血值低于40%则立刻重置“盾壁”调息时间，该效果最多每3分钟触发一次。",
                       "order": "11", "pos": 4, "is_skill": 0, "meta": None, "extend": None, "id": "14841"},
                 "5": {"name": "仇非", "icon": 14086,
                       "desc": "自身气血值低于1%时，消耗全部怒气，短时不会重伤，持续6秒，期间自身禁疗。结束时若自身怒气大于等于60点，回复自身50%气血值。此效果最多3分30秒触发一次。",
                       "order": "11", "pos": 5, "is_skill": 0, "meta": None, "extend": None, "id": "25212"}}, "12": {
                 "1": {"name": "阵云结晦", "icon": 17157,
                       "desc": "被动效果：施展“绝刀”会对前方扇形范围5个目标造成点外功伤害，施展“血怒”和“绝刀”会获得1层“阵云”。<br/>主动效果：消耗4层“阵云”，一段招式进行刺击对前方6尺矩形范围的最多5个敌对目标造成100%武器伤害外加点外功伤害；二段招式进行挥斩对前方8尺扇形范围的最多5个敌对目标造成100%武器伤害外加点外功伤害；三段会向20尺内的目标冲刺劈砍造成100%武器伤害外加点外功伤害，冲刺前时自身和目标距离每超过2尺，额外造成1次点伤害，最多5次。绝刀额外范围伤害以及3段招式对非侠士目标造成的伤害都会提高60%。",
                       "order": "12", "pos": 1, "is_skill": 1, "meta": "扬旌蔽五岳，杀气作阵云。",
                       "extend": "范围攻击技，擎刀状态下方可施展，多段释放造成外功伤害。", "id": "30769"}, "2": {"name": "矢尽兵穷", "icon": 16191,
                                                                                      "desc": "施展后在原地插下旗帜，向12尺范围内的敌方玩家发出战斗邀请，施展时每个拥有自身流血效果的目标会使自身获得“在野”效果，使自身获得不受限的加速值加成7.5%，移动速度提高5%，该效果最多作用4次。3秒后在旗帜半径12尺内生成决斗场，范围内自身以及最多5个敌方玩家被疗伤成效额外降低10%，免疫击退和被拉。受到邀请未在场内和离开决斗场的敌方玩家获得“怯战”效果，造成的伤害降低60%，持续12秒。决斗场最多存在15秒，在苍云离开后消失。",
                                                                                      "order": "12", "pos": 2,
                                                                                      "is_skill": 1,
                                                                                      "meta": "绝处方续，死地后生。",
                                                                                      "extend": "功能技，能有效分割战场。",
                                                                                      "id": "29066"},
                 "3": {"name": "祭血关山", "icon": 17698,
                       "desc": "一段招式歃血御城，进入“祭血”状态，每秒消耗自身6%的最大气血值，不断转化为环绕自身的“御城领域”，领域最多持续30秒。在自身领域中将持续获得“盾壁”效果，每秒增加自身4%最大气血值的伤害化解量，自身基础攻击力增加20%，最多3名敌方玩家每秒将获得一层“歃血”外功不利效果。若自身血量低于20%，则将提前自动结束“祭血”状态。二段招式吹角关山，主动结束“祭血”状态。下一个“苍雪刀”套路下招式将为目标添加“锋寒”不利状态，状态持续期间将吸收目标所获得的治疗量。状态持续时间和吸收量将根据自身进入“祭血”状态的时长决定，最多吸收60%目标最大气血值的治疗量，持续4秒；最少吸收15%目标最大气血值的治疗量，持续1秒。调息时间30秒。",
                       "order": "12", "pos": 3, "is_skill": 1, "meta": "白刃交于前，视死若生者， 烈士之勇也。",
                       "extend": "辅助技，可消耗自身气血值转化为领域。", "id": "32619"}, "4": {"name": "扬旌沙场", "icon": 7505,
                                                                             "desc": "可对敌对玩家目标施展，强迫目标与自身进行对决，期间不受其他玩家招式影响，持续20秒。效果期间气血百分比低于20%者或持续时间结束后气血百分比较低者失败，对决胜利者若为苍云则使自身小队成员气血上限、伤害、治疗效果提高25%，受到所有伤害降低25%，持续20秒，对决胜利者若为目标则使目标小队成员气血上限、伤害、治疗效果提高5%，受到所有伤害降低5%，持续20秒。",
                                                                             "order": "12", "pos": 4, "is_skill": 1,
                                                                             "meta": "兴师欲战，若彼坚壁，当攻其主。",
                                                                             "extend": "攻击技，选择敌对目标进行决斗。",
                                                                             "id": "15196"},
                 "5": {"name": "断马摧城", "icon": 14087,
                       "desc": "举盾对自身8尺范围最多5个目标造成一次锤击，造成外功伤害并使其眩晕3秒。当前每拥有10点怒气此次伤害提高7.5%，并使其眩晕时长增加0.25秒。被命中的目标受到惊吓，攻击力下降50%，并在5秒内逐渐恢复。外功伤害>",
                       "order": "12", "pos": 5, "is_skill": 1, "meta": "高城楼橹数千重，一追击地勇摧之。",
                       "extend": "攻击技，擎盾状态下方可施展，造成自身范围的高额伤害，怒气高时施展最佳。", "id": "25213"}}}}


from collections import namedtuple

_recipe = namedtuple('recipe_data', ['index', 'slot', 'desc', 'value'])

recipe = {
    # 盾刀
    1863: _recipe(79, "atRecipePhysicsCriticalPercent", "盾刀2%会心", 0.02),     # pushButton_{key}
    1864: _recipe(15, "atRecipePhysicsCriticalPercent", "盾刀3%会心", 0.03),
    1865: _recipe(16, "atRecipePhysicsCriticalPercent", "盾刀4%会心", 0.04),
    1860: _recipe(13, "atRecipeDamagePercent", "盾刀3%伤害", 0.03),
    1861: _recipe(17, "atRecipeDamagePercent", "盾刀4%伤害", 0.04),
    1862: _recipe(18, "atRecipeDamagePercent", "盾刀5%伤害", 0.05),
    1866: _recipe(14, "atSkillEventHandler", "盾刀第三段+5回怒", None),
    # 盾压
    1856: _recipe(24, "atSkillEventHandler", "盾压-1s调息", None),
    1857: _recipe(21, "atSkillEventHandler", "盾压-1s调息", None),
    1854: _recipe(22, "atRecipePhysicsCriticalPercent", "盾压3%会心", 0.03),
    1855: _recipe(19, "atRecipePhysicsCriticalPercent", "盾压4%会心", 0.04),
    1852: _recipe(23, "atRecipeDamagePercent", "盾压4%伤害", 0.04),
    1853: _recipe(25, "atRecipeDamagePercent", "盾压5%伤害", 0.05),
    1858: _recipe(20, "atSkillEventHandler", "盾压5%触发", None),
    1859: _recipe(26, "atSkillEventHandler", "盾压5%触发", None),
    # 劫刀
    1833: _recipe(30, "atRecipePhysicsCriticalPercent", "劫刀2%会心", 0.02),
    1834: _recipe(27, "atRecipePhysicsCriticalPercent", "劫刀3%会心", 0.03),
    1835: _recipe(32, "atRecipePhysicsCriticalPercent", "劫刀4%会心", 0.04),
    1830: _recipe(31, "atRecipeDamagePercent", "劫刀3%伤害", 0.03),
    1831: _recipe(33, "atRecipeDamagePercent", "劫刀4%伤害", 0.04),
    1832: _recipe(29, "atRecipeDamagePercent", "劫刀5%伤害", 0.05),
    1836: _recipe(28, "atSkillEventHandler", "劫刀-5耗怒", None),
    # 斩刀
    1841: _recipe(37, "atRecipePhysicsCriticalPercent", "斩刀2%会心", 0.02),
    1842: _recipe(34, "atRecipePhysicsCriticalPercent", "斩刀3%会心", 0.03),
    1843: _recipe(39, "atRecipePhysicsCriticalPercent", "斩刀4%会心", 0.04),
    1838: _recipe(38, "atRecipeDamagePercent", "斩刀3%伤害", 0.03),
    1839: _recipe(40, "atRecipeDamagePercent", "斩刀4%伤害", 0.04),
    1840: _recipe(36, "atRecipeDamagePercent", "斩刀5%伤害", 0.05),
    1844: _recipe(35, "atSkillEventHandler", "斩刀锁足", None),
    1845: _recipe(41, "atSkillEventHandler", "斩刀解锁足减速", None),
    # 绝刀
    1848: _recipe(44, "atRecipePhysicsCriticalPercent", "绝刀3%会心", 0.03),
    1849: _recipe(47, "atRecipePhysicsCriticalPercent", "绝刀4%会心", 0.04),
    1846: _recipe(45, "atRecipeDamagePercent", "绝刀4%伤害", 0.04),
    1847: _recipe(46, "atRecipeDamagePercent", "绝刀5%伤害", 0.05),
    1895: _recipe(48, "atSkillEventHandler", "绝刀-1s调息", None),
    1896: _recipe(49, "atSkillEventHandler", "绝刀-2s调息", None),
    1850: _recipe(42, "atSkillEventHandler", "绝刀-15耗怒", None),
    # 盾飞
    1955: _recipe(50, "atRecipePhysicsCriticalPercent", "盾飞2%会心", 0.02),
    1956: _recipe(52, "atRecipePhysicsCriticalPercent", "盾飞3%会心", 0.03),
    1953: _recipe(51, "atRecipeDamagePercent", "盾飞3%伤害", 0.03),
    1954: _recipe(53, "atRecipeDamagePercent", "盾飞4%伤害", 0.04),
    1957: _recipe(43, "atSkillEventHandler", "盾飞+5s持续", None),
    1958: _recipe(54, "atSkillEventHandler", "盾飞+5s持续", None),
    # 盾舞
    1904: _recipe(55, "atRecipePhysicsCriticalPercent", "盾舞3%会心", 0.03),
    1905: _recipe(57, "atRecipePhysicsCriticalPercent", "盾舞4%会心", 0.04),
    1902: _recipe(58, "atRecipeDamagePercent", "盾舞4%伤害", 0.04),
    1903: _recipe(59, "atRecipeDamagePercent", "盾舞5%伤害", 0.05),
    1906: _recipe(61, "atSkillEventHandler", "盾舞+1尺范围", None),
    1907: _recipe(60, "atSkillEventHandler", "盾舞+1尺范围", None),
    1908: _recipe(56, "atSkillEventHandler", "盾舞+1s持续", None),
    1909: _recipe(62, "atSkillEventHandler", "盾舞+2s持续", None),
    # 盾墙
    1880: _recipe(67, "atSkillEventHandler", "盾墙-5s调息", None),
    1881: _recipe(65, "atSkillEventHandler", "盾墙-5s调息", None),
    1882: _recipe(69, "atSkillEventHandler", "盾墙-5s调息", None),
    1885: _recipe(68, "atSkillEventHandler", "盾墙+5%移速", None),
    1886: _recipe(63, "atSkillEventHandler", "盾墙+5%移速", None),
    1887: _recipe(70, "atSkillEventHandler", "盾墙+5%移速", None),
    1888: _recipe(66, "atSkillEventHandler", "盾墙+10%减伤", None),
    1889: _recipe(64, "atSkillEventHandler", "盾墙+10%减伤", None),
    # 血怒
    1870: _recipe(71, "atSkillEventHandler", "血怒+5回怒", None),
    1871: _recipe(77, "atSkillEventHandler", "血怒+5回怒", None),
    1872: _recipe(75, "atSkillEventHandler", "血怒+5回怒", None),
    1867: _recipe(74, "atSkillEventHandler", "血怒+1s持续", None),
    1868: _recipe(73, "atSkillEventHandler", "血怒+1s持续", None),
    1869: _recipe(78, "atSkillEventHandler", "血怒+1s持续", None),
    1873: _recipe(76, "atSkillEventHandler", "血怒2%回血", None),
    1874: _recipe(72, "atSkillEventHandler", "血怒3%回血", None),
    # 其他秘籍
    1879: _recipe(None, "atRecipeDamagePercent", "绝刀+30%", 306/1024),
    4409: _recipe(None, "atRecipeDamagePercent", "斩刀+30%", 306/1024),
    4918: _recipe(None, "atRecipeDamagePercent", "绝刀+20%", 205/1024),
    4919: _recipe(None, "atRecipeDamagePercent", "绝刀+40%", 410/1024),
    4920: _recipe(None, "atRecipeDamagePercent", "绝刀+60%", 614/1024),
    4921: _recipe(None, "atRecipeDamagePercent", "绝刀+80%", 819/1024),
}



special_stones = {
    5599: ('atVitalityBasePercentAdd', 81),
    5598: ('atVitalityBasePercentAdd', 71),
    5597: ('atVitalityBasePercentAdd', 61),
    5610: ('atStrengthBasePercentAdd', 81),
    5609: ('atStrengthBasePercentAdd', 71),
    5608: ('atStrengthBasePercentAdd', 61),
    5613: ('atAgilityBasePercentAdd', 81),
    5612: ('atAgilityBasePercentAdd', 71),
    5611: ('atAgilityBasePercentAdd', 61),
}

global_params = {
    'fCriticalStrikeParam': 9.53,
    'fCriticalStrikePowerParam': 3.335,
    'fOvercomeParam': 9.53,
    'fInsightParam': 9.189,
    'fHasteRate': 11.695,
    'fParryParam': 4.345,
    'fSurplusParam': 13.192,
    'fPhysicsShieldParam': 5.091,

}

LEVEL_RATE = 450
LEVEL_CONST = 45750


_npc_attribs = namedtuple('npc_attrib', ['defense', 'critical'])
npc_attribute_data = {
    120: _npc_attribs(7412, 3930),
    121: _npc_attribs(11073, 4146),
    122: _npc_attribs(15528, 4360),
    123: _npc_attribs(26317, 4574),
    124: _npc_attribs(27550, 4789),
}
