from ui.coords_transform import transform
from add_functionality.make_screen import save_screenshot
class Drawer:
    def __init__(self,canvas,width,height,country,root):
        self.country = country
        self.width = width
        self.height = height
        self.canvas = canvas
        self.root = root # для работы функции save_screenshot
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
                fill_color = None
                if state.sentiment == None:
                    fill_color = '#a7a09f'
                elif state.sentiment > 0:
                    fill_color = '#feff66'
                elif state.sentiment < 0:
                    fill_color = '#109eef'
                elif state.sentiment == 0:
                    fill_color = 'white'


                state.polygons_id.append( self.canvas.create_polygon(*dots, fill=fill_color, outline='black', width=1,tags='state') )

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

    def update_polygons(self):
        print('обновляем состояение полигонов')
        for state in self.country.states:
            state.sentiment = None
            state.calculate_sentiment()
            fill_color = None
            if state.sentiment == None:
                fill_color = '#a7a09f'
            elif state.sentiment > 0:
                fill_color = '#feff66'
            elif state.sentiment < 0:
                fill_color = '#109eef'
            elif state.sentiment == 0:
                fill_color = 'white'
            for id in state.polygons_id:
                self.canvas.itemconfig(id,fill=fill_color)
        save_screenshot(self.root)
        print('можно делать скриншот')


    def draw_tweets(self):
        for state in self.country.states:
            for tweet in state.tweets:
                t_x,t_y = transform(tweet.location.longitude,
                                  tweet.location.latitude,
                                  self.country.min_lon,
                                  self.country.max_lon,
                                  self.country.min_lat,
                                  self.country.max_lat,
                                  self.width,
                                  self.height)

                self.canvas.create_oval(t_x-3,t_y-3,t_x+3,t_y+3,fill='red',tags='tweet')
        save_screenshot(self.root)

    def delete_tweets(self):
        self.canvas.delete('tweet')
        save_screenshot(self.root)
