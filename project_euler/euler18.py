pyramid = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]

# position = 0
# rolling_sum = 0
# sum_list = []

# for idx, row in enumerate(pyramid):
#     # rolling_sum += row[position]
#     sum_list.append(row[position])
#     print(row[position])
#     if len(pyramid) > idx + 1:
#         if pyramid[idx+1][position+1] > pyramid[idx+1][position]:
#             position += 1

# print(sum_list)
# print(sum(sum_list))


# possible_paths = [(0, 0,75)]

# row_idx = 0

# while True:
#     row_idx += 1

#     current_path = possible_paths.pop(0)
#     next_row = current_path[1] + 1

#     possible_paths.append(current_path[0], next_row, (current_path[2] + ))


possible_paths = [(0,75)]

for row in pyramid:
    for num in row:



