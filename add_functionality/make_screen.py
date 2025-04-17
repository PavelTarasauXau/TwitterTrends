from PIL import ImageGrab
import os
def save_screenshot(window):
    print('сделали скриншот')
    # Получаем координаты окна
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    width = window.winfo_width()
    height = window.winfo_height()
    save_directory = "C:\\Users\\tazhu\\PycharmProjects\\OOP_project\\Data\\imgs"  # Укажите нужный путь
    save_filename = "screenshot.png"
    save_path = os.path.join(save_directory, save_filename)
    # Делаем скриншот в области окна
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    # Сохраняем изображение (перезапишется, если файл уже существует)
    screenshot.save(save_path)