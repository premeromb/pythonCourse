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
            [[2,0], [1,1], [0,2]] ]

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

def oposite_turn():
    if game_turn == 'X':
        return 'O'
    else:
        return 'X'

def initialize_game():
    draw_cells()

def clear_grid():
    global grid
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
  

def is_player_close_to_win(player):
    for combination in scheme:
        cont = 0
        position_to_win = []
        for position in combination:
            if grid[position[0]][position[1]] == player:
                cont +=1
            if grid[position[0]][position[1]] == ' ':
                position_to_win = position
        if cont == 2 and position_to_win:
            return [position_to_win[0] + 1, position_to_win[1] + 1]
    return False

def is_grid_complete():
    for row in grid:
        for cell in row:
            if cell == ' ':
                return False
    return True

def is_end_game():
    if is_player_win('X') or is_player_win('O') or is_grid_complete():
        return True
    else:
        return False

def is_correct_parameters(parameters):
    if len(parameters) not in [1, 3]:
        print("Bad parameters!")
        return False
    elif len(parameters) == 1 and parameters[0] != 'exit':
        print("Bad parameters!")
        return False
    elif len(parameters) == 3 and (parameters[0] != 'start' or  parameters[1] not in ['user', 'easy', 'medium'] or parameters[2] not in ['user', 'easy', 'medium']):
        print("Bad parameters!")
        return False
    else: 
        return True


def game_ended():
    if is_player_win('X'):
        print("X wins")
    elif is_player_win('O'):
        print("O wins")
    elif is_grid_complete():
        print("Draw")

def user_next_move():
    read_next_move()

def play_easy_level():
    print('Making move level "easy"')
    coordinates = [randrange(3), randrange(3)]
    while is_occupied(coordinates):
        coordinates = [randrange(3), randrange(3)]
    add_to_grid(coordinates)

def play_medium_level():
    print('Making move level "medium"')

    coordinates_to_win = is_player_close_to_win(game_turn)
    coordinates_not_to_lose = is_player_close_to_win(oposite_turn())

    if coordinates_to_win != False:
        print("va a ganar")
        add_to_grid(coordinates_to_win)
    elif coordinates_not_to_lose != False:
        print("evita perder")
        add_to_grid(coordinates_not_to_lose)
    else:
        print("de momento nada")
        coordinates = [randrange(3), randrange(3)]
        while is_occupied(coordinates):
            coordinates = [randrange(3), randrange(3)]
        add_to_grid(coordinates)



def computer_next_move(game_level):
    if game_level == 'easy':
        play_easy_level()
    elif game_level == 'medium':
        play_medium_level()

def game_turn_controller(game_level_1, game_level_2):
    while not is_end_game():
        if game_level_1 == 'user':
            user_next_move()
        else:
            computer_next_move(game_level_1)
        if not is_end_game():
            if game_level_2 == 'user':
                user_next_move()
            else:
                computer_next_move(game_level_2)


def start_game(parameters):
    game_turn_controller(parameters[1], parameters[2])
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
        start_game(parameters)

def game():
    while True:
        menu()
        print()

game()