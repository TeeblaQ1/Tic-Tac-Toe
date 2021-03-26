grid = [" " for _ in range(9)]


def print_grid(cells):
    print(f"""
    ---------
    | {cells[0]} {cells[1]} {cells[2]} |
    | {cells[3]} {cells[4]} {cells[5]} |
    | {cells[6]} {cells[7]} {cells[8]} |
    ---------
    """)


X_win = ["X", "X", "X"]
O_win = ["O", "O", "O"]


def x_wins(matrix):
    if matrix[:3] == X_win or matrix[3:6] == X_win or matrix[6:9] == X_win:
        return True
    elif matrix[:7:3] == X_win or matrix[1:8:3] == X_win or matrix[2:9:3] == X_win:
        return True
    elif matrix[0:9:4] == X_win or matrix[2:7:2] == X_win:
        return True
    else:
        return False


def o_wins(matrix):
    if matrix[:3] == O_win or matrix[3:6] == O_win or matrix[6:9] == O_win:
        return True
    elif matrix[:7:3] == O_win or matrix[1:8:3] == O_win or matrix[2:9:3] == O_win:
        return True
    elif matrix[0:9:4] == O_win or matrix[2:7:2] == O_win:
        return True
    else:
        return False


print_grid(grid)
counter = 1
while True:
    coordinates = input("Enter the coordinates: ").split()
    if len(coordinates) != 2:
        print("Please enter two coordinates (must be separated by a space) to represent row and column")
        continue
    if not coordinates[0].isdigit() or not coordinates[1].isdigit():
        print("You should enter a number!")
        continue
    elif int(coordinates[0]) not in range(0, 4) or int(coordinates[1]) not in range(0, 4):
        print("Coordinates should be from 1 to 3!")
        continue
    spot = ((int(coordinates[0]) - 1) * 3) + (int(coordinates[1])) - 1
    if grid[spot] == " " or grid[spot] == "_":
        if counter % 2 == 1:
            grid[spot] = 'X'
        else:
            grid[spot] = 'O'
        print_grid(grid)
        counter += 1
    else:
        print("This cell is occupied! Choose another one!")
    if x_wins(grid):
        print("X wins")
        break
    elif o_wins(grid):
        print("O wins")
        break
    elif " " not in grid and "_" not in grid:
        print("Draw")
        break
    else:
        continue
