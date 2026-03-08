# from ..modules.module import suml, prodl, __counter
import sys

# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(suml(zeroes))
# print(prodl(ones))


# if __name__ == "__main__":
#     print("main was the file run")


# print(__counter)


# for p in sys.path:
#     print(p)


# s1 = '12.8'
# i = int(s1)
# s2 = str(i)
# f = float(s2)
# print(s1 == s2)



# num_str = str(9081726354)

# segments_list = [
#     {'0': '***', '1': '  *', '2': '***', '3': '***', '4':'* *', '5':'***', '6': '***', '7': '***', '8': '***', '9': '***',},
#     {'0': '* *', '1': '  *', '2': '  *', '3': '  *', '4':'* *', '5':'*  ', '6': '*  ', '7': '  *', '8': '* *', '9': '* *',},
#     {'0': '* *', '1': '  *', '2': '***', '3': '***', '4':'***', '5':'***', '6': '***', '7': '  *', '8': '***', '9': '***',},
#     {'0': '* *', '1': '  *', '2': '*  ', '3': '  *', '4':'  *', '5':'  *', '6': '* *', '7': '  *', '8': '* *', '9': '  *',},
#     {'0': '***', '1': '  *', '2': '***', '3': '***', '4':'  *', '5':'***', '6': '***', '7': '  *', '8': '***', '9': '***',},
# ]

# for i in range(5):
#     for num in num_str:
#         print(segments_list[i][num], end=' ')
#     print()


# digits = [ '1111110',  	# 0
# 	   '0110000',	# 1
# 	   '1101101',	# 2
# 	   '1111001',	# 3
# 	   '0110011',	# 4
# 	   '1011011',	# 5
# 	   '1011111',	# 6
# 	   '1110000',	# 7
# 	   '1111111',	# 8
# 	   '1111011',	# 9
# 	   ]

# digits = [
#     '1111110111111',
#     '0010100101001',
#     '1110111110111',
#     '1110111101111',
#     '1011111101001',
#     '1111011101111',
#     '1111011111111',
#     '1110100101001',
#     '1111111111111',
#     '1111111101111'
# ]
# order = []

# def print_number(num):
#     str_num = str(num)
#     result_str = ''
#     for i in range(5):
#         temp_str = ''
#         for num in num_str:
#             if i == 0:
#                 temp_str += digits[int(num)][:3].replace('0', ' ').replace('1', '*')
#             elif i == 1:
#                 temp_str += (digits[int(num)][3] + ' ' + digits[int(num)][4]).replace('0', ' ').replace('1', '*')
#             elif i == 2:
#                 temp_str += digits[int(num)][5:8].replace('0', ' ').replace('1', '*')
#             elif i == 3:
#                 temp_str += (digits[int(num)][8] + ' ' + digits[int(num)][9]).replace('0', ' ').replace('1', '*')
#             elif i == 4:
#                 temp_str += digits[int(num)][10:].replace('0', ' ').replace('1', '*')
#             temp_str += ' '

#         result_str += temp_str + '\n'
#     return result_str


# print(print_number(int(input("Enter the number you wish to display: "))))





# IBAN Validator.

# iban = input("Enter IBAN, please: ")
# iban = iban.replace(' ','')

# if not iban.isalnum():
#     print("You have entered invalid characters.")
# elif len(iban) < 15:
#     print("IBAN entered is too short.")
# elif len(iban) > 31:
#     print("IBAN entered is too long.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#         print(iban2)
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("IBAN entered is valid.")
#     else:
#         print("IBAN entered is invalid.")



# def caesar_cipher_2(origin_str, shift):
#     encrypt_str = ''
#     for i in origin_str:
#         if not i.isalpha():
#             new_ord = ord(i)
#         else:
#             new_ord = ord(i) + shift
#             if new_ord > (90 if i.isupper() else 122):
#                 new_ord -= 26
#         encrypt_str += chr(new_ord)

#     return encrypt_str


# user_str = input("Enter sample: ")
# user_shift = int(input("Enter shift value: "))

# print(caesar_cipher_2(user_str, user_shift))

# print(ord("z"))
# print(chr(97))


