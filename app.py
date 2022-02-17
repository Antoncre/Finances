"""
Dzięki tej aplikacji użytkownicy mogą dodawać
swoje wydatki i dochody oraz wyświetlać je w wygodny,
posortowany według daty sposób
"""

import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import datas.database, datas.lang_help


MONTHS = {
        "01": "January:",
        "02": "February:",
        "03": "March:",
        "04": "April:",
        "05": "May:",
        "06": "June:",
        "07": "July:",
        "08": "August:",
        "09": "September:",
        "10": "October:",
        "11": "November:",
        "12": "December:"
        }

language = 'pl'
now = datetime.now()
view = 0
price = ''
date = ''
description = ''
can_do = 1
with_dates = 1
deleting_item = 0
h_info = 0
h_to_use = 0


def en():
    global language, MONTHS
    language = 'en'
    cancel_func()
    MONTHS = {
        "01": "January:",
        "02": "February:",
        "03": "March:",
        "04": "April:",
        "05": "May:",
        "06": "June:",
        "07": "July:",
        "08": "August:",
        "09": "September:",
        "10": "October:",
        "11": "November:",
        "12": "December:"
        }
    root.title('Finances app')
    button.config(text='Apply')
    cancel.config(text='Cancel')
    el_view_menu.entryconfig(0, label='Dated')
    el_view_menu.entryconfig(1, label="Anton's Arrange")
    help_menu.entryconfig(0, label='About App')
    help_menu.entryconfig(1, label='How To Use')
    delete_menu.entryconfig(0, label='Delete Items')
    delete_menu.entryconfig(1, label='Delete All ❗❗❗')
    if with_dates and not h_info and not h_to_use:
        dates()
    elif not with_dates and not h_info and not h_to_use:
        lc()
    elif h_info:
        help_info()
    elif h_to_use:
        help_usage()
    else:
        dates()


def ua():
    global language, MONTHS
    language = 'ua'
    cancel_func()
    MONTHS = {
        "01": "Січень:",
        "02": "Лютий:",
        "03": "Березень:",
        "04": "Квітень:",
        "05": "Травень:",
        "06": "Червень:",
        "07": "Липень:",
        "08": "Серпень:",
        "09": "Вересень:",
        "10": "Жовтень:",
        "11": "Листопад:",
        "12": "Грудень:"
    }
    root.title('Фінансова програма')
    button.config(text='Підтвердити')
    cancel.config(text='Відмінити')
    el_view_menu.entryconfig(0, label='Датовано')
    el_view_menu.entryconfig(1, label='Структура Антона')
    help_menu.entryconfig(0, label='Про Программу')
    help_menu.entryconfig(1, label='Користування')
    delete_menu.entryconfig(0, label='Видалити Елементи')
    delete_menu.entryconfig(1, label='Видалити Все ❗❗❗')
    if with_dates and not h_info and not h_to_use:
        dates()
    elif not with_dates and not h_info and not h_to_use:
        lc()
    elif h_info:
        help_info()
    elif h_to_use:
        help_usage()
    else:
        dates()


def pl():
    global language, MONTHS
    language = 'pl'
    cancel_func()
    MONTHS = {
        "01": "Styczeń:",
        "02": "Luty:",
        "03": "Marzec:",
        "04": "Kwiecień:",
        "05": "Maj:",
        "06": "Czerwiec:",
        "07": "Lipiec:",
        "08": "Sierpień:",
        "09": "Wrzesień:",
        "10": "Październik:",
        "11": "Listopad:",
        "12": "Grudzień:"
    }
    root.title('Aplikacja finansowa')
    button.config(text='Potwierdź')
    cancel.config(text='Anuluj')
    el_view_menu.entryconfig(0, label='Według Daty')
    el_view_menu.entryconfig(1, label='Układ Antona')
    help_menu.entryconfig(0, label='O Aplikacji')
    help_menu.entryconfig(1, label='Korzystanie')
    delete_menu.entryconfig(0, label='Usuń elementy')
    delete_menu.entryconfig(1, label='Usuń wszystko ❗❗❗')
    if with_dates and not h_info and not h_to_use:
        dates()
    elif not with_dates and not h_info and not h_to_use:
        lc()
    elif h_info:
        help_info()
    elif h_to_use:
        help_usage()
    else:
        dates()


