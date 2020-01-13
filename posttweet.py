#生成したフェイクニュースをツイート
import requests
from requests_oauthlib import OAuth1Session, OAuth1

def postTweet(sentence):
    url = "https://api.twitter.com/1.1/statuses/update.json?status=sasasasa"

    oauth = OAuth1(
    'JolGq4w2PqMWCfDr4szMLcupZ',
    'd8e2UuJTs9decX8siayCPiujQxplCpY9nGacoKhrZCjw0i7Zee',
    '1214413074179866625-XZsV1CVPd72h5wQ56zjNAMWycLKCA8',
    'b4K4lUXSWcmcXDI5QnsdBA9xVwpSAcLzrY6lQ8ozlXKtm'
    )

    response = requests.request("POST", url, auth=oauth)
    print(response.text.encode('utf8'))