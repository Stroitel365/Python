from decimal import Decimal as Dcm
import random

# Functions


def make_int_from_float(num: float):
    count = 0
    div = 1
    while True:
        if num*div != int(num*div):
            count += 1
            div *= 10
        else:
            break
    num = num*div
    return num


def Random_places(in_list: list):
    input_list = list(in_list)
    for i in range(len(input_list)):
        new_i = random.randint(0, len(input_list)-1)
        input_list[i], input_list[new_i] = input_list[new_i], input_list[i]
    return input_list


""" 
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


number = float(input('Введите число : '))
number = make_int_from_float(number)
sum = 0
while number > 0:
    sum = sum + (number % 10)
    number //= 10
else:
    print(f'Сумма цифр в числе равна: {Dcm(sum)}') 
"""

""" 
# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

number = int(input('Введите число : '))
in_list = []
for i in range(1, number+1):
    in_list.append(round(((1+1/i)**i), 4))
sum_item = 0
for item in in_list:
    sum_item += round(item, 4)
print(*in_list, sep=', ')
print(f'Сумма чисел в списке {in_list}: {sum_item}') 
"""

""" 
# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

first_list = input(" Введите числа или слова через пробел: ")
first_list = first_list.split(' ')
second_list = list(Random_places(first_list))
print(f' Было {first_list} стало {second_list}') 
"""
