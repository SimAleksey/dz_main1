
#  Задание 1

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Lst1 = []
# Lst2 = []
# for b in a :
#     if b <= 5:
#         Lst1.append(b)
#     else:
#         Lst2.append(b)
#
# print(Lst1)
# print(Lst2)

# Задание 2

# user = input(': ')
# LOL = user.split('+')
# POP = 0
# for a in LOL:
#     POP += int(a)
# print(POP)

# Задание 3

# user = input(': ')
# Magamed = user.split()
# Magamed = sorted(Magamed, reverse=True)
# a = int(len(Magamed))
# b = int(Magamed.pop(0))
# print(b / a)

# задание 4

# ocenka = input('Оценка: ')
#
# Lst = ocenka.split()
#
# o = 0
#
# for a in Lst:
#     if a == 'A+':
#         o += 4.0
#     elif a == 'A':
#         o += 4.0
#     elif a == 'A-':
#         o += 3.7
#     elif a == 'B+':
#         o += 3.3
#     elif a == 'B':
#         o += 3.0
#     elif a == 'B-':
#         o += 2.7
#     elif a == 'C+':
#         o += 2.3
#     elif a == 'C':
#         o += 2.0
#     elif a == 'C-':
#         o += 1.7
#     elif a == 'D+':
#         o += 1.3
#     elif a == 'D':
#         o += 1.0
#     elif a == 'F':
#         o += 0
#
# print(o / len(Lst))

# Задание 5

# numbers = [1, 2, 3, 4, 5, 6, 7]
# b = []
# for a in numbers:
#     a = a*a
#     b.append(a)
# print(b)

# Задание 6

# print('''  1   2   3   4   5   6   7   8   9
# 1 01  02  03  04  05  06  07  08  09
# 2 02  04  06  08  10  12  14  16  18
# 3 03  06  09  12  15  18  21  24  27
# 4 04  08  12  16  20  24  28  32  36
# 5 05  10  15  20  25  30  35  40  45
# 6 06  12  18  24  30  36  42  48  54
# 7 07  14  21  28  35  42  49  56  63
# 8 08  16  24  32  40  48  56  64  72
# 9 09  18  27  36  45  54  63  72  81
# ''')

# Задание 7

# user = input(': ')
# Lst1 = user.split(', ')
# nocopy = []
# buity = []
# abc = ''
# for a in Lst1:
#     if a not in nocopy:
#         nocopy.append(a)
# abc = ', '.join(nocopy)
# buity.append(abc)
# print(buity)