name, add_param = input('Введите автора и дополнительный параметр: ').split(' ', 1)
min_or_max = {}
names_for_not = []
novels_for_not = []
years_for_not = []
ss = []
import csv

with open('library.csv') as f:
    csvfile = csv.DictReader(f, delimiter=' ', quotechar='|', fieldnames=['names', 'novels', 'years', 'topics'])
    for row in csvfile:
        names = row.get('names').split(',')
        names_for_not.append(names[0])
        novels_for_not.append(row.get('novels'))
        years_for_not.append(row.get('years'))
        if name in names[0] and add_param in row.get('years'):
            print(row.get('names'), row.setdefault('novels'), row.get('years'))
        if name in names[0] and add_param in row.get('novels'):
            print(row.get('names'), row.get('novels'), row.get('years'))
        if name in names[0]:
            min_or_max[row.get('years')] = row.get('novels')
            if add_param == 'first':
                print(row.get('names'), row.get('novels'), min(min_or_max.keys()))
            elif add_param == 'last':
                print(row.get('names'), row.get('novels'), max(min_or_max.keys()))
if name not in names_for_not or add_param not in novels_for_not and add_param not in years_for_not and add_param not in {'first', 'last'}:
    print('Такого писателя нет в библиотеке, или проверьте корректность введенных данных.')