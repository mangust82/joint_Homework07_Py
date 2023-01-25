import view
import model
import idSort


path = 'database.csv'


def ClickButton():
    data_base = model.load_file(path)[1]
    while True:
        num_menu = view.main_menu()
        if num_menu == '':
            print('Exit')
            break
        elif num_menu == '1':
            view.show_database(data_base)
        elif num_menu == '2':
            find_str = view.second_menu('Введите строку поиска: ')
            model.find_cont(find_str, data_base)
        elif num_menu == '3':
            path_file = view.second_menu(
                'Выберите файл для импорта в формате (.\databig.csv или .\datasmall.csv data.txt) : ')
            status, data_base = model.ChangeBase(path_file, data_base)
            if status:
                print('Файл успешно загружен')
            else:
                print(
                    'Во время загрузки произошла ошибка, проверьте путь к файлу и наличие файла в директориии')

        elif num_menu == '4':
            file_name = view.second_menu(
                'Выберите имя экспортируемого файла: ')
            model.unload_file(file_name, data_base)

        elif num_menu == '5':
            data_base = model.add_cont(data_base, view.add_user())
            model.unload_file('database.csv', data_base)

        elif num_menu == '6':
            num_user = view.inputNumber(
                f'Введите строку удаляемого контакта от 1 до {len(data_base)}:', len(data_base))
            model.del_cont(data_base, num_user)
            model.unload_file('database.csv', data_base)

        elif num_menu == '7':
            data_base = idSort.sortUserId(data_base)

        elif num_menu == '8':
            edit_user_db = []
            num_user = view.inputNumber(
                f'Введите строку редактируемого контакта от 1 до {len(data_base)}:', len(data_base))
            edit_user_db.append(data_base[num_user-1])
            view.show_str(edit_user_db)
            data_base = model.edit_cont(
                data_base, view.add_user(), num_user-1)
            model.unload_file('database.csv', data_base)
