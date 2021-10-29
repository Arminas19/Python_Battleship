from random import randint

Scores = {
    'Player': 0,
    'Computer': 0
}
board = []
Computer_board = []
water = ['-']

class Game:
    def __init__(num_ships):
        ...
    
    def setup_boards(self, player_name):
        self.player_board = Board(player_name)
        self.computer_board = Board()

    def make_move(self, board, coordinates):
        if self.check_coordiantes(board, coordinates):
            if hit:
                self.score[board] +=1

        return False

    
class Board:
    def __init__(self, ship_hit, ship, type, guess, player_name="Computer"):
        self.player_name = player_name
        self.ship_hit = 'X'
        self.type = type
        self.ship = 'O'
        self.guess = []


    def init(self, type):
        """
        Creates the game board that the user can play in.
        """
        ...

    def render_board(self, board):
        
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


    def add_ships(self):
        """
        Adds ships to game_board function and Computer function.
        """
        if type == 'Computer':
            while self.num_ships >= len(self.ship):
                Computer_board.append(self.ship)
        else:
            if type == 'Player':
                while self.num_ships >= len(self.ship):
                    board.append(self.ship)

    def guesses(self, row, column, ship_coordinates):
        """
        Returns a value of hit or miss.
        """
        self.ship_coordinates = ((row, column))
        self.guess.append((row, column))
        if (row, column) in board[ship_coordinates] == 'X':
            return 'Hit'
        else:
            return 'Miss'

    

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
    print(Computer_board)


def New_game():
    """
    Starts a new game and welcomes the user to the game.
    """
    print('Welcome To Battleship!! ')
    print('How to play? Try and guess where the')
    print('enemy ships are by choosing a row and a column.')
    print('Example: row: 2  comlumn: D \n \n\n')

    print('Enter Your Name: ')
    print('\n\n\n')
    player_name = input('          ')
    game = new Game(5)
    game.setup_boards(player_name)

    moves = 5
    while moves:
        coorinate_accepted =False
        while not coorinate_accepted:
            # Accept user coordinates
            game.make_move(player, coordinates)
        
        coorinate_accepted =False
        while not coorinate_accepted:
            # Generate random coordinates
            game.make_move(computer, random_coordinates)

        moves -=1

        if game.result:
            break

    if not game.result:
        # Do something

    
    winner = game.get_winner()




    pb = new Setup_Board(num_ships, ship_hit, ship, type, guess).Player_board('Player')
    # Player_board(type='Player')
    computer_board(type='Computer')


New_game()
