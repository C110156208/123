a_list=[]
b_list=[]
win=[]
a=input("甲方的數字:")
b=input("乙方的數字:")
for i in a:
    a_list.append(i)
for i in b:
    b_list.append(i)
a_list=list(map(int,a_list))
b_list=list(map(int,b_list))
for i1 in range(len(a_list)):
    if a_list[i1] > b_list[i1]:
        win.append("贏")
    elif a_list[i1] == b_list[i1]:
        win.append("和")
    elif a_list[i1] < b_list[i1]:
        win.append("輸")
win1 = "".join(win)
print(f"洗刷刷結果:{win1}")