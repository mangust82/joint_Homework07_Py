# Загрузка прошла успешно True неуспешно False
import csv 
import mod_exp



# def load_file(path_file):
#      new_db = []
#      with open(f'{path_file}', 'r', encoding='UTF-8')as File:
#         reader = csv.DictReader(File)
#         for row in reader:
#             new_db.append(row)
#         # print(new_db)
        
# path_file = second_menu('Выберите файл для импорта: ')
# if load_file(path_file):
#     print('Файл успешно загружен')
# else:
#     print('Ошибка')
   
def load_file(path_file):
    new_db = []
    with open(f'{path_file}', 'r', encoding='UTF-8') as File:
        reader = csv.reader(File, delimiter=';', quotechar=',',  quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            new_db.append(row)
    # print(*new_db, sep ='\n') 
    return True, new_db 

def db_update(path_file):
    status1, new_db = load_file(path_file)
    status2, db = load_file('database.csv')
    db.extend(new_db)
    mod_exp.unload_file('database.csv',db)
    return status1==True and status2==True
     


if __name__ =='__main__':  
    # path_file = second_menu('Выберите файл для импорта: ')
    load_file(path_file)
    db_update(path_file)

# _,db = load_file('database.csv')
# print(db) 
# db.extend(new_db)

# mod_exp.unload_file('database.csv',db)
