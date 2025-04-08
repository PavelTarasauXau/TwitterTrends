import bisect
import re

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

        i = 0
        while i < len(words):

            remaining_words = len(words) - i

            if remaining_words > 7:
                phrase_run = 7
            else:
                phrase_run = remaining_words

            matched = False

            while phrase_run > 0:
                phrase = ' '.join(words[i:i + phrase_run])
                idx = bisect.bisect_left(keys, phrase)

                if idx < len(keys) and keys[idx] == phrase:
                    sentiment_score += sentiment_dict[phrase]
                    i += phrase_run
                    matched = True
                    break
                else:
                    phrase_run -= 1

            if not matched:
                i += 1

        self.sentiment = sentiment_score if sentiment_score != 0.0 else None

    def __repr__(self):
        return f"Tweet({self.location}, {self.datetime}, Sentiment={self.sentiment}, '{self.text[:30]}...')"
