#Akazawa
#2つのツイートを形態素解析し固有名詞，人物名，地名などを抽出→{"固有名詞":[Str],"人物名":[Str]}のような形式で返す→①

import MeCab

def categorizeWords(sentence):
    mecab = MeCab.Tagger()
    mecab.parse('')
    nodes = mecab.parseToNode(sentence)

    dict = {}

    while nodes:
        if nodes.feature.split(",")[1] == "固有名詞":
            if nodes.feature.split(",")[2] in dict:
                dict[nodes.feature.split(",")[2]].append(nodes.feature.split(",")[6])
            else:
                dict[nodes.feature.split(",")[2]] = [nodes.feature.split(",")[6]]
        nodes = nodes.next
   
    return dict
