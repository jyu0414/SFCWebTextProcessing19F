#Akazawa
#2つのツイートを形態素解析し固有名詞，人物名，地名などを抽出→{"固有名詞":[Str],"人物名":[Str]}のような形式で返す→①

import MeCab

def categorizeWords(sentence):
    mecab = MeCab.Tagger()
    nodes = mecab.parseToNode(sentence)
    
    

    id0 = []
    id1 = []
    id2 = []
    id3 = []
    id4 = []
    id5 = []
    id6 = []
    id7 = []
    id8 = []
    id9 = []
    id10 = []
    id11 = []
    id12 = []
    id13 = []
    id14 = []
    id15 = []
    id16 = []
    id17 = []
    id18 = []
    id19 = []
    id20 = []
    id21 = []
    id22 = []
    id23 = []
    id24 = []
    id25 = []
    id26 = []
    id27 = []
    id28 = []
    id29 = []
    id30 = []
    id31 = []
    id32 = []
    id33 = []
    id34 = []
    id35 = []
    id36 = []
    id37 = []
    id38 = []
    id39 = []
    id40 = []
    id41 = []
    id42 = []
    id43 = []
    id44 = []
    id45 = []
    id46 = []
    id47 = []
    id48 = []
    id49 = []
    id50 = []
    id51 = []
    id52 = []
    id53 = []
    id54 = []
    id55 = []
    id56 = []
    id57 = []
    id58 = []
    id59 = []
    id60 = []
    id61 = []
    id62 = []
    id63 = []
    id64 = []
    id65 = []
    id66 = []
    id67 = []
    id68 = []


    while nodes:
        if nodes.feature.split(',')[1] == '間投':
            id0 += [nodes.surface]
            print(nodes.posid)

        elif nodes.feature.split(',')[0] == 'フィラー':
            id1 += [nodes.surface]
        
        elif nodes.feature.split(',')[0] == '感動詞':
            id2 += [nodes.surface]

        elif nodes.feature.split(',')[1] == 'アルファベット':
            id3 += [nodes.surface] 

        elif nodes.feature.split(',')[1] == '一般':
            id4 += [nodes.surface]
            print(nodes.posid)
        
        elif nodes.feature.split(',')[1] == '括弧開':
            id5 += [nodes.surface]

        elif nodes.feature.split(',')[1] == '括弧閉':
            id6 += [nodes.surface] 

        elif nodes.feature.split(',')[1] == '句点':
            id7 += [nodes.surface]
        
        elif nodes.feature.split(',')[1] == '空白':
            id8 += [nodes.surface]

        elif nodes.feature.split(',')[1] == '読点':
            id9 += [nodes.surface] 
            print(nodes.posid)


        nodes = nodes.next
    





categorizeWords("日本政府が韓国向け輸出管理厳格化の対象にしている「フッ化水素」。韓国の産業通商資源省は、韓国の化学メーカーが不純物を「1兆分の1」まで抑え、大量生産が可能な製造技術を確立したと発表しました。")
    #return {"固有名詞":["あ","い"],"人名":["う","え"]}