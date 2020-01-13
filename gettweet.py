
#Sasaki
#ニュースを配信しているアカウントから適当なツイートを3つ選択する→文字列の配列を返す
import requests
import json

def getTweet():
    
    tweets = getTweetTextsFor("Yomiuri_Online")

    return getRelatedTweets(tweets)

def getTweetTextsFor(name):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}&count=5".format(name)

    payload = {}
    headers = {
    'Authorization': 'OAuth oauth_consumer_key="JolGq4w2PqMWCfDr4szMLcupZ",oauth_token="1214413074179866625-XZsV1CVPd72h5wQ56zjNAMWycLKCA8",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1578887051",oauth_nonce="OM5nRo29hB8",oauth_version="1.0",oauth_signature="pGeueAyxyo2LEAMf%2BNk%2BVYGyzXk%3D"'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    
    jdic = json.loads(response.text.encode('utf8'))
    texts = list(map(lambda cont: cont["text"],jdic))
    return texts

def getRelatedTweets(tweets):
    return tweets[0:2]
