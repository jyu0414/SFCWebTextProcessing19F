#Twitter Bot by Team10
import gettweet
import categorizewords
import labeling
import posttweet
import exchangewords

if __name__ == '__main__':
    tweets = gettweet.getTweet()
    post = exchangewords.exchangeWords(categorizewords.categorizeWords(tweets[0]),labeling.labeling(tweets[1]))
    print(post)
    posttweet.postTweet(post)
    
    