import random


class Setup_Board:
    """
    This setup_Board class sets up all the other methods so that they can all be connected and used together.
    """
    def __init__(self, num_ships, ship_hit, ship, type, guess, water,
                 computer_board, board, player_name, row, column, alpabet, numbers, computer_board2):
        self.num_ships = 5
        self.ship_hit = 'X'
        self.type = type
        self.ship = 'O'
        self.guess = []
        self.water = ['-']
        self.computer_board = []
        self.board = []
        self.player_name = player_name
        self.row = 9
        self.column = 9
        self.computer_board2 = []

    def validate_corordinates(self, player_name, alpabet, numbers):
        """
        Vaildates the corordinates that the Player Choose, it also updates the render_computer_board and 
        the render_computer_board2() functions once the corordinates have been set. 
        """
        self.num_ships = 5
        while self.num_ships > 0:

            self.alpabet = None
            self.alpabet = input('Enter a Row: ')
            if self.alpabet.isdigit() and int(self.alpabet) >= 0 and int(self.alpabet) <= 9:
                self.alpabet = int(self.alpabet)
                self.numbers = None
                self.numbers = input('Enter a Column: ')
                if self.numbers.isdigit() and int(self.numbers) >= 0 and int(self.numbers) <= 9:
                    self.numbers = int(self.numbers)
                    if self.computer_board[self.alpabet][self.numbers] == 'O':
                        print('You Hit')
                        self.num_ships -= 1
                        self.computer_board[self.alpabet][self.numbers] = 'X'
                        self.computer_board2[self.alpabet][self.numbers] = 'X'
                        self.render_computer_board2(alpabet, numbers)
                        self.make_guess(player_name)
                    elif self.computer_board2[self.alpabet][self.numbers] == 'X':
                        print('Already picked this Corordinate, Please Pick again.')
                    else:
                        if self.computer_board2[self.alpabet][self.numbers] == '-':
                            print('You Missed')
                            self.computer_board2[self.alpabet][self.numbers] = 'X'
                            self.render_computer_board2(alpabet, numbers)
                            self.make_guess(player_name) 
                                           
                else:
                    print('row and colum must be between 0 and 9, they must be an int')
            else:
                print('row and colum must be between 0 and 9, they must be an int')

        if self.num_ships == 0:
            print('Player Has Won, starting new game')
            New_game()

    def populate_boards(self, computer_board, board):
        """
        Populates the two boards, render_computer_board and reder_player_board. 
        """
        del computer_board
        del board

        for board in [self.computer_board, self.board]:
            counter = 1
            while counter <= 5: 
                random_number_x = random.randrange(10)
                random_number_y = random.randrange(10)

                if board[random_number_x][random_number_y] == 'O':
                    continue
                else:
                    board[random_number_x][random_number_y] = 'O'
                    counter += 1
            
    def make_guess(self, player_name):
        """
        computer will auto guess Corordinates, and this will update the render_player_board() function.
        """
        self.num_ships = 5
        computer_guess_x = random.randrange(10)
        computer_guess_y = random.randrange(10)
        while self.num_ships > 0:
            print(f'computer row: {computer_guess_x}')
            print(f'computer column: {computer_guess_y}')
            if self.board[computer_guess_x][computer_guess_y] == 'O':
                print('Computer has Hit one of your ships')
                self.board[computer_guess_x][computer_guess_y] = 'X'
                self.num_ships -= 1
                self.render_Player_board('Player', player_name) 
                break
               
            elif self.board[computer_guess_x][computer_guess_y] == '-':
                print('Computer has Missed')
                self.board[computer_guess_x][computer_guess_y] = 'X'
                self.render_Player_board('Player', player_name)  
                break
               
            else:
                computer_guess_x = random.randrange(10)
                computer_guess_y = random.randrange(10)
                                  
        if self.num_ships == 0:
            print('Computer has Won, starting new game')
            New_game()      
         
    def render_Player_board(self, type, player_name):
        """
        Creates the game board that the Computer will guess in.
        """
        print('\n\n\n')
        print(f'          {self.player_name}')
        print('    0 1 2 3 4 5 6 7 8 9')
        print('  +---------------------+')
        for self.row in range(10):
            self.board.append(self.water * 10)

        letters = 0
        for self.row in range(10):
            print(chr(letters + 65), end=' | ')
            for self.column in range(len(self.board[letters])):
                print(self.board[letters][self.column], end=' ')
            print('| ')
            letters += 1
        print('  +---------------------+ \n\n\n')

    def render_computer_board(self, type):
        """
        renders Computers Board that the user will play in.
        """
        print('         COMPUTER ')
        print('    0 1 2 3 4 5 6 7 8 9')
        print('  +---------------------+')
        for self.row in range(10):
            self.computer_board.append(self.water * 10)

        letters = 0
        for self.row in range(10):
            print(chr(letters + 65), end=' | ')
            for self.column in range(len(self.computer_board[letters])):
                print(self.computer_board[letters][self.column], end=' ')
            print('| ')
            letters += 1
        print('  +---------------------+ \n\n\n')

    def render_computer_board2(self, alpabet, numbers):
        """
        renders Computer Board that the user will see, their is 2 computer board, one is for the user to see
        and the other render_computer_board function is to play on. 
        """
        print('         COMPUTER ')
        print('    0 1 2 3 4 5 6 7 8 9')
        print('  +---------------------+')
        for self.row in range(10):
            self.computer_board2.append(self.water * 10)

        letters = 0
        for self.row in range(10):
            print(chr(letters + 65), end=' | ')
            for self.column in range(len(self.computer_board2[letters])):
                print(self.computer_board2[letters][self.column], end=' ')
            print('| ')
            letters += 1
        print('  +---------------------+ \n\n\n')


def New_game():
    """
    Starts a new game and welcomes the user to the game.
    """
    computer_board2 = []
    alpabet = None
    numbers = None
    column = 9
    row = 9
    computer_board = []
    board = []
    num_ships = 5
    ship_hit = 'X'
    ship = 'O'
    guess = []
    water = ['-']
    print('-------------------------------------------')
    print('Welcome To Battleship!! ')
    print('How to play? Try and guess where the')
    print('enemy ships are by choosing a row and a column.')
    print('Example: row: 2  comlumn: 2 \n \n\n')
    print('Row and column must be between 0 and 9.')
    player_name = (input('Enter Your Name: '))
    print('-------------------------------------------\n\n\n')
    setup_pb = Setup_Board(num_ships, ship_hit, ship, type, guess, water,
                           computer_board, board, player_name, row, column, alpabet, numbers, computer_board2)
    print('---------------------------------------------')
    print('This is what the boards look like.')
    setup_pb.render_Player_board('Player', player_name)
    setup_pb.render_computer_board('Computer')
    print('---------------------------------------------')
    setup_pb.populate_boards(computer_board, board)
    print('---------------------------------------------')
    print('Game Starts Here')
    setup_pb.render_Player_board('Player', player_name)
    setup_pb.render_computer_board2(alpabet, numbers)
    setup_pb.make_guess(player_name)
    setup_pb.validate_corordinates(player_name, alpabet, numbers)
    

New_game()
