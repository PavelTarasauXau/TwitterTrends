from pathlib import Path
from datetime import datetime
import csv


class TweetLocation:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"TweetLocation(lat={self.latitude}, lon={self.longitude})"


class Tweet:
    def __init__(self, location: TweetLocation, dt: datetime, text: str):
        self.location = location
        self.datetime = dt
        self.text = text
        self.sentiment = 0.0##

    #добавить очищение текста от знаков препинания перед анализом
    def calculate_sentiment(self, sentiment_dict):
        words = self.text.lower().split()
        sentiment_score = sum(sentiment_dict.get(word, 0) for word in words)
        self.sentiment = sentiment_score

    def __repr__(self):
        return f"Tweet({self.location}, {self.datetime}, Sentiment={self.sentiment}, '{self.text[:30]}...')"


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
                word, score = row[0].strip().lower(), float(row[1])
                sentiment_dict[word] = score
        print(f"Загружено {len(sentiment_dict)} слов с коэффициентами сентимента.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return sentiment_dict


if __name__ == "__main__":
    tweets = read_tweets("cali_tweets2014.txt")
    sentiment_dict = load_sentiment_dict("sentiments.csv")

    for tweet in tweets:
        tweet.calculate_sentiment(sentiment_dict)

    print(tweets[:5])



