from tkinter import *
from tkinter import ttk
import json
import math

root = Tk()
root.title("TWITTER-TRENDS  ")
root.geometry("1250x600")
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



canvas.create_polygon(
    10,10,
    100,40,
    200,100,
    40,90,
    10,10,
    fill='white',
    outline='black'
)




with open("states.json", "r") as file:
    data = json.load(file)




# начальные значения из файла
x_min = -117.033359
x_max = -117.033359
y_min = 49.000239
y_max = 49.000239


# функция для перевода из земных координат (широты и долготы) в плоские координаты
# и учёта границ canvas
def transform(lon, lat):
    """Преобразует координаты (lon, lat) в пиксели для Canvas"""
    x = (lon - x_min) / (x_max - x_min) * root.winfo_width()
    y = (1 - (lat - y_min) / (y_max - y_min)) * root.winfo_height()  # Инверсия Y
    return [x, y]

# первый ращ делаем цикл чтобы распарсить данные и сформировать границы координат
#  проходимся по ключам
for state in data: # ключи(названия штатов)
    for x in data[state]: # список полигонов
        for y in x: # контуры
            for polygon in y: # полигон
                if isinstance(polygon,list):
                        if polygon[0] < x_min: x_min = polygon[0]
                        elif polygon[0] > x_max: x_max = polygon[0]
                        if polygon[1] < y_min: y_min = polygon[1]
                        elif polygon[1] > y_max: y_max = polygon[1]

                   # print( transform(*polygon) )
                else:
                    if y[0] < x_min:
                        x_min = y[0]
                    elif y[0] > x_max:
                        x_max = y[0]
                    if y[1] < y_min:
                        y_min = y[1]
                    elif y[1] > y_max:
                        y_max = y[1]
                   # print( transform(*y) )



line_params = {
    "count":1,
    "dot_1":None,
    "dot_2":None
}
count = 0
def draw_line(dot):
    line_params[f'dot_{line_params["count"]}'] = dot
    line_params['count'] +=1
    if line_params['count'] == 3:
        canvas.create_line(*line_params["dot_1"],*line_params["dot_2"])
        line_params["count"] = 1 # обнуляем счётчик
        line_params["dot_1"] = line_params["dot_2"] # делаем вторую точку первой и по новой

print(x_min)
print(x_max)
print(y_min)
print(y_max)

# второй цикл нужен для того чтобы уже с готовыми границами получать правильные координаты и рисовать карту
for state in data: # ключи(названия штатов)
    print(f'{state} \n')
    for x in data[state]: # список полигонов
        for y in x: # контуры
            for polygon in y: # полигон
                if isinstance(polygon,list):
                   draw_line( transform(*polygon) )
                else:
                    draw_line( transform(*y) )

root.mainloop()
