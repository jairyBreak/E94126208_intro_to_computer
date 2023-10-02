dict = {"index":["國文","英文","數學","自然","社會"],"StuA":[50, 60, 70, 80, 90],"StuB":[57, 86, 73, 82, 43],"StuC":[97, 96, 86, 97, 83]}
print(dict)
val = list(dict.values())#value轉成list
for i in range(1,len(dict)):
    #val = list(dict.values())
    #print(val)
    avg = (val[i][0]+val[i][1]+val[i][2]+val[i][3]+val[i][4])/5#算學生平均
    print(list(dict.keys())[i],"平均成績：",avg)#輸出學生平均
for j in range(5):
    avg1 = (val[1][j]+val[2][j]+val[3][j])/3#算科目平均
    print(val[0][j],"成績平均：",avg1)#輸出科目平均