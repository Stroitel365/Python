def input_number():
    while True:
        try:
            number = int(input('Enter number: '))
            return number
        except:
            print('Error')


def input_operation():
    while True:
        operation = input('Enter operation: ')
        if operation in ['+', '-', '/', '*', '=']:
            return operation
        else:
            print('Enter correct operation')


def print_to_console(value_text):
    print(value_text)

def print_log_off():
    print("Goodbuy")

def print_error_zero():
    print(" На ноль делить нельзя")