from utils.game import Board
from utils.player import Player

if __name__ == "__main__":
    print("**************************************************")
    print("***             WE TAKE YOUR MONEY             ***")
    print("***            Enjoy your experience           ***")
    print("**************************************************")
    print("\n")
    
    player1 = Player("Alan Turing")
    player2 = Player("Rachel Thomas")
    player3 = Player("Tom Crasset")
    
    while True:
        take_a_seat = input("Do you want to take a seat (Y/N) :")
        if take_a_seat in ('Y', 'y', 'N', 'n'):
            if(take_a_seat in ('Y', 'y')):
                player4 = Player(input("What's your name ? "), True)
            else:
                player4 = Player("Jérôme Coumont")
            break
    
    game = Board([player1, player2, player3, player4])
    game.start_game()