# Сохраняем файл в папке проекта
import csv

def unload_file(file_name, list_of_list):
    with open (file_name,'w',newline='', encoding='UTF-8') as data_base:
        writer =csv.writer(data_base, delimiter=';',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(list_of_list)
        # writer.writerows([['12','456'],['34'],['56']])
    print("Writing complete")

def second_menu(text):
    a = input(text)
    return(a)

# file_name = second_menu('Выберите имя экспортируемого файла: ')
# unload_file(file_name)
         
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)


# def unload_file(path: str):
#     with open(path, 'r', encoding='UTF8') as file:
#         data_base = []
#         base = []
#         for line in file:
#             if ';' in line:
#                 temp = line.strip().split(';')  
#                 data_base.append(temp)
#             elif line != '':
#                 if line != '\n':
#                     base.append(line.strip())
#                 else:
#                     data_base.append(t)
#                     t= []      
#     return data_base

