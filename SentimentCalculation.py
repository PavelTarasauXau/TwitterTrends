from pathlib import Path
from datetime import datetime
import csv
import re
from collections import defaultdict


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
        text_without_punctuation = re.sub(r"[^\w\s'-]", "", self.text)
        words = text_without_punctuation.lower().split()

        sentiment_score = 0.0
        word_count = len(words)

        trie = sentiment_dict['trie']
        scores = sentiment_dict['scores']

        i = 0
        while i < word_count:
            current_node = trie
            matched_phrase = None
            phrase_length = 0

            for j in range(i, word_count):
                word = words[j]
                if word in current_node:
                    current_node = current_node[word]
                    if '_' in current_node:
                        matched_phrase = current_node['_']
                        phrase_length = j - i + 1
                else:
                    break

            if matched_phrase:
                sentiment_score += scores[matched_phrase]
                i += phrase_length
            else:
                i += 1

        self.sentiment = sentiment_score

    def __repr__(self):
        return f"Tweet({self.location}, {self.datetime}, Sentiment={self.sentiment}, '{self.text[:30]}...')"


def build_trie(sentiment_dict):
    trie = {}
    scores = {}

    for phrase, score in sentiment_dict.items():
        words = phrase.split()
        current_node = trie

        for word in words:
            if word not in current_node:
                current_node[word] = {}
            current_node = current_node[word]
        current_node['_'] = phrase
        scores[phrase] = score

    return {'trie': trie, 'scores': scores}


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

    return build_trie(sentiment_dict)

#перенести функцию main когда все будет готово
if __name__ == "__main__":
    tweets = read_tweets("cali_tweets2014.txt")
    sentiment_dict = load_sentiment_dict("sentiments.csv")

    for tweet in tweets:
        tweet.calculate_sentiment(sentiment_dict)

    for tweet in tweets:
        print(tweet)
