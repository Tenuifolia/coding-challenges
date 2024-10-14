

# def bin_to_dec(bin_num):
#     count = 0
#     power = len(bin_num) - 1
#     for num in bin_num:
#         count += int(num) * (2 ** power)
#         power -= 1

#     return count



# print(bin_to_dec('1111111111111111111100000000000000000000'), '\n', bin_to_dec('0000000000000000000011111111111111111111'))


def get_num_of_paths(grid_range):
    paths = [[0 for i in range(grid_range + 1)] for j in range(grid_range + 1)]
    paths[grid_range][grid_range] = 1
    queue = [(grid_range, grid_range)]

    while queue:
        current_coordinate = queue.pop(0)

        # check if row above the current_coordinate exists:
        if current_coordinate[0] - 1 >= 0:
            # if that coordinate is not in the queue then add it.
            if (current_coordinate[0] - 1, current_coordinate[1]) not in queue:
                queue.append((current_coordinate[0] - 1, current_coordinate[1]))
            paths[current_coordinate[0] - 1][current_coordinate[1]] += paths[current_coordinate[0]][current_coordinate[1]]

        # check if column to the left of current_coordinate exists:
        if current_coordinate[1] - 1 >= 0:
            # if that coordinate is not in the queue then add it.
            if (current_coordinate[0], current_coordinate[1] -1) not in queue:
                queue.append((current_coordinate[0], current_coordinate[1] -1))
            paths[current_coordinate[0]][current_coordinate[1] - 1] += paths[current_coordinate[0]][current_coordinate[1]]

    return paths

print(get_num_of_paths(20))