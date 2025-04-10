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

        text_without_punctuation = re.sub(r"[^\w\s'-]", "", self.text)
        words = text_without_punctuation.lower().split()
        words_len = len(words)

        i = 0
        while i < words_len:
            remaining_words = words_len - i
            phrase_run = min(7, remaining_words)

            matched = False
            while phrase_run > 0 and not matched:
                phrase = ' '.join(words[i:i + phrase_run])
                idx = binary_search(keys, phrase)

                if idx != -1:
                    sentiment_score += sentiment_dict[phrase]
                    i += phrase_run
                    matched = True
                else:
                    phrase_run -= 1

            if not matched:
                i += 1

        self.sentiment = sentiment_score if sentiment_score != 0.0 else None
    def __repr__(self):
        return f"Tweet({self.location}, {self.datetime}, Sentiment={self.sentiment}, '{self.text[:30]}...')"

