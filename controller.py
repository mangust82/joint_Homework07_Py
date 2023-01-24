import init
import view
import find
import mod_imp
import mod_exp
import edit_db

def SaveDataBase(name_data_base, data_base):
    field_names = ['Фамилия', 'Имя', 'Телефон', 'Комментарий']
    for dataUser in data_base:
        addList.append(dataUser)
    with open(name_data_base, 'w', newline='', encoding='UTF-8') as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=field_names, quoting=csv.QUOTE_ALL, delimiter=';')
        for i in addList:
            writer.writerow(i)


path = 'database.csv'

def ClickButton():
    data_base = init.init(path)
    while True:

        num_menu = view.main_menu()
        if num_menu == '':
            print('Exit')
            break
        elif num_menu == '1':
            view.show_database(data_base)
        elif num_menu == '2':
            find_str = view.second_menu('Введите строку поиска: ')
            find.find_cont(find_str, data_base)
        elif num_menu == '3':
            path_file = view.second_menu('Выберите файл для импорта: ')
            if mod_imp.db_update(path_file):
                print('Файл успешно загружен')
            else:
                print(
                    'Во время загрузки произошла ошибка, проверьте путь к файлу и наличие файла в директориии')

        elif num_menu == '4':
            file_name = view.second_menu(
                'Выберите имя экспортируемого файла: ')
            mod_exp.unload_file(file_name, data_base)

        elif num_menu == '5':
            data_base = edit_db.add_cont(data_base, view.add_user())
            mod_exp.unload_file('database.csv', data_base)

        elif num_menu == '6':
            num_user = view.second_menu(
                'Введите строку удаляемого контакта: ')
            data_base = edit_db.del_cont(data_base, num_user)
            mod_exp.unload_file('database.csv', data_base)

        elif num_menu == '7':
            edit_user_db = []
            num_user = int(view.second_menu(
                'Введите строку редактируемого контакта: '))
            edit_user_db.append(data_base[num_user])
            view.show_str(edit_user_db)
            data_base = edit_db.edit_cont(data_base, view.add_user(), num_user)

            # data_base = edit_db.edit_cont(data_base, num_user)
            # mod_exp.unload_file('database.csv', data_base)

        elif num_menu == '8':
            SaveDataBase('databaseSave.csv', data_base)

