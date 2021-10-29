from random import randint

Scores = {
    'Player': 0,
    'Computer': 0
}


class Setup_Board:
    def __init__(self, num_ships, ship_hit, ship, type, guess, water,
                 computer_board, board, player_name):
        self.num_ships = 5
        self.ship_hit = 'X'
        self.type = type
        self.ship = 'O'
        self.guess = []
        self.water = ['-']
        self.computer_board = []
        self.board = []
        self.player_name = player_name

    def add_ships(self):
        """
        Adds ships to game_board function and Computer function.
        """
        if type == 'Computer':
            while self.num_ships >= len(self.ship):
                self.computer_board.append(self.ship)
        else:
            if type == 'Player':
                while self.num_ships >= len(self.ship):
                    self.board.append(self.ship)

    def guesses(self, row, column, ship_coordinates):
        """
        Returns a value of hit or miss.
        """
        self.ship_coordinates = ((row, column))
        self.guess.append((row, column))
        if (row, column) in self.computer_board[ship_coordinates] == 'X':
            return 'Hit'
        else:
            return 'Miss'

    def render_Player_board(self, type, player_name):
        """
        Creates the game board that the user can play in.
        """
        print('\n\n\n')
        print(f'          {self.player_name}')
        print('    0 1 2 3 4 5 6 7 8 9')
        print('  +---------------------+')
        for row in range(10):
            self.board.append(self.water * 10)

        letters = 0
        for row in range(10):
            print(chr(letters + 65), end=' | ')
            for column in range(len(self.board[letters])):
                print(self.board[letters][column], end=' ')
            print('| ')
            letters += 1
        print('  +---------------------+ \n\n\n')

    def render_computer_board(self, type):
        """
        renders Computers Board
        """

        print('         COMPUTER ')
        print('    0 1 2 3 4 5 6 7 8 9')
        print('  +---------------------+')
        for row in range(10):
            self.computer_board.append(self.water * 10)

        letters = 0
        for row in range(10):
            print(chr(letters + 65), end=' | ')
            for column in range(len(self.computer_board[letters])):
                print(self.computer_board[letters][column], end=' ')
            print('| ')
            letters += 1
        print('  +---------------------+ \n\n\n')


def New_game():
    """
    Starts a new game and welcomes the user to the game.
    """
    computer_board = ['']
    board = []
    num_ships = 5
    ship_hit = 'X'
    ship = 'O'
    guess = []
    water = ['-']
    print('Welcome To Battleship!! ')
    print('How to play? Try and guess where the')
    print('enemy ships are by choosing a row and a column.')
    print('Example: row: 2  comlumn: D \n \n\n')
    player_name = input('Enter Your Name: ')

    setup_pb = Setup_Board(num_ships, ship_hit, ship, type, guess, water,
                           computer_board, board, player_name)
                           
    setup_pb.render_Player_board('Player', player_name)
    setup_pb.render_computer_board('Computer')


New_game()
