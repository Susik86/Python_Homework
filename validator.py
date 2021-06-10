import re


# email validator
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def validate_email(email):
    if re.search(regex, email):
        print("Valid Email")
    else:
        print("Invalid Email")



# phone_number validator
new_regex =  '^(0(55|93|91)\s[0-9]+\s\d{2}\s\d{2})$'

# for - it will be [-]



def validate_number(number):
    if re.search(new_regex, number):
        print("Valid Armenian Number")
    else:
        print("Invalid Armenian Number")