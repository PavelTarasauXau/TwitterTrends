from pathlib import Path
from datetime import datetime
from Tweet import Tweet
from TweetLocation import TweetLocation
from PrefixTree import PrefixTree, build_prefix_tree
from FileChoose import get_tweet_file
from ReadTweets import read_tweets
from SentimentDict import load_sentiment_dict
import csv
import tkinter as tk
#########################################
from tkinter import *
from tkinter import ttk
import json

from coords_transform import transform
from Country import *
from Data_Parser import Parser
from Map_Drawer import Drawer




def main():
    file_name = get_tweet_file()

    tweets = read_tweets(file_name)
    sentiment_dict = load_sentiment_dict("sentiments.csv")

    for tweet in tweets:
        tweet.calculate_sentiment(sentiment_dict)

    #######################################################
    root = Tk()
    root.title("TWITTER-TRENDS  ")
    root.geometry("1520x780")
    root.update_idletasks() # чтобы размеры применились до того как захочу их получить в качестве свойств окна

    #########
    topics = ["Cali", "Family", "Football", "High School", "Movie", "Shopping", "Snow", "Texas", "Weekend"]
    # по умолчанию будет выбран первый элемент из languages
    topic_var = StringVar(value=topics[0])

    label = ttk.Label(textvariable=topic_var)
    label.pack(anchor=NW, padx=6, pady=6)

    combobox = ttk.Combobox(textvariable=topic_var, values=topics)
    combobox.pack(anchor=NW, padx=6, pady=6)

    print(combobox.get())
    ########

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
    parser = Parser(usa,tweets)
    parser.parse()

    # демонстрация созданных классов
    for shtat in usa.states:
        print(f'штааат {shtat.name}')
        print(shtat.sentiment)
        print(f'кол-во твиттов - {len(shtat.tweets)}')
        # shtat.display_info()
        # av_x,av_y = shtat.average_values()
        # print(f'среднее значение координат: x - {av_x} y - {av_y} ')
    usa.display_info()

    # drawer - рисует карту
    drawer = Drawer(canvas,root.winfo_width(),root.winfo_height(),usa)
    drawer.draw()

    root.mainloop()
if __name__ == "__main__":
    main()

