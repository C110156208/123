n=int(input('輸入一正整數:'))
if n %11 ==0 and n % 2==0 and n % 5 != 0 and n % 7 !=0:
    print(f'{n}為新公倍數?YES')
else:
    print(f'{n}為新公倍數?NO')