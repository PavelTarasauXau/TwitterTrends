import re
from PrefixTree import PrefixTree


class Tweet:
    def __init__(self, location, dt, text):
        self.location = location
        self.datetime = dt
        self.text = text
        self.sentiment = None

    def calculate_sentiment(self, sentiment_tree):
        text_without_punctuation = re.sub(r"[^\w\s'-]", "", self.text)
        words = text_without_punctuation.lower().split()

        sentiment_score = 0.0
        i = 0

        while i < len(words):
            matched_phrase, score, phrase_length = sentiment_tree.search(words, i)
            if matched_phrase:
                sentiment_score += score
                i += phrase_length
            else:
                i += 1

        self.sentiment = sentiment_score

    def __repr__(self):
        return f"Tweet({self.location}, {self.datetime}, Sentiment={self.sentiment}, '{self.text[:30]}...')"

