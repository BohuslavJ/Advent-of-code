# opening of data and clearing the "\n"
with open("Day 5 Hydrothermal Venture_data.txt") as f:
    data = f.readlines()
    clean_data = []
    for _ in data:
        clean_data.append(_.replace(' -> ', ',').strip())

field = [[0 for i in range(1000)] for j in range(1000)]
#print(field)

for line in clean_data:
    _ = line.split(",")
    x1 = int(_[0])
    x2 = int(_[2])
    y1 = int(_[1])
    y2 = int(_[3])
    if x1 == x2 or y1 == y2:
        if y1 == y2:
            if x1 > x2:
                for __ in range(x1-x2+1):
                    field[x2+__][y1] += 1
            else:
                for __ in range(x2-x1+1):
                    field[x1+__][y1] += 1
        if x1 == x2:
            if y1 > y2:
                for __ in range(y1-y2+1):
                    field[x1][y2+__] += 1
            else:
                for __ in range(y2-y1+1):
                    field[x1][y1+__] += 1

    else:
        continue


result = 0
for rows in range(1000):
    for col in range(1000):
        if field[rows][col] >= 2:
            print(field[rows][col], rows, col)
            result += 1
print(result)

