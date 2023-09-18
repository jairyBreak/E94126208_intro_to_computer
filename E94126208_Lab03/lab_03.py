num = int(input("input a number:"))
print(num)
if num % 2 == 0:
    print("this number is even.")
else:
    print("this number is odd.")

fir = input("input your student ID first character")
nim = input("input your student ID last 8 number") 
if int(nim) % 2 == 0:
    print("your student ID number is even.")
else:
    print("your student ID  number is odd.")
print(fir+nim)
