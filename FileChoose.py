import os
import sys

def get_tweet_file():
    print("Выберите файл для анализа:")
    print("0 - cali_tweets2014.txt (по умолчанию)")
    print("1 - family_tweets2014.txt")
    print("2 - football_tweets2014.txt")
    print("3 - high_school_tweets2014.txt")
    print("4 - movie_tweets2014.txt")
    print("5 - shopping_tweets2014.txt")
    print("6 - snow_tweets2014.txt")
    print("7 - texas_tweets2014.txt")
    print("8 - weekend_tweets2014.txt")
    print("9 - Выход из программы")

    while True:
        choice = input("Введите число от 0 до 8 для выбора файла или 9 для выхода: ").strip()
        base_path = "tweet_topics"

        match choice:
            case "0":
                return os.path.join(base_path, "cali_tweets2014.txt")
            case "1":
                return os.path.join(base_path, "family_tweets2014.txt")
            case "2":
                return os.path.join(base_path, "football_tweets2014.txt")
            case "3":
                return os.path.join(base_path, "high_school_tweets2014.txt")
            case "4":
                return os.path.join(base_path, "movie_tweets2014.txt")
            case "5":
                return os.path.join(base_path, "shopping_tweets2014.txt")
            case "6":
                return os.path.join(base_path, "snow_tweets2014.txt")
            case "7":
                return os.path.join(base_path, "texas_tweets2014.txt")
            case "8":
                return os.path.join(base_path, "weekend_tweets2014.txt")
            case "9":
                print("Выход из программы...")
                sys.exit(0)
            case _:
                print("Ошибка: введите число от 0 до 9!")
                continue  # Повторяем запрос