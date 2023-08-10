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
from PyCode.config import *
from PyCode.utilities import *
Tile_Size = 64


num_of_cards = card_to_player_ratio


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

    def roll_dice(self):
        pass

    def build_deck(self, num_players): # creates the game deck based on the number of players
        card_dict = num_of_cards[num_players]
        for x in range(card_dict["Alchemist"]):
            self.Game_Deck.append(self.Cards[0])
        for x in range(card_dict["Assassin"]):
            self.Game_Deck.append(self.Cards[1])
        for x in range(card_dict["Cleric"]):
            self.Game_Deck.append(self.Cards[2])
        for x in range(card_dict["Commoner"]):
            self.Game_Deck.append(self.Cards[3])
        for x in range(card_dict["Jester"]):
            self.Game_Deck.append(self.Cards[4])
        for x in range(card_dict["King"]):
            self.Game_Deck.append(self.Cards[5])
        for x in range(card_dict["Knight"]):
            self.Game_Deck.append(self.Cards[6])
        for x in range(card_dict["Marksman"]):
            self.Game_Deck.append(self.Cards[7])
        for x in range(card_dict["Merchant"]):
            self.Game_Deck.append(self.Cards[8])
        for x in range(card_dict["Necromancer"]):
            self.Game_Deck.append(self.Cards[9])
        for x in range(card_dict["Princess"]):
            self.Game_Deck.append(self.Cards[10])
        for x in range(card_dict["Queen"]):
            self.Game_Deck.append(self.Cards[11])
        for x in range(card_dict["Thief"]):
            self.Game_Deck.append(self.Cards[12])
    def create_players(self, num_players):
        for i in range(num_players):
            self.Players.append(Player())

    def deal_cards(self):
        random.shuffle(self.Game_Deck)
        random.shuffle(self.Game_Deck)
        random.shuffle(self.Game_Deck)
        index = 0
        for i in range(3):
            for player in self.Players:
                player.current_deck.append(self.Game_Deck[index])
                index += 1

Game = GuildGame()
Game.start_game()
