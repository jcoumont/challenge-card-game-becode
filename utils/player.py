import random
from typing import List

from utils.card import Card


class Player:
    """Class defining a player characterized by:
    - his name
    - his list of cards to play - cards
    - his list of history card (played card) - history
    """

    history: List[Card]
    cards: List[Card]

    def __init__(self, name: str, interactive: bool = False):
        """
        Constructor

        :param name : A str that is the player name
        :param interactive : A bool that indicate if the player
                             chooses himself the card to play
        """
        self.name = name
        self.history = []
        self.cards = []
        self.interactive = interactive

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def play(self) -> Card:
        """
        Function that will play a random card or ask the player
        to choose it if interactive is True.

        :return A Card that is the played card
        """
        # Choose the card to play
        if self.interactive:
            # Display all available card
            for i in range(1, len(self.cards) + 1):
                print(f"{i} : {self.cards[i-1]}")
            while True:
                try:
                    in_choice = int(input("Which card to play ? (number)"))
                    played_card = self.cards[in_choice - 1]
                    break
                except Exception:
                    pass

        else:
            played_card = random.choice(self.cards)
        # Update the history and the cards still to play
        self.history.append(played_card)
        self.cards.remove(played_card)
        # Print of the play
        print(f"{self.name} {self.turn_count} played: {played_card}")

        return played_card

    def add_card(self, card: Card):
        """
        Function that will add a card in the player's hand (cards)

        :param card : a Card that will be added in the player's hand
        """
        self.cards.append(card)

    @property
    def turn_count(self) -> int:
        """
        Property that will give the count of played turns

        :return: an int that is the count of played turns
        """
        return len(self.history)

    @property
    def number_of_cards(self) -> int:
        """
        Property that will give the amount of cards in the player's hand
        (cards to play)

        :return: an int that is the amount of cards in the player's hand
        """
        return len(self.cards)
