#3. Write python script to check whether a input number is perfect number of not.

def perfect(num):
    s=0
    for i in range(1,n):
        if num%i==0:
            s=s+i
    if s==num:
        print("Number is perfect")
    else:
        print("Not perfect")

n=int(input("Enter number:"))
perfect(n)
