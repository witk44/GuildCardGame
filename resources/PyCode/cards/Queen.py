


class Queen:
    def __init__(self) -> None:
        self.cost = 5
        self.cooldown = 0
        self.alive = True
        self.ability_description = " Allows the player to revive a dead card from their deck. Upon being played, the queen must be removed from the game and placed next to the deck in a separate area. The queen must either be placed face down or face up depending on whether it is challenged by other players or not. The dead card that is selected to be revived is shuffled back into the deck and the player draws 2 new cards"