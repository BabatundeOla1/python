player1name = input("Player 1 Enter your name: ")
player2name = input("P;ayer 2 Enter your name: ")

capitalize_player1name = player1name.capitalize()
capitalize_player2name = player2name.capitalize()

first_character = capitalize_player1name[0]
second_character = capitalize_player2name[0]
print()

game_board = [[" ","|"," ","|"," "],
              ["-","+","-","+","-"],
              [" ","|"," ","|"," "],
              ["-","+","-","+","-"],
              [" ","|"," ","|"," "],]

def create_game_board(board):
    for index in range(len(game_board)):
        for elements in range(len(game_board)):
            print(game_board[index][elements], end=" ")
        print()

def player1_move(game_board, player1_name):
    if player1_name == player2name:
        return "Kindly choose another name"

        player1_position = int(input("Player 1 Enter your position(1-9): "))

        if player1_position < 1 or player1_position > 9:
            return "Invalid Position"
        else:
            method_name2(game_board, player1_name, player1_position)

        create_game_board(game_board)
        get_winner()


def method_name2(game_board, player1_name, player1_position):
    match player1_position:
        case 1:
            game_board[0][0] = player1_name
        case 2:
            game_board[0][2] = player1_name
        case 3:
            game_board[0][4] = player1_name
        case 4:
            game_board[2][0] = player1_name
        case 5:
            game_board[2][2] = player1_name
        case 6:
            game_board[2][4] = player1_name
        case 7:
            game_board[4][0] = player1_name
        case 8:
            game_board[4][2] = player1_name
        case 9:
            game_board[4][4] = player1_name


def player2_move(game_board, player2_name):
    if player2_name == player1name:
        return "Kindly choose another name"

    while True:
        player2_position = int(input("Player 2 Enter your position(1-9): "))

        if player2_position < 1 or player2_position > 9:
            return "Invalid Position"
        else:
            method_name(game_board, player2_name, player2_position)

        create_game_board(game_board)
        get_winner()


def method_name(game_board, player2_name, player2_position):
    match player2_position:
        case 1:
            game_board[0][0] = player2_name
        case 2:
            game_board[0][2] = player2_name
        case 3:
            game_board[0][4] = player2_name
        case 4:
            game_board[2][0] = player2_name
        case 5:
            game_board[2][2] = player2_name
        case 6:
            game_board[2][4] = player2_name
        case 7:
            game_board[4][0] = player2_name
        case 8:
            game_board[4][2] = player2_name
        case 9:
            game_board[4][4] = player2_name


def get_winner():

        print(game_board[2][0], "Win")




print(player1_move(game_board, first_character))
print(player2_move(game_board, second_character))






