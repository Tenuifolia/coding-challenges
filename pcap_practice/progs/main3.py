





# class TestClass:
#     def __init__(self, n):
#         self.__i = 0
#         self.__n = n
#         self.__output = 0


#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration

#         if self.__output == 0:
#             self.__output = 1
#         else:
#             self.__output *= 2

#         return self.__output
    



# for i in TestClass(10):
#     print(i)






# def power_of_2(n):
#     pwrs_list = []
    
#     count = 0
#     while count < n:
#         pwrs_list.append(2**count)
#         count += 1

#     for i in pwrs_list:
#         yield i


# # print(list(power_of_2(5)))


# for i in power_of_2(5):
#     print(i)


# print([x for x in map(lambda x: x* x, range(1,6))])


# print(tuple((x for x in range(5))))
# print(tuple(x for x in range(5)))



any_list = [1, 2, 3, 4]
even_list = list(map(lambda x: x | 1 , any_list)) # Complete the line here.
print(even_list)
 