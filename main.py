from termcolor import colored
from os import system

titleText = colored("""
< 사칙연산 스도쿠 해결 프로그램 >
by Woohyun Jung


""", "green")

def edit(string): 
    system("cls")
    print(titleText + string)

board = []
enter = 0
def display_board():
    ims_board = [[0 for _2 in range(9)] for _ in range(9)]
    str_board = ""
    for i in board:
        for j in i[1]:
            x, y = j
            ims_board[y][x] = i[0]
    
    for i in ims_board:
        str_board += "".join(map(lambda x: str(x).ljust(5), i)) + '\n'

    return str_board

'''
board=[
    [9, [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)]],
    [11, [(3, 0), (4, 0)]],
    [11, [(5, 0), (6, 0)]],
    [25, [(7, 0), (8, 0), (7, 1)]],
    [50, [(2, 1), (2, 2), (2, 3), (1, 2), (0, 2), (0, 3)]],
    [24, [(3, 1), (3, 2), (3, 3)]],
    [90, [(4, 1), (5, 1), (6, 1)]],
    [12, [(8, 1), (8, 2)]],
    [48, [(4, 2), (5, 2), (4, 3)]],
    [5, [(6, 2), (7, 2)]],
    [6, [(1, 3), (1, 4)]],
    [10, [(5, 3), (6, 3)]],
    [13, [(7, 3), (8, 3)]],
    [2, [(0, 4), (0, 5)]],
    [14, [(2, 4), (3, 4)]],
    [64, [(4, 4), (5, 4), (6, 4), (7, 4)]],
    [3, [(8, 4), (8, 5)]],
    [2, [(1, 5), (2, 5)]],
    [36, [(3, 5), (2, 6), (3, 6)]],
    [15, [(0, 6), (1, 6)]],
    [112, [(4, 5), (5, 5), (4, 6)]],
    [25, [(6, 5), (7, 5), (7, 6)]],
    [7, [(8, 6), (8, 7), (8, 8)]],
    [42, [(7, 7), (7, 8), (6, 8)]],
    [15, [(6, 6), (6, 7)]],
    [27, [(5, 6), (5, 7), (5, 8)]],
    [15, [(1, 7), (2, 7)]],
    [15, [(3, 7), (4, 7)]],
    [120, [(0, 7), (0, 8), (1, 8)]],
    [288, [(2, 8), (3, 8), (4, 8)]]
]
'''

try:
    while enter < 81:
        edit(colored("< 현재 스도쿠 >\n", "magenta") + display_board() + '\n')
        num = input("숫자: ")
        coord = [tuple(map(lambda x: int(x) - 1, i.strip("()").split(','))) for i in input("좌표((x,y) 사이에 띄어쓰기): ").split(' ')]
        board.append([num, coord])
        enter += len(coord)
except:
    edit(colored("입력 중 오류가 발생했습니다", "red"))
    exit()

print(board)
