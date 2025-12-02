def length(num):
    l = 0
    while num // 10:
        l += 1
        num //= 10
    return l + 1


def get_possible_number(num):
    return num + 1


def is_valid(num):
    l = length(num)
    s = str(num)
    sub_len = l // 2
    while sub_len >= 1:
        if l % sub_len:
            sub_len -= 1
            continue
        sub_s = str(num % 10**sub_len)
        rep = l // sub_len
        if sub_s * rep == s:
            return True
        sub_len -= 1

        # print(num,sub_len)
    return False


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
