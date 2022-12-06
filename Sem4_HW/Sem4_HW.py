"""Задана натуральная степень k. Сформировать случайным образом список коэффициентов
 (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
 Пример:
 если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
# import random
#
# k = int(input('Введите степень многочлена k: '))
# indD = {}
#
# for j in range(k + 1):
#     indD[j] = random.randint(-100, 100)
#     if indD[j] > 0:
#         indD[j] = '+' + str(indD[j])
#
# # print(indD)
# equation = ''
# for i in range(k, -1, -1):
#     if indD[i] != 0:
#         if indD[i] == 1:
#             if i == 0:
#                 equation += '1'
#             elif i == 1:
#                 equation += 'x'
#             else:
#                 equation += f'x^{i} +'
#         else:
#             if i == 0:
#                 equation += f'{indD[i]}'
#             elif i == 1:
#                 equation += f'{indD[i]}*x'
#             else:
#                 equation += f'{indD[i]}*x^{i}'
#
# print(equation + " = 0 ")
# eq_write = equation + " = 0 "
# with open('first_equation_taskA.txt', 'w') as data:
#     data.write(eq_write)

"""
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.

"""

#
# def create_list_of_parts(str_eq):
#     str_eq = str_eq.replace(' ', '')
#     str_eq = str_eq[2:-4].split("+")
#     for i in range(len(str_eq)):
#         if str_eq[i].count("*x") > 1:
#             temp_list = list(str_eq[i].split('-'))
#             del str_eq[i]
#             for j in range(len(temp_list) - 1, -1, -1):
#                 if j != 0:
#                     temp_list[j] = '-' + temp_list[j]
#                 str_eq.insert(i, temp_list[j])
#         elif "*x" in str_eq[-1]:
#             temp_list = list(str_eq[-1].split('-'))
#             del str_eq[-1]
#             for j in range(0, len(temp_list)):
#                 if j != 0:
#                     temp_list[j] = '-' + temp_list[j]
#                 str_eq.append(temp_list[j])
#     return str_eq
#
#
# def create_dictionary_for_koefs(str_eq):
#     dic_eq = {}
#
#     for i in range(len(str_eq)):
#         if '*x^' in str_eq[i]:
#             t_list = str_eq[i].split("*x^")
#             dic_eq[t_list[1]] = t_list[0]
#         elif i == len(str_eq) - 2:
#             t_list = str_eq[i][:-2]
#             # print(t_list)
#             dic_eq['1'] = t_list
#         elif i == len(str_eq) - 1:
#             dic_eq['0'] = str_eq[i]
#
#     return dic_eq
#
#
# def create_sum_dictionary(f_dic, s_dic):
#     sum_dic = {}
#     if len(f_dic) > len(s_dic):
#         for item_1dic in f_dic:
#             if item_1dic in s_dic:
#                 sum_dic[item_1dic] = int(f_dic[item_1dic]) + int(s_dic[item_1dic])
#             else:
#                 sum_dic[item_1dic] = int(f_dic[item_1dic])
#         for items_2dic in s_dic:
#             if items_2dic not in sum_dic:
#                 sum_dic[items_2dic] = int(s_dic[items_2dic])
#     else:
#         for item_2dic in s_dic:
#             if item_2dic in f_dic:
#                 sum_dic[item_2dic] = int(f_dic[item_2dic]) + int(s_dic[item_2dic])
#             else:
#                 sum_dic[item_2dic] = int(s_dic[item_2dic])
#         for items_1dic in f_dic:
#             if items_1dic not in sum_dic:
#                 sum_dic[items_1dic] = int(f_dic[items_1dic])
#     return sum_dic
#
#
# def create_sum_str_from_dic(dic_summ):
#     summ_eq = ''
#     for key in dic_summ:
#         if int(key) > 1:
#             if dic_summ[key] > 0:
#                 summ_eq += '+' + str(dic_summ[key]) + '*x^' + key
#             else:
#                 summ_eq += str(dic_summ[key]) + '*x^' + key
#         elif int(key) == 1:
#             if dic_summ[key] > 0:
#                 summ_eq += '+' + str(dic_summ[key]) + '*x' + key
#             else:
#                 summ_eq += str(dic_summ[key]) + '*x' + key
#         elif int(key) == 0:
#             if dic_summ[key] > 0:
#                 summ_eq += '+' + str(dic_summ[key])
#             else:
#                 summ_eq += str(dic_summ[key])
#     return summ_eq
#
#
# file_1 = open('first_equation_taskB.txt', 'r')
# f_eq = str(file_1.readlines(1))
# file_2 = open('second_equation_taskB.txt', 'r')
# s_eq = str(file_2.readlines(1))
# file_1.close()
# file_2.close()
# #  print(f_eq)
# #  print(s_eq)
#
# f_eq = create_list_of_parts(f_eq)
# s_eq = create_list_of_parts(s_eq)
# #  print(f_eq)
# #  print(s_eq)
#
# dic_f_eq = create_dictionary_for_koefs(f_eq)
# dic_s_eq = create_dictionary_for_koefs(s_eq)
# # print(dic_f_eq)
# # print(dic_s_eq)
#
# dic_sum = create_sum_dictionary(dic_f_eq, dic_s_eq)
# # print(dic_sum)
#
# sum_eq = create_sum_str_from_dic(dic_sum)+'=0'
# # print(sum_eq)
#
# with open('Sum_of_2_equation_taskB', 'w') as data:
#     data.write(sum_eq)
