"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.

fffffdddrrrr = 5f3d4r
"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
with open('Input.txt', 'r') as data:
    in_str = data.read()
in_out = ''
forward = True

for i in range(len(in_str)):
    if in_str[i].isdigit():
        forward = False

if forward:
    temp_count = -1
    temp_list = []
    for i in range(len(in_str) - 1):
        if in_str[i] != in_str[i + 1]:
            temp_list.append(in_str[temp_count + 1:i + 1])
            temp_count = i
    temp_list.append(in_str[temp_count + 1:])
    for i in range(len(temp_list)):
        in_out += str(len(temp_list[i])) + temp_list[i][0]
else:
    temp_list = []
    for i in range(0, len(in_str), 2):
        temp_list.append(in_str[i:i + 2])
    for i in range(len(temp_list)):
        j = 0
        while j < int(temp_list[i][0]):
            in_out += temp_list[i][1]
            j += 1
with open('Out.txt', 'w') as result:
    result.write(in_out)
