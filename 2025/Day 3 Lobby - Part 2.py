ans = 0


def getMaxVoltage(battery_bank, batteries_limit):
    if batteries_limit == 0:
        return ""
    if len(battery_bank) == batteries_limit:
        return battery_bank
    curr_max_index = 0
    for i in range(1, len(battery_bank) - batteries_limit + 1):
        if battery_bank[i] > battery_bank[curr_max_index]:
            curr_max_index = i
    return battery_bank[curr_max_index] + getMaxVoltage(
        battery_bank[curr_max_index + 1 :], batteries_limit - 1
    )


try:
    with open("input/Day 3 Lobby.txt", "r") as file:
        for line in file:
            line = line.strip()
            length = len(line)
            current_ans = getMaxVoltage(line, 12)
            ans += int(current_ans)
            print("line:", line, "current_ans:", current_ans, "ans:", ans)
    print("ans:", ans)
except FileNotFoundError:
    print("Error: The file was not found,")
