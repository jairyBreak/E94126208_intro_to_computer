def gcd(a,b):
    if a>=b: #let smaller number become divisor
        be = a
        do = b
    else:
        be = b
        do = a

    if a==0 or b==0: #check the number is not 0
        print("0沒有gcd")
    else:
        left = be % do
        if left == 1: #if the remainder is 1,they are relatively prime
            
            print(f"{a}跟{b}互質")
        elif left == 0: #the remainder is 0,their biggest common factor is the divisor of the last division
            print(f"{a}跟{b}的gcd=",do)
        else:
            return gcd(do,left) #if the remainder > 1,change the remainder to divisor and the divisor to dividend and keep doing divison
ans1 = gcd(80, 20)
ans2 = gcd(10, 0)
ans3 = gcd(19, 20)