
# Задание 1

# cities = {
#     'Moscow': (550, 370),
#     'London': (510, 510),
#     'Paris': (480, 480)
# }
#
# distances = {}
# moscow = cities['Moscow']
# london = cities['London']
# paris = cities['Paris']
#
# m_l = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
# m_p = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
# l_p = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5
#
# distances['m_l'] = m_l
# distances['m_p'] = m_p
# distances['l_p'] = l_p
#
# print(distances)

# ЗАдание 2

# n = {'number': [1, 2, 3, 4, 5, 6, 7]}
# l = []
# for l in n.values():
#     print(sum(l) / len(l))

# Задание 3

# students = int(input(': '))
# wtf = {}
# l = []
# number = []
# nas = []
# while True:
#     user = input(': ')
#     if user == 'stop':
#         break
#     if len(user.split()) == 3:
#         student, lesson, ocenka = user.split()
#         wtf.setdefault(lesson)
#         for j in ocenka:
#             number.append(int(j))
#             if len(number) == students:
#                 nas.append(round(sum(number) / students, 1))
#                 l.insert(0, f'Средний балл:{nas.copy()}')
#                 l.insert(1,f'Максимальный балл:{max(number)}')
#                 l.insert(2,f'Минимальный балл:{min(number)}')
#                 nas.clear()
#                 number.clear()
#         d = [f'{student}: {ocenka}']
#         for i in d:
#             l.append(i)
#             wtf[lesson] = l.copy()
#             if len(l)  > students + 3:
#                 a = l.pop()
#                 l.clear()
#                 l.append(a)
# print(wtf)

# Задание 4
# user = {}
# while True:
#     user_comand = input(': ')
#     if user_comand == 'stop':
#         break
#     if len(user_comand.split(': ')) == 2:
#         Day, lesson = user_comand.split(': ')
#         l = ''.join(lesson)
#         user[Day] = l.split(' ')
#     if user_comand in user:
#         print(user.get(user_comand))
# print(user)


# Задание 5

# sad = {}
# n = int(input(': '))
#
# for i in range(1, n+1):
#     sad[i] = i * i
# print(sad)

# Задание 6

# lst1 = [1,2,3]
# lst2 = [4,5,6]
# n = {}
#
# for i in range(len(lst1)):
#     n[lst1[i]] = lst2[i]
#
# print(n)

# Задание 7

# a = {'ads': 'asds'}
# b = {1: 2}
# d = {}
#
# for key, values in a.items():
#     d[key] = values
# for key, values in b.items():
#     d[key] = values
# print(d)

# Задание 8

# goods = {
# 'Лампа': '12345',
# 'Стол': '23456',
# 'Диван': '34567',
# 'Стул': '45678',
# }
# store = {
# '12345': [
# {
# 'quantity': 27,
# 'price': 42
# },
# ],
# '23456': [
# {
# 'quantity': 22,
# 'price': 510
# },
# {
# 'quantity': 32,
# 'price': 520
# },
# ],
# '34567': [
# {
# 'quantity': 2,
# 'price': 1200
# },
# {
# 'quantity': 1,
# 	'price': 1150
# },
# ],
# '45678': [
# {
# 'quantity': 50,
# 'price': 100
# },
# {
# 'quantity': 12,
# 'price': 95
# },
# {
# 'quantity': 43,
# 'price': 97
#   },
#  ],
# }
#
#
# for product_name, product_id in goods.items():
#     total_quantity = 0
#     price = 0
#     for data in store[product_id]:
#         price += data['quantity'] * data['price']
#         total_quantity += data['quantity']
#     print()
#     print(f'{product_name}: id: {product_id}. Cумма: {price}. Количество: {total_quantity}')































