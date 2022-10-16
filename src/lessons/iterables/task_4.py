comands = input('Введите название 16-ти команд: ')
results_matchs = input('Введите результаты 29 игр: ')
l_comands = comands.split(' ')
l_results_matchs = results_matchs.split(' ')
vin_one = []
vin_two = []
point_first = 0
point_second = 0

for first, last in zip(l_comands[0:8], l_comands[15:6:-1]):
    x = [int(i) for i, in l_results_matchs[0].split(':')]
    if len(x) == 2:
        point_first += x[0]
        point_second += x[1]
        x = [int(i) for i, in l_results_matchs[0].split(':')]
        if len(x) == 2:
            point_first += x[0]
            point_second += x[1]
        l_results_matchs.pop(0)
    l_results_matchs.pop(0)
    if point_first > point_second:
        vin_one.append(first)
    else:
        vin_one.append(last)
    point_first = 0
    point_second = 0
for first, last in zip(vin_one[0:4], vin_one[7:3:-1]):
    x = [int(i) for i in l_results_matchs[0].split(':')]
    if len(x) == 2:
        point_first += x[0]
        point_second += x[1]
        x = [int(i) for i, in l_results_matchs[0].split(':')]
        if len(x) == 2:
            point_first += x[0]
            point_second += x[1]
        l_results_matchs.pop(0)
    l_results_matchs.pop(0)
    if point_first > point_second:
        vin_two.append(first)
    else:
        vin_two.append(last)
    point_first = 0
    point_second = 0
vin_one.clear()
for first, second in zip(vin_two[0:3:2], vin_two[1:4:2]):
    x = [int(i) for i in l_results_matchs[0].split(':')]
    if len(x) == 2:
        point_first += x[0]
        point_second += x[1]
        x = [int(i) for i, in l_results_matchs[0].split(':')]
        if len(x) == 2:
            point_first += x[0]
            point_second += x[1]
        l_results_matchs.pop(0)
    l_results_matchs.pop(0)
    if point_first > point_second:
        vin_one.append(first)
    else:
        vin_one.append(second)
    point_first = 0
    point_second = 0
vin_two.clear()
for first, second in zip(vin_one[0:1], vin_one[1:2]):
    x = [int(i) for i in l_results_matchs[0].split(':')]
    if x[0] > x[1]:
        print(first)
    else:
        print(second)
