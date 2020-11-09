from typing import List
import random

from utils.card import Card
from utils.player import  Player

class Deck:
    '''
    Class defining the deck
    '''
    cards = []

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def fill_deck(self):
        '''
        Procedure that fill the deck with all the playing cards (52 cards)
            A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
            for each symbols ♥,♦,♣,♠
        '''
        for symbol, color in (('♥', 'red'),('♦', 'red'), ('♣', 'black'),('♠','black')):
            for value in ('A','2','3','4','5','6','7','8','9','10','J','Q','K') :
                self.cards.append(Card(value, color, symbol))

    def shuffle(self):
        '''
        Procedure that shuffle randomly the cards' deck
        '''
        random.shuffle(self.cards)

    def distribute(self, players : list[Player]):
        '''
        Funcion that distribute the card to a list of players

        :param players: A list of Player to which distribute the cards
        '''
        while len(self.cards) >= len(players):
            for player in players:
                player.add_card(self.cards[0])
                self.cards.pop(0)

class Board:
    """ 
    Class representing a playing board thcharacterized by :
    - a list of players
    - a turn count
    - a list of active cards (played cards in the current turn)
    - a list of history cards (played cards in the previous turns)
    """
    
    turn_count = int
    active_cards : list[Card]
    history_cards : list[list[Card]]

    def __init__(self, players : List[Player]):
        '''
        Constructor

        :param players: A list of players taking a sit at the board
        '''
        self.turn_count = 0
        self.players = players
        self.active_cards = list[Card]
        self.history_cards = list[list[Card]]

    def __str__(self):
        return "Board"
    
    def start_game(self):
        '''
        Procedure that will start the game
        '''
        # Initialize a new deck
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        # Initialize the hand of each player
        deck.distribute(self.players)
        # Start the play
        self.history_cards = []
        while any(player.number_of_cards > 0 for player in self.players):
            self.active_cards = []
            self.turn_count +=1
            for player in self.players:
                played_card = player.play()
                self.active_cards.append(played_card)
            print(f'\nTurn count : {self.turn_count}')
            print(f'Active cards : {self.active_cards}')
            print(f'History cards : {len(self.history_cards)}')
            print('------------------------------------------')
            # Transfert active card to history cards
            self.history_cards.extend(self.active_cards)
            # Flush the active cards
            self.active_cards.clear()
        


        



