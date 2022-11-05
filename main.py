from player.player import Player



player = Player([], [])

for i in range(300*16):
    player.Timer(i)
    player.CastSkill(13045, 1)      # /cast 盾压
    player.CastSkill(13047, 1)      # /cast 盾击
    player.CastSkill(13044, 1)      # /cast 盾刀

    if player.rage == 110:
        player.CastSkill(13391, 1)

    print(player.rage)
    print(player.buffs)

print(player.casted)



