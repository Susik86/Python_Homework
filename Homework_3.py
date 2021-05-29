# Task 1
# 1. Տրված է տարբեր մթերքներ պարունակող foods dictionary։ Ցավոք մեր օրգանիզմը լակտոզը լավ չի մարսում։ Պետք է ստեղծենք լիստ (ցանկալի է comprehension-ով), որը կունենա foods dictionary-ի երկարությունը և տարրերը կլինեն այսպես։ Եթե սնունդը միայն կալցիում է պարունակում, լիստի համապատասխան տարրը կլինի 'Edible', իսկ եթե ոչ՝ 'I'm not eating that'։
# #
# Output list - ```
# ["I'm not eating that",
#  'Edible',
#  'Edible',
#  "I'm not eating that",
#  'Edible',
#  'Edible']
#  ```

# In[26]:

#
# foods = {'Milk': 'Calcium, Lactose', 'Nutella': 'Calcium',
#          'Cheese': 'Calcium', 'Yoghurt': 'Calcium, Lactose',
#          'Spinach': 'Calcium', 'Fish': 'Calcium'}
#
# list2 = []
#
# for item in (foods.values()):
#     if item == "Calcium":
#         list2.append(item)
#         print("Edible")
# else:
#     print("I'm not eating that")
#
#
#

# Task 2
# 2. Ստեղծել լիստ, որը պարունակում է 1-100 այն թվերը, որոնք ավարտվում են 3-ով։

# new_list = []
# for x in range(1, 101):
#     if x % 3 == 0:
#         new_list.append(x)
#
#     else:
#         print(new_list)




# Task 3
# 3. Ստեղծել նոր սթրինգ, որը կլինի տրված սթրինգը, բայց բոլոր ձայնավորները ջնջված։

#
#
# litany = """I must not fear. Fear is the mind-killer.
# Fear is the little-death that brings total obliteration.
# I will face my fear.
# I will permit it to pass over me and through me.
# And when it has gone past, I will turn the inner eye to see its path.
# Where the fear has gone there will be nothing. Only I will remain."""
#
#
# new_string = str()
# String = litany.lower()
# for i in String:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         pass
#     else:
#         new_string = new_string + i
#
# if len(new_string) == 0:
#     print('No vowel found in ' + String)
# else:
#     print(String + ' after removing vowels ' + new_string)


# Task 4
# 4. Լիստի մեջ առանձնացնել տրված սթրինգի բոլոր այն բառերը, որոնց երկարությունը 5-ից քիչ է։
#
#
# poem = """All that is gold does not glitter,
# Not all those who wander are lost;
# The old that is strong does not wither,
# Deep roots are not reached by the frost.
#
# From the ashes a fire shall be woken,
# A light from the shadows shall spring;
# Renewed shall be blade that was broken,
# The crownless again shall be king."""
#
#
# list = []
#
# for word in poem.split():
#     if len(word) < 5:
#         list.append(word)
#
# print(list)




# Task 5
# Ֆունկցիաներ

# 1. Ստեղծել max()/min() ֆունկցիաների ձեր տարբերակը։ Պետք է մուտքագրվի թվերի լիստ և վերադարձվի առավելագույնը/նվազագույնը։ Տվեք ֆունկցիային keyword argument, որը սկզբից False է և ֆունկցիան վերադարձնում է առավելագույն արժեքը։ Եթե այդ արգումենը դարձնենք True, ֆունկցիան կվերադարձնի նվազագույնը։ Ստուգել հետևյալ թեստերի միջոցով՝
#
# lst = [4, 5, 6, 1, 19]
# lst2 = [5, 1, 98, -42, 2]
#
#
# # max
# def maximum(*args, **kwargs):
#    Max = 0
#    for item in lst:
#        if item > Max:
#            Max=item
#    return Max
#
#
# print(maximum([4, 5, 6, 1, 19]))
#
#
# # min
# def minimum(*args, **kwargs):
#    Min = 0
#    for item in lst2:
#        if item < Min:
#            Min=item
#    return Min
#
#
# print(minimum([5, 1, 98, -42, 2]))



# Task 6
# 2. Գրեք ֆունկցիա, որը կվերցնի սթրինգ և կվերադարձնի մեծատառերի և փոքրատառերի քանակը tuple-ով։
#
# Թեստերը՝
#
# ```
# string = 'King Arthur of Camelot'     count_letters(string) = (3, 16)
# string = ''                           count_letters(string) = (0, 0)
# string = 'How many?'                  count_letters(string) = (1, 6)
# ```


