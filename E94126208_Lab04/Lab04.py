lis = [["A"], ["B"], ["C"]]


for i in range(3):
    print("輸入", lis[i][0],"學生成績",sep="")
    chi = int(input("{0}國文成績：".format(lis[i][0])))
    mat = int(input("{0}數學成績：".format(lis[i][0])))
    eng = int(input("{0}英文成績：".format(lis[i][0])))
    lpp = [chi,mat,eng]
    for k in range(3):
        lis[i].append(lpp[k])

    #lis[i].append(chi)
    #lis[i].append(mat)
    #lis[i].append(eng)
for j in range(3):
    num = (lis[j][1]+lis[j][2]+lis[j][3])/3
    lis[j].append(round(num,1))
    print(lis[j])
