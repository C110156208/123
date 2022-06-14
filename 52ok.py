w="紅豆生南國，春來發幾枝？願君多采擷，此物最相思。"
m="春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。"
c="，。"
for i in range(len(c)):
    w=w.replace(c[i],"")
    m=m.replace(c[i],"")

c1=[]
for i in w:
    for j in m:
        if i==j:
            c1.append(j)
print(c1)