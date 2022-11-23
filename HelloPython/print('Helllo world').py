# print('Helllo world')
# - комментарий на python
""" a = 123  # int
b = 1.23  # float
value = None  # чтобы потом в коде применить нужного типа данных
print(type(a))
print(type(b))
print(type(value))
value = 123458
# print(type(value))
s = 'hello word'
print(s)
s = 'hello "word"'
print(s)
s = "hello 'word'"
print(s)
s = 'hello \'word\''
print(s)
s = 'hello \n\'word\''
print(s)
print(s, '-',b,'-',a)
print('{}-{}-{}'.format(a,b,s))
print(f'{a}-{b}-{s}')
print('{2}-{1}-{0}'.format(a,b,s))

f = True
t = False
print(f,t)
list = [1,'two2',3.21,True]
print(list) """

""" # input
print('Insert a')
a = input()
print(a)
 """
""" a = +123
b = -432
c = a+b
print(c)
c = a-b
print(c)
c = round(a/b,3)
print(c)
c = b//a
print(c)
c = b%a
print(c)
c = a**b
print(c) """
""" a = 10
a += 5
print(a)
a = 10
a -= 5
print(a) """

""" a = 1 < 4 and 5 > 2
print(a)
a = [1,2]
b = [1,2]
print(a==b) """
""" 
f = [1, 2, 3, 4]
print(f[0] % 2 == 0)
print( not f[0] % 2)
 """
""" 
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
    print('a больше')
else:
    print(b)
    print('b больше')
 """
""" 
username = input("Введите имя: ")
if username == "Masha":
    print("Hey! It's Masha")
elif username == "Marina":
    print("Come back later")
elif username == "Ilnar":
    print("Ilnar is the best")
else:
    print('Hello ', username)
     """

""" original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)
 """
""" 
for i in 1, -2, 3, 14, 5:
    print(i**2)
 """
""" r = range(10,-1,-2)
for i in r:
    print(i)
 """
""" line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
print(line) """

text = 'съешь ещё этих мягких французских булок'
""" print(len(text))  # 39
print('ещё' in text)  # True
print(text.isdigit())  # False
print(text.islower())  # True
print(text.replace('ещё', 'ЕЩЁ'))
for c in text:
    print(c)
 """
""" print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2]
print(text[:]) """
""" 
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)  # [20, 4, 6, 8, 10]
print(numbers)  # [10, 2, 3, 4, 5]
colors = ['red', 'green', 'blue']
for e in colors:
    print(e)  # red green blue
for e in colors:
    print(e*2)  # redred greengreen blueblue
colors.append('gray')  # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])  # True
colors.remove('red')  # del colors[0] # удалить элемент
 """

""" def f(x):
    return x**2
     """
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType