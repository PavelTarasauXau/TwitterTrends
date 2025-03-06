from pathlib import Path
from datetime import datetime


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

    def __repr__(self):
        return f"Tweet({self.location}, {self.datetime}, '{self.text[:30]}...')"


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


if __name__ == "__main__":
    tweets = read_tweets("cali_tweets2014.txt")
    print(tweets[:5])
