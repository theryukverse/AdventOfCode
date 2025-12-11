def get_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


try:
    points = []
    with open("input/Day 9 Movie Theater.txt", "r") as file:
        for line in file:
            x, y = [int(val) for val in line.strip().split(",")]
            points.append([x, y])
        ans = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                ans = max(ans, get_area(points[i], points[j]))
        print(ans)
except FileNotFoundError:
    print("File not found")
