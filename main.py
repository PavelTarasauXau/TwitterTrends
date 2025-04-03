from pathlib import Path
from datetime import datetime
from Tweet import Tweet
from TweetLocation import TweetLocation
from PrefixTree import PrefixTree, build_prefix_tree
from FileChoose import get_tweet_file
from ReadTweets import read_tweets
from SentimentDict import load_sentiment_dict
import csv
import tkinter as tk
from draw_map import creating_map

def main():
    file_name = get_tweet_file()

    tweets = read_tweets(file_name)
    sentiment_dict = load_sentiment_dict("sentiments.csv")

    for tweet in tweets:
        tweet.calculate_sentiment(sentiment_dict)
        print(tweet)

    creating_map()

if __name__ == "__main__":
    main()




