# Task 1
# def mult(a, b):
#     return a * b
#
# print(mult(5, 5))
# assert(mult)
#
#
# def minus(a, b):
#     return a - b
#
# print(minus(10, 5))
# assert(minus)
#
#
# def div(a, b):
#     if a == 0:
#         print("Error raises")
#     else:
#         a / b
#
#
# print(div(25, 5))
# assert div
#
#
# def sum_numbers(a, b):
#     return a + b
#
# print(sum_numbers(25, 5))
# assert(sum_numbers)



# Task 2
# 1. Գրել հետևյալ ֆունկցիաները որպես լամբդա

# # 1
# def square(x):
#     return x ** 2
#
# square = lambda x: x ** 2
# print(square(10))
#
#
# # 2
# def circle_area(r, pi=3.14):
#     return pi * r ** 2
#
# circle_area = lambda r, pi=3.14: pi * r ** 2
# print(circle_area(10, 3.14))
#
#
# # 3
# def sum_to_power(x, y, p):
#     return (x + y) ** p
#
#
# sum_to_power = lambda x, y, p: (x + y) ** p
# print(sum_to_power(10, 10, 5))



# Task 3
# Ստեղծեք լիստ, որը կպարունակի մինչև 200 թվերը։ Օգտագործելով filter ֆունկցիան, այդ լիստից առանձնացրեք միայն այն թվերը, որոնք ավարտվում են 7-ով։"""

# list_1 = []
#
# for i in range(1, 201):
#     list_1.append(i)
#
# print(list_1)
#
#
# filtered_list = list(filter(lambda i: i % 10 == 7, list_1))
# print(filtered_list)
#

# Task 4
# 3. Sort ֆունկցիան ընդունում է key կոչվող kwarg-ը։ Այն ընդունում է ֆունկցիա։ Տրված լիստը սովորական sort-ով կսորտավորենք այբբենական կարգով։ Lambda-ի օգնությամբ սորտավորեք ըստ գնահատականի։"""
#
#

# grades = [('Math', 17),
#           ('Physics', 8),
#           ('Geography', 15),
#           ('History', 19),
#           ('Geometry', 4)]
#
#
#
# mapped_list = list(map(lambda x: isinstance(x, int), list1))
# mapped_list
#



# Task 5
# """4. Ստեղծել 3 թվային լիստ։ map ֆունկցիայի ու լամբդայի միջոցով վերադարձնել լիստ, որը կպարունակի ստեղծած երեք լիստերի տարրերի գումարը"""


total_a = 0

list_a = [1, 3, 4, 5, 6, 7, 8]
for ele in range(0, len(list_a)):
    total_a = total_a + list_a[ele]


print("Sum of all elements in given list: ", total_a)


total_b = 0

list_b = [1, 3, 2, 6, 7, 8]
for ele in range(0, len(list_b)):
    total_b = total_b + list_a[ele]

# printing total value
print("Sum of all elements in given list: ", total_b)


total_c = 0

list_c = [1, 3, 2]
for ele in range(0, len(list_c)):
    total_c = total_c + list_c[ele]

# printing total value
print("Sum of all elements in given list: ", total_c)

total = 0

