animal_list=["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
n=int(input("請輸入年份"))
if n<0 :
    print("輸入錯誤")
else:
    a= (n%12)-4
    print(animal_list[a])