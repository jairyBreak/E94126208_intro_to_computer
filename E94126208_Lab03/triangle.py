a = int(input("輸入三角形的第一個邊長"))
b = int(input("輸入三角形的第二個邊長"))
c = int(input("輸入三角形的第三個邊長"))
li = [a,b,c]
li.sort()
#print(li)
if  li[0] + li[1] <= li[2] or li[2]<=0 :
    print("這三邊長無法構成一個合理的三角形")
elif li[0] == li[2]:
    print("這是一個正三角形")
elif li[0] == li[1] or li[1] == li[2]:
    print("這是一個等腰三角形")
else:
    print("這是一個一般三角形")
    
