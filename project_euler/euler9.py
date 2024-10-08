

sum_to_1000 = []

for i in range(1,999):
    for j in range(i,999):
        for k in range(j,999):
            if i+j+k == 1000:
                # if {i,j,k} not in sum_to_1000:
                trio = {i,j,k}
                if len(trio) == 3:
                    sum_to_1000.append({i,j,k})
    print(i)

# for i in range(1, 999):
#     for j in range(1, 999):
#         for k in range(1, 999):

# pythagorean_trio = []

pythagorean_trio_product = 0

for trio in sum_to_1000:
    a,b,c = sorted(list(trio))
    if a**2 + b**2 == c**2:
        pythagorean_trio_product = a * b * c

print(pythagorean_trio_product)