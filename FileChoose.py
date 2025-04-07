import os

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

    choice = input("Введите номер (0-8) или название файла: ").strip()

    base_path = "tweet_topics"

    match choice:
        case "0":
            file_name = "cali_tweets2014.txt"
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
        case _:
            file_name = choice

    return os.path.join(base_path, file_name)