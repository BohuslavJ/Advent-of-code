# opening of data and clearing the "\n"
with open("Day 3 Binary Diagnostic_data.txt") as f:
    data = f.readlines()
    clean_data = []
    for _ in data:
        clean_data.append(_.strip())

# setting starting values
counter_0, counter_1 = 0, 0
result_binary, result_binary_reverse = "", ""

# creating binary result out of given data
for _ in range(len(clean_data[1])):
    for row in clean_data:
        if row[_] == "0":
            counter_0 += 1
        else:
            counter_1 += 1
    if counter_0 > counter_1:
        result_binary += "0"
    else:
        result_binary += "1"
    counter_0, counter_1 = 0, 0

print(result_binary)
# extracting result out of binary result
for _ in result_binary:
    if _ == "0":
        result_binary_reverse += "1"
    else:
        result_binary_reverse += "0"
result_decimal_gamma = int(result_binary, 2)
result_decimal_epsilon = int(result_binary_reverse, 2)

print(result_decimal_gamma * result_decimal_epsilon)
