import math

prime_nums = [2, 3]

def is_prime(x):
    if x in prime_nums:
        return True

    for prime in prime_nums:
        if x % prime == 0:
            return False

    upper_limit = int(math.sqrt(x) + 1)
    # for i in range(3, upper_limit):
    #     if x % i == 0:
    #         return False

    divisor = prime_nums[-1] + 2

    while divisor < upper_limit:
        if is_prime(divisor):
            prime_nums.append(divisor)
        if x % divisor == 0:
            return False

        divisor += 2
    return True


rolling_num = 5

while len(prime_nums) < 10001:
    if is_prime(rolling_num):
        prime_nums.append(rolling_num)
    rolling_num += 2

print(prime_nums[10000])