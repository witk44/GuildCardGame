import pygame
import random
from PyCode.cards.Alchemist import Alchemist
from PyCode.cards.Assassin import Assassin
from PyCode.cards.Cleric import Cleric
from PyCode.cards.Commoner import Commoner
from PyCode.cards.Jester import Jester
from PyCode.cards.King import King
from PyCode.cards.Knight import Knight
from PyCode.cards.Marksman import Marksman
from PyCode.cards.Merchant import Merchant
from PyCode.cards.Necromancer import Necromancer
from PyCode.cards.Princess import Princess
from PyCode.cards.Queen import Queen
from PyCode.cards.Thief import Thief
from PyCode.Player import Player

Tile_Size = 64

class GuildGame:
    def __init__(self) -> None:
        self.Cards = [Alchemist(), Assassin(), Cleric(), Commoner(), Jester(), King(),
                      Knight(), Marksman(), Merchant(), Necromancer(), Princess(), Queen(), Thief()]
        self.Game_Deck = []
        self.Players = []

        self.build_deck(4)

    def start_game(self):
        self.create_players(3)
        self.deal_cards()

    def build_deck(self, num_players): # creates the game deck based on the number of players
        for card in self.Cards:
            self.Game_Deck.append(card)

    def create_players(self, num_players):
        for i in range(num_players):
            self.Players.append(Player())

    def deal_cards(self):
        random.shuffle(self.Game_Deck)
        index = 0
        for i in range(3):
            for player in self.Players:
                player.current_deck.append(self.Game_Deck[index])
                index += 1

Game = GuildGame()
Game.start_game()
