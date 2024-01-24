# initialization
board = [[' ']*3 for _ in range(3)]


#  display the board
def display_board():
    a = 0
    for line in board:
        a += 1
        print(" | ".join(line))
        if a == 3:
            print('\n')
        else:
            print("-" * 9)

# User input
def get_choice():
    line = int(input("Veuillez choisir votre ligne "))
    column = int(input("Veuillez choisir votre colonne "))
    return line, column


# Check the user's choice
def check_choice(line, column):
    if board[line-1][column-1] == "X" or board[line-1][column-1] == "0":
        print("Le choix n'est pas disponible")
        return False
    elif 1 > line < 4 or 1 > column < 4 :
        print("Veuillez choisir un numéro entre 1 et 3")
        return False
    else:
        return True


line, column = get_choice()
if check_choice(line, column):
    board[line - 1][column - 1] = "X"
display_board()

