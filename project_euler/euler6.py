


sum_of_squares = 0
rolling_sum = 0

for i in range(1,101):
    sum_of_squares += i**2
    rolling_sum += i


square_of_sum = rolling_sum**2

print(sum_of_squares - square_of_sum)