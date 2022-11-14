from urllib.request import urlopen
# text = input("Text: ")
# emails = text.split(",")
# output = "\n".join(emails)
# print(output)


# def square(x):
#     return x*x


# x = int(input("x:"))
# sqr = square(x)
# print(sqr)

# def get_condition(city):
#     url = "http://wttr.in/" + city + "?format=%C"
#     page = urlopen(url)
#     raw = page.read()
#     condition = raw.decode("utf-8")
#     return condition

# city = input("City: ")
# condition = get_condition(city)
# if condition == 'Clear':
#     print("No umbrella needed")
# else:
#     print("Bring umbrella")

# def get_temperature(city):
#     url = "http://wttr.in/" + city + "?format=%t"
#     page = urlopen(url)
#     raw = page.read()
#     temp = raw.decode("utf-8")
#     return temp

# def gt3(x):
#     if x > 3:
#         return True
#     else:
#         return False

# x = int(input("gt3 x: "))
# gt3_function = gt3(x)
# print(gt3_function)

# def both_gt_3(x, c):
#     return x > 3 and x > 3

# x = int(input("x:"))
# c = int(input("c:"))
# both_gt_3_function = both_gt_3(x, c)
# print(both_gt_3_function)


# def sum3(lst_of_num):
#     return sum(lst_of_num) * 3


# lst_of_num = [2, 3, 5]
# sum3_function = sum3(lst_of_num)
# print(sum3_function)

# def sumv(dict):
#     val = dict.values()
#     return sum(val)


# dict = {"a": 4, "b": 5}
# sumv_function = sumv(dict)
# print(sumv_function)

# def is_jack_one(dict):
#     return dict["jack"] == 1


# dict = {"jack": 1, "blob": 2, "fish": 15}
# is_jack_one_function = is_jack_one(dict)
# print(is_jack_one_function)

# def add3_jack(dict):
#     val = dict["jack"]
#     return val + 3


# dict = {"jack": 2, "blob": 2, "fish": 15}
# add3_jack_function = add3_jack(dict)
# print(add3_jack_function)

# Episode 12 Excercises

# def gt5(x):
#     if x > 5:
#         return 'Yay!'


# print(gt5(10))


# def reaction(name):
#     if name == 'among us':
#         return 'Yah!'

# print(reaction('among us'))

# def gt5o(x):
#     if x > 5:
#         return 'Yah!'
#     else:
#         return 'nu!'

# print(gt5o(6))

# def reaction(name):
#     if name == 'among us':
#         return 'Yah!'
#     else:
#         return 'nu!'

# print(reaction('among us'))

# def blackjack(lst_of_num):
#     sum_of_num = sum(lst_of_num)
#     if sum_of_num < 21:
#         return sum_of_num

# lst_of_num = [3, 5, 5, 5, 2]
# print(blackjack(lst_of_num))

# def can_cook(lst_of_strings):
#     if 'lemon' in lst_of_strings:
#         return lst_of_strings
#     else:
#         return lst_of_strings is None


# lst_of_strings = ['apple', 'blueberry', 'lemon', 'cherry']
# print(can_cook(lst_of_strings))

# def laugh(lst):
#     if True in lst:  # if any(lst): would work here as well
#         return "hahaha"
#     else:
#         return "uh"


# print(laugh([True, False, False]))

# def odd_number():
#     x = 5
#     while x <= 15:
#         print(x)
#         x += 2

# print(odd_number())

# def print_from_to(x, c):
#     while x <= c:
#         print(x)
#         x += 1

# print(print_from_to(3, 6))

# def not_multiple_three(x):
#     while x <= 10:
#         if x % 3 != 0:
#             print(x)
#             x += 1
#         else:
#             x += 1
        
# print(not_multiple_three(5))

# def not_multiple_of_six(x):
#     while x <= 15:
#         if x % 6 != 0:
#             print(x)
#         x += 1

# print(not_multiple_of_six(5))

# For Loops
# def check(password):
#     has_number = False
#     for i in password:
#         if i.isdigit():
#             has_number = True
#     return has_number

# password = input("Password: ")
# has_number = check(password)
# print(has_number)

# def print_list(lst):
#     for i in lst:
#         print(i)


# lst = ['gdsgfsd', 'sfsfsfsf', 'fsfsfsf']
# print_lists = print_list(lst)

# def print_gt3(lst):
#     for i in lst:
#         if i > 3:
#             print(i)


# lst = [3, 6, 8, 9, 2]
# print_gt3(lst)

# def print_add3(lst):
#     for i in lst:
#         print(i + 3)

# print_add3([3, 6, 9])

# def print_a_names(names):
#     for i in names:
#         if i.startswith('a') or i.startswith('A'):
#             print(i)

# names = ['arminas', 'Arminas', 'Struna', 'Timmy', 'adi']
# print_a_names(names)

# def print_nums_gt3(lst):
#     for i in lst:
#         if i > 3:
#             print(i)


# lst = [1, 2, 3, 4, 5, 6]
# print_nums_gt3(lst)

# def get_name(lst):
#     for i in lst:
#         if i.startswith('A'):
#             return i


# lst = ['Arminas', 'Struna', 'Adi']
# print_return = get_name(lst)
# print(print_return)

# def get_odd(lst):
#     for i in lst:
#         if i % 2 == 1:
#             return i

# lst = [2, 3, 4, 5]
# get_return = get_odd(lst)
# print(get_return)