from posixpath import split
from turtle import st

avgsum = 0
student = []
a1,a2 = map(int,input("請輸入考試次數及學生數:").split(" "))
students_float = list(map(float,input("每次考試所占比率:").split(" ")))
for i1 in range(a2):
    a3 = list(map(int,input("").split(" ")))
    student.append(a3)
for i2 in range(a2):
    for i3 in range(a1):
        avgsum += student[i2][i3] * students_float[i3]
print(f"全班總平均值為:{avgsum/a2}")