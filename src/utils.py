import json
from datetime import datetime

def data_load(file_path):
    """
    Функция, загружающая список json
    :return:данные для работы
    """

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def mask_kard(str_):
    """
    Функция, определяющая счет это или карта и выводящая результат с замаскированным номером
    :param str_: вход строки с номером
    :return: номер счета или карты
    """
    if str_ != None:
        str_list = str_.split(' ')
        numb = str_list[-1]
        if len(str_list) > 2:
            return f"{str_list[0]} {str_list[1]} {numb[:4]} {numb[4:6]}** **** {numb[-4:]}"
        else:
            if str_list[0] == 'Счет':
                return 'Счет ' + '**' + numb[-4:]
            return f"{str_list[0]} {numb[:4]} {numb[4:6]}** **** {numb[-4:]}"
    return "None"

def filter_sort(data):
    """
    Функция, которая отбирает последние 5 оперaций по дате со статусом EXECUTED
    :param data: список данных для сортировки
    :return: 5 последних операций
    """
    items = []
    for item in data:
        if item.get('state') == "EXECUTED":
            items.append(item)
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items[:5]


def form_date(data):
    """
    Функция, форматирующая дату
    :param data: Строка с датой
    :return: строка с нужным форматом
    """
    new_date = datetime.fromisoformat(data)
    formated_date = new_date.strftime('%d.%m.%Y')
    return formated_date

