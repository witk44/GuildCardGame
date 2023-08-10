



class Player:
    def __init__(self) -> None:
        self.current_deck =  []
        self.faked_deck = self.current_deck
        self.gold = 0
        self.socket = 0

    def pocket(self):
        if self.gold < 20:
            self.gold+=1