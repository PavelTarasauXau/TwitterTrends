from pathlib import Path
from datetime import datetime
from Tweet import Tweet
from TweetLocation import TweetLocation
from PrefixTree import PrefixTree, build_prefix_tree
import csv

#change the way the prefix tree works
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

    return build_prefix_tree(sentiment_dict)


if __name__ == "__main__":
    tweets = read_tweets("cali_tweets2014.txt")
    sentiment_dict = load_sentiment_dict("sentiments.csv")

    for tweet in tweets:
        tweet.calculate_sentiment(sentiment_dict)

    for tweet in tweets:
        print(tweet)
