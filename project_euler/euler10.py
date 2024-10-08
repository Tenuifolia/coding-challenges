import math

def is_prime(x):
    if x in prime_nums:
        return True

    for prime in prime_nums:
        if x % prime == 0:
            return False

    upper_limit = int(math.sqrt(x) + 1)

    divisor = prime_nums[-1] + 2

    while divisor < upper_limit:
        if is_prime(divisor):
            prime_nums.append(divisor)
        if x % divisor == 0:
            return False

        divisor += 2
    return True



# prime_nums = [2, 3]

# next_num = 5

# while prime_nums[-1] < 2000000:
#     if is_prime(next_num):
#         prime_nums.append(next_num)
#         # print(prime_nums[-1])
#     next_num += 2
#     if len(prime_nums) % 1000 == 0:
#         print(prime_nums[-1])


# with open("primes.txt", "a") as prime_file:

#     for idx, prime in enumerate(prime_nums):
#         if (idx+1) % 15 == 0:
#             space = '\n'
#         else:
#             space = ', '

#         prime_file.write(str(prime)+space)



# print(sum(prime_nums))


print(142915828925 - 2000003)