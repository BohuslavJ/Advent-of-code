with open("Day 2 Drive!_data.txt") as f:
    x, y, aim = 0, 0, 0
    for line in f:
        if "forward" in line:
            value = line.strip("forward ")
            x += int(value)
            y += int(value)*aim
        if "down" in line:
            value = line.strip("down ")
            aim += int(value)
        if "up" in line:
            value = line.strip("up ")
            aim -= int(value)
    print(x, y, aim, x*y)
