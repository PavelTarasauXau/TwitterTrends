class State:
    def __init__(self,name):
        self.name = name
        self.polygons = []
        self.tweets = []
        self.sentiment = None
        self.min_lon = -117.033359
        self.max_lon = -117.033359
        self.min_lat = 49.000239
        self.max_lat = 49.000239
        self.polygons_id = []
    def average_values(self):
        sum_x = 0
        sum_y = 0
        count = 0
        for polygon in self.polygons:
            for dot in polygon.dots:
                sum_x += dot[0]
                sum_y += dot[1]
                count += 1
        self.av_x = sum_x/count
        self.av_y = sum_y/count
    def calculate_sentiment(self):
        for tweet in self.tweets:
            if tweet.sentiment != None:
                # по умолчанию значение поля sentiment = None, делаем проверку на это
                if self.sentiment != None:
                    self.sentiment += tweet.sentiment
                else:
                    self.sentiment = tweet.sentiment
    def display_info(self):
        print(f'\n\nштат {self.name}')
        print(self.min_lon, self.max_lon, self.min_lat, self.max_lat)
        for i in range(len(self.polygons)):
            print(f'полигон {i+1}')
            print('его точки : ',end=' ')
            print(self.polygons[i].display_info())