def add():
    a = []
    for el in datas.database.listing():
        a.append(el['price'])
    return "%.2f" % sum(a)


def srt():
    r = datas.database.listing()
    datas.database.sort(r)


def os():
    srt()
    display_text.configure(state='normal')
    display_text.delete('1.0', tk.END)
    display_text.tag_config('minus', foreground='#F15C20')
    display_text.tag_config('plus', foreground='#57D233')
    display_text.tag_config('m', foreground='magenta')
    display_text.tag_config('p', foreground='purple')
    display_text.tag_config('o', foreground='#C0682D')
    display_text.tag_config('g', foreground='#569421')
    display_text.tag_config('y', foreground='#DED866')
    display_text.tag_config('h', foreground='#A0FFF1', font=('Bookman Old Style', '15', 'italic'))
    display_text.tag_config('hu', foreground='#95E4A1', font=('Sans', '13'))


def dates():
    global with_dates, h_info, h_to_use
    os()
    with_dates = 1
    h_to_use = 0
    h_info = 0
    for exp in datas.database.listing():
        f_2f = "%.2f" % exp['price']
        to_print_price = "%-9s" % f_2f
        to_print_date = "%-10s" % exp['date']
        if float(f_2f) < 0:
            display_text.insert(tkinter.END, f"{to_print_date}  {to_print_price}  {exp['description']}\n", 'minus')
        else:
            display_text.insert(tkinter.END, f"{to_print_date}   {to_print_price} {exp['description']}\n", 'plus')
    if language == 'en':
        display_text.insert(tkinter.END, f"\nTotal: {add()}")
    elif language == 'pl':
        display_text.insert(tkinter.END, f"\nŁącznie: {add()}")
    elif language == 'ua':
        display_text.insert(tkinter.END, f"\nЗагалом: {add()}")
    else:
        display_text.insert(tkinter.END, f"\nTotal: {add()}")
    display_text.see(tkinter.END)
    display_text.configure(state='disabled')


