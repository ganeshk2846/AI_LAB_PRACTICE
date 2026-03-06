# Interactive Tic-Tac-Toe using Minimax

import math

board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    print(board[0],'|',board[1],'|',board[2])
    print("---------")
    print(board[3],'|',board[4],'|',board[5])
    print("---------")
    print(board[6],'|',board[7],'|',board[8])
    print("\n")

def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

def is_full():
    return ' ' not in board

def minimax(is_max):

    if check_winner('X'):
        return 1
    if check_winner('O'):
        return -1
    if is_full():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)
        return best


def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move


print("Tic Tac Toe Game")
print("You are O, Computer is X")
print("Positions are 0-8\n")

print_board()

while True:

    # User move
    user = int(input("Enter your move (0-8): "))
    
    if board[user] != ' ':
        print("Position already taken!")
        continue

    board[user] = 'O'
    print_board()

    if check_winner('O'):
        print("You Win!")
        break

    if is_full():
        print("Draw!")
        break

    # Computer move
    comp = best_move()
    board[comp] = 'X'
    print("Computer move:", comp)
    print_board()

    if check_winner('X'):
        print("Computer Wins!")
        break

    if is_full():
        print("Draw!")
        break