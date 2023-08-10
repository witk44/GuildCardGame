


class Cleric:
    def __init__(self) -> None:
        self.cost = 0
        self.cooldown = 0
        self.alive = True
        self.ability_description = "The cleric can be used to block one execution. When a player is selected to be executed, they may flip over their cleric and save themselves from having to kill a card. After being used, the cleric must be removed from the game and placed in the same area that the queens are. This card cannot be bluffed under any circumstances."