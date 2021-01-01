from random import randrange

DIMENSION = 3
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

user_player = 'X'
computer_player = 'O'

game_level = 'easy'

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
        

def add_to_grid(coordinates, game_turn):
    grid[coordinates[0] - 1][coordinates[1] - 1] = game_turn
    draw_cells()

def read_next_move(game_turn):
    done = False
    while not done:
        try:
            coordinates = [int(data) for data in input("Enter the coordinates: ").split()]
            while not is_valid_coordinates(coordinates):
                coordinates = [int(data) for data in input("Enter the coordinates: ").split()]
            done = True
        except ValueError:
            print("You should enter numbers!")
        
    add_to_grid(coordinates, game_turn)



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

def check_game_state():
    if is_player_win('X'):
        print("X wins")
        exit()
    elif is_player_win('O'):
        print("O wins")
        exit()
    elif is_grid_complete():
        print("Draw")
        exit()

def initialize_game():
    draw_cells()

def user_next_move():
    read_next_move(user_player)
    check_game_state()

def computer_next_move():

    if game_level == 'easy':
        print('Making move level "easy"')
        coordinates = [randrange(3), randrange(3)]
        while is_occupied(coordinates):
            coordinates = [randrange(3), randrange(3)]
        add_to_grid(coordinates, computer_player)

    check_game_state()


initialize_game()

while(True):
    user_next_move()
    
    computer_next_move()



