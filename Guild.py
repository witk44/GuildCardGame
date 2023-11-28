import pygame
import random
from resources.PyCode.cards.Alchemist import Alchemist
from resources.PyCode.cards.Assassin import Assassin
from resources.PyCode.cards.Cleric import Cleric
from resources.PyCode.cards.Commoner import Commoner
from resources.PyCode.cards.Jester import Jester
from resources.PyCode.cards.King import King
from resources.PyCode.cards.Knight import Knight
from resources.PyCode.cards.Marksman import Marksman
from resources.PyCode.cards.Merchant import Merchant
from resources.PyCode.cards.Necromancer import Necromancer
from resources.PyCode.cards.Princess import Princess
from resources.PyCode.cards.Queen import Queen
from resources.PyCode.cards.Thief import Thief
from resources.PyCode.Player import Player
from resources.PyCode.config import *
from resources.PyCode.utilities import *
from resources.main_menu import MainMenu
import subprocess
Tile_Size = 64


num_of_cards = card_to_player_ratio

# Initialize Pygame
pygame.init()






class GuildGame:
    def __init__(self) -> None:
        self.Cards = [Alchemist(), Assassin(), Cleric(), Commoner(), Jester(), King(),
                      Knight(), Marksman(), Merchant(), Necromancer(), Princess(), Queen(), Thief()]
        self.Game_Deck = []
        self.Players = []
        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.screen_info = pygame.display.Info()
        self.screen_width, self.screen_height = self.screen_info.current_w, self.screen_info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Guild Card Game")

        self.build_deck(4)
        self.game_finished = False

    def start_game(self):
        self.create_players(3)
        self.deal_cards()

    def roll_dice(self):
        die_rolls_player = {}
        die_rolls = []
        for player in self.Players:
            number = random.randint(1,6)
            die_rolls_player[player] = number
            die_rolls.append(number)

        for i in range(6):
            if die_rolls.count(i) > 1:
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

    
def kill_player_card(player):
    pass

def select_player(player):
    FONT = pygame.font.Font(None,36)
    screen = Game.screen
    y = 200
    for player in Game.Players:
        text = FONT.render(str(player), True, (150,150,150))
        text_rect = text.get_rect(center=(screen_width // 2, y))
        screen.blit(text, text_rect)
        y += 50
    
     # Update the display
    pygame.display.flip()


# Function to start the server in a separate thread
def start_server():
    global server_process
    server_process = subprocess.Popen(['python', app_path('resources/PyCode/server.py')])
    server_on = True

# Function to start the client in a separate thread
def start_client():
    global client_process  
    
    client_process = subprocess.Popen(['python', app_path('resources/PyCode/client.py')])
    client_on = True

def kill_client():
    client_process.kill()

def kill_server():
    server_process.kill()

def launch():
   
    Game = GuildGame()
    mainMenu = MainMenu(Game.screen,Game.screen_width,Game.screen_height)
    process = mainMenu.main_menu()
    if(process):
        start_client()
    else:
        start_server()
    
    # Game.start_game()
    # Game.roll_dice()



    pass





launch()


    