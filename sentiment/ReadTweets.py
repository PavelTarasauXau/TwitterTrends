#файл для чтения твитов из .txt файла

from pathlib import Path
from datetime import datetime
from sentiment.Tweet import Tweet
from sentiment.TweetLocation import TweetLocation
import csv
import tkinter as tk

def read_tweets(file_name):
    file_path = file_name
    tweets = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("\t")
                if len(parts) < 4:
                    continue

                coords = parts[0].strip("[]").split(", ")
                location = TweetLocation(float(coords[0]), float(coords[1]))
                dt = datetime.strptime(parts[2], "%Y-%m-%d %H:%M:%S")
                text = parts[3]

                tweets.append(Tweet(location, dt, text))

        print(f"Прочитано {len(tweets)} твитов.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден. (файл с твиттами)")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return tweets
