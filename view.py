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
    for idx, man in enumerate(list_of_dict):

        # man = list(el) #убрала валуа, с ним не работает. список списков
        print(f'{(idx+1):4}  Фамилия: {man[0]:10} Имя: {man[1]:8} Номер: {man[2]:10} Комментарий: {man[3]:3}') # пробкл был нишний
# добавила {(idx):4} плюс один, тк неправильная опять нумерация была

def second_menu(text):
    a = input(text)
    return(a)

def add_user():
    F_name = input('Введите имя: ')
    L_name = input('Введите фамилию: ')
    phonenum = input('Введите номер телефона: ')
    coment = input('Введите комментарий: ')
    user_dict = {'Фамилия': F_name, 'Имя': L_name,'Телефон': phonenum , 'Комментарий': coment}
    return user_dict

def show_str(list_of_dict):
    #pass
    print(f'N  Фамилия:        Имя:        Номер:           Комментарий: ')
    for idx, el in enumerate(list_of_dict):
        man = el # не валуа с ним не работает
        print(f'{man[0]}      {man[1]}       {man[2]}         {man[3]}')

# вызов меню(тест)
# main_menu()