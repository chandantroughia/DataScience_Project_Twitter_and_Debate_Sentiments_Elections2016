import tweepy
import json
import requests

def query_online_sentiment_api(sentence):
    url = "http://text-processing.com/api/sentiment/"
    response = requests.post(url, data={"text": sentence})

    print(response)
    print(response.text)

def get_tweets(api):
    """ Make two lists of @realDonaldTrump and @HillaryClinton tweets
    from July 27th 2016 to September 31st.

    trump oldest tweet id = 758452289376022529
    hillary oldest tweet id = 758452201341747200

    gary johnson oldest tweet id = 758104722607837186

        api: twitter tweepy API
    """

    trump_tweets_json = []
    for tweet in tweepy.Cursor(api.user_timeline,
                               id="realDonaldTrump",
                               since_id=758452289376022529).items():
        trump_tweets_json.append(tweet._json)
        trump_tweets.append(tweet)

    # print(len(trump_tweets))
    # print(trump_tweets)

    f_json = open("trupm_tweets_json.json", "w")
    f_json.write(json.dumps(trump_tweets_json))
    f_json.close()


    hill_tweets_json = []
    for tweet in tweepy.Cursor(api.user_timeline,
                               id="HillaryClinton",
                               since_id=758452201341747200).items():
        hill_tweets_json.append(tweet._json)

    # print(hill_tweets)

    f_json = open("hill_tweets_json.json", "w")
    f_json.write(json.dumps(hill_tweets_json))
    f_json.close()


    # print(hill_tweets)

    # return trump_tweets, hill_tweets

def make_api():
    """ Make the API using one of a few tokens for 45 queries every 15 min. """
    # # twitter data science
    consumer_key = "Op1h3AT8jrCiI2rmcdlZdc94r"
    consumer_secret = "MTz5bDQyjif9P3VMg7eJ2FKZFo1WOdcljETKLFznS8SQ0SZHXZ"
    access_token = "37131221-sAexAda1kRhXdH4i3NITumDPKWLCOJ1JUlMNJIiZR"
    access_token_secret = "DRBuhi8jzIkpdlG9p74zzOSirPD0AtJIyVgUzywpaUKcv"

    # # ITWS 4200 lab
    # consumer_key = "CkXTNz0ODXZ3RWftYhuT2Q5c1"
    # consumer_secret = "2HpMvW3Yh7JMdv1uP5gkkIWXSTag34L2oZtvkTC8qxuCgiqbr0"
    # access_token = "37131221-Do49jxHkueRpNgk5jfQDrMkeaALaLR14FZZh57HNt"
    # access_token_secret = "nCGBL1mnxr78ma0MAoDwcgE317SmLgNybOFo8IBawy7bV"

    # # FRC Shirt exchange
    # consumer_key = "QmEduN3tKqH2aq2Y3xRleA"
    # consumer_secret = "qMaKdUrEZKdYOcduUg8875FpgLVGgIMcVgklpfBVw"
    # access_token = "37131221-JbPN1tX7nTr6er8f6yvN573QhQsZbWCFgPyl9FLWV"
    # access_token_secret = "IJttSpA1rSU1aO8WmvrcMInpYn1XN5VU9lqJ01yGyfoal"


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api


def score_tweets(trump_tweets, hill_tweets):
    """Load tweets from cache and score them with the online API."""
    # print("scoring trump tweets")
    # for tweet in trump_tweets:
    #     tweet["sentiment"] = query_online_sentiment_api(tweet["text"])

    # # save them again
    # with open("trump_tweets_scored.json", "w") as f:
    #         f.write(json.dumps(trump_tweets))

    print("scoring hill tweets")
    for tweet in hill_tweets:
        tweet["sentiment"] = query_online_sentiment_api(tweet["text"])

    with open("hill_tweets_scored.json", "w") as f:
            f.write(json.dumps(hill_tweets))

def read_from_cache():
    """ Read tweets from the stored json files."""
    trump_tweets = []
    with open("trupm_tweets_json.json", "r") as f:
        trump_tweets = json.loads(f.read())

    hill_tweets = []
    with open("hill_tweets_json.json", "r") as f:
        hill_tweets = json.loads(f.read())

    print(len(trump_tweets))
    print("")
    print(len(hill_tweets))

    return trump_tweets, hill_tweets


def query_online_sentiment_api(sentence):
    url = "http://text-processing.com/api/sentiment/"
    response = requests.post(url, data={"text": sentence})

    # print(response)
    return json.loads(response.text)


if __name__ == '__main__':
    # api = make_api()
    # get_tweets(api)

    trump_tweets, hill_tweets = read_from_cache()
    score_tweets(trump_tweets, hill_tweets)
    


