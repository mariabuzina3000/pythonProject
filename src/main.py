from utils import data_load, mask_kard, filter_sort, form_date

file_path = '../data.json'
def main():
    data = data_load(file_path)
    sorted_operations = filter_sort(data)
    for operation in sorted_operations:
        operation['date'] = form_date(operation['date'])
        from_who = mask_kard(operation.get('from'))
        to_who = mask_kard(operation.get('to'))


        print(f'{operation["date"]} {operation["description"]}')
        print(f'{from_who} -> {to_who}')
        print(f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')

main()