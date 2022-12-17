def f(x):
    return x ** 2


g = f

# print(type(f))
# print(type(g))
#
# print(type(f(4)))
# print(type(g(4)))
#
# def calc1(x):
#     return x + 10
#
#
# # print(calc1(10))
#
#
# def calc2(x):
#     return x * 10
#
#
# # print(calc1(10))
#
#
# def math(op, x):
#     print(op(x))
#
#
# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x + y

#
# sum = lambda q, w: q + w  # тоже что функция вверху
#
#
# def mylt(x, y):
#     return x * y
#
#
# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a,b)
#
#
# # calc(sum, 4, 5)
#
# calc(lambda q, w: q + w)  # тоже что в 50 строчке

# List comprehetion
#
# list = []
#
# for i in range(1, 21):
#     if (i % 2 == 0):
#         list.append(i);
#
# print(list)
#
# list = [i for i in range(1, 21)]
#
# print(list)
#
# list = [i for i in range(1, 21) if i % 2 == 0]
#
# print(list)
#
# list = [(i, i) for i in range(1, 21) if i % 2 == 0]
#
# print(list)
#
#
# def f(x):
#     return x ** 3
#
#
# list = [f(i) for i in range(1, 21) if i % 2 == 0]
#
# print(list)
#
# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
#
# print(list)

list_in = [1, 2, 5, 4, 8, 6]

list_out = [(i, i ** 2) for i in list_in if i % 2 == 0]

print(list_out)
#
# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close()
# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
#     out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]
#
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x,x**2), res)
# print(res)

#
# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
#
# print(li)

# data = list(map(int, input().split()))
# print(data)


# data = list(map(int, ' 1 2 3 4 5 666 7 7'.split()))
# for e in data:
#     print(e)
#
# print('---')
#
# for e in data:
#     print(e)


# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = list(map(int, data))
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# data = [x for x in range(10)]
# # res = list(filter(lambda x: x % 2 == 0, data))
# res = list(filter(lambda x: not x % 2, data)) # тоже что 156 строка
# print(res)

# data = '1 2 3 5 8 15 23 38'.split()
#
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14]
#
# data = list(zip(users, ids))  # работает по минимальному количеству элементов
# print(data)
#
# data = list(enumerate(users))
# print(data)