# def is_palindrome(sample_str):
#     if not sample_str:
#         return False
#     test_str = ''.join(char for char in sample_str.lower() if char.isalpha())

#     return test_str == test_str[::-1]

# user_str = input("Enter sample: ")

# print(is_palindrome(user_str))


# def anagram_check(str_1, str_2):
#     if not str_1 or not str_2:
#         return False

#     return sorted(str_1.lower().replace(" ", "")) == sorted(str_2.lower().replace(" ", ""))

# user_str_1 = input("Enter first sample: ")
# user_str_2 = input("Enter second sample: ")

# print(anagram_check(user_str_1, user_str_2))


# def digit_of_life(birth_date):
#     str_num = str(birth_date)

#     life_digit = sum([int(i) for i in str_num])

#     while life_digit > 9:
#         life_digit = sum([int(i) for i in str(life_digit)])

#     return life_digit

# user_date = input("Enter your birthdate in MMDDYYYY format: ")

# print("Your life digit is: ", digit_of_life(user_date))


# def word_find(word, scramble):

#     start = 0
#     for char in word:
#         position = scramble.find(char, start)
#         if position == -1:
#             return False
#         start = position + 1
#         # if word.lower().count(char) > scramble.lower().count(char):
#         #     return False
#     return True
# print(word_find('donor', 'Nabucodonosor'))
# print(word_find('donut', 'Nabucodonosor'))





# def sudoku_check(rows):
#     # for row in rows:
#     #     if sorted(row) != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#     #         return False
#     # return True


#     check = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     columns = [[], [], [], [], [], [], [], [], []]
#     sub_squares = [[], [], [], [], [], [], [], [], []]
#     diag_1 = ''
#     diag_2 = ''
#     count = 0
#     for row_idx, row in enumerate(rows):
#         if sorted(row) != check:
#             print("Failed row: ", row)
#             return False
#         print(sorted(row))
#         for i in range(9):
#             columns[i].append(row[i])
#             sub_squares[i//3 + 3 * (row_idx//3)].append(row[i])
#         diag_1 += row[count]
#         diag_2 += row[8-count]
#         count += 1
#     print('columns')
#     for column in columns:
#         if sorted(column) != check:
#             print("Failed column: ", column)
#             return False
#         print(sorted(column))
#     print('sub_squares')
#     for sub_square in sub_squares:
#         if sorted(sub_square) != check:
#             print("Failed sub_square: ", sub_square)
#             return False
#         print(sub_square)

#     if sorted(diag_1) != check and sorted(diag_2) != check:
#         print("Failed diag: ", diag_1, diag_2)
#         return False
#     print(f"diagonals\n{sorted(diag_1)}\n{sorted(diag_2)}")

#     return True






# sample_rows_1 = [
#     "295743861",
#     "431865927",
#     "876192543",
#     "387459216",
#     "612387495",
#     "549216738",
#     "763524189",
#     "928671354",
#     "154938672",
# ]

# sample_rows_2 = [
#     "195743862",
#     "431865927",
#     "876192543",
#     "387459216",
#     "612387495",
#     "549216738",
#     "763524189",
#     "928671354",
#     "254938671",
# ]

# sample_rows_3 = [
#     "581427693",
#     "374596812",
#     "962138475",
#     "629385741",
#     "157964328",
#     "843271569",
#     "418752936",
#     "295643187",
#     "736819254",
# ]
# print("\n-- 1")
# print(sudoku_check(sample_rows_1))
# print("\n-- 2")
# print(sudoku_check(sample_rows_2))
# print("\n-- 3")
# print(sudoku_check(sample_rows_3))



# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
# def checkset(digs):
#     return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# # A list of rows representing the sudoku.
# rows = [ ]
# for r in range(9):
#     ok = False
#     while not ok:
#         row = input("Enter row #" + str(r + 1) + ": ")
#         ok = len(row) == 9 or row.isdigit()
#         if not ok:
#             print("Incorrect row data - 9 digits required")
#     rows.append(row)

# ok = True

# # Check if all rows are good.
# for row in rows:
#     if not checkset(row):
#         ok = False
#         break

