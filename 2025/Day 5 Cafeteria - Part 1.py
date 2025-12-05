fresh_items = 0

try:
    is_input = True
    ranges = []
    with open("input/Day 5 Cafeteria.txt", "r") as file:
        for line in file:
            if line.strip() == "":
                is_input = False
                continue
            if is_input:
                ranges.append([int(s) for s in line.strip().split("-")])
            else:
                item = int(line.strip())
                for r in ranges:
                    if r[0] <= item <= r[1]:
                        print("Fresh Item", item)
                        fresh_items += 1
                        break
        print("fresh_items", fresh_items)
except FileNotFoundError:
    print("Error: The file was not found.")
