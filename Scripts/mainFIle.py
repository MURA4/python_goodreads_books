# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""
Основной модуль
----------
Автор: Хасанов М.

"""
from tkinter import Tk, Frame, Label, DoubleVar, Scale, Button, HORIZONTAL
import tkinter.ttk as ttk
from Scripts.config import *
from Library.creategui import show,download,download_main,update_table
root = Tk()
root.title("Analyse")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (gui_width / 2)
y = (screen_height / 2) - (gui_height / 2)
root.geometry("%dx%d+%d+%d" % (gui_width, gui_height, x, y))
frame1 = Frame(root, width=600, height=350)
frame2 = Frame(root, width=600, height=100)
frame22 = Frame(root, width=600, height=300)
frame3 = Frame(root, width=1200, height=300)
frame1.place(x = 10, y =10 )
frame2.place(x = 610, y =10 )
frame22.place(x = 610, y =110)
frame3.place(x = 10, y = 360)
lbl_0 = Label(frame1, text='Отбор по базе данных')
lbl_0.config(font=("Courier", 12))
lbl_0.place( x =0, y = 0)
lbl_1 = Label(frame2, text='Построение зависимостей')
lbl_1.config(font=("Courier", 12))
lbl_1.place(x = 0 , y =0)
var_2 = DoubleVar()
var_3 = DoubleVar()
var_4 = DoubleVar()
var_5 = DoubleVar()
var_6 = DoubleVar()
var_7 = DoubleVar()
var_8 = DoubleVar()
var_9 = DoubleVar()
lbl_2 = Label(frame1, text="Average rating from")
lbl_2.grid(row=1, column=1)
sca_2= Scale(frame1, variable = var_2, orient=HORIZONTAL,
             length=150, from_=0, to=5, tickinterval=1, resolution=0.1)
sca_2.grid(row=1, column=3)
lbl_3 = Label(frame1, text="to")
lbl_3.grid(row=1, column=4)
sca_3=Scale(frame1,variable=var_3,orient=HORIZONTAL,
             length=150,from_=0,to=5,tickinterval=1,resolution=0.1)
sca_3.set(5.0)
sca_3.grid(row=1, column=5)
lbl_4 = Label(frame1, text="Number of pages from")
lbl_4.grid(row=2, column=1)
sca_4 = Scale(frame1,variable = var_4, orient=HORIZONTAL,
             length=150, from_=0, to=6576, tickinterval=3288, resolution=1)
sca_4.grid(row=2, column=3)
lbl_5 = Label(frame1, text="to")
lbl_5.grid(row=2, column=4)
sca_5 = Scale(frame1,variable = var_5, orient=HORIZONTAL,
             length=150, from_=0, to=6576, tickinterval=3288, resolution=1)
sca_5.set(6576.0)
sca_5.grid(row=2, column=5)
lbl_6 = Label(frame1, text="Rating count from")
lbl_6.grid(row=3, column=1)
sca_6 = Scale(frame1, variable = var_6, orient=HORIZONTAL,
             length=150, from_=0, to=250000, tickinterval=250000, resolution=1000)
sca_6.grid(row=3, column=3)
lbl_7 = Label(frame1, text="to")
lbl_7.grid(row=3, column=4)
sca_7 = Scale(frame1, variable = var_7, orient=HORIZONTAL,
             length=150, from_=0,  to=250000, tickinterval=250000, resolution=1000)
sca_7.set(4600000.0)
sca_7.grid(row=3, column=5)
lbl_8 = Label(frame1, text="Text reviews from")
lbl_8.grid(row=4, column=1)
sca_8 = Scale(frame1,variable = var_8, orient=HORIZONTAL,
             length=150, from_=0, to=20000, tickinterval=20000, resolution=100)
sca_8.grid(row=4, column=3)
lbl_9 = Label(frame1, text="to")
lbl_9.grid(row=4, column=4)
sca_9 = Scale(frame1,variable = var_9, orient=HORIZONTAL,
             length=150, from_=0, to=20000, tickinterval=20000, resolution=100)
sca_9.set(94300)
sca_9.grid(row=4, column=5)
download_init_data_base = Button(frame1, text ='Скачать',
                                 command= lambda : download_main(frame3))
download_init_data_base.grid(row=5, column=1)
reload_data_base= Button(frame1, text='Обновить базу данных',
                         command=lambda :update_table(frame3,var_2,var_3,var_4,var_5,var_6,var_7,var_8,var_9))
reload_data_base.grid(row=5, column=2)
values = ['choose', 'average_rating','num_pages',
          'ratings_count','text_reviews_count']
combo_hist = ttk.Combobox(frame2,values = values)
combo_plot1 = ttk.Combobox(frame2,values =values )
combo_plot2 = ttk.Combobox(frame2,values =values )
combo_plot1.place(x = 0, y = 60)
combo_plot2.place(x = 200, y = 60)
combo_plot1.current(0)
combo_plot2.current(0)
ttk.Button(frame2, text = 'Построить график' ,
           command =lambda: show(frame22,combo_plot1,combo_plot2)).place(x = 60, y = 30)
root.mainloop()