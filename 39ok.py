for i in range(1,6):
    for a in range(6-i):
        print(" ",end="")
    for u in range(i+(i-1)):
        if u%2==0:
            print(" ",end="")
        else:
            print("*",end="")
    print()
for i in range(6,1,-1):
    for a in range(6-i):
        print(" ",end="")
    for u in range(i+(i-1)):
        if u%2==0:
            print(" ",end="")
        else:
            print("*",end="")
    print()