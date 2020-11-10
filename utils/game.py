from typing import List
import random

from utils.card import Card
from utils.player import Player


class Deck:
    """
    Class defining the deck
    """

    cards = []

    def __init__(self):
        """
        Constructor
        """

    def __str__(self):
        print(self.cards)

    def fill_deck(self):
        """
        Procedure that fill the deck with all the playing cards (52 cards)
            A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
            for each symbols ♥,♦,♣,♠
        """
        for symbol, color in (
            ("♥", "red"),
            ("♦", "red"),
            ("♣", "black"),
            ("♠", "black"),
        ):
            for value in (
                "A",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
            ):
                self.cards.append(Card(value, color, symbol))

    def shuffle(self):
        """
        Procedure that shuffle randomly the cards' deck
        """
        random.shuffle(self.cards)

    def distribute(self, players: list[Player]):
        """
        Funcion that distribute the card to a list of players

        :param players: A list of Player to which distribute the cards
        """
        while len(self.cards) > 0:
            for player in players:
                try:
                    player.add_card(self.cards[0])
                    self.cards.pop(0)
                except IndexError:
                    break  # To leave when no more cards due an 52%len(players) != 0


class ScoreBoard:
    """
    Class representing the scoreboard characterized by
    - a list of player and their associated score
    """

    def __init__(self, players: List[Player]):
        """
        Constructor

        :param players : a list of Player
        """
        self.dico_score = {}
        for player in players:
            self.dico_score[player] = 0

    def award_points(self, winning_cards: List[Card]):
        """
        Procedure that increased the score of players who have played the best cards.
        """
        for player in self.dico_score.keys():
            if player.history[-1] in winning_cards:
                self.dico_score[player] = self.dico_score[player] + 1

    def __str__(self):
        txt_score = "-----------------"
        txt_score += "\n-  Score Board  -"
        txt_score += "\n-----------------"
        for player in self.dico_score.keys():
            txt_score += f"\n{player.name} : {self.dico_score[player]}"
        return txt_score

    def get_winners(self) -> List[Player]:
        """
        Function that will return the player who has the maximum score

        :return : a list of Player (normaly 1 but more if equality)
        """
        winners = []
        winners.append(list(self.dico_score.keys())[0])
        for player in list(self.dico_score.keys())[1:]:
            comparaison = self.dico_score[winners[0]] - self.dico_score[player]
            if comparaison < 0:
                winners.clear()
                winners.append(player)
            elif comparaison == 0:
                winners.append(player)
        return winners


class Board:
    """
    Class representing a playing board characterized by :
    - a list of players
    - a turn count
    - a list of active cards (played cards in the current turn)
    - a list of history cards (played cards in the previous turns)
    """

    turn_count = int
    active_cards: list[Card]
    history_cards: list[list[Card]]

    def __init__(self, players: List[Player]):
        """
        Constructor

        :param players: A list of players taking a sit at the board
        """
        self.turn_count = 0
        self.players = players
        self.active_cards = list[Card]
        self.history_cards = list[list[Card]]
        self.score_board = ScoreBoard(players)

    def __str__(self):
        return "Board"

    def start_game(self):
        """
        Procedure that will start the game
        """
        # Initialize a new deck
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        # Initialize the hand of each player
        deck.distribute(self.players)
        # Start the play
        self.history_cards = []

        while all(player.number_of_cards > 0 for player in self.players):
            self.active_cards = []
            self.turn_count += 1

            for player in self.players:
                played_card = player.play()
                self.active_cards.append(played_card)

            # Search the higher card played
            higher_cards = []
            higher_cards.append(self.active_cards[0])
            for card in self.active_cards[1:]:
                comparaison = higher_cards[0].force - card.force
                if comparaison < 0:
                    higher_cards.clear()
                    higher_cards.append(card)
                elif comparaison == 0:
                    higher_cards.append(card)

            self.score_board.award_points(higher_cards)

            # Print turn info
            print(f"\nTurn count : {self.turn_count}")
            print(f"Active cards : {self.active_cards}")
            print(f"History cards : {len(self.history_cards)}")
            print(f"\nBest card(s) : {higher_cards}")
            print(self.score_board)
            print("------------------------------------------")
            # Transfert active card to history cards
            self.history_cards.extend(self.active_cards)
            # Flush the active cards
            self.active_cards.clear()
        print("--         THE GAME IS DONE             --")
        print("------------------------------------------")
        print("AND THE WINNER(S) IS .......")
        print(self.score_board.get_winners())
