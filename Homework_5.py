import random
import os
from validator import validate_email
from validator import validate_number


# Task 1
# 1. Գրել "Կախաղան" խաղը։ Այս տնային աշխատանքի folder-ի մեջ կգտնեք տեքստային ֆայլ, որը պարունակում է անգլերեն բառեր։
# Ծրագիրը պետք է կարդա ֆայլը, ընտրի կամայական բառ, իսկ օգտագործողը պետք է փորձի գուշակել։
# Բառը ընտրելուց հետո, ծրագիրը պրինտ է անում բառի տառերի քանակությամբ _ նշան։
# Ամեն ճիշտ գուշակված տառը հայտնվում է համապատասխան վայրում։ Օրինակ պահված է car բառը։ ծրագիրը ասելու է՝
#
# ```
# Guess a letter!
# _ _ _
# ```
#
# a ներմուծելուց հետո, կստանանք այսպիսի արձագանք
# ```
# Guess a letter!
# _ a _
# ```
#
# User-ը ունի այնքան գուշակելու հնարավորություն, որքան բառի երկարությունն է։

# In[ ]:

#
#
# try:
#     print("Start")
#     with open("Random_words.txt", 'r') as f:
#         new_line = (random.choice(list(f))).strip()
#         print(new_line)
#
#     size_random_word = str(len(new_line))
#     print(size_random_word)
#     word_space = int(size_random_word) * "-"
#     print(word_space)
#     while '-' in word_space:
#         guessed_letter = input("Guess a letter!")
#         if guessed_letter in new_line:
#             for index in range(len(new_line)):
#                 if guessed_letter == new_line[index]:
#                     word_space = word_space[:index] + guessed_letter + word_space[index + 1:]
#             print(word_space)
#         else:
#             print("Incorrect")
#         reminder = input("Do you want continue?")
#         if reminder != "yes":
#             break
#
# except Exception as e:
#     print("Something went wrong!", e)
# finally:
#     print("End")
#


# Task 2
# Գրել ծրագիր, որը կգտնի և կվերադարձնի ֆայլի միջի ամենաերկար բառը։
# Որպես օրինակ ֆայլ կարող եք օգտագործել տնային աշխատանքի folder-ի միջի Animal_farm.txt.txt ֆայլը։


# with open('Animal_farm.txt') as file:
#     data = file.read().split()
#     max_word = len(max(data, key = len))
#     print(max_word)
#     res = [word for word in data if len(word) == max_word]
#     print(res)
#


# Task 3

# 3. Գրել ֆունկցիա, որը կստանա ֆայլի path-ը որպես արգումենտ և կվերադարձնի դրա չափսերը բայթերով։
#
# f = "/Users/susannakarapetyan/PythonACA/basic/Random_words.txt"
#
#
# def get_size(f):
#     return os.path.getsize(f)
#
# print(get_size(f))


# Task 4
# Ստեղծեք validator.py անունով մոդուլ։
# Դրա մեջ պետք է ունենաք երկու ֆունկցիա, validate_email և validate_number, որոնցից մեկը պատասխանատու կլինի ստուգելու, թե արդյոք փոխանցված սթրինգը էլեկտրոնային փոստի հասցե է,
# իսկ մյուսը, թե արդյոք հայկական հեռախոսահամար է:
# Հեռախոսահամարը պետք է սկսվի 0-ով, և պարզության համար ենթադրենք, որ միայն 093, 055, 091-ով սկսվողներն են հայկական։
# Վալիդ համարը կարող է ֆորմատավորված լինել հետևյալ ձևերով․

# 091 42 53 32
# 091 42-53-32
# 091 425 332
# 091 425-332
# Ապա այդ մոդուլն իմպորտ արեք ձեր կոդի մեջ և մի քանի թեստային վալիդացիա արեք։
# Եթե exception-ներ լինեն, handle արեք։



# email = "susik@yopmail.com"
#
# # valid email
# try:
#     print(validate_email(email))
# except Exception as e:
#     print("Something went wrong!", e)
# finally:
#     print("End")
#
#
# email = "susikyopmail.com"
#
# # invalid email
# try:
#     print(validate_email(email))
# except Exception as e:
#     print("Something went wrong!", e)
# finally:
#     print("End")


# valid number
number = "093 32 32 32"
print(validate_number(number))

# valid number
try:
    print(validate_number(number))
except Exception as e:
    print("Something went wrong!", e)
finally:
    print("End")


# # invalid number
number = "099032 32 32"
print(validate_number(number))

# valid number
try:
    print(validate_number(number))
except Exception as e:
    print("Something went wrong!", e)
finally:
    print("End")
