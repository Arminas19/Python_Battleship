num_ships = 5
computer_board = []

while num_ships > 0:
    Alpabet = None
    Alpabet = input('Enter a Row: ')
    if Alpabet.isdigit() and int(Alpabet) >= 0 and int(Alpabet) <= 9:
        Alpabet = int(Alpabet)
        Numbers = None
        Numbers = input('Enter a Column: ')
        if Numbers.isdigit() and int(Numbers) >= 0 and int(Numbers) <= 9:
            Numbers = int(Numbers)
            if computer_board[Alpabet][Numbers] == 'O':
                print('Hit')
                num_ships -= 1
                computer_board[Alpabet][Numbers] = 'X'
            else:
                if computer_board[Alpabet][Numbers] == 'X':
                    print('Already picked this Corordinate, Please Pick again.')
                else:
                    if computer_board[Alpabet][Numbers] == '-':
                        print('Missed')
                        computer_board[Alpabet][Numbers] = 'X'

        else:
            print('row and colum must be between 0 and 9, they must be an int')
    else:
        print('row and colum must be between 0 and 9, they must be an int')
        
"""
    if computer_board[Alpabet][Numbers] == 'O':
        print('Hit')
        num_ships -= 1
        computer_board[Alpabet][Numbers] = 'X'
        # return 'Hit'

    else:
        if computer_board[Alpabet][Numbers] == 'X':
            print('Already picked this Corordinate, Please Pick again.')
        else:
            if computer_board[Alpabet][Numbers] == ['-']:
                print('Missed')
                computer_board[Alpabet][Numbers] = 'X'
                # return 'Missed'
"""