class Country:
    def __init__(self,name,json_data):
        self.name = name
        self.states = []
        # иницилизировал поля начальными значениями из файла
        self.json_data = json_data
        self.min_lon = -117.033359
        self.max_lon = -117.033359
        self.min_lat = 49.000239
        self.max_lat = 49.000239
    def display_info(self):
        print(f'Country {self.name} has {len(self.states)} states')
        print(f'Borders: min_lon - {self.min_lon}\n max_lon - {self.max_lon}'
              f'\n min_lat - {self.min_lat}\n max_lat - {self.max_lat}')

    def count_borders(self):
        for state in self.json_data:  # ключи(названия штатов)
            for polygon in self.json_data[state]:  # полигон
                for point in polygon:  # точка полигона
                    if point[0] < self.min_lon:
                        self.min_lon = point[0]
                    elif point[0] > self.max_lon:
                        self.max_lon = point[0]
                    if point[1] < self.min_lat:
                        self.min_lat = point[1]
                    elif point[1] > self.max_lat:
                        self.max_lat = point[1]