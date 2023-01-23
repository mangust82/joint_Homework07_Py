def main_menu():
    print('1. Показать справочник контактов (жми 1) ')
    print('2. Поиск (жми 2) ')
    print('3. Импорт базы контактов (жми 3) ')
    print('4. Экспорт базы контактов (жми 4) ')
    print('5. Добавить новый контакт (жми 5)  ')
    print('6. Удалить контакт (жми 6)  ')
    print('7. Редактирование контакта (жми 7) ')
    print('8. Для выхода жми 8 \n')
    menu = input('Выберите пункт меню: ')
    return menu

def show_database(list_of_dict):
    #pass
    for idx, el in enumerate(list_of_dict):

        man = list(el.values())
        print(f'{idx:4}  Фамилия: {man[0]:10} Имя: {man[1]:8} Номер: {man[2]:10} Комментарий: {man[3]: 3}')


def second_menu(text):
    a = input(text)
    return(a)

def add_user():
    F_name = input('Введите имя: ')
    L_name = input('Введите фамилию: ')
    phonenum = input('Введите номер телефона: ')
    coment = input('Введите комментарий: ')
    user_dict = {}
    return user_dict

# вызов меню(тест)
# main_menu()