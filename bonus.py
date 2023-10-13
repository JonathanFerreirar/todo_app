filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    new_file = filename.replace(".", "-", 1)

waiting_list = ["sen", "ben", "abiel", "zub",
                "lupy", "11", "1", "55", "5", "111"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    continue
#    print(f"{index + 1}.{item.capitalize()}")

buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    continue
#    print(first, second, third)

nome = 'jonathan rodrigo'
# print(nome.title())


a = [1, 2, 3]
b = [10, 20, 30]

# print(list(x))

for number, item in zip(a, b):
    pass
    # print(number, item)

# This is list comprehensions in Python

new_filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in new_filenames]

# print(filenames)

teste = 'jonathan in'

if 'jonathan' in teste:
    pass
# print("All Okay")

elif 'in' in teste:
    pass


# print("Have in")

# CHECK IF PASSWORD IS STRONG
# password = input("Enter new password")
#
# results = {
#
# }
#
# if len(password) >= 8:
#     results["length"] = True
# else:
#     results["length"] = False
#
# has_number = False
# for letter in password:
#     if letter.isdigit():
#         has_number = True
#
# results["digits"] = has_number
#
# has_upper = False
#
# for letter in password:
#     if letter.isupper():
#         has_upper = True
# results["upper"] = has_upper
#
# if all(results.values()):
#     print("Strong Password")
# else:
#     print("Weak Password")

def is_leap(year):
    leap = False
    is_dived_four = year % 4
    is_dived_hundred = year % 100
    is_dived_four_hundred = year % 400

    if is_dived_four == 0:
        if is_dived_hundred == 0:
            if is_dived_four_hundred == 0:
                leap = True
        else:
            leap = True

    return leap


print(is_leap(1995))
