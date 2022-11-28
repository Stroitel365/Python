# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# my_list = ['dkfje5h454f','jfdf87434hf', 'eiudj834', 'sdjf123209875']
# number = input('Enter symbol: ')

# for item in my_list:
#     for char in item:
#         if char==number:
#             print(f'symbol {number} is in the list {item}')
#             break
#     else:
#         print(f'symbol {number} is not in the list {item}')

#  Второй вариант

# for item in my_list:
#     if number in item:
#         print(f'symbol {number} is in the list {item}')
#     else:
#         print(f'symbol {number} is not in the list {item}')

# C подсчетом места

# for item in my_list:
#     count =0
#     for i in range(len(item)):
#         if item[i]==number:
#             print(f'symbol {number} is in the list {item}'
#                 f'on {i} position')
#             count+=1
#     print(f'symbol {number} is in the list {item} {count} times')


# 3. Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: False
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: False
# - список: [], ищем: "123", ответ: False


# my_list = ["123", "234", 123, "567"]
# char_input = input('Enter symbol: ')
# count = 0
# for i in range(len(my_list)):
#     if char_input == my_list[i]:
#         count += 1
#         if count == 2:
#             print(
#                 f'Второе вхождение  символа {char_input} находится на позиции {i}')
# else:
#     if count < 2:
#         print("False")
