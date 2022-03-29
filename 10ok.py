N,M=map(int,input("輸入N M的值:").split())
nums1=list(map(int,input("輸入矩陣第1列為:").split()))
nums2=list(map(int,input("輸入矩陣第2列數值為:").split()))
for i in range(N):
    for n in range(M):
        print(f"輸出矩陣數值第{n+1}列:{nums1[n]} {nums2[n]}")
    break
