
from tkinter import *
from PIL import Image
import os

def save_canvas_as_png(canvas):
    # Временно сохраняем как EPS (PostScript)
    eps_file = "temp_map.eps"
    canvas.postscript(file=eps_file, colormode='color')

    # Конвертируем в PNG
    img = Image.open(eps_file)
    img.save('C:\\Users\\tazhu\\PycharmProjects\\OOP_project\\Data\\imgs\\map', "png")

    # Удаляем временный файл, если хочешь
    os.remove(eps_file)

# Пример использования

