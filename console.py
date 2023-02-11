from termcolor import colored
from os import system

from solver import sdoku

titleText = colored("""
< 사칙연산 스도쿠 해결 프로그램 >
by Woohyun Jung


""", "green")

def edit(string): 
    system("cls")
    print(titleText + string)

board = []
enter = 0
def display_board(inp_board, typ=0):
    str_board = ""

    if typ == 0:
        ims_board = [[0 for _2 in range(9)] for _ in range(9)]
        for i in inp_board:
            for j in i[1]:
                x, y = j
                ims_board[y][x] = i[0]
    elif typ == 1:
        ims_board = inp_board

    for i in ims_board:
        str_board += "".join(map(lambda x: str(x).ljust(5), i)) + '\n'

    return str_board

try:
    while enter < 81:
        edit(colored("< 현재 스도쿠 >\n", "magenta") + display_board(board) + '\n')
        num = input("숫자: ")
        coord = [tuple(map(lambda x: int(x) - 1, i.strip("()").split(','))) for i in input("좌표((x,y) 사이에 띄어쓰기): ").split(' ')]
        board.append([num, coord])
        enter += len(coord)
except:
    edit(colored("입력 중 오류가 발생했습니다", "red"))
    exit()

check_board = [[0] * 9 for i in range(9)]
for i in board:
    for j in i[1]:
        x, y = j
        check_board[y][x]  = i[0]

check_n = 0
for i in check_board:
    for j in i:
        if j != 0:
            check_n += 1

if check_n != 81:
    edit(colored("입력에 문제가 있습니다", "red"))
    exit()

edit(colored("잠시만 기다려주세요 (예상 시간: 1~2분)", "yellow"))
res = sdoku(board).solve()
edit(colored("< 정답 >\n", "magenta") + display_board(res, 1) + '\n')
