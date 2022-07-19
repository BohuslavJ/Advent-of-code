with open("Day 1 Sonar Sweep_data.txt") as f:
    counter = 0
    previous = 0
    for line in f:
        if int(line) > int(previous):
            counter += 1
        previous = line
        print (line, counter)
    print(counter-1)