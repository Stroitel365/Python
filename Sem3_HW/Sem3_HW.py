""" 
# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

# in_list = input(" Введите числа через пробел: ")
# in_list = in_list.split(' ')
# out_list = []
# sum = 0
# for i in range(1, len(in_list), 2):
#     sum += int(in_list[i])
# print(sum)

""" 
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16]
[2, 3, 5, 6] => [12, 15]
"""

# inp_list = input(" Введите числа через пробел: ")
# inp_list = inp_list.split(' ')
# outp_list = []
# for i in range(len(inp_list) // 2):
#     outp_list.append(int(inp_list[i]) * int(inp_list[len(inp_list) - 1 - i]))
# if len(inp_list) % 2 != 0:
#     outp_list.append(
#         int(inp_list[len(inp_list) // 2]) * int(inp_list[len(inp_list) // 2]))
# print(f'Произведение пар чисел: {outp_list}')

""" 
# Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части
# элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
# from decimal import Decimal as Dcm
#
# in_list = input(" Введите числа через пробел: ")
# in_list = in_list.split(' ')
# max_temp = Dcm(in_list[0]) - Dcm(in_list[0]) // 1
# min_temp = Dcm(in_list[0]) - Dcm(in_list[0]) // 1
# for item in in_list:
#     if '.' in item:
#         if max_temp < Dcm(item) - Dcm(item) // 1:
#             max_temp = Dcm(item) - Dcm(item) // 1
#         if min_temp > Dcm(item) - Dcm(item) // 1:
#             min_temp = Dcm(item) - Dcm(item) // 1
# print(
#     f'Разница между максимальным и минимальным значением дробной части элементов'
#     f' в списке {in_list}: {max_temp - min_temp}')

""" 
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
"""

#
# def Make_10_into_bytes(number: int):
#     number_2 = ''
#     while number != 0:
#         temp = number % 2
#         number_2 = str(temp) + number_2
#         number //= 2
#     return number_2
#
#
# number_10 = int(input("Введите число для перевода: "))
# number_2 = Make_10_into_bytes(number_10)
#
# print(f'Число {number_10} в двоичной системе исчисления : {number_2}')

""" 
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

number = int(input("Введите число для формирования списка: "))
fib_list = [1, 0, 1]
for i in range(2, number + 1):
    fib_list.append(fib_list[i - 1] + fib_list[i])
for i in range(1, number):
    fib_list.insert(0, fib_list[1] - fib_list[0])
print(*fib_list, sep=', ')
