def mul(arr):
    res = 1
    for i in arr:
        res *= i
    return res


class sdoku:
    def __init__(self, inp):
        self.inp = inp

        self.board = [[0] * 9 for i in range(9)]
        self.res_board = [[0] * 9 for i in range(9)]
        self.x = []

        for i in range(len(inp)):
            for j in inp[i][1]:
                x, y = j
                self.board[y][x] = i
                self.x.append(j)

        self.x_check = [[0] * 10 for i in range(9)]
        self.y_check = [[0] * 10 for i in range(9)]

    def _solver(self, zi):
        if zi == 81:
            return True

        x, y = self.x[zi]

        rn = self.inp[self.board[y][x]][0]
        fn = 0
        lo = False
        ln = []

        for i, j in self.inp[self.board[y][x]][1]:
            if self.res_board[j][i] != 0:
                fn += 1
                ln.append(self.res_board[j][i])

        if fn == len(self.inp[self.board[y][x]][1]) - 1:
            lo = True

        for num in range(1, 10):
            if not self.x_check[x][num] and not self.y_check[y][num]:
                if lo:
                    check = False
                    if fn == 1:
                        check = (
                            check
                            or (abs(ln[0] - num) == rn)
                            or ((ln[0] / num) == rn)
                            or ((num / ln[0]) == rn)
                        )
                    check = check or (sum(ln) + num == rn) or (mul(ln) * num == rn)

                    if not check:
                        continue

                self.x_check[x][num] = True
                self.y_check[y][num] = True
                self.res_board[y][x] = num

                if self._solver(zi + 1):
                    return True

                self.res_board[y][x] = 0
                self.x_check[x][num] = False
                self.y_check[y][num] = False

        return False

    def solve(self):
        self._solver(0)
        return self.res_board
