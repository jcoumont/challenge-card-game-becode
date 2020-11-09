from utils.game import Board
from utils.player import Player

if __name__ == "__main__":

    
    player1 = Player("Alan Turing")
    player2 = Player("Rachel Thomas")
    player3 = Player("Tom Crasset")
    player4 = Player("Jérôme Coumont")
    
    game = Board([player1, player2, player3, player4])
    game.start_game()
    
