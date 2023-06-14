from utils import data_load, mask_kard, filter_sort, form_date


def main():
    data = data_load()
    sorted_operations = filter_sort(data)
    for operation in sorted_operations:
        new_date = form_date(sorted_operations)
        from_who = mask_kard(operation.get('from'))
        print(operation)

    print(f'{new_date} {operation["description"]}')
    print(f'{from_who}')

main()