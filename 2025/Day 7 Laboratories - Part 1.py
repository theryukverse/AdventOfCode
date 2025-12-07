beams = set()
beam_splits = 0
try:
    with open("input/Day 7 Laboratories.txt", "r") as file:
        for line in file:
            line = line.strip("\n")
            new_beams = set()
            dead_beams = set()
            for index in beams:
                if line[index] == "^":
                    beam_splits += 1
                    left = index - 1
                    right = index + 1
                    dead_beams.add(index)
                    if not left < 0:
                        new_beams.add(left)
                    if not right >= len(line):
                        new_beams.add(right)
            for index, char in enumerate(line):
                if char == "S":
                    beams.add(index)
            beams.difference_update(dead_beams)
            beams.update(new_beams)
            print(beams)
        print("ans", beam_splits)
except FileNotFoundError:
    print("File not found")
