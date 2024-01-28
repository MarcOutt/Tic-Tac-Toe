# initialization
EMPTY_CELL = ' '

board = [[EMPTY_CELL] * 3 for _ in range(3)]

player_1 = False
player_2 = False


#  display the board
def display_board():
    for a, line in enumerate(board, start=1):
        print(" | ".join(line))
        if a == 3:
            print('\n')
        else:
            print("-" * 9)


# User input
def get_choice(player):
    if player == "X":
        print("C'est au tour du joueur 1 de jouer")
    else:
        print("C'est au tour du joueur 2 de jouer")

    while True:
        try:
            line = int(input("Veuillez choisir votre ligne "))
            column = int(input("Veuillez choisir votre colonne "))
            if 0 < line < 4 and 0 < column < 4:
                return line, column
            else:
                print("Veuillez choisir un numéro entre 1 et 3")
        except ValueError:
            print("Veuillez entrer un nombre entier valide")


# Check the user's choice
def check_choice(line, column):
    return board[line -1][column -1] == EMPTY_CELL


def check_win(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            if player == "X":
                print("Le joueur 1 a gagné")
            else:
                print("Le joueur 2 a gagné")
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            if player == "X":
                print("Le joueur 1 a gagné")
            else:
                print("Le joueur 2 a gagné")
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        if player == "X":
            print("Le joueur 1 a gagné")
        else:
            print("Le joueur 2 a gagné")
        return True
    return False


def play(player):
    line, column = get_choice(player)
    if check_choice(line, column):
        board[line - 1][column - 1] = player
    display_board()
    return check_win(player)


print("""           __ _  __ _ _ __ ___   ___  ___ 
          / _` |/ _` | '_ ` _ \ / _ \/ __|
         | (_| | (_| | | | | | |  __/\__ |
          \__, |\__,_|_| |_| |_|\___||___/
           __/ |                          
          |___/            \n""")
print("WELCOME TO TIC TAC TOE \n")

print(display_board())

while player_1 == False and player_2 == False:
    player_1 = play("X")
    if player_1:
        break
    player_2 = play("O")
