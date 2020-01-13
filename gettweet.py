
#Sasaki
#ニュースを配信しているアカウントから適当なツイートを3つ選択する→文字列の配列を返す
import requests
import json
from requests_oauthlib import OAuth1Session, OAuth1

def getTweet():
    
    tweets = getTweetTextsFor("Yomiuri_Online")

    return getRelatedTweets(tweets)

def getTweetTextsFor(name):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}&count=5".format(name)

    oauth = OAuth1(
    'JolGq4w2PqMWCfDr4szMLcupZ',
    'd8e2UuJTs9decX8siayCPiujQxplCpY9nGacoKhrZCjw0i7Zee',
    '1214413074179866625-XZsV1CVPd72h5wQ56zjNAMWycLKCA8',
    'b4K4lUXSWcmcXDI5QnsdBA9xVwpSAcLzrY6lQ8ozlXKtm'
    )

    response = requests.request("GET", url, auth=oauth)
    
    jdic = json.loads(response.text.encode('utf8'))
    texts = list(map(lambda cont: cont["text"],jdic))
    return texts

def getRelatedTweets(tweets):
    return tweets[0:2]
