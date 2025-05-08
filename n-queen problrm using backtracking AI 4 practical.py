def solve(n):
    def ok(queens, row, col):
        for r in range(row):
            c = queens[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def place(row):
        if row == n:
            res.append(queens[:])
            return
        for col in range(n):
            if ok(queens, row, col):
                queens[row] = col
                place(row + 1)

    queens = [-1] * n
    res = []
    place(0)
    return res

# Run and print solutions
n = 4
for sol in solve(n):
    for i in sol:
        print("." * i + "Q" + "." * (n - i - 1))
    print()
