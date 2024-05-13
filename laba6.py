import csv
import random
import os


def sep_string(s, sep):
    l = ''
    for i in s:
        l += i + ' ' + sep + ' '
    return l

def Show():
    print("Enter param: top - 1, bottom - 2, random - 3")
    p = 0
    while p < 1 or p > 3:
        p = int(input())
        if p < 1 or p > 3:
            print ("Error. Enter 1, 2 or 3")

    print("Enter number: ")
    q = 0
    while q < 1:
        q = input()
        if q == '':
            q = 5
            break
        q = int(q)
        if q < 1:
            print("Error. Enter positive number")

    print("Enter separator: ")
    sep = ''
    sep = input()
    if sep == '':
        sep = ','



    with open("Titanic.csv", 'r', newline='') as f:  # сам открывает и закрывает
        reader = csv.reader(f)
        s = [row for row in reader]

# для рандомных строчек
        if p == 3:
            count = 0
            index = []
            while count < q:
                a = random.randint(1, len(s)-1)
                if a in index:
                    continue
                else:
                    index.append(a)
                    count += 1

        i = 0
        for row in s: #каждая строка
            if i == 0:
                print(sep_string(row, sep))
                i+= 1
                continue

            if p == 1:
                if i <= q:
                    print(sep_string(row, sep))

            if p == 2:
                if i >= len(s) - q:
                    print(sep_string(row, sep))

            if p == 3:
                for k in index:
                    if k == i:
                        print(sep_string(row, sep))

            i += 1
        if len(s) < q:
            print("Строк недостаточно")

def Info():
    with open("Titanic.csv", 'r', newline='') as f:
        reader = csv.reader(f)
        s = [row for row in reader]
        print(len(s) - 1, 'x', len(s[0]))

        a = [0]*12

        for i in range(len(a)):
            if i == 0 or i == 1 or i == 2 or i == 5 or i == 6 or i == 7:
                a[i] = 'int'
            if i == 3 or i == 4 or i == 8 or i == 10 or i == 11:
                a[i] = 'str'
            if i == 9:
                a[i] = 'float'

        for i in range(len(s[0])):
            counter = 0

            for j in s:
                if j == s[0]:
                    continue
                if j[i] !='':
                    counter += 1

            print(s[0][i], counter, a[i])

def DelNan():
    with open("Titanic.csv", 'r', newline='') as f:
        reader = csv.reader(f)
        s = [row for row in reader]

        del_str = []

        for i in range(1, len(s)):
            for t in range(len(s[i])):
                if s[i][t] == '':
                    del_str.append(i)
                    break

        print(len(s))

        for i in range(len(del_str) -1, -1, -1):
            s.pop(del_str[i])
        print(len(s))

        with open('some.csv', 'w', newline='') as f1:
            writer = csv.writer(f1)
            writer.writerows(s)

def MakeDs():
    with open("Titanic.csv", 'r', newline='') as f:  # сам открывает и закрывает
        reader = csv.reader(f)
        s = [row for row in reader]
        c_test = int(len(s) * 0.3)
        c_train = len(s) - c_test

        count = 0
        index_test = []
        index_train = []

        while count < c_test:
            a = random.randint(1, len(s) - 1)
            if a in index_test:
                continue
            else:
                index_test.append(a)
                count += 1

        for i in range(len(s)):
            if i in index_test:
                continue
            else:
                index_train.append(i)

        w_test = []
        w_train = []

        for i in range(len(s)):
            if i in index_train:
                w_train.append(s[i])
            else:
                w_test.append(s[i])

        os.mkdir('workdata')

        with open('workdata/test.csv', 'w', newline='') as f1:
            writer = csv.writer(f1)
            writer.writerows(w_test)

        with open('workdata/train.csv', 'w', newline='') as f1:
            writer = csv.writer(f1)
            writer.writerows(w_train)


MakeDs()
DelNan()
Info()
Show()