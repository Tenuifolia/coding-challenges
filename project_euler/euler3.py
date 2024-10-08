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

def get_next_least_factor(big_num, current_factor):
    # max_range = int(math.sqrt(og_num) + 1)

    current_factor += 2

    while current_factor < big_num:
        if big_num % current_factor == 0:
            return current_factor
        current_factor += 2
    print("failed")



# og_num = 600851475143

# least_factor = 3

# max_factor_is_prime = False

# solution = 0

# while not max_factor_is_prime:
#     max_factor = og_num / least_factor
#     if not (max_factor).is_integer():
#         least_factor += 2
#         continue
#     print(least_factor, max_factor)
#     print(prime_nums)
#     if is_prime(max_factor):
#         solution = max_factor
#         break
#     else:
#         least_factor = get_next_least_factor(og_num, least_factor)

# print(solution)

# for i in range (1, max_range):
#     if is_prime(i):
#         if og_num %


print(is_prime(6857))
print(prime_nums)