w=input("請輸入文字:")
word=[]
for i in w:
    c=w.count(i,0,len(w))
    if c>1 and i not in word:
        word.append(i)
print(word)