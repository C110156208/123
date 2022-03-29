a,b=map(int,input("輸入月租費型式及通話時間").split(","))
if a == 186:
    if  (b*0.09)/a<2 and (b*0.09)/a >=1 :
        print("通話費為%.f" % float((b*0.09)*0.9))
    elif (b*0.09)/a >2:
        print("通話費為%.f" % float((b*0.09)*0.8))
    else:
        print("通話費為186")
elif a == 386:
    if  (b*0.08)/a<2 and (b*0.08)/a >=1 :
        print("通話費為%.f" % float((b*0.08)*0.8))
    elif (b*0.08)/a >2:
        print("通話費為%.f" % float((b*0.08)*0.7))
    else:
        print("通話費為386")
elif a == 586:
    if  (b*0.07)/a<2 and (b*0.07)/a >=1 :
        print("通話費為%.f" % float((b*0.07)*0.7))
    elif (b*0.07)/a >2:
        print("通話費為%.f" % float((b*0.07)*0.6))
    else:
        print("通話費為586")
elif a == 986:
    if  (b*0.06)/a<2 and (b*0.06)/a >=1 :
        print("通話費為%.f" % float((b*0.06)*0.6))
    elif (b*0.08)/a >2:
        print("通話費為%.f" % float((b*0.06)*0.5))
    else:
        print("通話費為986")