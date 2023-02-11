from tkinter import Tk, Button, Label, IntVar
from tkinter.font import Font
from tkinter.simpledialog import askinteger

from time import time

from solver import sdoku

class GuiSudoku:
    def __init__(self):
        self.window = Tk()
        self.window.title("사칙연산 스도쿠")

        self.btn_arr = [[[] for _2 in range(9)] for _ in range(9)]
        self.lbl_arr = [[[] for _2 in range(9)] for _ in range(9)]

        self.cache = []
        self.board = []

        self.registered_num = 0

    def solve(self):
        self.sovle_btn.grid_remove()
        self.wait_btn.grid(row=13, column=0, columnspan=9)
        start_time = time()
        res = sdoku(self.board).solve()

        for x in range(9):
            for y in range(9):
                self.lbl_arr[x][y].config(text = str(res[y][x]))
        
        self.wait_btn.config(text = f"{time() - start_time}s")
        

    def add_board(self):
        value = askinteger("숫자 입력", "연산을 해서 나올 숫자를 입력해주세요", minvalue = 1, maxvalue = 10000)
        self.addnum_btn.grid_forget()
        self.ok_btn.grid(row = 13, column = 0, columnspan = 9)
        
        self.btn_clicking = True
        self.ok.set(0)
        
        self.ok_btn.wait_variable(self.ok)
        
        self.ok.set(0)
        self.btn_clicking = False
        self.board.append([value, self.cache])
        self.registered_num += len(self.cache)
        for i, j in self.cache:
            self.btn_arr[i][j].grid_remove()
            self.lbl_arr[i][j].config(text = str(value))
            self.lbl_arr[i][j].grid(row = j + 1, column = i, columnspan = 1)
        self.cache = []

        self.ok_btn.grid_forget()
        self.addnum_btn.grid(row=13, column=0, columnspan=9)

        if self.registered_num == 81:
            self.addnum_btn.grid_remove()
            self.sovle_btn.grid(row=13, column=0, columnspan=9)

    def arrange_widgets(self):
        self.btn_clicking = False

        def generate_btn_func(x, y):
            def add_cache():
                if not self.btn_clicking:
                    return

                if (x, y) in self.cache:
                    self.cache.remove((x, y))
                    self.btn_arr[x][y].config(bg = "gray")
                else:
                    self.cache.append((x, y))
                    self.btn_arr[x][y].config(bg = "red")
            return add_cache

        for y in range(9):
            for x in  range(9):
                self.btn_arr[x][y] = Button(
                    self.window,
                    width = 2, font = Font(size=15), bg = "gray", fg = "white",
                    command = generate_btn_func(x, y)
                )
                self.btn_arr[x][y].grid(row = y + 1, column = x, columnspan = 1)
        
                self.lbl_arr[x][y] = Label(self.window, width = 2, font = Font(size=15), bg = "gray", fg = "white")

        self.ok = IntVar()
        self.ok_btn = Button(
            self.window, 
            text = "OK", width = 40, height = 1,
            command = lambda: self.ok.set(1)
        )
        self.ok_btn.grid(row = 13, column = 0, columnspan = 9)
        self.ok_btn.grid_forget()
        
        self.addnum_btn = Button(
            self.window, 
            text = "Add Number", width = 40, height = 1,
            command = self.add_board
        )
        self.addnum_btn.grid(row=13, column=0, columnspan=9)
        
        self.sovle_btn = Button(
            self.window, 
            text = "Solve", width = 40, height = 1,
            command = self.solve
        )
        self.sovle_btn.grid(row=13, column=0, columnspan=9)
        self.sovle_btn.grid_forget()

        self.wait_btn = Button(
            self.window, 
            text = "Wait..", width = 40, height = 1
        )
        self.wait_btn.grid(row=13, column=0, columnspan=9)
        self.wait_btn.grid_forget()


    def start(self):
        self.arrange_widgets()
        self.window.mainloop()


GuiSudoku().start()