


class King:
    def __init__(self) -> None:
        self.cost = 0
        self.cooldown = 1
        self.alive = True
        self.ability_description = "The king allows the player to pocket 3 gold as their turn instead of the usual 1 gold"

    def ability(self,player):
        player.gold += 3
        if player.gold >20:
            player.gold = 20