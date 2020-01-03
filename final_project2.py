
# coding=gbk
import jieba.posseg as pseg
import jieba
import jieba
excludes = {}
txt = open("黎明破晓的街道.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(500):
    openfile=open("renwubiao","at")
    openfile.write(str(items[i])+' '+'\n')
    openfile.close

