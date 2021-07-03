from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from janome.charfilter import *

#外向性,調和性,誠実性,神経的,経験の開放性=11111

class MyValue:#評価指標クラス
    def __init__(self):
        self.gaikou=0
        self.tyouwa=0
        self.seijitu=0
        self.sinkei=0
        self.kaihou=0

worddict=dict()
count=0
Myvalue=MyValue()

f = open('pr.txt','r',encoding = "utf_8")#prファイル読み込み
pr = f.read()
f.close()

f = open('positive.txt','r',encoding = "utf_8")#単語リスト読み込み
wordlist = f.read().strip().split(',')
f.close()

for hyouka in wordlist:#単語と評価指標を分ける
    hyouka = hyouka.split('=')
    worddict[hyouka[0]]=hyouka[1]#worddictに単語をキーとする指標をstrで格納

tokenizer = Tokenizer()#tokenizerjanome

token_filters = [POSStopFilter(['記号','助詞','助動詞','接続詞']),TokenCountFilter(att='base_form')]#filtering,省く品詞と単語を一般的に変更
analyzer = Analyzer(tokenizer=tokenizer,token_filters=token_filters)
prdict = dict(analyzer.analyze(pr))#prdictに単語と数を格納
print(prdict)
prwords=list(prdict.keys())#prwordsに自己PRの単語リストを作る
for checkwords in prwords:
    if(checkwords in worddict):
        print(checkwords)
        wordstimes=int(prdict[checkwords])
        Myvalue.kaihou=Myvalue.kaihou+(int(worddict[checkwords][-1])*wordstimes)
        Myvalue.sinkei=Myvalue.sinkei+(int(worddict[checkwords][-2])*wordstimes)
        Myvalue.seijitu=Myvalue.seijitu+(int(worddict[checkwords][-3])*wordstimes)
        Myvalue.tyouwa=Myvalue.tyouwa+(int(worddict[checkwords][-4])*wordstimes)
        Myvalue.gaikou=Myvalue.gaikou+(int(worddict[checkwords][-5])*wordstimes)
        count=count+wordstimes

sum=Myvalue.kaihou+Myvalue.sinkei+Myvalue.seijitu+Myvalue.tyouwa+Myvalue.gaikou

Myvalue.kaihou=round(Myvalue.kaihou*100/sum,1)
Myvalue.sinkei=round(Myvalue.sinkei*100/sum,1)
Myvalue.seijitu=round(Myvalue.seijitu*100/sum,1)
Myvalue.tyouwa=round(Myvalue.tyouwa*100/sum,1)
Myvalue.gaikou=round(Myvalue.gaikou*100/sum,1)


print("あなたの外交度は.."+str(Myvalue.gaikou)+"%")
print("あなたの協調性は.."+str(Myvalue.tyouwa)+"%")
print("あなたの誠実さは.."+str(Myvalue.seijitu)+"%")
print("あなたの精神力は.."+str(Myvalue.sinkei)+"%")
print("あなたの知的好奇心は.."+str(Myvalue.kaihou)+"%")