a = int(input("請輸入度數"))
b = 0
c = 0
if a <= 120:
    b = a * 2.10
    c = a * 2.10
    print("summer months:",b)
    print("Non-summer months:",c)
elif a > 120 and a <= 330:
    b = ((a - 120) * 3.02) + 252
    c = ((a - 120) * 2.68) + 252
    print("summer months:",b)
    print("Non-summer months:",c)
elif a > 330 and a <= 500:
    b = ((a - 330) * 4.39) + 252 + 634.2
    c = ((a - 330) * 3.61) + 252 + 562.8
    print("summer months:",b)
    print("Non-summer months:",c)
elif a > 500 and a <= 700:
    b = ((a - 500) * 4.97) + 252 + 634.2 + 746.3
    c = ((a - 500) * 4.01) + 252 + 562.8 + 613.7
    print("summer months:",b)
    print("Non-summer months:",c)
elif a > 700:
    b = ((a - 700) * 5.63) + 252 + 634.2 + 746.3 + 994
    c = ((a - 700) * 4.50) + 252 + 562.8 + 613.7 + 802
    print("summer months:",b)
    print("Non-summer months:",c)