# # Task 1


fahrenheit = "F"
celsius = "C"
t = '96.8F'
c = '36C'


if fahrenheit in t:
    value_stripped = t.strip("F")
    t_value = float(value_stripped)
    converted_celsius = (5 / 9) * (t_value - 32)
    print(f"{t} in Celsius units is {converted_celsius}")


elif celsius in c:
    value_stripped_c = c.strip("C")
    c_value = int(value_stripped_c)
    converted_celsius_c = (c_value - 32) / 1.8
    print(f"{c} in Fahrenheit units is {converted_celsius_c }")




# Task 2


number = 15

if number/5 and number/3:
    print("FizzBuzz")

elif number/3:
    print("Buzz")

elif number/5:
    print("Fizz")

else:
    print(number)




# Task 3

grades = {'Math': 15,
          'Physics': 11,
          'Geography': 18,
          'History': 20,
          'Geometry': 19}


values = grades.values()
total_sum = sum(values)
print(total_sum)


if total_sum <= 40:
    print("Fail")

elif 41 <= total_sum <= 60:
    print("Satisfactory")

elif 61 <= total_sum <= 80:
    print("Good")

elif 81 <= total_sum <= 100:
    print("Outstanding")

elif total_sum > 100 or total_sum < 0:
    print("Something's wrong with the input")

else:
    print(total_sum)






# Other solution by Hrach
# Task 1

fahrenheit = "F"
celsius = "C"
t = '36F'
c = '36C'

if fahrenheit in t:
    value_stripped = t.strip("F")
    t_value = float(value_stripped)
    converted_celsius = (5 / 9) * (t_value - 32)
    print(f"{t} in Celsius units is {converted_celsius}")  # Էստեղ ես .format() կօգտագործեի, որ ոչ ամբողջ թվերի երկարությունը
                                                           # սահմանափակեի

elif celsius in c:
    value_stripped_c = c.strip("C")
    c_value = int(value_stripped_c)
    converted_celsius_c = (c_value - 32) / 1.8
    print(f"{c} in Fahrenheit units is {converted_celsius_c }")
# Կարող ենք մի ինփութի վրա ստուգել։ Միայն t հայտարարենք ու if-ում ստուգենք t-n

"""==============================================================="""

t = '96.8F'

if "f" in t or "F" in t:
    value_stripped = t.strip("F")
    t_value = float(value_stripped)
    converted_celsius = (5 / 9) * (t_value - 32)
    print("{} in Celsius units is {:.2f}C".format(t, converted_celsius))
elif "c" in t or "C" in t:
    value_stripped_c = t.strip("C")
    c_value = int(value_stripped_c)
    converted_celsius_c = 9 / 5 * c_value + 32
    print("{} in Fahrenheit units is {:.2f}F".format(t, converted_celsius_c ))

"""==============================================================="""

# Task 2
number = 35

if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")

elif number % 3 == 0:
    print("Buzz")

elif number % 5 == 0:
    print("Fizz")

else:
    print(number)


