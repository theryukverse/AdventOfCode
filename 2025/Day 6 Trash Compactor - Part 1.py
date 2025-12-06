ans = 0
try:
    mrx = []
    with open("input/Day 6 Trash Compactor.txt", "r") as file:
        for line in file:
            for index, num in enumerate(line.strip().split()):
                if index < len(mrx):
                    mrx[index].append(num)
                else:
                    mrx.append([num])
        for ques in mrx:
            if ques[-1] == "+":
                curr_ans = 0
                for num in ques[:-1]:
                    curr_ans += int(num)
            else:
                curr_ans = 1
                for num in ques[:-1]:
                    curr_ans *= int(num)
            ans += curr_ans
    print("ans", ans)

except FileNotFoundError:
    print("File not found")
