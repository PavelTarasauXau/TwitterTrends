from pathlib import Path
from datetime import datetime
from sentiment.Tweet import Tweet
from sentiment.TweetLocation import TweetLocation
from sentiment.ReadTweets import read_tweets
from sentiment.SentimentDict import load_sentiment_dict
import csv
import tkinter as tk
from tkinter import ttk
#########################################
from tkinter import *
from tkinter import ttk
import json
from ui.coords_transform import transform
from ui.Country import *
from ui.States_Parser import Parser
from ui.Map_Drawer import Drawer
#########################################
import sys
import os
import threading
import asyncio

# Добавляем корень проекта в sys.path, чтобы Python увидел папку bot
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Bot.app import main_func  # Импортируем бота

data_bot = {}


def run_bot():
    asyncio.run(main_func(data_bot))

def main():



    def prepare_tweets(name_of_file="Data/tweet_topics/cali_tweets2014.txt"):
        file_name = name_of_file

        tweets = read_tweets(file_name)
        sentiment_dict = load_sentiment_dict("Data/sentiments.csv")

        for tweet in tweets:
            tweet.calculate_sentiment(sentiment_dict)
        return tweets

    prepare_tweets()


    #######################################################
    root = Tk()
    root.title("TWITTER-TRENDS  ")
    root.geometry("1520x780")
    root.update_idletasks() # чтобы размеры применились до того как захочу их получить в качестве свойств окна

    #########
    topics = ["Cali", "Family", "Football", "High School", "Movie", "Shopping", "Snow", "Texas", "Weekend"]
    # по умолчанию будет выбран первый элемент из languages
    topic_var = StringVar(value=topics[0])




    def selected(event):
        # получаем выделенный элемент
        selection = combobox.get()
        if selection == "Cali":
            selection = 'Data/tweet_topics/cali_tweets2014.txt'
        elif selection == 'Family':
            selection = "Data/tweet_topics/family_tweets2014.txt"
        elif selection == 'Football':
            selection = "Data/tweet_topics/football_tweets2014.txt"
        elif selection == 'High School':
            selection = 'Data/tweet_topics/high_school_tweets2014.txt'
        elif selection == 'Movie':
            selection = 'Data/tweet_topics/movie_tweets2014.txt'
        elif selection == 'Shopping':
            selection = 'Data/tweet_topics/shopping_tweets2014.txt'
        elif selection == 'Snow':
            selection = 'Data/tweet_topics/snow_tweets2014.txt'
        elif selection == 'Texas':
            selection = 'Data/tweet_topics/texas_tweets2014.txt'
        elif selection == 'Weekend':
            selection = 'Data/tweet_topics/weekend_tweets2014.txt'
        print(selection)
        canvas.delete('tweet')
        canvas.delete('tweet')
        update_state_of_map(prepare_tweets(selection))

    combobox = ttk.Combobox(textvariable=topic_var, values=topics)
    combobox.pack(anchor=NW, padx=3, pady=3)
    combobox.bind("<<ComboboxSelected>>", selected)

    canvas = Canvas(bg="white", width=root.winfo_width(), height=root.winfo_height())
    canvas.pack(anchor=CENTER,expand=1)


    lbl = Label(text='MAP OF THE STATES')
    lbl.config(
        background='black',
        anchor=CENTER,
        borderwidth=2,
        font=('Arial',15),
        cursor='heart',
        padx=20,
        pady=10,
        foreground='white'
    )
    root.update_idletasks()

    canvas.create_window(root.winfo_width()/2, 50, anchor=CENTER, window=lbl, width=300, height=50)

    root_icon = PhotoImage(file='data/imgs/twitter.png')
    root.iconphoto(False,root_icon)


    with open("data\\states.json") as file:
        data = json.load(file)

    # создаём объект страны
    usa = Country('USA',data)

    # определяем границы карты для корректной работы функции transform
    usa.count_borders()




    # парсер которой создаёт экземеляры классов (State Polygon)
    def update_state_of_map(tweets):

        parser.update_states(tweets)
        drawer.update_polygons()
        # если мы вызываем функцию обновления состояния карты в ответ на выбор в списке
        # то тогда мы не рисуем всё заново а просто рисуем твитты

    parser = Parser(usa, prepare_tweets())
    parser.parse()

    data_bot['country'] = usa # передаём объект со штатами и твиттами актульный (бот его считывает)
    # он сможет также этот объект изменять
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()


    drawer = Drawer(canvas, root.winfo_width(), root.winfo_height(), usa)
    drawer.draw()

    root.mainloop()


if __name__ == "__main__":
    main()

