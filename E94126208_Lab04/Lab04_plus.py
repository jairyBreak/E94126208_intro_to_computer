lis = [3, 2, 2, 3, 6, 5, 4, 3, 2, 1]
val = int(input("輸入刪除值"))
for i in range(len(lis)):
    lis[i] = int(lis[i])
cou = 0
for j in range(len(lis)):
    if lis[j]== val:
        cou = cou+1
for k in range(cou):
    lis.remove(val)
print("刪除後list:",lis,"刪除後list的長度：",len(lis))