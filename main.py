from pathlib import Path
from datetime import datetime
from Tweet import Tweet
from TweetLocation import TweetLocation
from PrefixTree import PrefixTree, build_prefix_tree
import csv
import tkinter as tk

def read_tweets(file_name):
    file_path = Path(__file__).parent / file_name
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
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return tweets


def load_sentiment_dict(file_name):
    file_path = Path(__file__).parent / file_name
    sentiment_dict = {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) != 2:
                    continue
                phrase, score = row[0].strip().lower(), float(row[1])
                sentiment_dict[phrase] = score
        print(f"Загружено {len(sentiment_dict)} фраз с коэффициентами сентимента.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return build_prefix_tree(sentiment_dict)


if __name__ == "__main__":
    print("Выберите файл для анализа:")
    print("1 - family_tweets2014.txt")
    print("2 - football_tweets2014.txt")
    print("3 - high_school_tweets2014.txt")
    print("4 - movie_tweets2014.txt")
    print("5 - shopping_tweets2014.txt")
    print("6 - snow_tweets2014.txt")
    print("7 - texas_tweets2014.txt")
    print("8 - weekend_tweets2014.txt")
    print("9 - cali_tweets2014.txt (по умолчанию)")

    choice = input("Input number from 1 to 9 to choose tweet topic: ").strip()

    match choice:
        case "1":
            file_name = "family_tweets2014.txt"
        case "2":
            file_name = "football_tweets2014.txt"
        case "3":
            file_name = "high_school_tweets2014.txt"
        case "4":
            file_name = "movie_tweets2014.txt"
        case "5":
            file_name = "shopping_tweets2014.txt"
        case "6":
            file_name = "snow_tweets2014.txt"
        case "7":
            file_name = "texas_tweets2014.txt"
        case "8":
            file_name = "weekend_tweets2014.txt"
        case "9" | "":
            file_name = "cali_tweets2014.txt"
        case _:
            file_name = choice

    tweets = read_tweets(file_name)
    sentiment_dict = load_sentiment_dict("sentiments.csv")

    for tweet in tweets:
        tweet.calculate_sentiment(sentiment_dict)

    for tweet in tweets:
        print(tweet)




