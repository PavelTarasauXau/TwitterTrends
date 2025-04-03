from State import State
from Polygon import Polygon
class Parser:
    def __init__(self,country):
        self.country = country # страна, которую парсер должен распарить

    def parse(self):
        for state in self.country.json_data: # state - массив полигонов
            any_state = State(name=state,color='white')
            for polygon in self.country.json_data[state]: # polygon - массив точек
                any_polygon = Polygon(polygon)
                any_state.polygons.append(any_polygon) # дополняем поле у state
            self.country.states.append(any_state) # дополняем поле у country