def lc():
    global with_dates, language, h_info, h_to_use
    os()
    with_dates = 0
    h_to_use = 0
    h_info = 0
    current_year = ""
    current_month = ""
    price_month_sum = []
    price_year_sum = []
    exp_month_sum = []
    exp_year_sum = []
    inc_month_sum = []
    inc_year_sum = []
    summ_to_print = "%.2f" % sum(price_month_sum)
    totm_wyd = "%.2f" % sum(exp_month_sum)
    totm_do = "%.2f" % sum(inc_month_sum)
    wp = 0
    start_func = 1
    for exp in datas.database.listing():
        if start_func:
            display_text.insert(tkinter.END, f"{exp['date'].split('-')[0]}:\n")
            start_func = 0
        f_2f = "%.2f" % exp['price']
        to_print_price = "%-9s" % f_2f
        sumy_to_print = "%.2f" % sum(price_year_sum)
        toty_wyd = "%.2f" % sum(exp_year_sum)
        toty_do = "%.2f" % sum(inc_year_sum)
        year = exp['date'].split('-')[0]
        month = exp['date'].split('-')[1]
        if month != current_month and wp != 0 or year != current_year and wp != 0:
            if language == 'en':
                display_text.insert(tkinter.END, f"\nMonthly expenses: {totm_wyd} zł\n", 'o')
                display_text.insert(tkinter.END, f"Monthly income: {totm_do} zł\n", 'g')
                display_text.insert(tkinter.END, f"\nMonthly: {summ_to_print} zł\n", 'y')
            elif language == 'ua':
                display_text.insert(tkinter.END, f"\nВитрати за місяць: {totm_wyd} zł\n", 'o')
                display_text.insert(tkinter.END, f"Прибуток за місяць: {totm_do} zł\n", 'g')
                display_text.insert(tkinter.END, f"\nЦього місяця загалом: {summ_to_print} zł\n", 'y')
            elif language == 'pl':
                display_text.insert(tkinter.END, f"\nMiesięczne wydatki: {totm_wyd} zł\n", 'o')
                display_text.insert(tkinter.END, f"Miesięczne dochody: {totm_do} zł\n", 'g')
                display_text.insert(tkinter.END, f"\nMiesięcznie: {summ_to_print} zł\n", 'y')
            else:
                display_text.insert(tkinter.END, f"\nMonthly expenses: {totm_wyd} zł\n", 'o')
                display_text.insert(tkinter.END, f"Monthly income: {totm_do} zł\n", 'g')
                display_text.insert(tkinter.END, f"\nMonthly: {summ_to_print} zł\n", 'y')
            price_month_sum = []
            exp_month_sum = []
            inc_month_sum = []
        if year != current_year and wp != 0:
            if language == 'pl':
                display_text.insert(tkinter.END, f"\nRoczne wydatki: {toty_wyd} zł\n")
                display_text.insert(tkinter.END, f"Roczne Dochody: {toty_do} zł\n")
                display_text.insert(tkinter.END, f"\nRocznie: {sumy_to_print} zł\n")
            elif language == 'ua':
                display_text.insert(tkinter.END, f"\nВитрати за рік: {toty_wyd} zł\n")
                display_text.insert(tkinter.END, f"Прибуток за рік: {toty_do} zł\n")
                display_text.insert(tkinter.END, f"\nЦього року загалом: {sumy_to_print} zł\n")
            elif language == 'en':
                display_text.insert(tkinter.END, f"\nAnnual expenses: {toty_wyd} zł\n")
                display_text.insert(tkinter.END, f"Annual income: {toty_do} zł\n")
                display_text.insert(tkinter.END, f"\nAnnually: {sumy_to_print} zł\n")
            else:
                display_text.insert(tkinter.END, f"\nAnnual expenses: {toty_wyd} zł\n")
                display_text.insert(tkinter.END, f"Annual income: {toty_do} zł\n")
                display_text.insert(tkinter.END, f"\nAnnually: {sumy_to_print} zł\n")
            price_year_sum = []
            exp_year_sum = []
            inc_year_sum = []
            display_text.insert(tkinter.END, f"\n{year}:\n")
        if month != current_month or year != current_year:
            if month in MONTHS:
                display_text.insert(tkinter.END, f"\n{MONTHS[month]}\n")
            else:
                display_text.insert(tkinter.END, f"\n{month}:\n")
            current_month = month
            current_year = year
            wp = 1
        if float(f_2f) >= 0:
            display_text.insert(tkinter.END, f" {to_print_price} {exp['description']}\n", 'plus')
            inc_month_sum.append(exp['price'])
            inc_year_sum.append(exp['price'])
        else:
            display_text.insert(tkinter.END, f"{to_print_price}  {exp['description']}\n", 'minus')
            exp_month_sum.append(exp['price'])
            exp_year_sum.append(exp['price'])
        price_month_sum.append(exp['price'])
        price_year_sum.append(exp['price'])
        summ_to_print = "%.2f" % sum(price_month_sum)
        totm_wyd = "%.2f" % sum(exp_month_sum)
        totm_do = "%.2f" % sum(inc_month_sum)
    if language == 'pl':
        display_text.insert(tkinter.END, f"\nMiesięczne wydatki: {totm_wyd} zł\n", 'o')
        display_text.insert(tkinter.END, f"Miesięczne dochody: {totm_do} zł\n", 'g')
        display_text.insert(tkinter.END, f"\nMiesięcznie: {summ_to_print} zł\n", 'y')
        display_text.insert(tkinter.END, f"\nŁącznie całość: {add()}", 'm')
    elif language == 'ua':
        display_text.insert(tkinter.END, f"\nВитрати за місяць: {totm_wyd} zł\n", 'o')
        display_text.insert(tkinter.END, f"Прибуток за місяць: {totm_do} zł\n", 'g')
        display_text.insert(tkinter.END, f"\nЦього місяця загалом: {summ_to_print} zł\n", 'y')
        display_text.insert(tkinter.END, f"\nЗагалом: {add()}", 'm')
    elif language == 'en':
        display_text.insert(tkinter.END, f"\nMonthly expenses: {totm_wyd} zł\n", 'o')
        display_text.insert(tkinter.END, f"Monthly income: {totm_do} zł\n", 'g')
        display_text.insert(tkinter.END, f"\nMonthly: {summ_to_print} zł\n", 'y')
        display_text.insert(tkinter.END, f"\nTotal: {add()}", 'm')
    display_text.see(tkinter.END)
    display_text.configure(state='disabled')


