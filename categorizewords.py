#Akazawa
#2つのツイートを形態素解析し固有名詞，人物名，地名などを抽出→{"固有名詞":[Str],"人物名":[Str]}のような形式で返す→①

import MeCab

def categorizeWords(sentence):
    mecab = MeCab.Tagger()
    mecab.parse('')
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
    print(nodes.surface)
    while nodes:

        print(nodes.surface)

        if nodes.posid == 0:
            id0 += [nodes.surface]

        elif nodes.posid == 1:
            id1 += [nodes.surface]
        
        elif nodes.posid == 2:
            id2 += [nodes.surface]

        elif nodes.posid == 3:
            id3 += [nodes.surface] 

        elif nodes.posid == 4:
            id4 += [nodes.surface]
        
        elif nodes.posid == 5:
            id5 += [nodes.surface]

        elif nodes.posid == 6:
            id6 += [nodes.surface] 

        elif nodes.posid == 7:
            id7 += [nodes.surface]
        
        elif nodes.posid == 8:
            id8 += [nodes.surface]

        elif nodes.posid == 9:
            id9 += [nodes.surface] 

        if nodes.posid == 10:
            id0 += [nodes.surface]

        elif nodes.posid == 11:
            id11 += [nodes.surface]
        
        elif nodes.posid == 12:
            id12 += [nodes.surface]

        elif nodes.posid == 13:
            id13 += [nodes.surface] 

        elif nodes.posid == 14:
            id14 += [nodes.surface]
        
        elif nodes.posid == 15:
            id15 += [nodes.surface]

        elif nodes.posid == 16:
            id16 += [nodes.surface] 

        elif nodes.posid == 17:
            id17 += [nodes.surface]
        
        elif nodes.posid == 18:
            id18 += [nodes.surface]

        elif nodes.posid == 19:
            id19 += [nodes.surface] 

        if nodes.posid == 20:
            id20 += [nodes.surface]

        elif nodes.posid == 21:
            id21 += [nodes.surface]
        
        elif nodes.posid == 22:
            id22 += [nodes.surface]

        elif nodes.posid == 23:
            id23 += [nodes.surface] 

        elif nodes.posid == 24:
            id24 += [nodes.surface]
        
        elif nodes.posid == 25:
            id25 += [nodes.surface]

        elif nodes.posid == 26:
            id26 += [nodes.surface] 

        elif nodes.posid == 27:
            id27 += [nodes.surface]
        
        elif nodes.posid == 28:
            id28 += [nodes.surface]

        elif nodes.posid == 29:
            id29 += [nodes.surface] 

        if nodes.posid == 30:
            id30 += [nodes.surface]

        elif nodes.posid == 31:
            id31 += [nodes.surface]
        
        elif nodes.posid == 32:
            id32 += [nodes.surface]

        elif nodes.posid == 33:
            id33 += [nodes.surface] 

        elif nodes.posid == 34:
            id34 += [nodes.surface]
        
        elif nodes.posid == 35:
            id35 += [nodes.surface]

        elif nodes.posid == 36:
            id36 += [nodes.surface] 

        elif nodes.posid == 37:
            id37 += [nodes.surface]
        
        elif nodes.posid == 38:
            id38 += [nodes.surface]

        elif nodes.posid == 39:
            id39 += [nodes.surface] 

        if nodes.posid == 40:
            id40 += [nodes.surface]

        elif nodes.posid == 41:
            id41 += [nodes.surface]
        
        elif nodes.posid == 42:
            id42 += [nodes.surface]

        elif nodes.posid == 43:
            id43 += [nodes.surface] 

        elif nodes.posid == 44:
            id44 += [nodes.surface]
        
        elif nodes.posid == 45:
            id45 += [nodes.surface]

        elif nodes.posid == 46:
            id46 += [nodes.surface] 

        elif nodes.posid == 47:
            id47 += [nodes.surface]
        
        elif nodes.posid == 48:
            id48 += [nodes.surface]

        elif nodes.posid == 49:
            id49 += [nodes.surface] 

        if nodes.posid == 50:
            id50 += [nodes.surface]

        elif nodes.posid == 51:
            id51 += [nodes.surface]
        
        elif nodes.posid == 52:
            id52 += [nodes.surface]

        elif nodes.posid == 53:
            id53 += [nodes.surface] 

        elif nodes.posid == 54:
            id54 += [nodes.surface]
        
        elif nodes.posid == 55:
            id55 += [nodes.surface]

        elif nodes.posid == 56:
            id56 += [nodes.surface] 

        elif nodes.posid == 57:
            id57 += [nodes.surface]
        
        elif nodes.posid == 58:
            id58 += [nodes.surface]

        elif nodes.posid == 59:
            id59 += [nodes.surface] 

        if nodes.posid == 60:
            id60 += [nodes.surface]

        elif nodes.posid == 61:
            id61 += [nodes.surface]
        
        elif nodes.posid == 62:
            id62 += [nodes.surface]

        elif nodes.posid == 63:
            id63 += [nodes.surface] 

        elif nodes.posid == 64:
            id64 += [nodes.surface]
        
        elif nodes.posid == 65:
            id65 += [nodes.surface]

        elif nodes.posid == 66:
            id66 += [nodes.surface] 

        elif nodes.posid == 67:
            id67 += [nodes.surface]
        
        elif nodes.posid == 68:
            id68 += [nodes.surface]


        #array += [nodes]
        #print(array[i])
        #i += 1

        nodes = nodes.next
    
    #print(array)
    #for i in range(len(array)):
        #word = array[i]

        #+= [word.surface]
        #print(word.surface)
        #print(word.posid)
    print(id0)    
    print(id1)
    print(id2)
    print(id3)
    print(id4)
    print(id5)
    print(id6)
    print(id7)
    print(id8)
    print(id9)
    print(id10)
    print(id11)
    print(id12)
    print(id13)
    print(id14)
    print(id15)
    print(id16)
    print(id17)
    print(id18)
    print(id19)
    print(id20)
    print(id21)
    print(id22)
    print(id23)
    print(id24)
    print(id25)
    print(id26)
    print(id27)
    print(id28)
    print(id29)
    print(id30)
    print(id31)
    print(id32)
    print(id33)
    print(id34)
    print(id35)
    print(id36)
    print(id37)
    print(id38)
    print(id39)
    print(id40)
    print(id41)
    print(id42)
    print(id43)
    print(id44)
    print(id45)
    print(id46)
    print(id47)
    print(id48)
    print(id49)
    print(id50)
    print(id51)
    print(id52)
    print(id53)
    print(id54)
    print(id55)
    print(id56)
    print(id57)
    print(id58)
    print(id59)
    print(id60)
    print(id61)
    print(id62)
    print(id63)
    print(id64)
    print(id65)
    print(id66)
    print(id67)
    print(id68)

    word = "{"+'"その他,間投"'+ ":" + str(id0) +","+ '"フィラー"' + str(id1) +","+ '"感動詞"' + str(id2) +","+ '"記号,アルファベット"' + str(id3) +","+ '"記号,一般"' + str(id4) +","+ '"記号,括弧開"' + str(id5) +","+ '"記号,括弧閉"' + str(id6) +","+ '"記号,句点"' + str(id7) +","+ '"記号,空白"' + str(id8) +","+ '"記号,読点"' + str(id9) +","+ '"形容詞,自立"' + str(id10) +","+ '"形容詞,接尾"' + str(id11) +","+ '"形容詞,非自立"' + str(id12) +","+ '"助詞,格助詞,一般"' + str(id13) +","+ '"助詞,格助詞,引用"' + str(id14) +","+ '"助詞,格助詞,連語"' + str(id15) +","+ '"助詞,係助詞"' + str(id16) +","+ '"助詞,終助詞"' + str(id17) +","+ '"助詞,接続助詞"' + str(id18) +","+ '"助詞,特殊"' + str(id19) +","+ '"助詞,副詞化"' + str(id20) +","+ '"助詞,副助詞"' + str(id21) +","+ '"助詞,副助詞／並立助詞／終助詞"' + str(id22) +","+ '"助詞,並立助詞"' + str(id23) +","+ '"助詞,連体化"' + str(id24) +","+ '"助動詞"' + str(id25) +","+ '"接続詞"' + str(id26) +","+ '"接頭詞,形容詞接続"' + str(id27) +","+ '"接頭詞,数接続"' + str(id28) +","+ '"接頭詞,動詞接続"' + str(id29) +","+ '"接頭詞,名詞接続"' + str(id30) +","+ '"動詞,自立"' + str(id31) +","+ '"動詞,接尾"' + str(id32) +","+ '"動詞,非自立"' + str(id33) +","+ '"副詞,一般"' + str(id34) +","+ '"副詞,助詞類接続"' + str(id35) +","+ '"名詞,サ変接続"' + str(id36) +","+ '"名詞,ナイ形容詞語幹"' + str(id37) +","+ '"名詞,一般"' + str(id38) +","+ '"名詞,引用文字列"' + str(id39) +","+ '"名詞,形容動詞語幹"' + str(id40) +","+ '"名詞,固有名詞,一般"' + str(id41) +","+ '"名詞,固有名詞,人名,一般"' + str(id42) +","+ '"名詞,固有名詞,人名,姓"' + str(id43) +","+ '"名詞,固有名詞,人名,名"' + str(id44) +","+ '"名詞,固有名詞,組織"' + str(id45) +","+ '"名詞,固有名詞,地域,一般"' + str(id46) +","+ '"名詞,固有名詞,地域,国"' + str(id47) +","+ '"名詞,数"' + str(id48) +","+ '"名詞,接続詞的"' + str(id49) +","+ '"名詞,接尾,サ変接続"' + str(id50) +","+ '"名詞,接尾,一般"' + str(id51) +","+ '"名詞,接尾,形容動詞語幹"' + str(id52) +","+ '"名詞,接尾,助数詞"' + str(id53) +","+ '"名詞,接尾,助動詞語幹"' + str(id54) +","+ '"名詞,接尾,人名"' + str(id55) +","+ '"名詞,接尾,地域"' + str(id56) +","+ '"名詞,接尾,特殊"' + str(id57) +","+ '"名詞,接尾,副詞可能"' + str(id58) +","+ '"名詞,代名詞,一般"' + str(id59) +","+ '"名詞,代名詞,縮約"' + str(id60) +","+ '"名詞,動詞非自立的"' + str(id61) +","+ '"名詞,特殊,助動詞語幹"' + str(id62) +","+ '"名詞,非自立,一般"' + str(id63) +","+ '"名詞,非自立,形容動詞語幹"' + str(id64) +","+ '"名詞,非自立,助動詞語幹"' + str(id65) +","+ '"名詞,非自立,副詞可能"' + str(id66) +","+ '"名詞,副詞可能"' + str(id67) +","+ '"連体詞"' + str(id68)+"}"

    #print(word)
   
    return word





#categorizeWords("日本政府が韓国向け輸出管理厳格化の対象にしている「フッ化水素」。韓国の産業通商資源省は、韓国の化学メーカーが不純物を「1兆分の1」まで抑え、大量生産が可能な製造技術を確立したと発表しました。")
    #return {"固有名詞":["あ","い"],"人名":["う","え"]}

x = categorizeWords("日産元会長、カルロス・ゴーン被告の海外逃亡で、東京地検が東京都港区の住居を出入国管理法違反の疑いで家宅捜索。レバノン政府は逃亡直前の12月20日、日本の外務副大臣にゴーン被告の送還を要求していました。")
#x = categorizeWords("「個人的な問題であり、分からない」。カルロス・ゴーン被告が入国する経緯への関与を否定したレバノン政府。入国は「合法的」としており、日本側が身柄引き渡し要請した場合に協力を得られるかは不透明です。")


print(x)
