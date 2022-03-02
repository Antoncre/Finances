"""
Dzięki tej aplikacji użytkownicy mogą dodawać
swoje wydatki i dochody oraz wyświetlać je w wygodny,
posortowany według daty sposób
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from functools import partial
import datas.database
import datas.lang_help

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
tye = 'date'
description = ''
can_do = 1
with_dates = 1
deleting_item = 0
latest_func = None
old_cat = None


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
    menubar.entryconfigure(0, label='Sort')
    menubar.entryconfigure(1, label='Language')
    menubar.entryconfigure(2, label='Delete')
    menubar.entryconfigure(3, label='Help')
    menubar.entryconfigure(4, label='Categories')
    el_view_menu.entryconfig(0, label='Dated')
    el_view_menu.entryconfig(1, label="Anton's Arrange")
    el_view_menu.entryconfig(2, label="By Price")
    help_menu.entryconfig(0, label='About App')
    help_menu.entryconfig(1, label='How To Use')
    delete_menu.entryconfig(0, label='Delete Items')
    delete_menu.entryconfig(1, label='Delete All ❗❗❗')
    categories_menu.entryconfig(0, label='+new category+')
    categories_menu.entryconfig(1, label='~edit categories~')
    categories_menu.entryconfig(2, label='-delete from category')
    latest_func()


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
    menubar.entryconfigure(0, label='Сортування')
    menubar.entryconfigure(1, label='Мова')
    menubar.entryconfigure(2, label='Видалення')
    menubar.entryconfigure(3, label='Довідка')
    menubar.entryconfigure(4, label='Категорії')
    el_view_menu.entryconfig(0, label='Датовано')
    el_view_menu.entryconfig(1, label='Структура Антона')
    el_view_menu.entryconfig(2, label='За Вартістю')
    help_menu.entryconfig(0, label='Про Программу')
    help_menu.entryconfig(1, label='Користування')
    delete_menu.entryconfig(0, label='Видалити Елементи')
    delete_menu.entryconfig(1, label='Видалити Все ❗❗❗')
    categories_menu.entryconfig(0, label='+нова категорія+')
    categories_menu.entryconfig(1, label='~едитувати категорію~')
    categories_menu.entryconfig(2, label='-видалити з категорії')
    latest_func()


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
    menubar.entryconfigure(0, label='Sortowanie')
    menubar.entryconfigure(1, label='Język')
    menubar.entryconfigure(2, label='Usuwanie')
    menubar.entryconfigure(3, label='Pomoc')
    menubar.entryconfigure(4, label='Kategorie')
    el_view_menu.entryconfig(0, label='Według Daty')
    el_view_menu.entryconfig(1, label='Układ Antona')
    el_view_menu.entryconfig(2, label='Według Wartości')
    help_menu.entryconfig(0, label='O Aplikacji')
    help_menu.entryconfig(1, label='Korzystanie')
    delete_menu.entryconfig(0, label='Usuń elementy')
    delete_menu.entryconfig(1, label='Usuń wszystko ❗❗❗')
    categories_menu.entryconfig(0, label='+nowa kategoria+')
    categories_menu.entryconfig(1, label='~edytuj kategorię~')
    categories_menu.entryconfig(2, label='-usuń z kategorii')
    latest_func()


def empty_function():
    pass


def add():
    a = []
    for el in datas.database.listing():
        a.append(el['price'])
    return "%.2f" % sum(a)


def srt():
    r = datas.database.listing()
    datas.database.sort(r, tye)


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
    global latest_func
    latest_func = dates
    os()
    for exp in datas.database.listing():
        f_2f = "%.2f" % exp['price']
        to_print_price = "%-9s" % f_2f
        to_print_date = "%-10s" % exp['date']
        if float(f_2f) < 0:
            display_text.insert(tk.END, f"{to_print_date}  {to_print_price}  {exp['description']}\n", 'minus')
        else:
            display_text.insert(tk.END, f"{to_print_date}   {to_print_price} {exp['description']}\n", 'plus')
    if language == 'en':
        display_text.insert(tk.END, f"\nTotal: {add()}")
    elif language == 'pl':
        display_text.insert(tk.END, f"\nŁącznie: {add()}")
    elif language == 'ua':
        display_text.insert(tk.END, f"\nЗагалом: {add()}")
    else:
        display_text.insert(tk.END, f"\nTotal: {add()}")
    display_text.see(tk.END)
    display_text.configure(state='disabled')


def pr():
    global latest_func
    latest_func = pr
    datas.database.sort('', 'price')
    os()
    for exp in datas.database.listing():
        f_2f = "%.2f" % exp['price']
        to_print_price = "%-9s" % f_2f
        to_print_date = "%-10s" % exp['date']
        if float(f_2f) < 0:
            display_text.insert(tk.END, f"{to_print_price} {to_print_date} {exp['description']}\n", 'minus')
        else:
            display_text.insert(tk.END, f" {to_print_price} {to_print_date} {exp['description']}\n", 'plus')
    if language == 'en':
        display_text.insert(tk.END, f"\nTotal: {add()}")
    elif language == 'pl':
        display_text.insert(tk.END, f"\nŁącznie: {add()}")
    elif language == 'ua':
        display_text.insert(tk.END, f"\nЗагалом: {add()}")
    else:
        display_text.insert(tk.END, f"\nTotal: {add()}")
    display_text.see(tk.END)
    display_text.configure(state='disabled')


def lc():
    global latest_func
    latest_func = lc
    os()
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
            display_text.insert(tk.END, f"{exp['date'].split('-')[0]}:\n")
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
                display_text.insert(tk.END, f"\nMonthly expenses: {totm_wyd} zł\n", 'o')
                display_text.insert(tk.END, f"Monthly income: {totm_do} zł\n", 'g')
                display_text.insert(tk.END, f"\nMonthly: {summ_to_print} zł\n", 'y')
            elif language == 'ua':
                display_text.insert(tk.END, f"\nВитрати за місяць: {totm_wyd} zł\n", 'o')
                display_text.insert(tk.END, f"Прибуток за місяць: {totm_do} zł\n", 'g')
                display_text.insert(tk.END, f"\nЦього місяця загалом: {summ_to_print} zł\n", 'y')
            elif language == 'pl':
                display_text.insert(tk.END, f"\nMiesięczne wydatki: {totm_wyd} zł\n", 'o')
                display_text.insert(tk.END, f"Miesięczne dochody: {totm_do} zł\n", 'g')
                display_text.insert(tk.END, f"\nMiesięcznie: {summ_to_print} zł\n", 'y')
            else:
                display_text.insert(tk.END, f"\nMonthly expenses: {totm_wyd} zł\n", 'o')
                display_text.insert(tk.END, f"Monthly income: {totm_do} zł\n", 'g')
                display_text.insert(tk.END, f"\nMonthly: {summ_to_print} zł\n", 'y')
            price_month_sum = []
            exp_month_sum = []
            inc_month_sum = []
        if year != current_year and wp != 0:
            if language == 'pl':
                display_text.insert(tk.END, f"\nRoczne wydatki: {toty_wyd} zł\n")
                display_text.insert(tk.END, f"Roczne Dochody: {toty_do} zł\n")
                display_text.insert(tk.END, f"\nRocznie: {sumy_to_print} zł\n")
            elif language == 'ua':
                display_text.insert(tk.END, f"\nВитрати за рік: {toty_wyd} zł\n")
                display_text.insert(tk.END, f"Прибуток за рік: {toty_do} zł\n")
                display_text.insert(tk.END, f"\nЦього року загалом: {sumy_to_print} zł\n")
            elif language == 'en':
                display_text.insert(tk.END, f"\nAnnual expenses: {toty_wyd} zł\n")
                display_text.insert(tk.END, f"Annual income: {toty_do} zł\n")
                display_text.insert(tk.END, f"\nAnnually: {sumy_to_print} zł\n")
            else:
                display_text.insert(tk.END, f"\nAnnual expenses: {toty_wyd} zł\n")
                display_text.insert(tk.END, f"Annual income: {toty_do} zł\n")
                display_text.insert(tk.END, f"\nAnnually: {sumy_to_print} zł\n")
            price_year_sum = []
            exp_year_sum = []
            inc_year_sum = []
            display_text.insert(tk.END, f"\n{year}:\n")
        if month != current_month or year != current_year:
            if month in MONTHS:
                display_text.insert(tk.END, f"\n{MONTHS[month]}\n")
            else:
                display_text.insert(tk.END, f"\n{month}:\n")
            current_month = month
            current_year = year
            wp = 1
        if float(f_2f) >= 0:
            display_text.insert(tk.END, f" {to_print_price} {exp['description']}\n", 'plus')
            inc_month_sum.append(exp['price'])
            inc_year_sum.append(exp['price'])
        else:
            display_text.insert(tk.END, f"{to_print_price}  {exp['description']}\n", 'minus')
            exp_month_sum.append(exp['price'])
            exp_year_sum.append(exp['price'])
        price_month_sum.append(exp['price'])
        price_year_sum.append(exp['price'])
        summ_to_print = "%.2f" % sum(price_month_sum)
        totm_wyd = "%.2f" % sum(exp_month_sum)
        totm_do = "%.2f" % sum(inc_month_sum)
    if language == 'pl':
        display_text.insert(tk.END, f"\nMiesięczne wydatki: {totm_wyd} zł\n", 'o')
        display_text.insert(tk.END, f"Miesięczne dochody: {totm_do} zł\n", 'g')
        display_text.insert(tk.END, f"\nMiesięcznie: {summ_to_print} zł\n", 'y')
        display_text.insert(tk.END, f"\nŁącznie całość: {add()}", 'm')
    elif language == 'ua':
        display_text.insert(tk.END, f"\nВитрати за місяць: {totm_wyd} zł\n", 'o')
        display_text.insert(tk.END, f"Прибуток за місяць: {totm_do} zł\n", 'g')
        display_text.insert(tk.END, f"\nЦього місяця загалом: {summ_to_print} zł\n", 'y')
        display_text.insert(tk.END, f"\nЗагалом: {add()}", 'm')
    elif language == 'en':
        display_text.insert(tk.END, f"\nMonthly expenses: {totm_wyd} zł\n", 'o')
        display_text.insert(tk.END, f"Monthly income: {totm_do} zł\n", 'g')
        display_text.insert(tk.END, f"\nMonthly: {summ_to_print} zł\n", 'y')
        display_text.insert(tk.END, f"\nTotal: {add()}", 'm')
    display_text.see(tk.END)
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
                one = float(content.split('-')[1])
                two = float(content.split('-')[2])
                if one <= 12 and two <= 31:
                    butt_stable.configure(state='normal')
                    root.bind('<Return>', lambda event: enter())
                else:
                    butt_stable.configure(state='disabled')
                    root.bind('<Return>', lambda event: empty_function())

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
    what_to_do_text.delete('1.0', tk.END)
    confirmation_text.delete('1.0', tk.END)
    input_text.delete('1.0', tk.END)
    confirmation_text.configure(state='disabled')
    what_to_do_text.configure(state='disabled')
    butt_stable.configure(state='disabled')
    can_do = 0
    enter()


def delete_items_func():
    global deleting_item
    deleting_item = 1
    dict_to_this = {}
    listy = []
    delete_menu.entryconfig(0, state='disabled')
    delete_menu.entryconfig(1, state='disabled')

    d_root = tk.Tk()

    d_root.geometry('1000x750')

    if language == 'ua':
        d_root.title('Видалення елементів')
    elif language == 'pl':
        d_root.title('Usuwanie elementów')
    elif language == 'en':
        d_root.title('Deleting items')
    else:
        d_root.title('Usuwanie elementów')

    d_root.option_add('*tearOff', False)

    def swap():
        global deleting_item
        deleting_item = 1
        try:
            delete_menu.entryconfig(0, state='normal')
            delete_menu.entryconfig(1, state='normal')
        except tk.TclError:
            pass
        d_root.destroy()

    def chk_for_chan():
        if len(listy) == 0:
            del_selected.configure(state='disabled')
        else:
            del_selected.configure(state='normal')

    def del_butt(li):
        if len(li) == 0:
            tk.messagebox.showinfo(title='Empty list', message="You haven't chosen any elements. Choose elements "
                                                               "you want to delete, and only then press tis button")
        else:
            for e in li:
                datas.database.delete(e[0], e[2], e[1])
            text_field.configure(state='normal')
            text_field.delete('1.0', tk.END)
            text_field.configure(state='disabled')
            try:
                if with_dates:
                    dates()
                else:
                    lc()
            except tk.TclError:
                pass
            swap()

    def inserting(d, p, ds, n):
        if dict_to_this[n].instate(['selected']):
            listy.append([d, p, ds])
            text_field.configure(state='normal')
            text_field.insert(tk.END, f"\n{n}. {ds}\n")
            text_field.configure(state='disabled')
        else:
            listy.remove([d, p, ds])
            text_field.configure(state='normal')
            n_text = text_field.get('1.0', f'{tk.END}-1c').replace(f"\n{n}. {ds}\n", "")
            text_field.delete('1.0', tk.END)
            text_field.insert(tk.END, n_text)
            text_field.configure(state='disabled')

    def add_obj():
        n = 0
        for exp in datas.database.listing():

            f_2f = "%.2f" % exp['price']
            to_print_price = "%-9s" % f_2f
            to_print_date = "%-10s" % exp['date']

            p_inserting = partial(inserting, exp['date'], exp['price'], exp['description'], n)
            dict_to_this[n] = ttk.Checkbutton(new_frame, text=f"{to_print_date}  {to_print_price}"
                                                              f"  {exp['description']}\n",
                                                              command=p_inserting)
            n += 1

    if language == 'ua':
        dels = 'Видвлити вибрані елементи'
        label = 'Вибрані елементи:'
    elif language == 'pl':
        dels = 'Usuń wybrane elementy'
        label = 'Wybrane elementy:'
    elif language == 'en':
        dels = 'Delete selected items'
        label = 'Selected items:'
    else:
        dels = 'Usuń wybrane elementy'
        label = 'Wybrane elementy:'

    par = partial(del_butt, listy)

    d_frame = tk.Frame(d_root)
    canvas = tk.Canvas(d_frame, bg="#D7D9D6")
    text_field = tk.Text(d_frame, width='50', height='25', wrap='word', bg="#4A4747", fg='white')
    del_selected = tk.Button(d_frame, width='50', height='10', text=dels, bg='#CF5828', fg='white', command=par)
    new_frame = tk.Frame(canvas)
    label_selected = tk.Label(d_frame, text=label)
    del_scrollbar = tk.Scrollbar(text_field, orient="vertical", width='7', command=text_field.yview, cursor='arrow')

    additional_scrollbar = ttk.Scrollbar(d_frame, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=additional_scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    d_frame.pack(expand=True, fill='both')
    additional_scrollbar.pack(side='left', fill='y')
    canvas.pack(side='left', expand=True, fill='both')
    canvas.create_window((0, 0), anchor='w', window=new_frame, width='700')

    label_selected.pack(side='top', fill='x')

    text_field.pack(side='top', fill='both', expand=True)
    del_scrollbar.pack(side='right', expand=False, fill='y')

    del_selected.pack(side='top', fill='both')
    add_obj()

    for ob in dict_to_this.values():
        ob.pack(side='top', fill='x')

    text_field["yscrollcommand"] = del_scrollbar.set
    text_field.tag_configure('center', justify='center')
    text_field.tag_add('center', 1.0, 'end')

    text_field.configure(state='disabled')

    d_root.bind('<Motion>', lambda event: chk_for_chan())

    d_root.protocol('WM_DELETE_WINDOW', swap)


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


def add_category_f():
    categories_menu.entryconfig(0, state='disabled')
    categories_menu.entryconfig(1, state='disabled')
    categories_menu.entryconfig(2, state='disabled')
    if language == 'ua':
        ad = 'Додати нову категорію'
        tl = 'Додавання категорії'
    elif language == 'pl':
        ad = 'Dodać nową kategorię'
        tl = 'Dodawanie kategorii'
    elif language == 'en':
        ad = 'Add new category'
        tl = 'Adding category'
    else:
        ad = 'Dodać nową kategorię'
        tl = 'Dodawanie kategorii'
    add_root = tk.Tk()
    add_root.geometry('400x85')
    add_root.title(tl)
    add_root.option_add('*tearOff', False)

    def swap():
        try:
            categories_menu.entryconfig(0, state='normal')
            categories_menu.entryconfig(1, state='normal')
            categories_menu.entryconfig(2, state='normal')
            latest_func
            add_root.destroy()
        except tk.TclError:
            print('tlc error occires')
            add_root.destroy()

    def tiny_button_f():
        illegal_characters = ['!', '@', '#', '$', '%', '&', '*', '"', "'", '+', '=', '{',
                              '}', '<', '>', '?', '/', '\n', '`', '|']
        txt = text_for_category.get('1.0', f'{tk.END}-1c')
        for char in illegal_characters:
            txt = txt.replace(char, '')
        try:
            """ delete categories from 3:end of categories """
            ch = len(datas.database.ch_categories())
            for element in range(ch):
                categories_menu.delete(4, 4+element)
            datas.database.new_category(txt)
            additional_categories()
            swap()
        except tk.TclError:
            add_root.destroy()

    def add_check():
        if text_for_category.get('1.0', f'{tk.END}-1c') == '':
            tiny_button.configure(state='disabled')
        else:
            tiny_button.configure(state='normal')

    text_for_category = tk.Text(add_root, width='25', height='2',)
    tiny_button = tk.Button(add_root, text=ad, width='20', height='2', command=tiny_button_f)

    text_for_category.pack(side='top', expand=False)
    tiny_button.pack(side='top', expand=False)

    tiny_button.configure(state='disabled')

    add_root.bind('<Motion>', lambda event: add_check())
    add_root.bind('<Button>', lambda event: add_check())
    add_root.bind('<KeyPress>', lambda event: add_check())
    add_root.protocol('WM_DELETE_WINDOW', swap)


def edit_category_f():
    dict_to_this = {}
    complete_list = []
    secure_choosing_dict = {}
    categories_menu.entryconfig(0, state='disabled')
    categories_menu.entryconfig(1, state='disabled')
    categories_menu.entryconfig(2, state='disabled')

    e_root = tk.Tk()

    e_root.geometry('1000x750')
    e_root.title('Editing Category')
    e_root.option_add('*tearOff', False)

    def swap():
        try:
            categories_menu.entryconfig(0, state='normal')
            categories_menu.entryconfig(1, state='normal')
            categories_menu.entryconfig(2, state='normal')
            latest_func
        except tk.TclError:
            pass
        e_root.destroy()

    def category_select():
        global old_cat
        current = list_of_categories.get()
        if current != old_cat:
            text_field.configure(state='normal')
            text_field.delete('1.0', tk.END)

            #if secure_choosing_dict[current]:
            #key error   pass

            for o in complete_list:
                dict_to_this[o[0]].state(['!alternate'])
                dict_to_this[o[0]].state(['!selected'])

            for o in complete_list:
                for el in datas.database.listing(f'datas/{current}.csv'):
                    if el['date'] == o[1] and el['price'] == o[2] and el['description'] == o[3]:
                        dict_to_this[o[0]].state(['!alternate'])
                        dict_to_this[o[0]].state(['selected'])
                        b = {'date': o[1], 'price': o[2], 'description': o[3]}
                        inserting(o[0], o[3], b)
            old_cat = current

    def inserting(n, ds, exp):
        c = list_of_categories.get()
        if dict_to_this[n].instate(['selected']):
            datas.database.add_to_category(c, exp)
            text_field.configure(state='normal')
            text_field.insert(tk.END, f"\n{n}. {ds}\n")
            text_field.configure(state='disabled')
        else:
            datas.database.del_from_category(c, exp)
            text_field.configure(state='normal')
            n_text = text_field.get('1.0', f'{tk.END}-1c').replace(f"\n{n}. {ds}\n", "")
            text_field.delete('1.0', tk.END)
            text_field.insert(tk.END, n_text)
            text_field.configure(state='disabled')

    def add_obj():
        n = 0
        for exp in datas.database.listing():
            f_2f = "%.2f" % exp['price']
            to_print_price = "%-9s" % f_2f
            to_print_date = "%-10s" % exp['date']

            complete_list.append([n, exp['date'], exp['price'], exp['description']])

            p_inserting = partial(inserting, n, exp['description'], exp)
            dict_to_this[n] = ttk.Checkbutton(new_frame, text=f"{to_print_date}  {to_print_price}"
                                                              f"  {exp['description']}\n",
                                              command=p_inserting)
            n += 1

    def checking():
        global old_cat
        old_cat = list_of_categories.get()

    if language == 'ua':
        label = 'Вибрані елементи:'
        c_label = 'Виберіть категорію'
    elif language == 'pl':
        label = 'Wybrane elementy:'
        c_label = 'Wybierz kategorię'
    elif language == 'en':
        label = 'Selected items:'
        c_label = 'Select category'
    else:
        label = 'Wybrane elementy:'
        c_label = 'Wybierz kategorię'

    d_frame = tk.Frame(e_root)
    canvas = tk.Canvas(d_frame, bg="#D7D9D6")
    text_field = tk.Text(d_frame, width='250', height='25', wrap='word', bg="#4A4747", fg='white')
    new_frame = tk.Frame(canvas)
    label_selected = tk.Label(d_frame, text=label)
    label_choose = tk.Label(d_frame, text=c_label)
    del_scrollbar = tk.Scrollbar(text_field, orient="vertical", width='7', command=text_field.yview, cursor='arrow')
    list_of_categories = ttk.Combobox(d_frame, width='25', height='2', state='readonly')

    additional_scrollbar = ttk.Scrollbar(d_frame, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=additional_scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    d_frame.pack(expand=True, fill='both')
    additional_scrollbar.pack(side='left', fill='y')
    canvas.pack(side='left', expand=True, fill='both')
    canvas.create_window((0, 0), anchor='w', window=new_frame, width='700')

    label_choose.pack(side='top', fill='x')
    list_of_categories.pack(side='top', expand=False)
    label_selected.pack(side='top', fill='x')

    text_field.pack(side='top', fill='both', expand=True)
    del_scrollbar.pack(side='right', expand=False, fill='y')

    list_of_categories['values'] = datas.database.ch_categories()

    add_obj()

    for ob in dict_to_this.values():
        ob.pack(side='top', fill='x')

    text_field["yscrollcommand"] = del_scrollbar.set
    text_field.tag_configure('center', justify='center')
    text_field.tag_add('center', 1.0, 'end')

    text_field.configure(state='disabled')
    e_root.protocol('WM_DELETE_WINDOW', swap)
    e_root.bind('<Motion>', lambda event: checking())
    e_root.bind('<<ComboboxSelected>>', lambda event: category_select())


def delete_category_f():
    categories_menu.entryconfig(0, state='disabled')
    categories_menu.entryconfig(1, state='disabled')
    categories_menu.entryconfig(2, state='disabled')
    if language == 'ua':
        ad = 'Видалити категорію'
        tl = 'Видалення категорії'
    elif language == 'pl':
        ad = 'Usunąć kategorię'
        tl = 'Usuwanie kategorii'
    elif language == 'en':
        ad = 'Delete category'
        tl = 'Deleting category'
    else:
        ad = 'Usunąć kategorię'
        tl = 'Usuwanie kategorii'

    add_root = tk.Tk()
    add_root.geometry('400x85')
    add_root.title(tl)
    add_root.option_add('*tearOff', False)

    def swap():
        try:
            categories_menu.entryconfig(0, state='normal')
            categories_menu.entryconfig(1, state='normal')
            categories_menu.entryconfig(2, state='normal')
        except tk.TclError:
            pass
        add_root.destroy()

    def tiny_button_f():
        current = list_of_categories.get()
        try:
            datas.database.del_category(current)
            categories_menu.delete(current)
            latest_func
            swap()
        except tk.TclError:
            swap()

    list_of_categories = ttk.Combobox(add_root, width='25', height='2', state='readonly')
    tiny_button = tk.Button(add_root, text=ad, width='20', height='2', command=tiny_button_f)

    list_of_categories.pack(side='top', expand=False)
    tiny_button.pack(side='top', expand=False)

    list_of_categories['values'] = datas.database.ch_categories()
    list_of_categories.get()
    add_root.protocol('WM_DELETE_WINDOW', swap)


def read_from_categories(t):
    a = []
    for el in datas.database.listing(f'datas/{t}.csv'):
        try:
            a.append(el['price'])
        except IndexError:
            pass
    s = "%.2f" % sum(a)
    display_text.configure(state='normal')
    display_text.delete('1.0', tk.END)
    display_text.insert(tk.END, f'{t.upper()}\n_______________\n')
    for exp in datas.database.listing(f'datas/{t}.csv'):
        if exp == ['']:
            pass
        else:
            f_2f = "%.2f" % exp['price']
            to_print_price = "%-9s" % f_2f
            to_print_date = "%-10s" % exp['date']
            if float(f_2f) < 0:
                display_text.insert(tk.END, f"{to_print_date}  {to_print_price}  {exp['description']}\n", 'minus')
            else:
                display_text.insert(tk.END, f"{to_print_date}   {to_print_price} {exp['description']}\n", 'plus')
    if language == 'en':
        display_text.insert(tk.END, f"\nTotal: {s}")
    elif language == 'pl':
        display_text.insert(tk.END, f"\nŁącznie: {s}")
    elif language == 'ua':
        display_text.insert(tk.END, f"\nЗагалом: {s}")
    else:
        display_text.insert(tk.END, f"\nTotal: {s}")
    display_text.see(tk.END)
    display_text.configure(state='disabled')


def additional_categories():
    for e in datas.database.ch_categories():
        if e == '':
            pass
        else:
            p_read_from_categories = partial(read_from_categories, e)
            categories_menu.add_command(label=f'{e}', command=p_read_from_categories)


def help_info():
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

    if can_do and (what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Insert price here:' or
                   what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Wprowadź kwotę:' or
                   what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Введіть суму:'):
        what_to_do_text.delete('1.0', tk.END)
        content = input_text.get('1.0', f"{tk.END}-1c").strip()
        try:
            prontent = content.split('\n')[0] + content.split('\n')[1]
            price = float(f"{prontent.split(',')[0]}.{prontent.split(',')[1]}")
        except IndexError:
            try:
                prontent = content.split('\n')[0] + content.split('\n')[1]
                price = float(prontent)
            except IndexError:
                try:
                    price = float(f"{content.split(',')[0]}.{content.split(',')[1]}")
                except IndexError:
                    price = float(content)

        if price > 0:
            if language == 'en':
                confirmation_text.insert(tk.END, f'Price:\n\n{price:.2f}\n\n', 'plus')
            elif language == 'pl':
                confirmation_text.insert(tk.END, f'Kwota:\n\n{price:.2f}\n\n', 'plus')
            elif language == 'ua':
                confirmation_text.insert(tk.END, f'Сума:\n\n{price:.2f}\n\n', 'plus')
            else:
                confirmation_text.insert(tk.END, f'Price:\n\n{price:.2f}\n\n', 'plus')
        else:
            if language == 'en':
                confirmation_text.insert(tk.END, f'Price:\n\n{price:.2f}\n\n', 'minus')
            elif language == 'pl':
                confirmation_text.insert(tk.END, f'Kwota:\n\n{price:.2f}\n\n', 'minus')
            elif language == 'ua':
                confirmation_text.insert(tk.END, f'Сума:\n\n{price:.2f}\n\n', 'minus')
            else:
                confirmation_text.insert(tk.END, f'Price:\n\n{price:.2f}\n\n', 'minus')

        if language == 'en':
            what_to_do_text.insert(tk.END, 'Insert date here:')
        elif language == 'pl':
            what_to_do_text.insert(tk.END, 'Wprowadź datę:')
        elif language == 'ua':
            what_to_do_text.insert(tk.END, 'Введіть дату:')
        else:
            what_to_do_text.insert(tk.END, 'Insert date here:')

    elif can_do and (what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Insert date here:' or
                     what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Wprowadź datę:' or
                     what_to_do_text.get('1.0', f'{tk.END}-1c') == 'Введіть дату:'):
        what_to_do_text.delete('1.0', tk.END)
        if input_text.get('1.0', f"{tk.END}-1c").strip() == '':
            date = now.strftime('%Y-%m-%d')
        else:
            try:
                to_date = input_text.get('1.0', f'{tk.END}-1c').replace('\n', '').strip().split()
                string_date = ''.join(to_date)
                date = f"{int(string_date.split('-')[0]):04d}-{int(string_date.split('-')[1]):02d}-" \
                       f"{int(string_date.split('-')[2]):02d}"
            except IndexError:
                date = input_text.get('1.0', f'{tk.END}-1c').strip()

        if language == 'en':
            confirmation_text.insert(tk.END, f'Date:\n\n{date}\n\n')
            what_to_do_text.insert(tk.END, 'Insert description here:')
        elif language == 'pl':
            confirmation_text.insert(tk.END, f'Data:\n\n{date}\n\n')
            what_to_do_text.insert(tk.END, 'Wprowadź opis:')
        elif language == 'ua':
            confirmation_text.insert(tk.END, f'Дата:\n\n{date}\n\n')
            what_to_do_text.insert(tk.END, 'Введіть опис:')
        else:
            confirmation_text.insert(tk.END, f'Date:\n\n{date}\n\n')
            what_to_do_text.insert(tk.END, 'Insert description here:')

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
                new_inside += f'{e}¸'
            description = new_inside.strip('¸')
            root.bind('<Return>', lambda event: empty_function())
        except IndexError:
            description = input_text.get('1.0', f'{tk.END}-1c').replace('\n', '').strip()
            root.bind('<Return>', lambda event: empty_function())
        if language == 'en':
            confirmation_text.insert(tk.END, f'Description:\n\n{description}\n\n')
            what_to_do_text.insert(tk.END, 'Check all info and press "Apply" or "Cancel"')
        elif language == 'pl':
            confirmation_text.insert(tk.END, f'Opis:\n\n{description}\n\n')
            what_to_do_text.insert(tk.END, 'Sprawdź wszystkie dane oraz kliknij "Potwierdź" lub "Anuluj"')
        elif language == 'ua':
            confirmation_text.insert(tk.END, f'Опис:\n\n{description}\n\n')
            what_to_do_text.insert(tk.END, 'Перевірте всі дані та натисніть "Підтвердити" або "Відмінити"')
        else:
            confirmation_text.insert(tk.END, f'Description:\n\n{description}\n\n')
            what_to_do_text.insert(tk.END, 'Check all info and press "Apply" or "Cancel"')

        input_text.delete('1.0', tk.END)
        input_text.configure(state='disabled')
        butt_stable.configure(state='disabled')
        button.configure(state='normal')

    else:
        input_text.configure(state='normal')
        what_to_do_text.delete('1.0', tk.END)
        if language == 'en':
            what_to_do_text.insert(tk.END, 'Insert price here:')
        elif language == 'pl':
            what_to_do_text.insert(tk.END, 'Wprowadź kwotę:')
        elif language == 'ua':
            what_to_do_text.insert(tk.END, 'Введіть суму:')
        else:
            what_to_do_text.insert(tk.END, 'Insert price here:')
        root.bind('<Return>', lambda event: empty_function())
        button.configure(state='disabled')
        can_do = 1

    what_to_do_text.tag_configure('center', justify='center')
    confirmation_text.tag_configure('center', justify='center')

    input_text.delete('1.0', tk.END)

    what_to_do_text.tag_add('center', 1.0, 'end')
    confirmation_text.tag_add('center', 1.0, 'end')

    confirmation_text.configure(state='disabled')
    what_to_do_text.configure(state='disabled')


root = tk.Tk()
root.geometry('1130x700')
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
categories_menu = tk.Menu(menubar)

menubar.add_cascade(menu=el_view_menu, label='Sort')
menubar.add_cascade(menu=lang_menu, label='Language')
menubar.add_cascade(menu=delete_menu, label='Delete')
menubar.add_cascade(menu=help_menu, label='Help')
menubar.add_cascade(menu=categories_menu, label='Categories')


el_view_menu.add_command(label='Dated', command=dates)
el_view_menu.add_command(label="Anton's Arrange", command=lc)
el_view_menu.add_command(label="By Price", command=pr)
lang_menu.add_command(label='English', command=en)
lang_menu.add_command(label='Polski', command=pl)
lang_menu.add_command(label='Українська', command=ua)
delete_menu.add_command(label='Delete Items', command=delete_items_func)
delete_menu.add_command(label='Delete All ❗❗❗', command=delete_all_func)
help_menu.add_command(label='About App', command=help_info)
help_menu.add_command(label='How To Use', command=help_usage)
categories_menu.add_command(label='+new category+', command=add_category_f)
categories_menu.add_command(label='~edit categories~', command=edit_category_f)
categories_menu.add_command(label='-delete category', command=delete_category_f)
categories_menu.add_command(label='---------------------')
additional_categories()

display_text = tk.Text(frame, height='15', width='93', bg='#4A4747', fg='white', cursor='arrow', wrap='word')
confirmation_text = tk.Text(frame, height='15', width='30', bg='#4A4747', fg='white', wrap='word', cursor='arrow')
what_to_do_text = tk.Text(frame, height='3', width='20', bg='#4A4747', fg='white', wrap='word', cursor='arrow')
button = tk.Button(frame, text='Apply', height='4', bg='green', width=9, fg='white', command=button_func)
cancel = tk.Button(frame, text='Cancel', height='4', bg='red', fg='white', width=9, command=cancel_func)
input_text = tk.Text(frame, height='15', width='20', bg='#3A413A', fg='white', cursor='arrow')
butt_stable = tk.Button(input_text, height='3', text='↲', bg='#3A413A', fg="white", command=enter)
my_scrollbar = tk.Scrollbar(frame, orient="vertical", width='7', command=display_text.yview, cursor='arrow')

what_to_do_text.insert(tk.END, 'Insert amount here:')
what_to_do_text.tag_configure('center', justify='center')
what_to_do_text.tag_add('center', 1.0, 'end')
what_to_do_text.configure(state='disabled')

display_text.configure(state='disabled')
confirmation_text.configure(state='disabled')
button.configure(state='disabled')

my_scrollbar.pack(side='left', expand=False, fill='y')
display_text.pack(side='left', expand=True, fill='both')
confirmation_text.pack(side='top', expand=True, fill='both')
input_text.pack(side='bottom', expand=True, fill='both')
cancel.pack(side='left')
what_to_do_text.pack(side='left', expand=True, fill='both')
button.pack(side='right')
butt_stable.pack(side='bottom')

display_text["yscrollcommand"] = my_scrollbar.set

root.bind('<Motion>', lambda event: check_for_changes())
root.bind('<Button>', lambda event: check_for_changes())
root.bind('<KeyPress>', lambda event: check_for_changes())
root.bind('<Escape>', lambda event: cancel_func())

latest_func = dates

if language == 'en':
    en()
elif language == 'pl':
    pl()
elif language == 'ua':
    ua()
else:
    pl()

root.mainloop()
