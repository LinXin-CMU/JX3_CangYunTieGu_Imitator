# coding: utf-8
# author: LinXin

# #
# self.player.CastSkill(13045, 1)  # /cast 盾压
#
# if not (self.player.IsHaveBuff(8499) or self.player.IsHaveBuff(8448)):
#     self.player.CastSkill(13046, 1)  # /cast [nobuff:盾挡] 盾猛
#
# if self.player.rage > 80 and True:
#     self.player.CastSkill(25213, 1)  # /cast 断马摧城
#
# self.player.CastSkill(13047, 1)  # /cast 盾击
# self.player.CastSkill(13044, 1)  # /cast 盾刀
#
# if self.player.rage == 110:
#     self.player.CastSkill(13391, 1)  # /cast [rage>109] 盾挡
# if self.player.rage >= 65 and (self.player.IsHaveBuff(8499) or self.player.IsHaveBuff(8448)):
#     self.player.CastSkill(13050, 1)  # /cast [rage>=65&buff:盾挡] 盾飞
# if self.player.GetSkillCoolDown(13054) > 0 and self.player.GetSkillCoolDown(13055) > 0:
#     self.player.CastSkill(13051, 1)  # /cast [bufftime:盾飞<9] 盾回
#
# self.player.CastSkill(13054, 1)  # /cast 斩刀
#
# if self.player.IsHaveBuff(24755):
#     self.player.CastSkill(13055, 1)  # /cast [buff:24755] 绝刀
#
# self.player.CastSkill(13052, 1)  # /cast 劫刀
#
# if not self.player.IsHaveBuff(8245) and (
#         self.player.IsHaveBuff(8499) or self.player.IsHaveBuff(8448)) and self.player.rage < 50:
#     self.player.CastSkill(13040, 1)



# 割裂
# if self.player.rage > 50:
#     self.player.CastSkill(25213, 1)  # /cast 断马摧城
#
# self.player.CastSkill(13045, 1)  # /cast 盾压
# self.player.CastSkill(13047, 1)  # /cast 盾击
# self.player.CastSkill(13044, 1)  # /cast 盾刀
#
# if self.player.rage == 110:
#     self.player.CastSkill(13391, 1)  # /cast [rage>109] 盾挡
#
# if self.target.GetBuff(8249).lasting < 5 * 16 and (self.player.IsHaveBuff(8499) or self.player.IsHaveBuff(8448)):
#     if self.player.rage >= 15 and self.target.GetBuff(21308):
#         self.player.CastSkill(13050, 1)
#     elif self.player.rage >= 30 and not self.target.GetBuff(21308):
#         self.player.CastSkill(13050, 1)
#
# if self.target.IsHaveBuff(8249) and not self.target.IsHaveBuff(21308):
#     self.player.CastSkill(13053, 1)
#
# self.player.CastSkill(13054, 1)
#
# if self.player.GetSkillCoolDown(13054) > 0 and self.target.GetBuff(21308).lasting > 0:
#     self.player.CastSkill(13051, 1)
#
# if self.player.GetBuff(8448).lasting > 0 and self.player.GetBuff(8245).lasting == 0:
#     self.player.CastSkill(13040, 1)

# 怒绝
# self.player.CastSkill(13045, 1)  # /cast 盾压
#
#             if not (self.player.IsHaveBuff(8499) or self.player.IsHaveBuff(8448)):
#                 self.player.CastSkill(13046, 1)  # /cast [nobuff:盾挡] 盾猛
#
#             if self.player.rage > 80 and True:
#                 self.player.CastSkill(25213, 1)  # /cast 断马摧城
#
#             self.player.CastSkill(13047, 1)  # /cast 盾击
#             self.player.CastSkill(13044, 1)  # /cast 盾刀
#
#             if self.player.rage == 110:
#                 self.player.CastSkill(13391, 1)  # /cast [rage>109] 盾挡
#
#             if self.player.rage >= 65 and (self.player.IsHaveBuff(8499) or self.player.IsHaveBuff(8448)):
#                 self.player.CastSkill(13050, 1)  # /cast [rage>=65&buff:盾挡] 盾飞
#
#             if self.player.GetSkillCoolDown(13054) > 0 and self.player.GetSkillCoolDown(13055) > 0:
#                 self.player.CastSkill(13051, 1)  # /cast [bufftime:盾飞<9] 盾回
#
#             self.player.CastSkill(13054, 1)  # /cast 斩刀
#
#             if self.player.IsHaveBuff(24755):
#                 self.player.CastSkill(13055, 1)  # /cast [buff:24755] 绝刀
#
#             self.player.CastSkill(13052, 1)  # /cast 劫刀
#
#             if not self.player.IsHaveBuff(8245) and (
#                     self.player.IsHaveBuff(8499) or self.player.IsHaveBuff(8448)) and self.player.rage < 50:
#                 self.player.CastSkill(13040, 1)
