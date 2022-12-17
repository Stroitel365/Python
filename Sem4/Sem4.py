import sys

sys.path.append('../')

import  Functions as f

"""
задайте строку из набора чисел. 
напишите программу, которая покажет большее и меньшее число. 
в качестве символа-разделителя используйте пробел.
"""

task_list = input('введите числа через пробел: ')
task_list = task_list.strip().split(' ')
for i in range(len(task_list)):
    task_list[i] =int(task_list[i])

print(f.MaxIntList(task_list))
print(f.MinIntList(task_list))

"""задайте два числа. напишите программу, которая найдёт нок 
(наименьшее общее кратное) этих двух чисел.
"""

# f_nums = input('введите числа через пробел: ')
# f_nums = f_nums.strip().split(' ')
# for i in range(len(f_nums)):
#     f_nums[i] =int(f_nums[i])
#
# max_num = f.MaxIntList(f_nums)#
# for i in range(max_num, f_nums[0]*f_nums[1]+1):
#     if i % f_nums[0] == 0 and i % f_nums[1] == 0:
#         print(i)
#         break

"""
найдите корни квадратного уравнения ax² + bx + c = 0 
с помощью математических формул нахождения корней квадратного уравнения
"""

# str = '12*x**2 + 12*x + 1 = 0'
# str = str.replace(' ', '')
# str = str[:-2].split('+')
# new_str = []
#
# for item in str:
#     new_str.append(item.split('*x')[0])
#
# print(new_str)
#
# a, b, c = new_str
# print(a, b, c)

"""
Наработки на ДЗ
"""

# import random
#
# koef = [0] * 3
# for i in range(len(koef)):
#     koef[i] = random.randint(0, 5)
#
# equation = f'{koef[0]}*x^2 + {koef[1]}*x+{koef[2]} = 0'
# print(equation)
