from tkinter import *
import json

from coords_transform import transform
from Country import *
from Data_Parser import Parser
from Map_Drawer import Drawer




def creating_map():

    root = Tk()
    root.title("TWITTER-TRENDS  ")
    root.geometry("1520x780")
    root.update_idletasks() # чтобы размеры применились до того как захочу их получить в качестве свойств окна



    canvas = Canvas(bg="white", width=root.winfo_width(), height=root.winfo_height())
    canvas.pack(anchor=CENTER,expand=1)


    lbl = Label(text='MAP OF THE STATES')
    lbl.config(
        background='black',
        anchor=CENTER,
        borderwidth=2,
        font=('Arial',15),
        cursor='heart',
        padx=20,
        pady=10,
        foreground='white'
    )
    root.update_idletasks()

    canvas.create_window(root.winfo_width()/2, 50, anchor=CENTER, window=lbl, width=300, height=50)

    root_icon = PhotoImage(file='data/imgs/twitter.png')
    root.iconphoto(False,root_icon)







    with open("states.json") as file:
        data = json.load(file)

    # создаём объект страны
    usa = Country('USA',data)
    # определяем границы карты для корректной работы функции transform
    usa.count_borders()
    # парсер которой создаёт экземеляры классов (State Polygon)
    parser = Parser(usa)
    parser.parse()
    # демонстрация созданных классов
    for shtat in usa.states:
        shtat.display_info()
        av_x,av_y = shtat.average_values()
        print(f'среднее значение координат: x - {av_x} y - {av_y} ')
    usa.display_info()

    # drawer - рисует карту
    drawer = Drawer(canvas,root.winfo_width(),root.winfo_height(),usa)
    drawer.draw()

    root.mainloop()