def check_for_changes():
    content = input_text.get('1.0', 'end-1c')

    if not content and (what_to_do_text.get('1.0', 'end-1c') == 'Insert price here:' or
                        what_to_do_text.get('1.0', 'end-1c') == 'Wprowadź kwotę:' or
                        what_to_do_text.get('1.0', 'end-1c') == 'Введіть суму:'):
        butt_stable.configure(state='disabled')
        root.bind('<Return>', lambda event: empty_function())

    elif content and (what_to_do_text.get('1.0', 'end-1c') == 'Insert price here:' or
                      what_to_do_text.get('1.0', 'end-1c') == 'Wprowadź kwotę:' or
                      what_to_do_text.get('1.0', 'end-1c') == 'Введіть суму:'):
        try:
            float(content)
            butt_stable.configure(state='normal')
            root.bind('<Return>', lambda event: enter())
        except ValueError:
            butt_stable.configure(state='disabled')
            root.bind('<Return>', lambda event: empty_function())
            try:
                float(f"{content.split(',')[0]}.{content.split(',')[1]}")
                butt_stable.configure(state='normal')
                root.bind('<Return>', lambda event: enter())
            except ValueError:
                butt_stable.configure(state='disabled')
                root.bind('<Return>', lambda event: empty_function())
            except IndexError:
                butt_stable.configure(state='disabled')
                root.bind('<Return>', lambda event: empty_function())

    elif content and (what_to_do_text.get('1.0', 'end-1c') == 'Insert date here:' or
                      what_to_do_text.get('1.0', 'end-1c') == 'Wprowadź datę:' or
                      what_to_do_text.get('1.0', 'end-1c') == 'Введіть дату:'):
        if not content.split('-')[3:]:
            try:
                float(content.split('-')[0])
                float(content.split('-')[1])
                float(content.split('-')[2])
                butt_stable.configure(state='normal')
                root.bind('<Return>', lambda event: enter())

            except IndexError:
                butt_stable.configure(state='disabled')
                root.bind('<Return>', lambda event: empty_function())
            except ValueError:
                butt_stable.configure(state='disabled')
                root.bind('<Return>', lambda event: empty_function())
        else:
            butt_stable.configure(state='disabled')
            root.bind('<Return>', lambda event: empty_function())

    elif not content and (what_to_do_text.get('1.0', 'end-1c') == 'Insert date here:' or
                          what_to_do_text.get('1.0', 'end-1c') == 'Wprowadź datę:' or
                          what_to_do_text.get('1.0', 'end-1c') == 'Введіть дату:'):
        butt_stable.configure(state='normal')
        root.bind('<Return>', lambda event: enter())

    elif (what_to_do_text.get('1.0', 'end-1c') == 'Insert description here:' or
          what_to_do_text.get('1.0', 'end-1c') == 'Wprowadź opis:' or
          what_to_do_text.get('1.0', 'end-1c') == 'Введіть опис:'):
        butt_stable.configure(state='normal')
        root.bind('<Return>', lambda event: enter())

    elif (what_to_do_text.get('1.0', 'end-1c') == 'Check all info and press "Apply" or "Cancel"' or
          what_to_do_text.get('1.0', 'end-1c') == 'Sprawdź wszystkie dane oraz kliknij "Potwierdź" lub "Anuluj"' or
          what_to_do_text.get('1.0', 'end-1c') == 'Перевірте всі дані та натисніть "Підтвердити" або "Відмінити"'):
        butt_stable.configure(state='disabled')
        root.bind('<Return>', lambda event: empty_function())
    else:
        butt_stable.configure(state='disabled')
        root.bind('<Return>', lambda event: empty_function())


def button_func():
    datas.database.new(price, description, date)
    if with_dates:
        dates()
    else:
        lc()
    confirmation_text.configure(state='normal')
    confirmation_text.delete('1.0', 'end-1c')
    confirmation_text.configure(state='disabled')
    enter()


