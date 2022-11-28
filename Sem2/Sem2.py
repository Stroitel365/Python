""" 
from decimal import Decimal as Dcm

# numbers = float(input('Enter list size: '))
# count = int(input('Enter accuracy: '))

# num: float  # reserve space for variable, but witout initialising it
# num = 8.8902


# def digit_after_dot_counter(num: float):
#     count = 0
#     div = 1
#     while True:
#         if num*div != int(num*div):
#             count += 1
#             div *= 10
#         else: break
#     return count


# numberO = num*100/10
# numberD = Decimal(str(num))*100/10
# numberD = Dcm(str(num))*100/10


# print(numberO,numberD) 

"""

""" 
coords = input('Enter coordinates with space: ')
coords = coords.split(' ')
print(coords)
if len(coords)/2 == 2:
    print("2D")
    # for item in coords:
    #     print(int(item))
    #     print(type(item))
elif len(coords)/2 == 3:
    print("3D")
else:
    print("Coordinates are wrong")
 """

"""
number = int (input("Enter number "))

my_list = []

for i in range(-number, number+1):
    my_list.append(i)

print(*my_list, sep =', ', end= ' list end') 
"""

""" 
my_list = [1, 2, 3]


def func(a,b,c):
    print(a, b, c, sep =', ', end= ' list end')
    
func(*my_list) 
"""

""" 
number = int(input("Enter number "))

if (number % 10 == 0 or number % 15 == 0) and number % 30 != 0:
    print(True)
else:
    print(False)
 """

"""  
# Напишите программу,  которая принимает на вход число N  и выдает последовательность из N членов
# Пример
# n=5 1, -3, 27, -81 

N = int(input("Enter number "))
list = []
for i in range(N):
    list.append((-3)**i)
print(*list, sep=', ') 
"""

""" 
# Для натурального n создать список,
# состоящий из элементов последовательности 3*n + 1.
# *Пример:*
# - Для n = 6: ['1: 4', '2: 7', '3: 10', '4: 13', '5: 16', '6: 19']
n = int(input("Enter number "))
list = []
for i in range(1,n+1):
    list.append(f'{i}:{3*n+1}')
print(*list, sep=', ') 

"""

import random
print(random.randint(0,100))
