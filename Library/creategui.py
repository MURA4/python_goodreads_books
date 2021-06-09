# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""
Модуль с основными функциями
"""
from Library.dataprep import create_data
from tkinter import *
import tkinter.ttk as ttk
from Scripts.config import \
    table_columns,clean_data_path,reload_data_path, download_data, save_graph_path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import csv
create_data()
path = clean_data_path
tmp_data = pd.read_csv(path)
count = 0
def show(frame22,combo_plot1,combo_plot2):
    """
    Функция вывода графика в приложении и сохранения его
    Входные параметры:
    Рамка вывода графика
    Выдвижной лист 1
    Выдвижной лист 2 
    ----------
    Автор: Моисеенков В.
    
    """
    if combo_plot1.get() != 'choose':
        global count
        for widgets in frame22.winfo_children():
            widgets.destroy()
        if combo_plot1.get() != combo_plot2.get() and combo_plot1.get() != 'choose'and combo_plot2.get() != 'choose':
            figure = plt.Figure(figsize=(5,2))
            ax = figure.add_subplot(111)
            ax.scatter(tmp_data[combo_plot1.get()],tmp_data[combo_plot2.get()],s = 7)
            chart_type = FigureCanvasTkAgg(figure, frame22)
            chart_type.get_tk_widget().place(x=10, y=10)
            # global count
            count+=1
            figure.savefig(save_graph_path+f'/Graph{count}')
        elif combo_plot1.get() != 'choose'and combo_plot2.get() != 'choose' and combo_plot1.get() == combo_plot2.get():
            figure = plt.Figure(figsize=(5, 2))
            ax = figure.add_subplot(111)
            ax.hist(tmp_data[combo_plot1.get()])
            chart_type = FigureCanvasTkAgg(figure,frame22)
            chart_type.get_tk_widget().place(x = 10, y =10)
            # global count
            count+=1
            figure.savefig(save_graph_path+f'/Graph{count}')



def download(frame3):
    """
    Функция скачивания и загрузки Базы Данных
    Входные параметры:
    Рамка вывода Базы Данных
    ----------
    Автор: Моисеенков В.

    """
    scrollbarx = Scrollbar(frame3, orient=HORIZONTAL)
    scrollbary = Scrollbar(frame3, orient=VERTICAL)
    columns = table_columns
    tree = ttk.Treeview(frame3, columns=columns, selectmode="extended",height = 15)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side = RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side = BOTTOM, fill=X)
    for i in columns:
        tree.heading(f'{i}', text=f'{i}', anchor=W)
    # tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column("#0", minwidth=0, width=0)
    for i in range(1, 12):
        tree.column(f'#{i}', stretch=NO, minwidth=106, width=106)

    tree.pack()
    with open(path) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            title = row['title']
            authors = row['authors']
            average_rating = row['average_rating']
            language_code = row['language_code']
            num_pages = row['num_pages']
            ratings_count = row['ratings_count']
            text_reviews_count = row['text_reviews_count']
            publication_date = row['publication_date']
            publisher = row['publisher']
            pub_year = row['pub_year']
            century = row['century']
            # is_big_book = row['is_big_book']
            tree.insert("", 0, values=(
            title, authors, average_rating, language_code, num_pages,ratings_count, text_reviews_count, publication_date, publisher,
            pub_year, century))

def reload(frame3,var_2,var_3,var_4,var_5,var_6,var_7,var_8,var_9):
    """
    Функция парсинга Базы Данных
    Входные параметры:
    Рамка вывода Базы Данных
    Значения всех шкал отбора
    ----------
    Автор: Леванов И.

    """
    av1 = float(var_2.get())
    av2 = float(var_3.get())
    pag1 = int(var_4.get())
    pag2 = int(var_5.get())
    rate1 = float(var_6.get())
    rate2 = float(var_7.get())
    rew1 = int(var_8.get())
    rew2 = int(var_9.get())
    newcsv = []
    with open(clean_data_path, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        reader = list(reader)
    with open(reload_data_path, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        if not newcsv:
            newcsv.append(reader[0])
            spamwriter.writerow(reader[0])
            reader.pop(0)
        for str in reader:
            if av2 > float(str[3])  > av1 and pag2 > float(str[5])  > pag1 \
                    and rate2 > float(str[6]) > rate1 and rew2 > float(str[7]) > rew1:
                newcsv.append(str)
                try:
                    spamwriter.writerow(str)
                except UnicodeEncodeError:
                    print()       
    global tmp_data
    tmp_data = pd.read_csv(reload_data_path)
    

def download_main(frame3):
    """
    Функция возврата базы данных первонаальному состоянию
    Входные параметры:
    Рамка вывода Базы Данных
    ----------
    Автор: Моисеенков В.
    
    """
    for widgets in frame3.winfo_children():
        widgets.destroy()
    global path
    path = download_data
    download(frame3)

def update_table(frame3,var_2,var_3,var_4,var_5,var_6,var_7,var_8,var_9):
    """
    Функция загрузки обновлённой базы данных
    Входные параметры:
    Рамка вывода Базы Данных
    Значения всех шкал отбора
    ----------
    Автор: Хасанов М.
    
    """
    for widgets in frame3.winfo_children():
        widgets.destroy()
    global path
    reload(frame3,var_2,var_3,var_4,var_5,var_6,var_7,var_8,var_9)
    path = reload_data_path
    download(frame3)