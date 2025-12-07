from collections import Counter

beams = Counter()
try:
    with open("input/Day 7 Laboratories.txt", "r") as file:
        for line in file:
            line = line.strip("\n")
            new_beams = Counter()
            dead_beams = Counter()
            for index in beams:
                if line[index] == "^":
                    left = index - 1
                    right = index + 1
                    dead_beams[index] -= beams[index]
                    if not left < 0:
                        new_beams[left] += beams[index]
                    if not right >= len(line):
                        new_beams[right] += beams[index]
            for index, char in enumerate(line):
                if char == "S":
                    beams[index] += 1
            beams.update(dead_beams)
            beams.update(new_beams)
            print("line", line, "ans", sum(beams.values()), "counter", beams)
        print("ans", sum(beams.values()))
except FileNotFoundError:
    print("File not found")
