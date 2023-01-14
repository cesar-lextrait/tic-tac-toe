
board = ["-", "-","-",
        "-", "-", "-",
        "-", "-", "-",]
joueur = "X"
joueur2 ="O"
winner = None
jeuEnCour = True


#imprimer le plateau
def printPlateau(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

#prendre entrée des joueurs 
def playerInput(board):
    while True:
        if joueur == "X":
            entree = int(input("Entrez un nombre entre 1 et 9\033[1;34m Player (X) \033[0;0m : "))
        else:
            joueur2 == "O"
            entree =int(input("Entrez un nombre entre 1 et 9\033[1;31m Player (O) \033[0;0m : "))
        if entree >= 1 and entree <= 9 and board[entree-1] == "-":
            board[entree-1] = joueur
            break
        else:
                print(f"Position déjà prise par le joueur - \033[1;34m Player (X) \033[0;0m !")
                print(f"Position déjà prise par le joueur - \033[1;31m Player (0) \033[0;0m !")
        printPlateau(board)

#check victoire 
def check_winner(board, check_type):
    global winner
    indexes = None
    if check_type == 'horizontale':
        indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    elif check_type == 'colomne':
        indexes = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    elif check_type == 'diagonale':
        indexes = [[0, 4, 8], [2, 4, 6]]
    for i in indexes:
        if board[i[0]] == board[i[1]] == board[i[2]] and board[i[0]] != "-":
            winner = board[i[0]]
            return True

def checkNul(board):
    if "-" not in board:
        printPlateau(board)
        print("Match nul")
        return True
    return False

def checkVictoire(board):
    if check_winner(board, 'horizontale'):
        print(f"Le gagnant est {winner}") 
    elif check_winner(board,'colomne'):
        print(f"Le gagnant est {winner}") 
    elif check_winner(board, 'diagonale'):
        print(f"Le gagnant est {winner}") 


#échanger joueurs
def altJoueur():
    global joueur
    if joueur == "X":
        joueur = "O"
    else:
        joueur ="X"


#cour du jeu 
while jeuEnCour:
    jeuEncour = True
    printPlateau(board)
    playerInput(board)
    if checkNul(board):
        break
    if checkVictoire(board):
        break
    altJoueur()
    