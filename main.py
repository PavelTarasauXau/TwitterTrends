from pathlib import Path
from datetime import datetime
from Tweet import Tweet
from TweetLocation import TweetLocation
from FileChoose import get_tweet_file
from ReadTweets import read_tweets
from SentimentDict import load_sentiment_dict
import csv
import tkinter as tk
from tkinter import ttk
#########################################
from tkinter import *
from tkinter import ttk
import json
from coords_transform import transform
from Country import *
from Data_Parser import Parser
from Map_Drawer import Drawer


def main():

    def prepare_tweets(name_of_file="tweet_topics/cali_tweets2014.txt"):
        file_name = name_of_file

        tweets = read_tweets(file_name)
        sentiment_dict = load_sentiment_dict("sentiments.csv")

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
            selection = 'tweet_topics/cali_tweets2014.txt'
        elif selection == 'Family':
            selection = "tweet_topics/family_tweets2014.txt"
        elif selection == 'Football':
            selection = "tweet_topics/football_tweets2014.txt"
        elif selection == 'High School':
            selection = 'tweet_topics/high_school_tweets2014.txt'
        elif selection == 'Movie':
            selection = 'tweet_topics/movie_tweets2014.txt'
        elif selection == 'Shopping':
            selection = 'tweet_topics/shopping_tweets2014.txt'
        elif selection == 'Snow':
            selection = 'tweet_topics/snow_tweets2014.txt'
        elif selection == 'Texas':
            selection = 'tweet_topics/texas_tweets2014.txt'
        elif selection == 'Weekend':
            selection = 'tweet_topics/weekend_tweets2014.txt'
        print(selection)
        canvas.delete('tweet')
        canvas.delete('tweet')
        state_of_map(prepare_tweets(selection),True)

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


    with open("states.json") as file:
        data = json.load(file)

    # создаём объект страны
    usa = Country('USA',data)
    # определяем границы карты для корректной работы функции transform
    usa.count_borders()
    # парсер которой создаёт экземеляры классов (State Polygon)
    def state_of_map(tweets,cond=False):
        parser = Parser(usa,tweets)
        parser.parse()

        drawer = Drawer(canvas,root.winfo_width(),root.winfo_height(),usa)
        # если мы вызываем функцию обновления состояния карты в ответ на выбор в списке
        # то тогда мы не рисуем всё заново а просто рисуем твитты
        if cond:
            drawer.draw_tweets()
        else:
            drawer.draw()
        # если мы вызываем из функции обновления значения списка то тогда обновляем значения полигонов
        if cond:
            drawer.update_polygons()

    state_of_map(prepare_tweets())

    root.mainloop()


if __name__ == "__main__":
    main()

