# # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# # Пример:
# # 6 -> да
# # 7 -> да
# # 1 -> нет
#
# week_day = int(input("Enter number of a day of a week: "))
# if week_day == 1 or week_day == 2 or week_day == 3 or week_day == 4 or week_day == 5:
#     print("It's not a weekend")
# elif week_day == 6 or week_day == 7:
#     print("It's a weekend")
# else:
#     print("It's not a day of a week")

# # Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
# x_var = [False, True]
# y_var = [False, True]
# z_var = [False, True]
# flag = None
# for i in x_var:
#     for j in y_var:
#         for k in z_var:
#             if (not (i or j or k)) == ((not i) and (not j) and (not k)):
#                 flag = True
#             else:
#                 flag = False
# print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is', flag)

# # Напишите программу, которая принимает на вход координаты точки (X и Y),
# # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# # Пример:
# # x=34; y=-30 -> 4
# # x=2; y=4 -> 1
# # x=-34; y=-30 -> 3
#
# y_coord = float(input("Enter Y coordinate: "))
# x_coord = float(input("Enter X coordinate: "))
# if y_coord > 0 and x_coord > 0:
#     print("The dot is located in I (1) quarter")
# elif y_coord > 0 and x_coord < 0:
#     print("The dot is located in II (2) quarter")
# elif y_coord < 0 and x_coord < 0:
#     print("The dot is located in III (3) quarter")
# else:
#     print("The dot is located in IV (4) quarter")


# # Напишите программу, которая по заданному номеру четверти,
# # показывает диапазон возможных координат точек в этой четверти (x и y).
# num_quarter = int(input("Enter a number of a quarter: "))
# if num_quarter == 1:
#     print("Coordinates X and Y of the dot can be: 0 < X < +Infinity; 0 < Y < +Infinity")
# elif num_quarter == 2:
#     print("Coordinates X and Y of the dot can be: - Infinity < X < 0; 0 < Y < +Infinity")
# elif num_quarter == 3:
#     print("Coordinates X and Y of the dot can be: - Infinity < X < 0; - Infinity < Y < 0")
# elif num_quarter == 4:
#     print("Coordinates X and Y of the dot can be: 0 < X < +Infinity; - Infinity < Y < 0")
# else:
#     print("Sorry, it's not a quarter number. Please,try again")

# # Напишите программу, которая принимает на вход координаты двух точек
# # и находит расстояние между ними в 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# # Пример:
# # A (3,6); B (2,1) -> 5,09
# # A (7,-5); B (1,-1) -> 7,21
#
# coord_y_1 = float(input("Enter Y coordinate of the first dot: "))
# coord_x_1 = float(input("Enter X coordinate of the first dot: "))
# coord_y_2 = float(input("Enter Y coordinate of the second dot: "))
# coord_x_2 = float(input("Enter X coordinate of the second dot: "))
# dist = ((coord_x_2 - coord_x_1) ** 2 + (coord_y_2 - coord_y_1) ** 2) ** 0.5
# print("Distance between two dots is:", dist)
