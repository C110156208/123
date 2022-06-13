num=input("輸入一整數序列為:").split(" ")
nlist=[]
for i in range(len(num)):
    nlist.append(num[i])

ele=max(nlist,key=nlist.count)
if nlist.count(ele)>=len(nlist)/2:
    print("過半元素為:",ele)
else:
    print("過半元素為:No")