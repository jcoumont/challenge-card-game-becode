import random

from utils.card import Card


class Player:
    """ Class defining a player characterized by:
        - his name
        - his list of cards to play - cards
        - his list of history card (played card) - history
    """
    
    history : list[Card]
    cards : list[Card]

    def __init__(self, name :str):
        '''
        Constructor

        :param name : A str that is the player name
        '''
        self.name = name
        self.history = []
        self.cards = []

    def __str__(self):
        return f"{self.name}"
    
    def play(self) -> Card:
        '''
        Function that will play a random card.
        
        :return A Card that is the played card
        '''
        # Choose the card to play
        played_card = random.choice(self.cards)
        # Update the history and the cards still to play
        self.history.append(played_card)
        self.cards.remove(played_card)
        # Print of the play
        print (f"{self.name} {self.turn_count} played: {played_card}")

        return played_card

    def add_card(self, card : Card):
        '''
        Function that will add a card in the player's hand (cards)

        :param card : a Card that will be added in the player's hand
        '''
        self.cards.append(card)

    @property
    def turn_count(self) -> int:
        '''
        Property that will give the count of played turns

        :return: an int that is the count of played turns
        '''
        return len(self.history)
    
    @property
    def number_of_cards(self) -> int:
        '''
        Property that will give the amount of cards in the player's hand (cards to play)

        :return: an int that is the amount of cards in the player's hand
        '''
        return len(self.cards)