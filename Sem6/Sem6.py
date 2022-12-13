# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#
# *Пример:*
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


f_list = [1, 2, 3, 5, 1, 5, 3, 10]

# 1 вариант
# s_list = []
# for i in range(len(f_list)):
#     if f_list.count(f_list[i]) == 1:
#         s_list.append(f_list[i])
# print(f_list)
# print(s_list)

# 2 вариант
# dict = {}
# for i in list:
#     if i in dict.keys():
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)
#
# new_list = []
# for j in dict.keys():
#     if dict[j] == 1:
#         new_list.append(j)
# print(new_list)

# 3 вариант
# my_dic ={}
# for key in f_list:
#     my_dic[key]=my_dic.get(key,0)+1
#
# new_list =[]
# for key,value in my_dic.items():
#     if value ==1:
#         new_list.append(key)
# print(new_list)


# my_dict = {1: 3, 2: 4, 3: 5, 5: 7, None: 1}
#
# for key in range(6):
#     print(my_dict.get(key, 0))  # выдает 0 (или другое) при ключе которого нету в словаре
# # если без гет сделать то выдаст ошибку в 0 элементе, что такого ключа нет
#
#


# 1. Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте
# операции +, -, /, *.приоритет операций стандартный.
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;

# str_in = input("Введите выражение без равно: ")
str_in = '1 + 2 * 3 - 7 + 4 / 2'
# print(str_in)
list_str = str_in.split()
print(list_str)
for i in range(len(list_str)):
    if list_str[i].isdigit():
        list_str[i] = int(list_str[i])
print(list_str)
temp = 0

while len(list_str) != 1:
    i = 0
    while ('*' in list_str or '/' in list_str) and i < len(list_str):
        if list_str[i] == '*':
            temp = list_str[i-1]*list_str[i+1]
            list_str.pop(i)
            list_str.pop(i)
            list_str[i - 1] = temp
            i -= 1
            print(list_str)
        elif list_str[i] == '/':
            temp = list_str[i - 1] / list_str[i + 1]
            list_str.pop(i)
            list_str.pop(i)
            list_str[i - 1] = temp
            print(list_str)
            i -= 1
        else:
            i += 1

    while ('+' in list_str or '-' in list_str) and i < len(list_str):
        if list_str[i] == '+':
            temp = list_str[i - 1] + list_str[i + 1]
            list_str.pop(i)
            list_str.pop(i)
            list_str[i - 1] = temp
            print(list_str)
            i -= 1
        elif list_str[i] == '-':
            temp = list_str[i - 1] - list_str[i + 1]
            list_str.pop(i)
            list_str.pop(i)
            list_str[i - 1] = temp
            print(list_str)
            i -= 1
        else:
            i += 1

print(list_str)
