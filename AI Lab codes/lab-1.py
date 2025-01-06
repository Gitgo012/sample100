def dominance(arr):
    arr = list(arr)
    x = arr.count('x')
    o = arr.count('o')

    if x > 0 and o == 0:
        if x == 3:
            return 100, 0
        return x, 0
    elif x == 0 and o > 0:
        if o == 3:
            return 0, 100
        return 0, o
    else:
        return 0, 0

def strength(board):
    x_strength = 0
    o_strength = 0
    #row operations
    for i in range(len(board)):
        xc, oc = dominance(board[i, 0:3])
        x_strength += xc
        o_strength += oc
    for j in range(len(board)):
        xc, oc = dominance(board[0:3, j])
        x_strength += xc
        o_strength += oc
    #diagonal 1
    diagonal1 = [board[0,0], board[1,1], board[2,2]]
    xc,oc = dominance(diagonal1)
    x_strength += xc
    o_strength += oc
    #diagonal 2
    diagonal2 = [board[0,2], board[1,1], board[2,0]]
    xc, oc = dominance(diagonal2)
    x_strength += xc
    o_strength += oc

    x_strength = 100 if x_strength >= 100 else x_strength
        
    if o_strength >= 100:
        o_strength = 100

    return x_strength-o_strength, o_strength-x_strength

import numpy as np

board = np.array([['x','b','o'],['o','b','o'],['x','b','o']])

print("Input Board:")
print(board)
x, y = strength(board)

print('X:', x)
print('O:', y)