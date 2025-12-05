def get_fresh_ids_count(ranges):
    ans = 0
    for r in ranges:
        ans += r[1] - (r[0] - 1)
    return ans


try:
    with open("input/Day 5 Cafeteria.txt", "r") as file:
        ranges = []
        for line in file:
            if line.strip() == "":
                break
            low, high = [int(s) for s in line.strip().split("-")]
            ranges.append([low, high])
        ranges.sort()
        ans = []
        for r in ranges:
            if not ans:
                ans.append(r)
            elif ans[-1][-1] >= r[0]:
                ans[-1][-1] = max(r[-1], ans[-1][-1])
            else:
                ans.append(r)
            print(ans)
        print("ans", get_fresh_ids_count(ans))
except FileNotFoundError:
    print("Error: The file was not found.")
