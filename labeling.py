#Takahashi
#1つのツイートを形態素解析し単語に品詞をつける→[("単語","品詞")]の形式で返す→②
import MeCab

def labeling(sentence):
    mecab = MeCab.Tagger()
    mecab.parse('')
    nodes = mecab.parseToNode(sentence)
    print(sentence)
    list = []
    while nodes:
        if nodes.feature.split(",")[0] == "BOS/EOS":
            pass
        elif nodes.feature.split(",")[1] == "固有名詞":
            list.append((nodes.surface,nodes.feature.split(",")[2]))
        else:
            if len(list) == 0 or type(list[-1]) == tuple:
                list.append(nodes.surface)
            else:
                list[-1] += nodes.surface

        nodes = nodes.next
    return list