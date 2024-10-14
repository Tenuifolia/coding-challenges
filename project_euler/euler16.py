

big_num = str(2 ** 1000)

rolling_sum = 0

for char in big_num:
    rolling_sum += int(char)

print(rolling_sum)