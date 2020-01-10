#Nemoto
#②の品詞が一致する場所に①からランダムで単語を入れ替える→Stringを返す
from random import randint as ran

def exchangeWords(categorizedWords,labeledSentence):
    size = len(labeledSentence)

    target = ran(0, size-1)
    list_cate = categorizedWords[labeledSentence[target][1]]
    size_cate = len(list_cate)-1

    change_num = ran(0, size_cate)
    change_str = list_cate[change_num]

    exchangeSentence = ''
    for x in range(size):
        strin = labeledSentence[x][0]
        if strin == labeledSentence[target][0]: #同じ単語はすべて入れ替える
            exchangeSentence += change_str
        else:
            exchangeSentence += labeledSentence[x][0]

    # print(target, change_num)
    return exchangeSentence

if __name__ == '__main__':
    categorizedWords = {"固有名詞":["あ","い"],"人名":["う","え"]}
    labeledSentence = [("あ","固有名詞"),("い","人名")]
    print(exchangeWords(categorizedWords, labeledSentence))


