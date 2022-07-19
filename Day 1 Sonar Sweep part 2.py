with open("Day 1 Sonar Sweep_data.txt") as f:
    data = f.readlines()
    clean_data = []
    for _ in data:
        clean_data.append(_.strip())


def sweeper(grouping):
    counter, damn_son2 = 0, 0
    for count, value in enumerate(clean_data):
        damn_son1 = 0
        try:
            for _ in range(grouping):
                damn_son1 += int(clean_data[count + _])
            if damn_son1 > damn_son2:
                counter += 1
            damn_son2 = damn_son1
        except:
            break
    return counter

print(sweeper(3)-1)
