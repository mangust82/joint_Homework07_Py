
# возвращаем вырезку из базы
def find_cont(find_str: str, data_base: list) -> list:
    find_data = []
    for item in data_base:
        if find_str.lower() in ' '.join(item.values()).lower():
            find_data.append(item)
    for item in find_data:
        i = data_base.index(item)
        item = list(item.values())
        print(f'{i:4} | {item[0]:13} | {item[1]:10} | {item[2]:12} | {item[3]}')  
    

