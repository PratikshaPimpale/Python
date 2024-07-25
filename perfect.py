def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if (s==n):
        print("perfect")
    else:
        print("Not perfect")

n=int(input("Enter number:"))
perfect(n)
        
