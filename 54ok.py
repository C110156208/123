km=float(input("請輸入路程公里數(km):"))
low_money=75
levelkm=1.5
limit=0.25
t=0
while True:
    if km<=1.5:
        print("所需車資為:",low_money)
        break
    else:
        while km>levelkm:
            km-=limit
            t+=5
            if km<=levelkm:
                t+=low_money
                print("所需車資為:",t)
                break
        break