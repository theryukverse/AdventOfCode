def length(num):
    l = 0
    while num // 10:
        l += 1
        num //= 10
    return l + 1


def get_possible_number(num):
    l = length(num)
    if l % 2:
        return int("1" + ("0" * l))
    else:
        return num + 1


def is_valid(num):
    l = length(num)
    if l % 2:
        return False
    else:
        denominator = 10 ** (l // 2)
        return num // denominator == num % denominator


ans = 0

try:
    with open("input/Day 2 Gift Shop.txt", "r") as file:
        contents = file.read()
        for rang in contents.strip().split(","):
            r = rang.strip().split("-")
            low = int(r[0])
            high = int(r[1])
            curr = low
            print(low, high)
            while curr <= high:
                # print("curr", curr)
                if is_valid(curr):
                    ans += curr
                    print("invalid Id", curr, "ans", ans)
                curr = get_possible_number(curr)
    print("ans", ans)

except FileNotFoundError:
    print("Error: The file was not found.")
