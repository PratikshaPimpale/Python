#2.Write python script to check whether a input number is Armstrong number or not.

def armstrong(num):
    s=0
    r=0
    while(num>0):
        r=num%10
        s=s+(r*r*r)
        num=num//10
    return s

num=int(input("Enter number:"))
if (num==armstrong(num)):
    print("Number is Armstrong")
else:
    print("Number not armstrong")
