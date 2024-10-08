
def find_chain_length(x):
    count = 0
    while x != 1:
        count += 1
        if x % 2 == 0:
            x /= 2
        else:
            x = (3 * x) + 1

    return count



largest_chain_length = 0
num_with_largest = 0

for i in range(1,1000000):
    chain_length = find_chain_length(i)
    if chain_length > largest_chain_length:
        largest_chain_length = chain_length
        num_with_largest = i


print(num_with_largest)