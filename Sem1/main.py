# # 1. Напишите программу, которая принимает на вход два числа и
# # проверяет, является ли одно число квадратом другого.
# #
# # *Примеры:*
# #
# # - 5, 25 -> да
# # - 4, 16 -> да
# # - 25, 5 -> ДА
# # - 8,9 -> нет
#
# print('Введите число а ')
# a = int(input())
# print('Введите число b ')
# b = int(input())
#
# # if b == a**2:
# #     print('да')
# # elif a == b**2:
# #     print('да')
# # else:
# #     print('нет')
#
# if b == a**2 or a == b**2:
#     print('да')
# else:
#     print('нет')

# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90


#
# coll = []
# for i in range(5):
#     x = int(input('Enter number: '))
#     coll.append(x)
# max_t = coll[0]
# for i in coll:
#     if max_t<i:
#         max_t=i
# print(max_t)

# num_in = float(input('Enter number:'))
# if int(num_in*10)%10!=0 and (num_in-int(num_in))!=0:
# 	print('Десятая часть:',int(num_in*10)%10)
# else:
# 	print('Число целое')



