from tkinter import *
from tkinter import ttk
import json
import threading



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







with open("states.json", "r") as file:
    data = json.load(file)




# начальные значения из файла
min_lon = -117.033359
max_lon = -117.033359
min_lat = 49.000239
max_lat = 49.000239


# функция для перевода из земных координат (широты и долготы) в плоские координаты
# и учёта границ canvas
def transform(lon, lat, padding=50):
    # Вычисляем коэффициенты масштабирования
    scale_x = (root.winfo_width() - 2 * padding) / (max_lon - min_lon)  # Масштаб по ширине
    scale_y = (root.winfo_height() - 2 * padding) / (max_lat - min_lat)  # Масштаб по высоте

    # Чтобы карта не была сжатой, можно выравнивать масштабы
    scale = min(scale_x, scale_y) * 3  # 1.2 растягивает карту немного

    # Переводим координаты в плоскую систему
    x = (lon - min_lon) * scale + padding
    y = (max_lat - lat) * scale + padding  # Инверсия, так как y идёт вниз

    return [x, y]


# первый ращ делаем цикл чтобы распарсить данные и сформировать границы координат
#  проходимся по ключам,
for state in data: # ключи(названия штатов)
    for polygon in data[state]: # полигон
        for point in polygon: # точка полигона
            if point[0] < min_lon: min_lon = point[0]
            elif point[0] > max_lon: max_lon = point[0]
            if point[1] < min_lat: min_lat = point[1]
            elif point[1] > max_lat: max_lat = point[1]



any_polygon = {
    'dots':[]
}

def draw_polygon(dot):
    if dot[0] in any_polygon['dots'] and dot[1] in any_polygon['dots']:
        any_polygon['dots'].extend(dot)
        # рисуем полигон
        print('рисую полигон')
        print(any_polygon['dots'])
        canvas.create_polygon(*any_polygon['dots'],fill='white',outline='black',width=1)
        # очищаем промежуточный объект
        any_polygon['dots'].clear()
    else:
        any_polygon['dots'].extend(dot)




# второй цикл нужен для того чтобы уже с готовыми границами получать правильные координаты и рисовать карту
for state in data: # ключи(названия штатов)
    print(f'draw state - {state}')
    count = 0
    for polygon in data[state]: # полигон
        count += 1
        for point in polygon: # точка полигона
            got_coords = transform(*point)
            # print(got_coords)
            draw_polygon( got_coords )
    print(count)

root.mainloop()
