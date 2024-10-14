

zero_to_9 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
ten_to_19 = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [ten_to_19, 6, 6, 5, 5, 5, 7, 6, 6]


rolling_sum = 0

rolling_sum += sum(zero_to_9)
rolling_sum += sum(ten_to_19)

for ten in tens:
    if type(ten) != int:
        continue
    for one in zero_to_9:
        rolling_sum += ten + one

for hundred in zero_to_9:
    if hundred == 0:
        continue
    for ten in tens:
        if type(ten) != int:
            for one in zero_to_9:
                if one == 0:
                    rolling_sum += hundred + 7
                else:
                    rolling_sum += hundred + 7 + 3 + one
            for teen in ten_to_19:
                rolling_sum += hundred + 7 + 3 + teen
        else:
            for one in zero_to_9:
                rolling_sum += hundred + 7 + 3 + ten + one

print(rolling_sum + 11)