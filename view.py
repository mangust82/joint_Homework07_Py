def main_menu():
    print()
    print('1-Отобразить данные, 2-Поиск по значению, 3-Импорт, 4-Экспорт', end='\t')
    print()
    print('5-Добавить контакт, 6-Удалить контакт, 7-Изменить контакт, 8-Выход Enter', end='\t')
    print()
    print()
    menu = input('Выберите пункт меню: ')
    return menu


def show_database(list_of_dict):
    print(list_of_dict)
    pass


def second_menu(text):
    a = input(text)
    return (a)


def add_user():
    F_name = input('Введите имя: ')
    L_name = input('Введите фамилию: ')
    phonenum = input('Введите номер телефона: ')
    coment = input('Введите комментарий: ')
    user_dict = {}
    return user_dict
