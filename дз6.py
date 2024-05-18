
# Задание 1
# products = []
# while True:
#     user = input(': ').lower()
#     if user == 'stop':
#         break
#     if len(user.split()) == 2:
#         comand , product = user.split()
#         if comand == 'add':
#             if product not in products:
#                 products.append(product)
#             else:
#                 print('Продукт уже в корзине')
#         if product == 'add':
#             print('.!.')
#         if comand == 'del':
#             if product not in products:
#                 print('Нечего удалять')
#             else:
#                 products.remove(product)
#         if product == 'del':
#             print('.!.')
#         if comand == 'search':
#             if product in products:
#                 print('Yes')
#             else:
#                 print('No')
#         if product == 'search':
#             print('.!.')
#
#     if user == 'show':
#         if len(products) != 0:
#             count = 0
#             for i in products:
#                 count += 1
#                 print(count, i)
#         else:
#             print(':(')
#     if user == 'clear':
#         if len(products) != 0:
#             products.clear()
#         else:
#             print('idi')

# Задача 2

# a = 9
#
# for i in range(1 , a + 1):
#     print(str(i) * i)

# Задача 3

# n = int(input(': '))
# m = int(input(': '))
# if n < m:
#     d = m
# else:
#     d = n
# while True:
#     if n % d != 0 or m % d != 0:
#         d -= 1
#     else:
#         print(d)
#         break

# Задача 4

# money = int(input(': '))
# year = int(input(': '))
#
# for i in range(year):
#     money = money + money * 0.1
#
# print(money)

# Задача 5

# from random import randint
#
# while True:
#     r = randint(1, 100)
#     user = input(': ')
#     if user == r :
#         print('You win')
#         break
#     if user == 'stop':
#         print('bye')
#         break
#     else:
#         print(r)

# Задача 6

# parol = 456
#
# popit = 5
#
# while True:
#     user = int(input(': '))
#     if user != parol:
#         popit -= 1
#         if popit != 0:
#             print('Неа', popit)
#     if user == parol:
#         print('Ага')
#         break
#     if popit == 0:
#         print('bye')
#         break

# Задача 7

# numbers = [12, 75, 150, 180, 145, 525, 50]
# num = []
#
#
# for i in numbers:
#     if i > 150:
#         continue
#     if i > 500:
#         break
#     if i % 5 == 0:
#         num.append(i)
#         print(i)
#
# print(num)

# Задача 8

# num = [0,1]
# while True:
#     a = num[-1] + num[-2]
#     num.append(a)
#     if a > 100:
#         break
# print(num)



