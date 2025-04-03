# файл для выбора .txt файла

def get_tweet_file():

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

    choice = input("Введите номер (1-9) или название файла: ").strip()

    match choice:
        case "1": return "family_tweets2014.txt"
        case "2": return "football_tweets2014.txt"
        case "3": return "high_school_tweets2014.txt"
        case "4": return "movie_tweets2014.txt"
        case "5": return "shopping_tweets2014.txt"
        case "6": return "snow_tweets2014.txt"
        case "7": return "texas_tweets2014.txt"
        case "8": return "weekend_tweets2014.txt"
        case "9" | "": return "cali_tweets2014.txt"
        case _: return choice