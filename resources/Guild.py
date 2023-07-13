import pygame
import cryptography
import pygase
import random
from PyCode.cards.Alchemist import *
from PyCode.cards.Assassin import *
from PyCode.cards.Cleric import *
from PyCode.cards.Commoner import *
from PyCode.cards.Jester import *
from PyCode.cards.King import *
from PyCode.cards.Knight import *
from PyCode.cards.Marksman import *
from PyCode.cards.Merchant import *
from PyCode.cards.Necromancer import *
from PyCode.cards.Princess import *
from PyCode.cards.Queen import *
from PyCode.cards.Thief import *
from PyCode.Player import *


Tile_Size = 64
Game_Deck = []
Cards = []
Players = []


class GuildGame:
    def __init__(self) -> None:
        create_cards()  
        build_deck(4)

    def start_game(self):
        create_players(3)
        deal_cards()
    
def create_cards(): #creates one instance of each card type
    Cards.append(Alchemist())
    Cards.append(Assassin())
    Cards.append(Cleric())
    Cards.append(Commoner())
    Cards.append(Jester())
    Cards.append(King())
    Cards.append(Knight())
    Cards.append(Marksman())
    Cards.append(Merchant())
    Cards.append(Nercomancer())
    Cards.append(Princess())
    Cards.append(Queen())
    Cards.append(Thief())

def build_deck(num_players): #creates the game deck based on number of players
    for card in Cards:
        Game_Deck.append(card)

def create_players(num_players):
    for i in range(num_players):
        Players.append(Player())

def deal_cards():
    for i in range(3):
        random.shuffle(Game_Deck)
    index = 0
    for i in range(3):
        for x in Players:
            x.current_deck.append(Game_Deck[index])
            index+=1
        
Game = GuildGame()
Game.start_game()
