#Nemoto
#②の品詞が一致する場所に①からランダムで単語を入れ替える→Stringを返す
import random

def exchangeWords(categorizedWords,labeledSentence):
    
    print(categorizedWords)
    print(labeledSentence)

    outputSentence = ""

    for part in labeledSentence:
        if type(part) == tuple:
            if part[0] in categorizedWords:
                outputSentence += random.choice(categorizedWords[part[0]])
            else:
                outputSentence += part[1]
        else:
            outputSentence += part
    return outputSentence


