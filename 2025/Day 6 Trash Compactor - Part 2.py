ans = 0


def get_vertical_line(mrx, i):
    vertical_line = ""
    for hor_line in mrx:
        if i < len(hor_line):
            vertical_line += hor_line[i]
    return vertical_line


try:
    mrx = []
    with open("input/Day 6 Trash Compactor.txt", "r") as file:
        line_len = 0
        for line in file:
            if not line_len:
                line_len = len(line.strip("\n"))
            mrx.append(line.strip("\n"))
            print(mrx[-1])
        ops = ""
        curr_ans = 0
        for i in range(line_len):
            vertical_line = get_vertical_line(mrx, i)
            if not vertical_line.strip():
                ans += curr_ans
                curr_ans = 0
                continue
            if vertical_line[-1] == "+":
                ops = "+"
                curr_ans = int(vertical_line[:-1].strip())
            elif vertical_line[-1] == "*":
                ops = "*"
                curr_ans = int(vertical_line[:-1].strip())
            else:
                if ops == "+":
                    curr_ans += int(vertical_line.strip())
                elif ops == "*":
                    curr_ans *= int(vertical_line.strip())
        ans += curr_ans
    print("ans", ans)
except FileNotFoundError:
    print("File not found")
