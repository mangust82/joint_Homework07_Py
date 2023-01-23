import init
import view
import find
import mod_imp
import mod_exp
import edit_db

def quit():
    input('Нажмите клавишу для выхода в главное меню: ')


path = 'database.csv'
def ClickButton():
    data_base = init.init(path)
    while True:
        num_menu = view.main_menu()
        if num_menu == 1:
            view.show_database(data_base)
            quit()
        elif num_menu == 2:
            find_str = view.second_menu('Введите строку поиска: ')
            find.filter(find_str, data_base)
            view.show_database(data_base)
            quit()
        elif num_menu == 3:
            path_file = view.second_menu('Выберите файл для импорта: ')
            if mod_imp.db_update(path_file):
                print('Ok')
            else:
                print('Not Ok')
            quit()
        elif num_menu == 4:
            file_name = view.second_menu('Выберите имя экспортируемого файла: ')
            mod_exp.unload_file(file_name)
            quit()
        elif num_menu == 5:
            data_base = edit_db.edit_db(data_base, view.add_user())
            quit()
        elif num_menu == 6:
            num_user = view.second_menu('Введите строку удаляемого контакта: ')
            data_base = edit_db.del_cont(data_base, num_user)
            quit()
        elif num_menu == 7:
            num_user = view.second_menu('Введите строку редактируемого контакта: ')
            data_base = edit_db.edit_cont(data_base, num_user)
            quit()
        elif num_menu == 8:
            exit()
        # else:
        #     quit()

    

        



# def add_contact():
#     pass



