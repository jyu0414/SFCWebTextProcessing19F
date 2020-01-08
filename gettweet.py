
#Sasaki
#ニュースを配信しているアカウントから適当なツイートを3つ選択する→文字列の配列を返す
import requests
import json

def getTweet():
    
    getTweetTextsFor("Sankei_news")
    getTweetTextsFor("")

    return ["日本政府が韓国向け輸出管理厳格化の対象にしている「フッ化水素」。韓国の産業通商資源省は、韓国の化学メーカーが不純物を「1兆分の1」まで抑え、大量生産が可能な製造技術を確立したと発表しました。",
    "日産元会長、カルロス・ゴーン被告の海外逃亡で、東京地検が東京都港区の住居を出入国管理法違反の疑いで家宅捜索。レバノン政府は逃亡直前の12月20日、日本の外務副大臣にゴーン被告の送還を要求していました。",
    "「個人的な問題であり、分からない」。カルロス・ゴーン被告が入国する経緯への関与を否定したレバノン政府。入国は「合法的」としており、日本側が身柄引き渡し要請した場合に協力を得られるかは不透明です。"]

def getTweetTextsFor(name):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}&count=10".format(name)

    payload = {}
    headers = {
        'Authorization': 'OAuth oauth_consumer_key="JolGq4w2PqMWCfDr4szMLcupZ",oauth_token="1214413074179866625-XZsV1CVPd72h5wQ56zjNAMWycLKCA8",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1578446430",oauth_nonce="TAbT3sy6Q39",oauth_version="1.0",oauth_signature="v6dUZkCTJkRFye7k6SuxQWRmE5w%3D"'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    
    jdic = json.loads(response.text.encode('utf8'))
    texts = list(map(lambda cont: cont["text"],jdic))
    print(texts)
    return texts
