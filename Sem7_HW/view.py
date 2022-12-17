def input_number():
    while True:
        try:
            number = int(input('Введите число: '))
            return number
        except:
            print('Введите число!')


def input_operation():
    while True:
        operation = input('Введите операцию: ')
        if operation in ['+', '-', '/', '*', '=']:
            return operation
        else:
            print("Введите операцию из списка: ['+', '-', '/', '*', '=']")


def input_equation():
    equation = input('Введите выражение: ')
    return equation


def print_to_console(value_text):
    print(value_text)


def print_log_off():
    print("Пока-пока!")


def print_error_zero():
    print("На ноль делить нельзя!")


def choose_method():
    while True:
        choice = input('Введите вариант ввода : 1 - строкой все выражение, '
                       '2 - последовательно цифры: ')
        if choice == '1' or choice == '2':
            return choice
        else:
            print('Неверное значение. Введите вариант ввода : 1 - строкой все '
                  'выражение, 2 - последовательно цифры: ')
