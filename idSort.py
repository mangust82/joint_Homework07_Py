import view
def sortUserId(data_base):
    data_base = sorted(data_base)
    view.show_database(data_base)
    return data_base