def cancel_func():
    global description, date, price, can_do
    description = ''
    date = ''
    price = ''
    confirmation_text.configure(state='normal')
    confirmation_text.configure(state='normal')
    what_to_do_text.delete('1.0', tkinter.END)
    confirmation_text.delete('1.0', tkinter.END)
    input_text.delete('1.0', tkinter.END)
    confirmation_text.configure(state='disable')
    what_to_do_text.configure(state='disable')
    butt_stable.configure(state='normal')
    can_do = 0
    enter()


def delete_all_func():
    if language == 'en':
        first = tk.messagebox.askokcancel(title="Deleting all elements", message="Are you sure you want "
                                                                                 "to delete ALL of the elements?")
    elif language == 'pl':
        first = tk.messagebox.askokcancel(title="Usuwanie wszystkich elementów", message="Na pewno chcesz "
                                                                                         "usunąć WSZYSTKIE elementy?")
    elif language == 'ua':
        first = tk.messagebox.askokcancel(title="Видалення всіх елементів", message="Ви впевнені що хочете "
                                                                                    "видалити ВСІ елементи?")
    else:
        first = tk.messagebox.askokcancel(title="Deleting all elements", message="Are you sure you want "
                                                                                 "to delete ALL of the elements?")
    if first:
        if language == 'en':
            second = tk.messagebox.askokcancel(title="Deleting all elements",
                                               message="Are you sure that you are sure "
                                                       "that you want to DELETE ALL"
                                                       " of the elements???")
        elif language == 'pl':
            second = tk.messagebox.askokcancel(title="Usuwanie wszystkich elementów",
                                               message="Na pewno na pewno "
                                                       "chcesz USUNĄĆ WSZYSTKIE elementy'???")
        elif language == 'ua':
            second = tk.messagebox.askokcancel(title="Видалення всіх елементів",
                                               message="Ви впевнені що ви впевнені "
                                                       "що хочете ВИДАЛИТИ ВСІ елементи???")
        else:
            second = tk.messagebox.askokcancel(title="Deleting all elements",
                                               message="Are you sure that you are sure "
                                                       "that you want to DELETE ALL"
                                                       " of the elements???")

        if second:
            datas.database.del_all()
            if with_dates:
                dates()
            else:
                lc()
            if language == 'en':
                tk.messagebox.showinfo(title='info', message="Deletion completed!")
            elif language == 'pl':
                tk.messagebox.showinfo(title='info', message="Usuwanie zakończone!")
            elif language == 'ua':
                tk.messagebox.showinfo(title='інфо', message="Видалення завершено!")
            else:
                tk.messagebox.showinfo(title='info', message="Deletion completed!")


def help_info():
    global h_info, h_to_use, with_dates
    h_to_use = 0
    h_info = 1
    os()
    if language == 'pl':
        display_text.insert(tk.END, datas.lang_help.h_pl, 'h')
    elif language == 'ua':
        display_text.insert(tk.END, datas.lang_help.h_ua, 'h')
    elif language == 'en':
        display_text.insert(tk.END, datas.lang_help.h_en, 'h')
    else:
        display_text.insert(tk.END, datas.lang_help.h_pl, 'h')

    display_text.tag_configure('center', justify='center')
    display_text.tag_add('center', 1.0, 'end')
    display_text.see('1.0')
    display_text.configure(state='disabled')


def help_usage():
    os()
    global h_to_use, h_info
    h_to_use = 1
    h_info = 0
    os()
    if language == 'pl':
        display_text.insert(tk.END, datas.lang_help.hu_pl, 'hu')
    elif language == 'ua':
        display_text.insert(tk.END, datas.lang_help.hu_ua, 'hu')
    elif language == 'en':
        display_text.insert(tk.END, datas.lang_help.hu_en, 'hu')
    else:
        display_text.insert(tk.END, datas.lang_help.hu_pl, 'hu')

    display_text.see('1.0')
    display_text.configure(state='disabled')


