


class Thief:
    def __init__(self) -> None:
        self.cost = 0
        self.cooldown = 2
        self.alive = True
        self.ability_description = "The thief can be blocked by a player who has a princess in any slot. A princess can block a thief 2 times before needing to be reshuffled. After the first use, the princess must be turned sideways to indicate that it has been used once already, after the second use it must be reshuffled for a new card"

    def ability(self,player1,player2):
        if player2.gold > -1 and player1.gold < 20:
            if player2.gold == 1:
                player1.gold += 1
                player2.gold-=1
            elif player2.gold ==0:
                player1.gold += 0
                player2.gold -=0
            else:
                player1.gold +=2
                player2.gold -=2
        if player1.gold >20:
            player1.gold = 20