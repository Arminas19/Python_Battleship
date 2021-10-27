from random import randint

Scores = {
    'Player': 0,
    'Computer': 0
}
board = []
Computer_board = []
water = ['-']


class Setup_Board:
    def __init__(self, num_ships, type):
        self.num_ships = num_ships
        self.type = type
        self.ship_hit = 'X'
        self.ship = 'O'


def game_board(self):
    """
    Creates the game board that the user can play in.
    """
    type = 'Player'
    print('Enter Your Name: ')
    print('\n\n\n')
    input('          ')
    print('    0 1 2 3 4 5 6 7 8 9')
    print('  +---------------------+')
    for row in range(10):
        board.append(water * 10)

    letters = 0
    for row in range(10):
        print(chr(letters + 65), end=' | ')
        for column in range(len(board[letters])):
            print(board[letters][column], end=' ')
        print('| ')
        letters += 1
    print('  +---------------------+ \n\n\n')


def computer_board(self):
    """
    Computers Board
    """
    type = 'Computer'
    print('         COMPUTER ')
    print('    0 1 2 3 4 5 6 7 8 9')
    print('  +---------------------+')
    for row in range(10):
        Computer_board.append(water * 10)

    letters = 0
    for row in range(10):
        print(chr(letters + 65), end=' | ')
        for column in range(len(board[letters])):
            print(Computer_board[letters][column], end=' ')
        print('| ')
        letters += 1
    print('  +---------------------+ \n\n\n')


def New_game():
    """
    Starts a new game and welcomes the user to the game.
    """
    print('Welcome To Battleship!! ')
    print('How to play? Try and guess where the')
    print('enemy ships are by choosing a row and column.')
    print('Example: row: 2  comlumn: D \n \n\n')

    game_board(board)
    computer_board(Computer_board)


New_game()
