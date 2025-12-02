current_point = 50
ans = 0

try:
    with open("input/Day 1 Secret Entrance - Part 1.txt", "r") as file:
        for line in file:
            value = int(line[1:])
            if line[0] == "R":
                current_point = (current_point + value) % 100
            else:
                current_point = (current_point - value) % 100
            if current_point == 0:
                ans += 1
            print("input", line, "cur", current_point, "ans", ans)
    print("ans:", ans)

except FileNotFoundError:
    print("Error: The file was not found.")
