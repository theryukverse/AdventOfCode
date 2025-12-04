current_point = 50
ans = 0

try:
    print("cur", current_point)
    with open("input/Day 1 Secret Entrance.txt", "r") as file:
        for line in file:
            prev = current_point
            value = int(line[1:])
            ans += value // 100
            value %= 100
            if line[0] == "R":
                new_point = current_point + value
                if new_point > 100:
                    ans += 1
            else:
                new_point = current_point - value
                if new_point < 0 and prev:
                    ans += 1
            current_point = new_point % 100
            if current_point == 0:
                ans += 1
            print("input", line.strip(), "cur", current_point, "ans", ans)
    print("ans:", ans)

except FileNotFoundError:
    print("Error: The file was not found.")