# # Check if all columns are good.
# if ok:
#     for c in range(9):
#         col = []
#         for r in range(9):
#             col.append(rows[r][c])
#         if not checkset(col):
#             ok = False
#             break

# # Check if all sub-squares (3x3) are good.
# if ok:
#     for r in range(0, 9, 3):
#         for c in range(0, 9, 3):
#             sqr = ''
#             # Make a string containing all digits from a sub-square.
#             for i in range(3):
#                 sqr += rows[r+i][c:c+3]
#             if not checkset(list(sqr)):
#                 ok = False
#                 break

# # Print the final verdict.
# if ok:
#     print("Yes")
# else:
#     print("No")




# def read_int(prompt, min, max):
#     user_input = input(prompt)
#     try:
#         user_input = float(user_input)
#         result = int(user_input) if user_input <= max and user_input >= min else f'the value is not with permitted range ({min} and {max})'
#     except ValueError:
#         result = 'wrong input'


#     return result

# v = read_int("Enter a number from -10 to 10: ", -10, 10)

# print("The number is:", v)





# class QueueError(IndexError):
#     pass


# class Queue:
#     def __init__(self):
#         self.queue = []
#     def put(self,elem):
#         self.queue.insert(0,elem)
#     def get(self):
#         if len(self.queue) > 0:
#             elem = self.queue[-1]
#             del self.queue[-1]
#             return elem
#         else:
#             raise QueueError


# class SuperQueue(Queue):
#     def __init__(self):
#         Queue.__init__(self)

#     def isempty(self):
#         return len(self.queue) == 0


# que = SuperQueue()
# que.put(1)
# que.put("dog")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Queue empty")



# class ExampleClass:
#     a = 1
#     def __init__(self):
#         self.b = 2


# example_object = ExampleClass()

# print(example_object.a)

# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))



# class Timer:
#     def __init__(self, hours = 0, minutes = 0, seconds = 0):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds

#     def __str__(self):
#         return f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}"

#     def next_second(self):
#         if self.__seconds < 59:
#             self.__seconds += 1
#         elif self.__minutes < 59:
#             self.__minutes += 1
#             self.__seconds = 0
#         elif self.__hours < 23:
#             self.__hours += 1
#             self.__minutes = 0
#             self.__seconds = 0
#         else:
#             self.__hours = 0
#             self.__minutes = 0
#             self.__seconds = 0

#     def prev_second(self):
#         if self.__seconds > 0:
#             self.__seconds -= 1
#         elif self.__minutes > 0:
#             self.__minutes -= 1
#             self.__seconds = 59
#         elif self.__hours > 0:
#             self.__hours -= 1
#             self.__minutes = 59
#             self.__seconds = 59
#         else:
#            self.__hours = 23
#            self.__minutes = 59
#            self.__seconds = 59


# class WeekDayError(Exception):
#     def __init__(self, message):
#         super().__init()
#         self.message = message



# class Weeker:
#     days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

#     def __init__(self, week_day):
#         if week_day not in Weeker.days_list:
#             raise WeekDayError
#         self.__week_day = week_day

#     def __str__(self):
#         return self.__week_day

#     def add_days(self, n):
#         self.__week_day = Weeker.days_list[(Weeker.days_list.index(self.__week_day) + n) % 7]

#     def subtract_days(self, n):
#         self.__week_day = Weeker.days_list[(Weeker.days_list.index(self.__week_day) - n) % 7]

# import math

# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__y

#     def distance_from_xy(self, x, y):
#         x_dif = abs(abs(self.__x) - abs(x))
#         y_dif = abs(abs(self.__y) - abs(y))

#         return math.sqrt(x_dif ** 2 + y_dif ** 2)

#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.getx(), point.gety())



# class Triangle(Point):
#     def __init__(self, point_a, point_b, point_c):
#         self.__points = [point_a, point_b, point_c]

#     def perimeter(self):
#         len_ab = self.__points[0].distance_from_point(self.__points[1])
#         len_bc = self.__points[1].distance_from_point(self.__points[2])
#         len_ca = self.__points[2].distance_from_point(self.__points[0])

#         return sum([len_ab, len_bc, len_ca])

import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)