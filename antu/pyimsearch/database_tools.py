import pandas as pd


def find_num(data, num):
    i, flag = 0, False
    while i < len(data):
        if data['No'][i] == str(num):
            flag = True
            break

        i += 1

    if flag:
        return i
    else:
        return -1


def load_database():
    return pd.read_csv('./antu/static/info.csv',encoding='gb2312')


def find_data_by_number(num):
    data = load_database()
    n = find_num(data, num)
    if n >= 0:

        return dict(data.iloc[n])
    else:
        return {'Discrip': 'NULL',
                'ImgLink': 'NULL',
                'Ingredients': 'NULL',
                'No': 'NULL',
                'Price': 'NULL',
                'ProLink': 'NULL',
                'RMB': 'NULL',
                'Review': 'NULL',
                'Title': 'NULL',
                'Titlezh':'NULL',
                'Discripzh':'NULL',
                'spec':'NULL',
                'Ingredientszh':'NULL'}
