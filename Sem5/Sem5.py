import random


def rand_letter():
    num = random.randint(0, 100)
    if num % 2 == 0:
        return '100'
    else:
        return '1'


def rand_letter2():
    num = random.randint(0, 100)
    if num % 2 == 0:
        return 'A'
    else:
        return 'B'


# my_list = [x for x in range(10)]
# print(my_list)
# my_list = [6 for x in range(10)]
# print(my_list)
# my_list = [random.randint(0, 100) for _ in range(10)]
# print(my_list)
# my_list = [random.randint(0, 100) for i in range(10) if i % 2 == 0]
# print(my_list)
# my_list = [rand_letter() for i in range(10)]
# print(my_list)
# my_list = list(map(int, my_list))
# print(my_list)
# my_list = list(map(lambda x: x ** 2, my_list))
# print(my_list)
# my_list = list(filter(lambda x: x > 90, my_list))
# print(my_list)
# my_list2 = [rand_letter2() for i in range(10)]
# print(my_list2)
# for i, item in enumerate(my_list2):
#     if item == 'B':
#         print(i, item)
# my_list_f = [rand_letter2() for i in range(10)]
# print(my_list_f)
# my_list_s = [rand_letter2() for i in range(5)]
# print(my_list_s)
# my_list_trd = [rand_letter2() for i in range(15)]
# print(my_list_trd)
#
# all_list = list(zip(my_list_f, my_list_s, my_list_trd)) # длина по минимальному элементу
# print(all_list)

"""
В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
"""

# path = r'result.txt'
#
# with open(path, 'r', encoding='UTF-8') as data:
#     data = data.readline()
#
# data = data.split(' ')
# data = list(map(int, data))
#
# for i in range(1, len(data)):
#     if data[i] - 1 != data[i - 1]:
#         print(f'Не хватает {data[i]-1}')


"""
Дан список чисел. Создайте список, в который попадают числа,
описываемые возрастающую последовательность.
Порядок элементов менять нельзя.

"""

# list_1 = [random.randint(0, 9) for i in range(15)]
# print(list_1)
# list_2 = []
# temp = []
# for j in range(len(list_1) - 1):
#     temp.append(list_1[j])
#     for i in range(j, len(list_1) - 1):
#         if temp[len(temp) - 1] < list_1[i + 1]:
#             temp.append(list_1[i + 1])
#     if len(temp) > 1:
#         list_2.append(temp)
#     temp = []
#
# max = 0
# for i in range(len(list_2)):
#     if len(list_2[i]) > len(list_2[max]):
#         max = i
#
# print(list_2)
# print(list_2[max])
