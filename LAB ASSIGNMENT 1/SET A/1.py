#1. Write python script to calculate sum of digits of a given input number.

def sum(num):
    s=0
    r=0
    while(num>0):
        r=num%10
        s=s+r
        num=num//10
    return s

num=int(input("Enter number:"))
print("Sum of digits=",sum(num))
