
import random
from random import randint



# Task 1
# 1. Գրեք ձեր սեփական պատահական թվերի գեներատորը։
# Ֆունկցիան կարող է վերցնել կամ չվերցնել արգումենտներ, և պետք է վերադարձնի պատահական թիվ։


def random_numbers():
    return randint(1, 101)


print(random_numbers())


# Task 2
# 2. Ստեղծեք ֆունկցիա, որը լիստը կլցնի կամայական գեներացված թվերով։
# Ստեղծեք 100 տարր պարունակող լիստ և այն լցրեք այդ ֆունկցիայի միջոցով։
# Այնուհետև ֆունկցիան պետք է վերադարձնի այդ լիստում կենտ թվերի քանակը։"""


def add_random_num_to_list(list_1):
    list_1.append(random.randint(1, 100))

    return list_1


if __name__ == '__main__':

    my_list = []
    for _ in range(100):
        add_random_num_to_list(my_list)
    odd_count = len(list(filter(lambda x: (x % 2 != 0), my_list)))
    a = list(filter(lambda x: (x % 2 != 0), my_list))
    print(a)
    print(odd_count)


# Task 3
# """3. Գրել ֆունկցիա, որը կվերցնի սթրինգ և կվերադարձնի լիստ։
# Այդ լիստը պետք է պարունակի սթրինգի այն բոլոր բառերը, որոնք սկսվում են ձայնավորով։"""


def string_vowels():
    string = input("Please enter a list of strings: ")
    new_list = string.split(" ")
    my_new_list = list(filter(lambda letter: letter[0] in "aeiou", new_list))
    return my_new_list


new = string_vowels()
print(new)









