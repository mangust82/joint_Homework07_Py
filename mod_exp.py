# Сохраняем файл в папке проекта

import csv


def unload_file(file_name, list_of_list):
    with open(file_name, 'w', newline='', encoding='UTF-8') as data_base:
        writer = csv.writer(data_base, delimiter=';',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(list_of_list)
    print("Writing complete")


def second_menu(text):
    a = input(text)
    return (a)
