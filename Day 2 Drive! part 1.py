with open("Day 2 Drive!_data.txt") as f:
    x, y = 0, 0
    for line in f:
        if "forward" in line:
            value = line.strip("forward ")
            x += int(value)
        if "down" in line:
            value = line.strip("down ")
            y += int(value)
        if "up" in line:
            value = line.strip("up ")
            y -= int(value)
    print(x, y, x*y)
