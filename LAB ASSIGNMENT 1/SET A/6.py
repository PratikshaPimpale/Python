#6. Write a program to calculate sum of first and last digit of a number.

n=int(input("Enter number:"))

d1=n%10
a=str(n)
a=a[::-1]
b=int(a)
d2=b%10
print("Sum of first & last digit=",(d1+d2))
