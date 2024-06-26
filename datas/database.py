"""
saving info in csv file as lists in format:
[date, price, description]
"""
import os
from datetime import datetime
from operator import itemgetter

T = "datas\\Transactions.csv"
C = "datas\\categories.csv"
naive_now = datetime.now()


def new(p, ds, d=naive_now.strftime('%Y-%m-%d')):
    with open(T, 'a', encoding='UTF-8') as file:
        file.write(f"{d},{p},{ds}\n")


def update_from_server():
    # check for differences
    # and download if present
    pass


def upload_to_server():
    # check for differences
    # and upload if present
    pass


def listing(a=T):
    if a != '':
        with open(a, 'r', encoding='UTF-8') as file:
            lines = [line.strip().split(',') for line in file.readlines()]
            if lines != [''] or lines != ['\n']:
                return [
                    {'date': line[0], 'price': float(line[1]), 'description': line[2]}
                    for line in lines
                ]
            else:
                return ""


def delete(da, de, pr):
    with open(T, 'r', encoding='UTF-8') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    with open(T, 'w', encoding='UTF-8') as file:
        for line in lines:
            if line[0] != da or float(line[1]) != pr or line[2] != de:
                file.write(f"{line[0]},{line[1]},{line[2]}\n")
            else:
                pass


def del_all():
    with open(T, 'w', encoding='UTF-8'):
        pass


def ch_categories() -> list:
    with open(C, 'r', encoding='UTF-8') as file:
        categories = file.read().strip().split(',')
        if categories == ['']:
            pass
        else:
            for e in categories:
                try:
                    open(f'datas\\{e}.csv', 'x', encoding='UTF-8')
                except FileExistsError:
                    pass
    return categories


def del_from_category(c, e):
    if c != '' and e != '':
        with open(f'datas\\{c}.csv', 'r', encoding='UTF-8') as file:
            lines = file.readlines()
        with open(f'datas\\{c}.csv', 'w', encoding='UTF-8') as file:
            for line in lines:
                element = line.strip().split(',')
                if element[0] != e['date'] or element[1] != str(e['price']) or element[2] != e['description']:
                    file.write(f"{line}")


def new_category(c):
    x = 0
    for e in ch_categories():
        if c == e:
            x = 1
    if x == 0:
        if ch_categories() == ['']:
            with open(C, 'a', encoding='UTF-8') as file:
                file.write(f'{c}')
        else:
            with open(C, 'a', encoding='UTF-8') as file:
                file.write(f',{c}')
    ch_categories()


def add_to_category(c, e):
    v = 0
    if c != '' and e != '':
        for el in listing(f'datas\\{c}.csv'):
            if el['date'] == e['date'] and el['price'] == e['price'] and el['description'] == e['description']:
                v += 1
            else:
                pass
        if v == 0:
            with open(f'datas\\{c}.csv', 'a', encoding='UTF-8') as file:
                file.write(f"{e['date']},{e['price']},{e['description']}\n")


def del_category(c):
    b = 0
    lit = ch_categories()
    open(C, 'w', encoding='UTF-8')
    for e in lit:
        if e == c:
            pass
        else:
            with open(C, 'a', encoding='UTF-8') as file:
                if b == 0:
                    file.write(f'{e}')
                else:
                    file.write(f',{e}')
                b += 1

    try:
        os.remove(f'datas\\{c}.csv')
    except FileNotFoundError:
        pass


def sort(r, tye):
    """this is supposed to execute save all y,m,d one by one"""
    sortered = sorting(r, tye)
    with open(T, 'w', encoding='UTF-8') as file:
        for e in sortered:
            file.write(f"{e['date']},{e['price']},{e['description']}\n")


def sorting(al, tye):
    al.sort(key=itemgetter(tye))
    return al
