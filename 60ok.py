e=input("請輸入一段小寫英文:")
en=[]
for i in range(len(e)):
    en.append(e[i])
for i in en:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        e=e.replace(i,".")
        e=e.replace(i,".")
        e=e.replace(i,".")
        e=e.replace(i,".")
        e=e.replace(i,".")
print(e)