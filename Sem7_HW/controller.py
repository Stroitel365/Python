import view
import model


def input_first():
    number = view.input_number()
    model.set_first(number)


def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == "/" and number == 0:
            view.print_error_zero()
        else:
            model.set_second(number)
            break


def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)

def input_equation():
    equation = view.input_equation()
    model.set_equation(equation)

def solution():
    oper = model.get_operation()
    if oper == "+":
        model.addition()
    elif oper == "-":
        model.difference()
    elif oper == "/":
        model.division()
    elif oper == "*":
        model.mult()
    result_string = f'{model.get_first()} {model.get_operation()} ' \
                    f'{model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())
    return False


def start():
    choice = view.choose_method()
    if choice == '1':
        input_equation()
        string_solution()
    else:
        input_first()
        while True:
            input_operation()
            if model.get_operation() == "=":
                view.print_log_off()
                break
            input_second()
            if solution():
                break


def string_solution():
    list_str = model.get_equation().split()
    for i in range(len(list_str)):
        if list_str[i].isdigit():
            list_str[i] = int(list_str[i])

    while len(list_str) != 1:
        i = 0
        while ('*' in list_str or '/' in list_str) and i < len(list_str):
            if list_str[i] == '*':
                temp = list_str[i - 1] * list_str[i + 1]
                list_str.pop(i)
                list_str.pop(i)
                list_str[i - 1] = temp
                i -= 1
            elif list_str[i] == '/':
                temp = list_str[i - 1] / list_str[i + 1]
                list_str.pop(i)
                list_str.pop(i)
                list_str[i - 1] = temp
                i -= 1
            else:
                i += 1

        while ('+' in list_str or '-' in list_str) and i < len(list_str):
            if list_str[i] == '+':
                temp = list_str[i - 1] + list_str[i + 1]
                list_str.pop(i)
                list_str.pop(i)
                list_str[i - 1] = temp
                i -= 1
            elif list_str[i] == '-':
                temp = list_str[i - 1] - list_str[i + 1]
                list_str.pop(i)
                list_str.pop(i)
                list_str[i - 1] = temp
                i -= 1
            else:
                i += 1
    view.print_to_console(list_str)
