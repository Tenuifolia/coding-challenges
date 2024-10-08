
def is_divisible(current_num):
    for i in divisors_list:
        if current_num % i != 0:
            return False
    return True

divisors_list = [11,12,13,14,15,16,17,18,19,20]
# divisors_list2= [2,3,4,5,6,7,8,9,11,13,17,19]

count = 2520

while True:
    if is_divisible(count):
        break
    count += 1

print(count)