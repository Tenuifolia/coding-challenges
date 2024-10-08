import math

def find_divisors(x):
    divisors = []
    square = math.sqrt(x)

    if square.is_integer():
        divisors.append(square)

    for i in range(1,int(square)+1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(x/i)

    return divisors


count = 1
triangle_num = 1

while True:
    count += 1

    divisors_length = len(find_divisors(triangle_num))
    print(triangle_num, divisors_length)
    if divisors_length > 500:
        break

    triangle_num += count
    # print(triangle_num)


print(triangle_num)

