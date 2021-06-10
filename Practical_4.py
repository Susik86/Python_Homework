import math
import pytz
# from datetime import datetime
from datetime import date
import datetime
from datetime import timedelta
import random
import os






# Task 1
# math մոդուլի օգնությամբ գտնենք ուղղանկյուն եռանկյան անհայտ կողմերը։ Տրված է եռանկյան մի կողմը և կողմի դիմացի անկյունը։
# Պետք է գտնենք անկյան կից կողմը և ներքնաձիգը։
# բանաձևեր՝

# sin(o) = a / c, որտեղ a-ն o անկյան դիմացի էջն է, իսկ c-ն ներքնաձիգը
# cos(o) = b / c, որտեղ b-ն o անկյանը կից էջն է


a = 3   # փոքր կողմը
o = 30  # անկյունը
c = a / math.sin(math.radians(o))
print(c)
b = math.sqrt(c ** 2 - a**2)
print(b)




# Task 2

# Գրեք ֆունկցիա, որը կհաշվի և կվերադարձնի երկու իրադարձությունների միջև ընկած ժամանակը օրերով։
# # Օգտվեք datetime և pytz մոդուլներից։

#
# def birthday(my_birthday, son_birthday):
#     print(my_birthday)
#     tz_yerevan = pytz.timezone('Asia/Yerevan')
#     mine = tz_yerevan.localize(my_birthday)
#     sons = tz_yerevan.localize(son_birthday)
#     difference = mine - sons
#     print(type(mine - sons))
#     print(abs(difference.days))
#
#
# my_birthday = datetime(1986, 11, 25, 17, 55)
# son_birthday = datetime(2011, 4, 30, 17, 55)
# print(birthday(my_birthday, son_birthday))
#
#


# Task 3

# Վերցնել Երևանի ժամանակը և այն ցույց տալ հետևյալ տեսքով
# DD/MM/YYYY, HH:MM:SS


# local_time = datetime.now(pytz.timezone("Asia/Yerevan"))
# print(datetime.strftime(local_time, format='%d/%m/%Y, %H:%M:%S'))
#



# Task 4
# Տպեք երեկվա, այսօրվա և վաղվա ամսաթվերը։ Օգտվեք datetime.timedelta-ից։
#
#
# today = date.today()
# yesterday = today - timedelta(days=1)
# tomorrow = today + timedelta(days=1)
# print('Yesterday : ', yesterday)
# print('Today : ', today)
# print('Tomorrow : ', tomorrow)
#



# Task 5
# Տպեք առաջիկա 5 օրերի ամսաթվերը։

# base = datetime.today()
# for x in range(0, 5):
#     print(base + timedelta(days=x))
#


# # Task 6
# Գրեք ֆունկցիա, որը կստանա ամսաթիվ և կվերադարձնի, թե այդ ամսաթիվը տարվա որերորդ շաբաթն է։

# datetime = datetime.
# def which_week(date):
#     c
#
#


# Task 7
# # Ստեղծեք ֆայլ, որը կպարունակի օրվա առևտուրը։ Ֆայլի վերևում գրեք ամսաթիվը, այնուհետև մթերքները իրենց քանակությամբ




# Task 8
# Բացեք երկու ֆայլ։ Մեկը նախորդ վարժության ֆայլը, մյուսը՝ նոր։ Առաջին ֆայլի ողջ պարունակությունը տեղափոխեք երկրորդ ֆայլի մեջ։
# Վերջում առաջին ֆայլը ջնջեք։


foods = ['Cheese', 'Tomato', 'Potato', 'Chicken', 'Milk', 'Coffee', 'Tea', 'Khorovats', 'Ice Cream']

with open('Shopping_list.txt', 'w') as file:

    file.write(datetime.date.today().strftime('%d/%m/%Y'))

    print('\n', file=file)

    for food in foods:
        # print(f'{food}: {random.randint(0, 10)}', file=file)
        print('{:<10}: {:>15}'.format(food, random.randint(0, 10)), file=file)

    with open('Shopping_list.txt', 'r') as old_file, open('Updated Shopping list.txt', 'w') as new_file:
        lines = old_file.readlines()
        print(lines)

        for line in lines:
            new_file.write(line)

    # os.remove('Shopping_list.txt')

foods = ['Cheese', 'Tomato', 'Tea', 'Khorovats', 'Ice Cream']

with open('Shopping list.txt', 'r') as old_file:
    with open('Updated Shopping list.txt', 'w') as new_file:
            today = date.today()
            tomorrow = today + timedelta(days=1)
            new_file.write(tomorrow().strftime('%d/%m/%Y'))
    for food in foods:
            # print(f'{food}: {random.randint(0, 10)}', file=file)
            print('{:<10}: {:>15}'.format(food, random.randint(0, 5)), file=file)

