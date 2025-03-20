from pathlib import Path
from datetime import datetime
import csv
#test

class TweetLocation:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"TweetLocation(lat={self.latitude}, lon={self.longitude})"


class Tweet:
    def __init__(self, location, dt, text):
        self.location = location
        self.datetime = dt
        self.text = text
        self.sentiment = None

    def calculate_sentiment(self, sentiment_dict):
        punctuations = [".", ",", "!", "?", ";", ":", "-", "—", "(", ")", "[", "]", "{", "}", "'", '"', "`", "“", "”", "…"]

        text_without_punctuation = self.text
        for p in punctuations:
            text_without_punctuation = text_without_punctuation.replace(p, "")

        words = text_without_punctuation.lower().split() #разбиваем текст на список слов и приводим к нижнему регистру
        sentiment_score = 0.0 #переменная для хранения общего сентимента
        found_phrases = False #флаг, указывающий найдены ли фразы

        def get_phrase_length(phrase):
            return len(phrase.split())

        #сортировка словаря(ключей) в порядке убывания
        sorted_phrases = sorted(sentiment_dict.keys(), key=get_phrase_length, reverse=True)

        for phrase in sorted_phrases:
            phrase_words = phrase.split()
            phrase_length = len(phrase_words)

            for i in range(len(words) - phrase_length + 1):
                if words[i:i + phrase_length] == phrase_words:
                    sentiment_score += sentiment_dict[phrase]
                    found_phrases = True

                    words[i:i + phrase_length] = [None] * phrase_length

        if found_phrases:
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
                phrase, score = row[0].strip().lower(), float(row[1])
                sentiment_dict[phrase] = score
        print(f"Загружено {len(sentiment_dict)} фраз с коэффициентами сентимента.")
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

    for tweet in tweets:
        print(tweet)