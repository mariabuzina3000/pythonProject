from src.utils import data_load, mask_kard, filter_sort, form_date
def test_data_load():
    text_test = [{"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
  {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
  {"state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
  {"state": "EXECUTED", "date": "2018-03-23T10:45:06.972075"},
  {"state": "EXECUTED", "date": "2019-04-04T23:20:05.206878"}]

    assert data_load('data_test.json') == text_test


def test_mask_kard():
    assert mask_kard("Maestro 1596837868705199") == 'Maestro 1596 83** **** 5199'
    assert mask_kard("Счет 64686473678894779589") == 'Счет **9589'
    assert mask_kard(None) == 'None'


def test_filter_sort():
    list = [{"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
  {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
  {"state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
  {"date": "2018-03-23T10:45:06.972075"},
  {"state": "EXECUTED", "date": "2019-04-04T23:20:05.206878"}]

    assert filter_sort(list) == [{"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
  {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
  {"state": "EXECUTED", "date": "2019-04-04T23:20:05.206878"},
  {"state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]


def test_form_date():
    list_test = "2019-08-26T10:50:58.294041"

    assert form_date(list_test) == '26.08.2019'

