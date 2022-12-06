# colors = ['red', 'green', 'blue']

# Первый вариант записи

""" data = open ('file.txt','w')
data = open ('file.txt','a')
data.writelines(colors) # запись без разделителей
data.write('\nline 132\n')
data.close() """ # ОБЯЗАТЕЛЬНО закрывать файл. Иначе процесс работы не останавливаетс яи удалить или изменить файл не получится

# Второй вариант записи
""" with open('file.txt','w') as data:
    data.write('\nline 1\n')
    data.write('line 32\n')

data.close() # При использовании 2го варианта не обязательно закрывать файл """


# exit()

# Считывание из файла

""" path = 'file.txt'
data = open(path,'r')
for line in data:
    print(line)
data.close()

exit() """

# import Func as F

# print(F.f(1))
# print(F.PowerTwo(2))



testList = [1, 2, 4 , 6, 8]
a = 5

print(testList)

for i in testList:
    i = a

print(testList)
