"""
zapisuje informacje w pliku csv w formacie:
[data, wartość, opis]
"""
from datetime import datetime
from operator import itemgetter

T = 'Transactions.csv'
now = datetime.now()


def new(p, ds, d=now.strftime('%Y-%m-%d')):
    with open(T, 'a') as file:
        file.write(f"{d},{p},{ds}\n")


def listing():
    with open(T, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
        return [
            {'date': line[0], 'price': float(line[1]), 'description': line[2]}
            for line in lines
        ]


def chck_to_delete(v, typ):
    with open(T, 'r') as file:
        lstt = []
        lines = [line.strip().split(',') for line in file.readlines()]
        for line in lines:
            if line[typ] != str(v):
                pass
            else:
                lstt.append(1)
        if len(lstt) == 0:
            return "nothing"
        elif len(lstt) == 1:
            return 'delete'
        else:
            pass


def one_r_del(da):
    with open(T, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    with open(T, 'w') as file:
        for line in lines:
            if line[0] != da:
                file.write(f"{line[0]},{line[1]},{line[2]}\n")
            else:
                print(f'{line} deleted')


def two_r_del(da, pr):
    with open(T, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    with open(T, 'w') as file:
        for line in lines:
            if line[0] != da or float(line[1]) != pr:
                file.write(f"{line[0]},{line[1]},{line[2]}\n")
            else:
                print(f'{line} deleted')


def delete(da, de, pr):
    with open(T, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    with open(T, 'w') as file:
        for line in lines:
            if line[0] != da or float(line[1]) != pr or line[2] != de:
                file.write(f"{line[0]},{line[1]},{line[2]}\n")
            else:
                print(f'{line} deleted')


def del_all():
    with open(T, 'w'):
        pass


def sort(r):
    """this is supposed to execute save all y,m,d one by one"""
    sortered = sorting(r)
    with open(T, 'w') as file:
        for e in sortered:
            file.write(f"{e['date']},{e['price']},{e['description']}\n")


def sorting(al):
    al.sort(key=itemgetter('date'))
    return al
