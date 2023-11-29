import pygame
import random
from cards.Alchemist import Alchemist
from cards.Assassin import Assassin
from cards.Cleric import Cleric
from cards.Commoner import Commoner
from cards.Jester import Jester
from cards.King import King
from cards.Knight import Knight
from cards.Marksman import Marksman
from cards.Merchant import Merchant
from cards.Necromancer import Necromancer
from cards.Princess import Princess
from cards.Queen import Queen
from cards.Thief import Thief
from Player import Player
from config import *
from utilities import *
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
        self.game_started = False
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

        
    def kill_player_card(self,player):
        pass

    def select_player(self,player):
        FONT = pygame.font.Font(None,36)
        screen = self.screen
        y = 200
        for player in self.Players:
            text = FONT.render(str(player), True, (150,150,150))
            text_rect = text.get_rect(center=(self.screen_width // 2, y))
            screen.blit(text, text_rect)
            y += 50
        
        # Update the display
        pygame.display.flip()
    def waiting_screen(self):
        # Load the image
        background_image = pygame.image.load("resources/images/WaitingScreen.jpg").convert()

        # Scale the image to fit the screen size
        background_image = pygame.transform.scale(background_image, (self.screen_width, self.screen_height))

        # Blit the image onto the screen
        self.screen.blit(background_image, (0, 0))

        # Display a "Waiting..." message in the center of the screen
        font = pygame.font.Font(None, 48)
        text = font.render("Waiting...", True, (255, 255, 255))  # White text
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()
