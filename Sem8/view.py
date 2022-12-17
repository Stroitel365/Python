def main_menu():
    print('\n1. Показать контакты')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход')


def choice_main_menu():
    while True:
        try:
            choice = int(input(' enter number'))
            if choice in range(0, 8):
                print()
                return choice
            else:
                print(' Please, enter number 0-7')
        except:
            print(' Error, please, enter number 0-7 ')


def input_new_contact():
    name = input(' Введите имя : ')
    numbers = input('Введите телефон : ')
    comment = input(' Input comment ')
    return [name, numbers, comment]


def input_remove_contact():
    id = int(input(' input id contact for removale'))
    return id


def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('Tel book is empty')


def load_success():
    print(' Load sucsess')


def log_off():
    print('Bye')


def safe_success():
    print(' Сохранено успешно')


def remove_success():
    print(' Удалено успешно')
