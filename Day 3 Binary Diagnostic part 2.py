# opening of data and clearing the "\n"
with open("Day 3 Binary Diagnostic_data.txt") as f:
    data = f.readlines()
    clean_data = []
    for _ in data:
        clean_data.append(_.strip())

# setting starting values
counter_0, counter_1 = 0, 0
result_binary, result_binary_reverse = "", ""

# finding out which number is more common
for _ in range(len(clean_data[1])):
    if len(clean_data) == 1:
        break
    for row in clean_data:
        if row[_] == "0":
            counter_0 += 1
        else:
            counter_1 += 1
    if counter_0 > counter_1:
        burn_them_all = "0"
    else:
        burn_them_all = "1"
    counter_0, counter_1 = 0, 0

# cosplaying Daenerys and burning commons
    for row in clean_data[:]:
        if row[_] == burn_them_all:
            clean_data.remove(row)
print(clean_data)

# extracting result out of binary result
result_decimal_oxygen = int(clean_data[0], 2)


with open("Day 3 Binary Diagnostic_data.txt") as f:
    data = f.readlines()
    clean_data = []
    for _ in data:
        clean_data.append(_.strip())

# setting starting values
counter_0, counter_1 = 0, 0
result_binary, result_binary_reverse = "", ""

# finding out which number is less common
for _ in range(len(clean_data[1])):
    if len(clean_data) == 1:
        break
    for row in clean_data:
        if row[_] == "0":
            counter_0 += 1
        else:
            counter_1 += 1
    if counter_1 >= counter_0:
        burn_them_all = "0"
    else:
        burn_them_all = "1"
    counter_0, counter_1 = 0, 0

# cosplaying Daenerys and burning commons
    for row in clean_data[:]:
        if row[_] == burn_them_all:
            clean_data.remove(row)
print(clean_data)


# extracting result out of binary result
for _ in result_binary:
    if _ == "0":
        result_binary_reverse += "1"
    else:
        result_binary_reverse += "0"
# extracting result out of binary result
result_decimal_co2 = int(clean_data[0], 2)

print(result_decimal_oxygen * result_decimal_co2)
