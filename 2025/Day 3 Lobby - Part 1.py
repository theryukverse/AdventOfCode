ans = 0

try:
    with open("input/Day 3 Lobby.txt", "r") as file:
        for line in file:
            line = line.strip()
            length = len(line)
            current_ans = "00"
            for i in range(length):
                for j in range(i + 1, length):
                    candidate = line[i] + line[j]
                    if candidate > current_ans:
                        current_ans = candidate
            ans += int(current_ans)
            print("line:", line, candidate, "current_ans:", current_ans, "ans:", ans)
    print("ans:", ans)
except FileNotFoundError:
    print("Error: The file was not found.")
