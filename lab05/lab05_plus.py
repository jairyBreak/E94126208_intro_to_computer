dict={}#建立字典
for i in range(4):
    index = input("enter index:")#輸入標籤
    value = list(input("enter value:").split(","))#輸入值並轉為list
    dict[index] = value
print(dict)