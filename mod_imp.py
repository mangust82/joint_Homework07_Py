# Загрузка прошла успешно True неуспешно False


import csv
import mod_exp


def load_file(path_file):
    new_db = []
    with open(f'{path_file}', 'r', encoding='UTF-8') as File:
        reader = csv.reader(File, delimiter=';',
                            quotechar=',',  quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            new_db.append(row)
    print(*new_db, sep='\n')
    return True, new_db


def db_update(path_file):
    status1, new_db = load_file(path_file)
    status2, db = load_file('database.csv')
    db.extend(new_db)
    mod_exp.unload_file('database.csv', db)
    return status1 == True and status2 == True
