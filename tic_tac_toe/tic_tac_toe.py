from random import randrange

DIMENSION = 3
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

game_turn = 'X'

scheme = [  [[0,0], [0,1], [0,2]],  # rows
            [[1,0], [1,1], [1,2]], 
            [[2,0], [2,1], [2,2]],

            [[0,0], [1,0], [2,0]],  # columns
            [[0,1], [1,1], [2,1]],
            [[0,2], [1,2], [2,2]], 
            
            [[0,0], [1,1], [2,2]],  # diagonals
            [[0,2], [1,1], [2,0]] ]

num_X = 0
num_O = 0

def read_cells():
    global num_O, num_X
    read = input("Enter the cells: ")
    index_read = 0
    if len(read) == 9:
        for row in range(0, DIMENSION):
            for cell in range(0, DIMENSION):
                if read[index_read] == '_':
                    grid[row][cell] = ' '
                else:
                    grid[row][cell] = read[index_read]
                    if read[index_read] == 'X':
                        num_X +=1
                    elif read[index_read] == 'O':
                        num_O += 1
                index_read += 1


def draw_cells():
    print("---------")
    for row in grid:
        print("| ", end='')
        for cell in row:
            print(cell + " ", end='')
        print("|")
    print("---------")

def change_turn():
    global game_turn
    if game_turn == 'X':
        game_turn = 'O'
    else:
        game_turn = 'X'

def initialize_game():
    draw_cells()

def clear_grid():
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def is_occupied(coordinates):
    if grid[coordinates[0] - 1][coordinates[1] - 1] == ' ':
        return False
    else:
        return True

def in_range(coordinates):
    if coordinates[0] > 3 or coordinates[0] < 1 or coordinates[1] > 3 or coordinates[1] <1:
        return False
    else:
        return True

def are_numbers(coordinates):
    if type(coordinates[0]) == int and type(coordinates[1]) == int:
        return True
    else:
        return False

def is_valid_coordinates(coordinates): 
    if not in_range(coordinates):
        print("Coordinates should be from 1 to 3!")
        return False
    elif is_occupied(coordinates):
        print("This cell is occupied! Choose another one!")
        return False
    else:
        return True  

def add_to_grid(coordinates):
    grid[coordinates[0] - 1][coordinates[1] - 1] = game_turn
    draw_cells()
    change_turn()

def read_next_move():
    done = False
    while not done:
        try:
            coordinates = [int(data) for data in input("Enter the coordinates: ").split()]
            while not is_valid_coordinates(coordinates):
                coordinates = [int(data) for data in input("Enter the coordinates: ").split()]
            done = True
        except ValueError:
            print("You should enter numbers!")
        
    add_to_grid(coordinates)

def check_initial_turn():
    if num_X > num_O:
        change_turn()

def is_player_win(player):
    for combination in scheme:
        cont = 0
        for position in combination:
            if grid[position[0]][position[1]] == player:
                cont +=1
        if cont == 3:
            return True
    return False

def is_grid_complete():
    for row in grid:
        for cell in row:
            if cell == ' ':
                return False
    return True

def game_ended():
    if is_player_win('X'):
        print("X wins")
    elif is_player_win('O'):
        print("O wins")
    elif is_grid_complete():
        print("Draw")

def is_end_game():
    if is_player_win('X') or is_player_win('O') or is_grid_complete():
        return True
    else:
        return False

def user_next_move():
    read_next_move()

def computer_next_move(game_level):
    if game_level == 'easy':
        print('Making move level "easy"')
        coordinates = [randrange(3), randrange(3)]
        while is_occupied(coordinates):
            coordinates = [randrange(3), randrange(3)]
        add_to_grid(coordinates)


def game_user_user():
    while not is_end_game():
        user_next_move()
        if not is_end_game():
            user_next_move()

def game_user_computer(game_level):
    while not is_end_game():
        user_next_move()
        if not is_end_game():
            computer_next_move(game_level)

def game_computer_user(game_level):
    while not is_end_game():
        ucomputer_next_move(game_level)
        if not is_end_game():
            user_next_move()

def game_computer_computer(game_level_1, game_level_2):
    while not is_end_game():
        computer_next_move(game_level_1)
        if not is_end_game():
            computer_next_move(game_level_2)


def is_correct_parameters(parameters):
    if len(parameters) not in [1, 3]:
        print("Bad parameters!")
        return False
    elif len(parameters) == 1 and parameters[0] != 'exit':
        print("Bad parameters!")
        return False
    elif len(parameters) == 3 and (parameters[1] not in ['user', 'easy'] or parameters[2] not in ['user', 'easy']):
        print("Bad parameters!")
        return False
    else: 
        return True

def start_menu(parameters):
    if parameters[1] == 'user' and parameters[2] == 'user':
        game_user_user()
    elif parameters[1] == 'user' and parameters[2] == 'easy':
        game_user_computer(parameters[2])
    elif parameters[1] == 'easy' and parameters[2] == 'user':
        game_computer_user(parameters[1])
    elif parameters[1] == 'easy' and parameters[2] == 'easy':
        game_computer_computer(parameters[1], parameters[2])

    game_ended()
    clear_grid()

def menu():
    parameters = input("Input command: ").split()
    while not is_correct_parameters(parameters):
        parameters = input("Input command: ").split()
    
    if parameters[0] == 'exit':
        exit()
    elif parameters[0] == 'start':
        initialize_game()
        start_menu(parameters)

while True:
    menu()
    print()

