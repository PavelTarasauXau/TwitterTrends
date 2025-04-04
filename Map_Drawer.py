from coords_transform import transform

class Drawer:
    def __init__(self,canvas,width,height,country):
        self.country = country
        self.width = width
        self.height = height
        self.canvas = canvas
    def draw(self):
        for state in self.country.states:
            for polygon in state.polygons:
                dots = []
                for dot in polygon.dots:
                    dots.extend( transform(dot[0],
                                           dot[1],
                                           self.country.min_lon,
                                           self.country.max_lon,
                                           self.country.min_lat,
                                           self.country.max_lat,
                                           self.width,
                                           self.height) )
                fill_color = 'gray'
                if state.sentiment > 0:
                    fill_color = 'yellow'
                elif state.sentiment < 0:
                    fill_color = 'blue'
                elif state.sentiment == 0:
                    fill_color = 'white'

                self.canvas.create_polygon(*dots, fill=fill_color, outline='black', width=1)
                # очищаем промежуточный объект
                dots.clear()

            av_x,av_y = transform(state.av_x,
                                  state.av_y,
                                  self.country.min_lon,
                                  self.country.max_lon,
                                  self.country.min_lat,
                                  self.country.max_lat,
                                  self.width,
                                  self.height)
            self.draw_text(av_x,av_y,state.name)


    def draw_text(self,x,y,txt):
        if txt == 'HI':
            x -= 10
            y += 10
        elif txt == 'PR':
            y += 15
        elif txt == 'AK':
            y -= 50
        elif txt == 'WA':
            x += 15
        elif txt == 'ID':
            y += 10
        elif txt == 'MT':
            y -= 10
            x += 15
        elif txt == 'AZ':
            x += 15

        self.canvas.create_text(x,y,text=txt,font='Arial 11 bold',fill='black',anchor='center')


