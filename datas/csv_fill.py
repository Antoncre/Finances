import string
import random
from datetime import date, timedelta, datetime

# This function is to randomly fill date, price and description in Finances application (also available on my GitHub)


def fill_csv(line_num: int, filename: str):
    for el in range(line_num):
        with open(filename, 'a', encoding='UTF-8') as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d')},{random.randint(-250, 10000)},{''.join(random.choice(string.ascii_letters) for _ in range(random.randint(3, 25)))}\n")


fill_csv(450, 'Transactions.csv')
