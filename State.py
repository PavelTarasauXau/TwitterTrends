class State:
    def __init__(self,name,color):
        self.name = name
        self.polygons = []
        self.color = color
    def average_values(self):
        sum_x = 0
        sum_y = 0
        count = 0
        for polygon in self.polygons:
            for dot in polygon.dots:
                sum_x += dot[0]
                sum_y += dot[1]
                count += 1
        return [sum_x/count,sum_y/count]
    def display_info(self):
        print(f'\n\nштат {self.name}')
        for i in range(len(self.polygons)):
            print(f'полигон {i+1}')
            print('его точки : ',end=' ')
            print(self.polygons[i].display_info())


