#файл для загрузки словаря сентиментов и преобразования его в дерево
from pathlib import Path
#from PrefixTree import build_prefix_tree
import csv

def load_sentiment_dict(file_name):
    file_path = file_name
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
        print(f"Файл {file_path} не найден. (файл с сентиментами)")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return sentiment_dict

