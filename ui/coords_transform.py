def transform(lon, lat,min_lon,max_lon,min_lat,max_lat,width,height,padding=30):
    # Вычисляем коэффициенты масштабирования
    scale_x = (width - 2 * padding) / (max_lon - min_lon)  # Масштаб по ширине
    scale_y = (height - 2 * padding) / (max_lat - min_lat)  # Масштаб по высоте

    # Чтобы карта не была сжатой, можно выравнивать масштабы
    scale = min(scale_x, scale_y) * 2.7

    # Переводим координаты в плоскую систему
    x = (lon - min_lon) * scale + padding
    y = (max_lat - lat) * scale + padding  # Инверсия, так как y идёт вниз
    return [x, y]