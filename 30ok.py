num = [1,2,3,4]
nums=[]
A=0
B=0
num=list(map(str,num))
num1 = input()
for i in num1:
    nums.append(i)
while True:
    for i1 in range(0,len(nums)):
        if nums[i1] == num[i1]:
            A +=1
        elif nums[i1] in num:
            B +=1
    if A == 4:
        print(f"{A}A{B}B")
        break
    else:
        print(f"{A}A{B}B")
        break