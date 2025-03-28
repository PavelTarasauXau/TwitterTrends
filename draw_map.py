from tkinter import *
from tkinter import ttk
import json



root = Tk()
root.title("TWITTER-TRENDS  ")
root.geometry("1920x1080")
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
#  проходимся по ключам,
for state in data: # ключи(названия штатов)
    for x in data[state]: # список полигонов
        for y in x: # контуры
            for polygon in y: # полигон
                if isinstance(polygon,list):
                    if polygon[0] < x_min: x_min = polygon[0]
                    elif polygon[0] > x_max: x_max = polygon[0]
                    if polygon[1] < y_min: y_min = polygon[1]
                    elif polygon[1] > y_max: y_max = polygon[1]
                else:
                    if y[0] < x_min:
                        x_min = y[0]
                    elif y[0] > x_max:
                        x_max = y[0]
                    if y[1] < y_min:
                        y_min = y[1]
                    elif y[1] > y_max:
                        y_max = y[1]



any_polygon = {
    'dots':[]
}
count = 0
def draw_polygon(dot):
    any_polygon['dots'].append(dot)
    if dot in any_polygon['dots']:
        # рисуем полигон
        canvas.create_polygon(*any_polygon['dots'],fill='red',outline='black')
        # очищаем промежуточный объект
        any_polygon['dots'].clear()


print(x_min)
print(x_max)
print(y_min)
print(y_max)
print('\n')

# второй цикл нужен для того чтобы уже с готовыми границами получать правильные координаты и рисовать карту
for state in data: # ключи(названия штатов)
    print(f'draw state - {state}')
    for x in data[state]: # список полигонов
        for y in x: # контуры
            for polygon in y: # полигон
                if isinstance(polygon,list):
                    got_coords = transform(*polygon)
                    print(got_coords)
                    draw_polygon( got_coords )
                else:
                    got_coords = transform(*y)
                    print(got_coords)
                    draw_polygon( got_coords )

root.mainloop()