
#Sasaki
#ニュースを配信しているアカウントから適当なツイートを3つ選択する→文字列の配列を返す
import requests
import json

def getTweet():
    
    tweets = getTweetTextsFor("Sankei_news")
    #tweets.extend(getTweetTextsFor("asahi"))
    #tweets.extend(getTweetTextsFor("Yomiuri_Online"))

    return getRelatedTweets(tweets)

def getTweetTextsFor(name):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Sankei_news&count=5"#.format(name)
    print(url)
    payload = {}
    headers = {
        'Authorization': 'OAuth oauth_consumer_key="JolGq4w2PqMWCfDr4szMLcupZ",oauth_token="1214413074179866625-XZsV1CVPd72h5wQ56zjNAMWycLKCA8",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1578448296",oauth_nonce="ozERTeWsUnM",oauth_version="1.0",oauth_signature="rRneoL%2BLLiypEakCnuoEoLzmoLs%3D"'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    
    jdic = json.loads(response.text.encode('utf8'))
    print(jdic)
    texts = list(map(lambda cont: cont["text"],jdic))
    print(texts)
    return texts

def getRelatedTweets(tweets):
    return tweets[0:1]
