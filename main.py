from random import randint

Scores = {
    'Player': 0,
    'Computer': 0
}
board = []
Computer_board = []
water = ['-']


class Setup_Board:
    def __init__(self, num_ships, ship_hit, ship, type, guess):
        self.num_ships = 5
        self.ship_hit = 'X'
        self.type = type
        self.ship = 'O'
        self.guess = []

    def add_ships(self):
        """
        Adds ships to game_board function and Computer function.
        """
        if type == 'Computer':
            while self.num_ships == len(self.ship):
                Computer_board.append(self.ship)
        else:
            if type == 'Player':
                while self.num_ships == len(self.ship):
                    board.append(self.ship)
                    board[water] = 'O'

    def guesses(self, row, column, ship_coordinates):
        self.ship_coordinates = [(row, column)]
        self.guess.append((row, column))
        if (row, column) in board[water] == 'O':
            return 'Hit'
        else:
            return 'Miss'

    
def Player_board(type):
    """
    Creates the game board that the user can play in.
    """

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


def computer_board(type):
    """
    Computers Board
    """

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
    print('enemy ships are by choosing a row and a column.')
    print('Example: row: 2  comlumn: D \n \n\n')

    Player_board(type='Player')
    computer_board(type='Computer')


New_game()
