
# Задание 1

# def max_(a):
#     print(max(a))
#
# max_([4,5,6])

# Задание 2

# num = [8, 2, 3, 0, 7]
# def sum():
#     a = 0
#     for i in num:
#         a += i
#     print(a)
#
# sum()

# Задание 3

# num = [8, 2, 3, -1, 7]
#
# def multi():
#     a = 1
#     for i in num:
#         a *= i
#     print(a)
#
# multi()

# Задание 4

# str1 = '1234abcd'
#
# def revers():
#     a = reversed(str1)
#     print(''.join(a))
#
# revers()

# Задание 5

# user = input(': ').lower()
#
# def palindrom (slovo: str):
#     if slovo == ''.join(reversed(slovo)):
#         print('Yes')
#     else:
#         print('No')
#
# palindrom(user)

# Задание 6

# money = int(input(': '))
# year = int(input(': '))
#
# def bank(a, b):
#     for i in range(1, b + 1):
#         a = a + (a/10)
#     print(a)
#
# bank(money, year)

# Задание 7

# nums = [45, 55, 60, 37, 100, 105, 220]
# a =[]
# def nums2():
#     for i in nums:
#         if i % 15 == 0:
#             nums.remove(i)
#             a.append(i)
#
# nums2()
# print(nums)
# print(a)

# Задание 8

# user = int(input(': '))
#
# def fact(a):
#     b = 1
#     for i in range(2, a):
#         b *= a
#     print(b)
#
# fact(user)

# Задание 9

# user = input(': ')
#
# def reg(a):
#     isu = 0
#     isl = 0
#     for i in a:
#         if i.isupper():
#             isu += 1
#         if i.islower():
#             isl += 1
#     print(user)
#     print('Верхний регистр: ',isu)
#     print('Нижний регистр: ',isl)
#
# reg(user)

# Задание 10

# create_phone_number = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
#
# def phone(l):
#     return f'({l[0]}{l[1]}{l[2]}) {l[3]}{l[4]}{l[5]}-{l[6]}{l[7]}{l[8]}{l[9]} '
#
# print(phone(create_phone_number))

# Задание 11

# 1

# name = input(': ')
#
# def print_name():
#     print(name)
#
# print_name()

# 2

# num = input(': ')
# def sum():
#     a,b,c = num.split()
#     print(int(a)+int(b)+int(c))
#
# sum()

# 3

# user = input(': ')
#
# def wtf():
#     a,b = user.split()
#     print(float(a) * float(b))
#
# wtf()

# 4

# user = input(': ')
#
# def wtf():
#     a,b,d = user.split()
#     if b == '+':
#         return print(int(a)+int(d))
#     if b == '-':
#         return print(int(a)-int(d))
#     if b == '*':
#         return print(int(a)*int(d))
#     if b == '/':
#         return print(int(a)/int(d))
#     if b == '%':
#         return print(int(a)%int(d))
#     if b == '**':
#         return print(int(a)**int(d))
#
# wtf()

# 5

user = int(input(': '))

def wtf():
    return print(f'{user - 1} \n{user} \n{user + 1}')

wtf()


