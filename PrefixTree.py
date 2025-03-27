from Node import Node

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, phrase, score):
        current_node = self.root
        words = phrase.split()

        for word in words:
            if word not in current_node.children:
                current_node.children[word] = Node(data=word)
            current_node = current_node.children[word]

        current_node.is_end = True
        current_node.sentiment_score = score

    def search(self, words, start_index):
        current_node = self.root
        matched_phrase = None
        sentiment_score = 0.0
        phrase_length = 0

        for i in range(start_index, len(words)):
            word = words[i]
            if word in current_node.children:
                current_node = current_node.children[word]
                if current_node.is_end:
                    matched_phrase = current_node.data
                    sentiment_score = current_node.sentiment_score
                    phrase_length = i - start_index + 1
            else:
                break

        return matched_phrase, sentiment_score, phrase_length


def build_prefix_tree(sentiment_dict):
    tree = PrefixTree()
    for phrase, score in sentiment_dict.items():
        tree.insert(phrase, score)
    return tree