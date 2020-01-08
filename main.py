#Twitter Bot by Team10
import gettweet
import categorizewords
import labeling
import posttweet

if __name__ == '__main__':
    #メンションされたツイートを取得
    gettweet.getTweet()
    mentionedTweets = ["日本政府が韓国向け輸出管理厳格化の対象にしている「フッ化水素」。韓国の産業通商資源省は、韓国の化学メーカーが不純物"]
    
    