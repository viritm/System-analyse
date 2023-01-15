from io import StringIO
import csv


def task(csvString):
    q = StringIO(csvString)
    result = []

    r1 = []     # Прямое управление
    r2 = []     # Прямое подчинение
    r3 = []     # Косвенное управление
    r4 = []     # Косвенное подчинение
    r5 = []     # Соподчинение

    with open(csvString, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            result.append(row)

    for el in result:
        for y in el:
            y = int(y)

    # Прямое управление
    for el in result:
        if el[0] not in r1:
            r1.append(str(el[0]))

    # Прямое подчинение
    for el in result:
        if el[1] not in r2:
            r2.append(str(el[1]))

    # Косвенное управление
    q = result
    w = result
    for i in range(len(q)):
        for j in range(len(result)):
            if i != j and q[i][0] not in r3 and q[i][1] == w[j][0]:
                r3.append(str(q[i][0]))

    # Косвенное подчинение
    for i in range(len(q)):
        for j in range(len(result)):
            if i != j and q[i][1] not in r4 and q[i][0] == w[j][1]:
                r4.append(str(q[i][1]))

    # Соподчинение
    for i in range(len(result)):
        for j in range(len(result)):
            if i != j and q[i][1] not in r5 and q[i][0] == w[j][0]:
                r5.append(str(q[i][1]))

    # Результат
    return [r1, r2, r3, r4, r5]


# print(task('file.csv'))
