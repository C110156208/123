def prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

num=input("請輸入正整數:")
list_=[]
for u in range(len(num)):
    for i in range(u,len(num)):
        key=int(num[u:i+1])
        if prime(key):list_.append(key)
print(f"子字串最大的質數值{max(list_)}")if len(list_)>0 else "No prime found"