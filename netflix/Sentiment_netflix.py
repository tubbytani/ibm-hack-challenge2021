from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
import re
import nltk
import os
import numpy as np
import pandas as pd
import tweepy
import sys
from textblob import TextBlob
from nltk.corpus import stopwords
def final():
    stoplist = set(stopwords.words("english"))

    consumer_key=""
    consumer_secret="" 
    access_token=""
    access_token_secret=""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    analyser = SentimentIntensityAnalyzer()


    def percentage(part, whole):
        return 100 * float(part)/float(whole)


    keyword = "netflix"
    num_tweet = 100
    last_id = None

    tweets = tweepy.Cursor(api.search,  q=keyword, lang='en', max_id=last_id,
                        tweets_mode="extended").items(num_tweet)
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    tweet_db = []
    neutral_list = []
    negative_list = []
    positive_list = []
    for tweet in tweets:

        tweet_db.append(tweet.text)
        analysis = TextBlob(tweet.text)
        score = analyser.polarity_scores(tweet.text)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']
        polarity += analysis.sentiment.polarity

        if neg > pos:
            negative_list.append(tweet.text)
            negative += 1

        elif pos > neg:
            positive_list.append(tweet.text)
            positive += 1

        elif pos == neg:
            neutral_list.append(tweet.text)
            neutral += 1

    positive = percentage(positive, num_tweet)
    negative = percentage(negative, num_tweet)
    neutral = percentage(neutral, num_tweet)
    polarity = percentage(polarity, num_tweet)
    positive = format(positive, '.1f')
    negative = format(negative, '.1f')
    neutral = format(neutral, '.1f')


    tweet_db = pd.DataFrame(tweet_db)
    neutral_list = pd.DataFrame(neutral_list)
    negative_list = pd.DataFrame(negative_list)
    positive_list = pd.DataFrame(positive_list)

    tweet_db.drop_duplicates(inplace=True)

    tweets = pd.DataFrame(tweet_db)
    tweets["text"] = tweets[0]


    def remove_rt(x): return re.sub('RT @\w+: ', " ", x)


    def rt(x): return re.sub(
        "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x)


    tweets["text"] = tweets.text.map(remove_rt).map(rt)
    tweets["text"] = tweets.text.str.lower()


    tweets[['polarity', 'subjectivity']] = tweets['text'].apply(
        lambda Text: pd.Series(TextBlob(Text).sentiment))
    for index, row in tweets['text'].iteritems():
        score = analyser.polarity_scores(row)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        # comp = score['compound']
        if neg > pos:
            tweets.loc[index, 'sentiment'] = "negative"
        elif pos > neg:
            tweets.loc[index, 'sentiment'] = "positive"
        else:
            tweets.loc[index, 'sentiment'] = "neutral"
        tweets.loc[index, 'neg'] = neg
        tweets.loc[index, 'neu'] = neu
        tweets.loc[index, 'pos'] = pos
        # tweets.loc[index, 'compound'] = comp
        #tweets.to_csv('sentimentn.csv')


    tweets_negative = tweets[tweets["sentiment"] == "negative"]
    tweets_positive = tweets[tweets["sentiment"] == "positive"]
    tweets_neutral = tweets[tweets["sentiment"] == "neutral"]


    def count_words(data, feature):
        total = data.loc[:, feature].value_counts(dropna=False)
        percentage = round(data.loc[:, feature].value_counts(
            dropna=False, normalize=True)*100, 2)
        count_df = []
        count_df = pd.concat([total, percentage], axis=1,
                            keys=['Total', 'Percentage'])
        return count_df


    count_df = count_words(tweets, "sentiment")
    return(count_df.to_dict())
    count_df = count_words(tweets, "sentiment")
    print(count_df.to_dict())
