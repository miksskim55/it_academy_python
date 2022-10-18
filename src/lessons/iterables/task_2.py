import csv
def read_input():
    input_string = input('Введите автора и дополнительный параметр: ')
    return input_string.split(' ', 1)

def read_file(library, novel_author):
    library = []
    with open('library.csv') as f:
        csvfile = csv.DictReader(f, delimiter=' ', quotechar='|', fieldnames=['name', 'novel', 'year', 'topic'])
        for row in csvfile:
            names = row.get('name').split(',')
            if row['name'].split(',')[0] == novel_author:
                library.append(row)
    return library

def main():
    novel_author, add_param = read_input()
    library = read_file('library.csv', novel_author)

    if add_param == 'first':
        first = min(library, key=lambda row: row['year'])
        print(', '.join( i for i in first.values()))
    elif add_param == 'last':
        last = max(library, key=lambda row: row['year'])
        print(', '.join( i for i in last.values()))
    elif next((x for x in library if x['year'] in add_param), None):
        year = next((x for x in library if x['year'] in add_param), None)
        print(', '.join(i for i in year.values()))
    elif next((x for x in library if x['novel'] in add_param), None):
        dict_library = {}
        for i in library:
            dict_library.update(i)
            if add_param in dict_library.get('novel'):
                print(', '.join(i for i in dict_library.values()))
    else:
        print('Такого писателя нет в библиотеке, или проверьте корректность введенных данных.')
if __name__ == '__main__':
    main()
