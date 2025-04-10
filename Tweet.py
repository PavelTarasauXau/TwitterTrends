import re
from BinarySearch import binary_search

class Tweet:
    def __init__(self, location, dt, text):
        self.location = location
        self.datetime = dt
        self.text = text
        self.sentiment = None

    def calculate_sentiment(self, sentiment_dict):
        keys = list(sentiment_dict.keys())
        sentiment_score = 0.0

        # Очищаем текст и разбиваем на слова
        text_without_punctuation = re.sub(r"[^\w\s'-]", "", self.text)
        words = text_without_punctuation.lower().split()
        words_len = len(words)

        i = 0
        while i < words_len:
            remaining_words = words_len - i
            phrase_run = min(7, remaining_words)  # Максимальная длина фразы - 7 слов

            matched = False
            while phrase_run > 0 and not matched:
                phrase = ' '.join(words[i:i + phrase_run])
                # Используем нашу функцию бинарного поиска вместо bisect
                idx = binary_search(keys, phrase)

                if idx != -1:  # Фраза найдена
                    sentiment_score += sentiment_dict[phrase]
                    i += phrase_run  # Перескакиваем на конец найденной фразы
                    matched = True
                else:
                    phrase_run -= 1  # Пробуем более короткую фразу

            if not matched:
                i += 1  # Не нашли фразу, переходим к следующему слову

        self.sentiment = sentiment_score if sentiment_score != 0.0 else None
    def __repr__(self):
        return f"Tweet({self.location}, {self.datetime}, Sentiment={self.sentiment}, '{self.text[:30]}...')"

