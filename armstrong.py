def armstrong(num):
    s=0
    r=0
    while(num>0):
        r=num%10
        s=s+(r*r*r)
        num=num//10
    return s
num=int(input("enter number:"))
if (num==armstrong(num)):
    print("Armstrong")
else:
    print("Not armstrong")
