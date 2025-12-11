from itertools import combinations


def parse_input(line):
    exp_indicator_lights = set()
    buttons = []
    req_joltage = None
    for item in line.strip().split(" "):
        if item[0] == "[":
            for i, char in enumerate(item[1:-1]):
                if char == "#":
                    exp_indicator_lights.add(i)
        elif item[0] == "(":
            buttons.append(list(map(int, item[1:-1].strip().split(","))))
        elif item[0] == "{":
            req_joltage = list(map(int, item[1:-1].strip().split(",")))
    return exp_indicator_lights, buttons, req_joltage


def get_min_buttons(exp_indicator_lights, buttons):
    indicator_lights = set()
    if indicator_lights == exp_indicator_lights:
        return 0
    for i in range(len(buttons) + 1):
        for combination in combinations(buttons, i):
            indicator_lights.clear()
            for button in combination:
                indicator_lights.symmetric_difference_update(button)
            if indicator_lights == exp_indicator_lights:
                return i
    return -1


try:
    with open("input/Day 10 Factory.txt", "r") as file:
        total_ans = 0
        for line in file:
            exp_indicator_lights, buttons, req_joltage = parse_input(line)
            ans = get_min_buttons(exp_indicator_lights, buttons)
            if total_ans != -1:
                total_ans += ans
            print(ans)
        print(total_ans)
except FileNotFoundError:
    print("File not found")
