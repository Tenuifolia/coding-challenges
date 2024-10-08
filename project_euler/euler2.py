rolling_sum = 2

fib_list = [1, 2]

count = 2

next_num = 0

while next_num < 4000000:
    next_num = fib_list[count-2] + fib_list[count-1]
    fib_list.append(next_num)

    count += 1

    if next_num % 2 == 0:
        rolling_sum += next_num


print(rolling_sum)