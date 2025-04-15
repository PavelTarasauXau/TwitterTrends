from ui.State import State
from ui.Polygon import Polygon
class Parser: # парсер котоорый парсит штаты и уже отпаршенные твиты соотносит со штатами
    def __init__(self,country,tweets):
        self.country = country # страна, которую парсер должен распарить
        self.tweets = tweets
    def parse(self):
        for state in self.country.json_data: # state - массив полигонов
            any_state = State(name=state)
            for polygon in self.country.json_data[state]: # polygon - массив точек

                for dot in polygon: # формируем границы
                    if dot[0] < any_state.min_lon:
                        any_state.min_lon = dot[0]
                    elif dot[0] > any_state.max_lon:
                        any_state.max_lon = dot[0]
                    elif dot[1] < any_state.min_lat:
                        any_state.min_lat = dot[1]
                    elif dot[1] > any_state.max_lat:
                        any_state.max_lat = dot[1]

                any_polygon = Polygon(polygon)
                any_state.polygons.append(any_polygon) # дополняем поле у state
                any_state.average_values() # "заставляем" класс посчитать свои средний значения

            self.country.states.append(any_state) # дополняем поле у country

        # после того как сформировали классы проходися по списку States у переданного класса Country
        for tweet in self.tweets:
            for state in self.country.states:
                # если координаты твитта попадают в диапазон границы координат штата то добавляем в список твиттов штата
                if (tweet.location.longitude >= state.min_lon and
                    tweet.location.longitude <= state.max_lon and
                    tweet.location.latitude >= state.min_lat and
                    tweet.location.latitude <= state.max_lat):
                    state.tweets.append(tweet)

        # когда сформировали штаты и привязали к ним соответствующие твитты
        # считаем сентимент каждого штата
        for state in self.country.states:
            state.calculate_sentiment()

    def update_states(self,tweets):
        self.tweets = tweets # обновляем твитты у парсера
        for state in self.country.states:
            state.tweets.clear() # очищаем у каждого штата принадлежащие ему твитты
        for tweet in self.tweets:
            for state in self.country.states:
                # если координаты твитта попадают в диапазон границы координат штата то добавляем в список твиттов штата
                if (tweet.location.longitude >= state.min_lon and
                    tweet.location.longitude <= state.max_lon and
                    tweet.location.latitude >= state.min_lat and
                    tweet.location.latitude <= state.max_lat):
                    state.tweets.append(tweet)
        for state in self.country.states:
            state.calculate_sentiment()




