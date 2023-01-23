
def init(path_file: str) -> list:
    with open(path_file, 'r', encoding = 'UTF-8') as database:
        temp_list = database.read().split('\n')
    list_of_dict = []
    for item in temp_list:
        temp = item.split(';')
        list_of_dict.append({'Фамилия': temp[0], 'Имя': temp[1],'Телефон': temp[2], 'Комментарий': temp[3]})
    return list_of_dict