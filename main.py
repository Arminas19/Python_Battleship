import random


class Setup_Board:
    def __init__(self, num_ships, ship_hit, ship, type, guess, water,
                 computer_board, board, player_name, row, column, alpabet, numbers):
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

    def validate_corordinates(self):
        """
        Vaildates the corordinates that the Computer and Player Choose
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
                        self.render_computer_board('Computer')
                       
                    elif self.computer_board[self.alpabet][self.numbers] == 'X':
                        print('Already picked this Corordinate, Please Pick again.')
                    else:
                        if self.computer_board[self.alpabet][self.numbers] == '-':
                            print('You Missed')
                            self.computer_board[self.alpabet][self.numbers] = 'X'
                            self.render_computer_board('Computer')
                            

                else:
                    print('row and colum must be between 0 and 9, they must be an int')
            else:
                print('row and colum must be between 0 and 9, they must be an int')

        if self.num_ships == 0:
            print('Player Has Won, starting new game')
            New_game()
    
    """
        Alpabet = None
        while True:
            Alpabet = input('Enter a Row: ')
            if Alpabet.isdigit() and int(Alpabet) >= 0 and int(Alpabet) <= 9:
                Alpabet = int(Alpabet) 
                break
            else: 
                print('Row must between 0 and 9 and be an int')
                continue

        Numbers = None
        while True:
            Numbers = input('Enter a Column: ')
            if Numbers.isdigit() and int(Numbers) >= 0 and int(Numbers) <= 9:
                Numbers = int(Numbers)
                break
            else: 
                print('Column must between 0 and 9 and be an int')
                continue

        print(self.computer_board[Alpabet][Numbers])

        if self.computer_board[Alpabet][Numbers] == 'O':
            print('Hit')
            self.computer_board[Alpabet][Numbers] = 'X'
            return 'Hit'

        else:
            if self.computer_board[Alpabet][Numbers] == 'X':
                print('Already picked this Corordinate, Please Pick again.')
            else:
                if self.computer_board[Alpabet][Numbers] == ['-']:
                    print('Missed')
                    self.computer_board[Alpabet][Numbers] = 'X'
                    return 'Missed'
        """

    def populate_boards(self, computer_board, board):
        """
        Populates the two boards
        """
        del computer_board
        del board

        for board in [self.computer_board, self.board]:
            counter = 1
            # computer_counter = 1
            while counter <= 5:  # or computer_counter <= 5:
                random_number_x = random.randrange(10)
                random_number_y = random.randrange(10)

                # print(random_number)
                # fill the computer board
                # check if already taken, if so continue but dont increase the counter
                if board[random_number_x][random_number_y] == 'O':
                    continue
                else:
                    # otherwise add the board 0, and increase the counter
                    board[random_number_x][random_number_y] = 'O'
                    counter += 1
                # if i == 'computer':
                #     # check if already taken, if so continue but dont increase the counter
                #     if self.computer_board[random_number][random_number] == 'O':
                #         continue
                #     else:
                #         # otherwise add the board 0, and increase the counter
                #         self.computer_board[random_number][random_number] = 'O'
                #         computer_counter += 1
                #         continue
                # elif i == 'player':
                #     if self.board[random_number][random_number] == 'O':
                #         continue
                #     else:
                #         self.board[random_number][random_number] = 'O'
                #         counter += 1
                #         continue

    def make_guess(self, player_name):
        """
        computer will auto guess.
        """
        computer_guess_x = random.randrange(10)
        computer_guess_y = random.randrange(10)
        while self.num_ships >= 0:
            print(f'computer row: {computer_guess_x}')
            print(f'computer column: {computer_guess_y}')
            if self.board[computer_guess_x][computer_guess_y] == 'O':
                print('Computer has Hit one of your ships')
                self.board[computer_guess_x][computer_guess_y] = 'X'
                self.num_ships -= 1
                self.render_Player_board('Player', player_name)
                
            elif self.board[computer_guess_x][computer_guess_y] == '-':
                print('Computer has Missed')
                self.board[computer_guess_x][computer_guess_y] = 'X'
                self.render_Player_board('Player', player_name)
                
            else:
                self.board[computer_guess_x][computer_guess_y] == 'X'

        if self.num_ships == 0:
            print('Computer has Won, starting new game')
            New_game()
         
    def render_Player_board(self, type, player_name):
        """
        Creates the game board that the user can play in.
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
        renders Computers Board
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


def New_game():
    """
    Starts a new game and welcomes the user to the game.
    """
    alpabet = None
    numbers = None
    # player_score = 9
    # computer_score = 9
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
                           computer_board, board, player_name, row, column, alpabet, numbers)
    print('---------------------------------------------')
    print('This is what the boards look like.')
    setup_pb.render_Player_board('Player', player_name)
    setup_pb.render_computer_board('Computer')
    print('---------------------------------------------')
    setup_pb.populate_boards(computer_board, board)
    print('---------------------------------------------')
    print('Game Starts Here')
    setup_pb.render_Player_board('Player', player_name)
    setup_pb.render_computer_board('Computer')
    setup_pb.validate_corordinates()
    setup_pb.make_guess(player_name)


"""
    if type == 'Player' and num_ships == 0:
        print('Computer has won, starting new game')
        New_game()
    else:
        if type == 'Computer' and num_ships == 0:
            print('Player Has Won, starting new game')
            New_game()
"""
"""
    # For player
    x, y = -1, -1
    while not setup_pb.validate_corordinates(self.board, x,y):
        x,y = input()
    make_move(self.board, x, y)

    # For computer
    x, y = -1 ,-1
    while not setup_pb.validate_corordinates(self.computer_board, x,y):
        x,y = make_guess()
    is_hit= make_move(self.computer_board, x, y)
"""

New_game()
