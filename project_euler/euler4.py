

def is_palindrome(test_num):
    return test_num == test_num[::-1]


palindromes = []

for i in range (1,1000):
    for j in range(1, 1000):
        str_num = str(i * j)
        if is_palindrome(str_num):
            palindromes.append(int(str_num))


print(max(palindromes))