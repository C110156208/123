bookA=["飢餓遊戲3","解憂雜貨店","怪獸與他們的產地","哈利波特6","我的阿富汗筆友","祈念之樹","樓下的房客","小王子"]
bookB=["房思琪的初戀樂園","等一個人咖啡","鬼滅之刃14","神農嘗百草","麥田捕手","老人與海","傲慢與偏見","與神同行"]
fb=input("請輸入欲查詢的書名:")
if fb in bookA:
    for i in range(len(bookA)):
        if fb==bookA[i]:
            print("在書架A的第%d本"%(i+1))
elif fb in bookB:
    for i in range(len(bookB)):
        if fb==bookB[i]:
            print("在書架B的第%d本"%(i+1))
else:
    print("查無此書籍")