import sys

sys.path.append('../')

import Functions as f

"""
задайте строку из набора чисел. 
напишите программу, которая покажет большее и меньшее число. 
в качестве символа-разделителя используйте пробел.
"""

task_list = input('введите числа через пробел: ')
task_list = task_list.strip().split(' ')
# for i in range(len(task_list)):
#     task_list[i] = int(task_list[i])

task_list = list(map(int, task_list)) # Вместо строк 15-16

print(f.MaxIntList(task_list))
print(f.MinIntList(task_list))

""" 
# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

number = int(input("Введите число для формирования списка: "))
fib_list = [0, 1]
for i in range(1, number):
    fib_list.append(fib_list[i - 1] + fib_list[i])
# for i in range(1, number):
#     fib_list.insert(0, fib_list[1] - fib_list[0])

nega_fib_list = [fib_list[i]*(-1)**(i+1) for i in range(len(fib_list) - 1, 0, -1)]
# Вместо строк 34-35

print(*(nega_fib_list+fib_list), sep=', ')


"""
Лямбда пример
"""

def sum(x, y):
    return x + y

def calc(op, a, b):
    print(op(a, b))
    return op(a,b)


calc(sum, 4, 5)

calc(lambda q, w: q + w)  # тоже что в 55 строчке
