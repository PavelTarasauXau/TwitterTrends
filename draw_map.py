


import json
import matplotlib.pyplot as plt

# Загружаем JSON-файл
with open("states.json", "r") as file:
    states_data = json.load(file)

# Создаем фигуру
fig, ax = plt.subplots(figsize=(10, 8))

# Обрабатываем каждый штат
for state, regions in states_data.items():
    for region in regions:
        for polygon in region:
            # Разбираем координаты
            lons, lats = zip(*polygon)  # Разделяем широту и долготу
            ax.plot(lons, lats, label=state)

# Добавляем подписи и оформление
ax.set_title("Границы штатов")
ax.set_xlabel("Долгота")
ax.set_ylabel("Широта")
ax.legend()
ax.grid(True)

# Отображаем карту
plt.show()
