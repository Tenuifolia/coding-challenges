
rolling_sum = 0

for i in range(1,1000):
    if i % 3 == 0:
        rolling_sum += i
    elif i % 5 == 0:
        rolling_sum += i

print(rolling_sum)