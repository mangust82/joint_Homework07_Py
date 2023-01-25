import view
import model
import csv #( добавила импорт csv тк без него него не вызывается csv.writer 
# и вообще это моя unload_fileфункция)
def SaveDataBase(name_data_base, data_base):
    field_names = ['Фамилия', 'Имя', 'Телефон', 'Комментарий']
    addList =[]
    for dataUser in data_base:
        addList.append(dataUser)
    with open(name_data_base, 'w', newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(
            csvfile, fieldnames=field_names, quoting=csv.QUOTE_ALL, delimiter=';')
        for i in addList:
            writer.writerows(i)


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
            path_file = view.second_menu('Выберите файл для импорта: ')
            if model.db_merge(path_file):
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
            num_user = int(view.second_menu(
                'Введите строку удаляемого контакта: '))
            data_base = model.del_cont(data_base, num_user)
            model.unload_file('database.csv', data_base)

        elif num_menu == '7':
            edit_user_db = []
            num_user = int(view.second_menu(
                'Введите строку редактируемого контакта: '))
            edit_user_db.append(data_base[num_user-1])
            view.show_str(edit_user_db)
            data_base = model.edit_cont(data_base, view.add_user(), num_user-1)
            model.unload_file('database.csv', data_base)
            # data_base = edit_db.edit_cont(data_base, num_user)
            # mod_exp.unload_file('database.csv', data_base)

        elif num_menu == '8':
            model.unload_file('databaseSave.csv', data_base)
# поставила свою функию сюда вместо SaveDataBase и вроде работает, 

