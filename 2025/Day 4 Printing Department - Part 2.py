floor = []
ans = 0


def print_floor(floor):
    print()
    for _ in floor:
        print(_)
    print()


def can_fork_lift(floor, row, col, row_len, col_len):
    if floor[row][col] != "@":
        return False
    adjacent_rolls_counter = 0
    if row > 0 and floor[row - 1][col] != ".":
        adjacent_rolls_counter += 1
    if col > 0 and row > 0 and floor[row - 1][col - 1] != ".":
        adjacent_rolls_counter += 1
    if col > 0 and floor[row][col - 1] != ".":
        adjacent_rolls_counter += 1
    if row + 1 < row_len and col > 0 and floor[row + 1][col - 1] != ".":
        adjacent_rolls_counter += 1
    if row + 1 < row_len and floor[row + 1][col] != ".":
        adjacent_rolls_counter += 1
    if row + 1 < row_len and col + 1 < col_len and floor[row + 1][col + 1] != ".":
        adjacent_rolls_counter += 1
    if col + 1 < col_len and floor[row][col + 1] != ".":
        adjacent_rolls_counter += 1
    if row > 0 and col + 1 < col_len and floor[row - 1][col + 1] != ".":
        adjacent_rolls_counter += 1
    if adjacent_rolls_counter < 4:
        return True
    return False


def clean_the_floor(floor):
    ans = 0
    col_len = len(floor)
    row_len = len(floor[0])
    for row in range(row_len):
        for col in range(col_len):
            if can_fork_lift(floor, row, col, row_len, col_len):
                floor[row][col] = "."
                ans += 1
    return ans


try:
    with open("input/Day 4 Printing Department.txt", "r") as file:
        for line in file:
            row = []
            for _ in line.strip():
                row.append(_)
            floor.append(row)
        while True:
            removed = clean_the_floor(floor)
            if removed:
                ans += removed
            else:
                break
        print_floor(floor)
        print(ans)
except FileNotFoundError:
    print("Error: The file was not found.")