def enter():
    global price, date, description, can_do
    what_to_do_text.configure(state='normal')
    confirmation_text.configure(state='normal')
    confirmation_text.tag_config('minus', foreground='#F15C20')
    confirmation_text.tag_config('plus', foreground='#57D233')

    if can_do and (what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Insert amount here:' or
                   what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Wprowadź kwotę:' or
                   what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Введіть суму:'):
        what_to_do_text.delete('1.0', tk.END)
        content = input_text.get('1.0', f"{tk.END}-1c")
        try:
            price = float(f"{content.split(',')[0]}.{content.split(',')[1]}")
        except ValueError:
            price = float(content)
        except IndexError:
            price = float(content)
        if price >= 0:
            if language == 'en':
                confirmation_text.insert(tkinter.END, f'Amount:\n\n{price:.2f}\n\n', 'plus')
            elif language == 'pl':
                confirmation_text.insert(tkinter.END, f'Kwota:\n\n{price:.2f}\n\n', 'plus')
            elif language == 'ua':
                confirmation_text.insert(tkinter.END, f'Сума:\n\n{price:.2f}\n\n', 'plus')
            else:
                confirmation_text.insert(tkinter.END, f'Amount:\n\n{price:.2f}\n\n', 'plus')
        else:
            if language == 'en':
                confirmation_text.insert(tkinter.END, f'Amount:\n\n{price:.2f}\n\n', 'minus')
            elif language == 'pl':
                confirmation_text.insert(tkinter.END, f'Kwota:\n\n{price:.2f}\n\n', 'minus')
            elif language == 'ua':
                confirmation_text.insert(tkinter.END, f'Сума:\n\n{price:.2f}\n\n', 'minus')
            else:
                confirmation_text.insert(tkinter.END, f'Amount:\n\n{price:.2f}\n\n', 'minus')

        if language == 'en':
            what_to_do_text.insert(tkinter.END, 'Insert date here:')
        elif language == 'pl':
            what_to_do_text.insert(tkinter.END, 'Wprowadź datę:')
        elif language == 'ua':
            what_to_do_text.insert(tkinter.END, 'Введіть дату:')
        else:
            what_to_do_text.insert(tkinter.END, 'Insert date here:')

    elif can_do and (what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Insert date here:' or
                     what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Wprowadź datę:' or
                     what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Введіть дату:'):
        what_to_do_text.delete('1.0', tk.END)
        if input_text.get('1.0', tk.END) == ('\n' or ''):
            date = now.strftime('%Y-%m-%d')
        else:
            date = input_text.get('1.0', f'{tk.END}-1c').replace('\n', '').strip()

        if language == 'en':
            confirmation_text.insert(tkinter.END, f'Date:\n\n{date}\n\n')
            what_to_do_text.insert(tkinter.END, 'Insert description here:')
        elif language == 'pl':
            confirmation_text.insert(tkinter.END, f'Data:\n\n{date}\n\n')
            what_to_do_text.insert(tkinter.END, 'Wprowadź opis:')
        elif language == 'ua':
            confirmation_text.insert(tkinter.END, f'Дата:\n\n{date}\n\n')
            what_to_do_text.insert(tkinter.END, 'Введіть опис:')
        else:
            confirmation_text.insert(tkinter.END, f'Date:\n\n{date}\n\n')
            what_to_do_text.insert(tkinter.END, 'Insert description here:')

    elif can_do and (what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Insert description here:' or
                     what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Wprowadź opis:' or
                     what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Введіть опис:'):
        what_to_do_text.delete('1.0', tk.END)
        try:
            inside = input_text.get('1.0', f'{tk.END}-1c').replace('\n', '').strip().split(',')
            g = inside[1]
            g += 'For code to look better'
            new_inside = ''
            for e in inside:
                new_inside += f'{e}⸥'
            description = new_inside.strip('⸥')

        except IndexError:
            description = input_text.get('1.0', f'{tk.END}-1c').replace('\n', '').strip()

        if language == 'en':
            confirmation_text.insert(tkinter.END, f'Description:\n\n{description}\n\n')
            what_to_do_text.insert(tkinter.END, 'Check all info and press "Apply" or "Cancel"')
        elif language == 'pl':
            confirmation_text.insert(tkinter.END, f'Opis:\n\n{description}\n\n')
            what_to_do_text.insert(tkinter.END, 'Sprawdź wszystkie dane oraz kliknij "Potwierdź" lub "Anuluj"')
        elif language == 'ua':
            confirmation_text.insert(tkinter.END, f'Опис:\n\n{description}\n\n')
            what_to_do_text.insert(tkinter.END, 'Перевірте всі дані та натисніть "Підтвердити" або "Відмінити"')
        else:
            confirmation_text.insert(tkinter.END, f'Description:\n\n{description}\n\n')
            what_to_do_text.insert(tkinter.END, 'Check all info and press "Apply" or "Cancel"')

        input_text.delete('1.0', tkinter.END)
        input_text.configure(state='disabled')
        butt_stable.configure(state='disabled')
        button.configure(state='normal')

    else:
        input_text.configure(state='normal')
        what_to_do_text.delete('1.0', tk.END)
        if language == 'en':
            what_to_do_text.insert(tkinter.END, 'Insert amount here:')
        elif language == 'pl':
            what_to_do_text.insert(tkinter.END, 'Wprowadź kwotę:')
        elif language == 'ua':
            what_to_do_text.insert(tkinter.END, 'Введіть суму:')
        else:
            what_to_do_text.insert(tkinter.END, 'Insert amount here:')
        button.configure(state='disabled')
        can_do = 1

    what_to_do_text.tag_configure('center', justify='center')
    confirmation_text.tag_configure('center', justify='center')

    input_text.delete('1.0', tkinter.END)

    what_to_do_text.tag_add('center', 1.0, 'end')
    confirmation_text.tag_add('center', 1.0, 'end')

    confirmation_text.configure(state='disabled')
    what_to_do_text.configure(state='disabled')


root = tk.Tk()
root.geometry('1130x800')
root.title('Finances app')
root.option_add('*tearOff', False)


frame = ttk.Frame(root)
frame.pack(fill='both', expand=True, padx=1, pady=(0, 0))

menubar = tk.Menu(root)
root.config(menu=menubar)

el_view_menu = tk.Menu(menubar)
lang_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)
delete_menu = tk.Menu(menubar)


menubar.add_cascade(menu=el_view_menu, label="⧫")
menubar.add_cascade(menu=lang_menu, label="⨁")
menubar.add_cascade(menu=delete_menu, label='⨂')
menubar.add_cascade(menu=help_menu, label='?')

el_view_menu.add_command(label='Dated', command=dates)
el_view_menu.add_command(label="Anton's Arrange", command=lc)
lang_menu.add_command(label='English', command=en)
lang_menu.add_command(label='Polski', command=pl)
lang_menu.add_command(label='Українська', command=ua)
delete_menu.add_command(label='Delete All ❗❗❗', command=delete_all_func)
help_menu.add_command(label='About App', command=help_info)
help_menu.add_command(label='How To Use', command=help_usage)


display_text = tk.Text(frame, height='15', width='93', bg='#4A4747', cursor='arrow', wrap='word')
confirmation_text = tk.Text(frame, height='20', width='30', bg='#4A4747', wrap='word', cursor='arrow')
what_to_do_text = tk.Text(frame, height='3', width='20', bg='#4A4747', fg='white', wrap='word', cursor='arrow')
button = tk.Button(frame, text='Apply', height='4', bg='green', width=9, command=button_func, cursor='plus')
cancel = tk.Button(frame, text='Cancel', height='4', bg='red', width=9, command=cancel_func, cursor='pirate')
input_text = tk.Text(frame, height='10', width='20', bg='#3A413A', cursor='arrow')
butt_stable = tk.Button(input_text, height='3', text='↲', bg='#3A413A', command=enter, cursor='heart')

what_to_do_text.insert(tkinter.END, 'Insert amount here:')
what_to_do_text.tag_configure('center', justify='center')
what_to_do_text.tag_add('center', 1.0, 'end')
what_to_do_text.configure(state='disabled')

display_text.configure(state='disabled')
confirmation_text.configure(state='disabled')
button.configure(state='disabled')

display_text.pack(side='left', expand=True, fill='both')
confirmation_text.pack(side='top', expand=True, fill='both')
input_text.pack(side='bottom', expand=True, fill='both')
cancel.pack(side='left')
what_to_do_text.pack(side='left', expand=True, fill='both')
button.pack(side='right')
butt_stable.pack(side='bottom')


root.bind('<Motion>', lambda event: check_for_changes())
root.bind('<Button>', lambda event: check_for_changes())

if language == 'en':
    en()
elif language == 'pl':
    pl()
elif language == 'ua':
    ua()
else:
    pl()

dates()
root.mainloop()
