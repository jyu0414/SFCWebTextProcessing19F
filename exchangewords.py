#Nemoto
#②の品詞が一致する場所に①からランダムで単語を入れ替える→Stringを返す
import random

def exchangeWords(categorizedWords,labeledSentence):
    
    print(categorizedWords)
    print(labeledSentence)

    outputSentence = ""

    for part in labeledSentence:
        if type(part) == tuple:
            outputSentence += random.choice(flatten(categorizedWords.values()))
            #if part[0] in categorizedWords:
                #random.choice(categorizedWords[part[1]])
            #else:
                #outputSentence += part[0]
        else:
            outputSentence += part
    return outputSentence

def flatten(nested_list):
    return [e for inner_list in nested_list for e in inner_list]


