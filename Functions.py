def PowerTwo(x):
    return x**2

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

def StringMultiplyBy(symbol,count=3): 
    # count=3 значит, что ели мы можем не передавать второй аргумент (тогда он автоматически присвоится 3м)
    return symbol*count

def concatenatio(*params):
    # * значит что мы можем передавать любое количество элементов 
    res: str = ""
    for item in params:
        res += item
    return res

def MaxIntList(list):
    max = list[0]
    for i in range(1, len(list)):
        if max < list[i]:
            max = list[i]
    return max

def MinIntList(list):
    min = list[0]
    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
    return min
