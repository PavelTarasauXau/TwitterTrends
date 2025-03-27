class Node:
    def __init__(self, data=None, is_end=False, sentiment_score=None):
        self.data = data
        self.is_end = is_end
        self.sentiment_score = sentiment_score
        self.children = {}
