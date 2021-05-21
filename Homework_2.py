
import math


# Task 1

# 1. Ստեղծեք լիստ, օգտագործելով loop կամ list comprehension, որը կպարունակի մինչև 100 բոլոր թվերը։ Ապա լուփի միջոցով print արեք միայն այն թվերը, որոնք բաժանվում են 7-ի:

# for x in range(1, 100):
#     if x % 7 == 0:
#        print (x)
#
#
# # with comprehension
# division_by_seven = [i for i in range(1, 100) if i % 7 == 0]
# print(division_by_seven)




# Task 2
"The task is not understandable"


# Task 3

"I couldn't do it."


# Task 4
# 4. Առանց count() մեթոդի, Loop-ի օգնությամբ հաշվել, թե քանի 'a' կա բանաստեղծության տրված հատվածում
#
#
# poem = """
# O Captain! my Captain! our fearful trip is done,
# The ship has weather’d every rack, the prize we sought is won,
# The port is near, the bells I hear, the people all exulting,
# While follow eyes the steady keel, the vessel grim and daring;
#                          But O heart! heart! heart!
#                             O the bleeding drops of red,
#                                Where on the deck my Captain lies,
#                                   Fallen cold and dead."""
#
# count = 0
# for char in poem:
#     if char.lower() == 'a':
#         count+=1
#         print(count)






# Task 5
# 5. Ստեղծել դատարկ լիստ, և այն լցնել մինչև 200-ը պարզ թվերով:

#
# lower = 2
# upper = 200
#
#
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
#             new_list = []
#             new_list.append(num)
#             print(new_list)
#
#




# Task 6
# 6. Ստեղծեք ձեր անձնական սորտավորող կոդը։ Տրված լիստը պետք է սորտավորեք նվազման կարգով առանց գործածելու sort() մեթոդը


# numbers = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]
#
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#
#         if numbers[i] < numbers[j]:
#            numbers[i], numbers[j] = numbers[j], numbers[i]
#
# print(numbers)



# 7. Ստեղծեք լիստ, որը կպարունակի առաջին 100 թվերը։ Այնուհետև ստեղծեք երկու նոր լիստ, որոնցից մեկը կպարունակի միայն առաջին լիստի զույգ թվերը, իսկ մյուսը՝ կենտ թվերը։

# first solution
# num_list_1_to_100 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#           31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#           41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#           51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
#           61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
#           71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
#           81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
#           91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#
#
# even, odd = [], []
# for i in num_list_1_to_100:
#     (even, odd)[i >> 0 & 1].append(i)
#
# print(even)
# print(odd)

#
# # second solution
# num_list_1_to_100 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#           31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#           41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#           51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
#           61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
#           71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
#           81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
#           91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#
# l_even=[]
# l_odd = []
# for i in num_list_1_to_100:
#     if i % 2 == 0:
#         l_even.append(i)
#     else:
#         l_odd.append(i)
#
# print(l_even)
# print(l_odd)



# # 8. Տրված է թիվ։ Այնպես արեք, որ ստանաք նոր թիվ, որը նախորդ թիվն է, թվանշանների տեղերը շրջած, օրինակ՝ 2451-ը պետք է դառնա 1542:
#
# number = 2451
# print(int(str(number)[::-3]))
#


# Task 9
rows = 10  # Multiplication table up to 10
columns = 10  # column values
for i in range(1, rows+1):
    for j in range(1, columns+1):
        c = i*j
        print("{:3d} ".format(c), end='')
    print("\n")


    
# Task 10
# 10. Տպեք հետևյալ պատկերը․
rows = 10

for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")




