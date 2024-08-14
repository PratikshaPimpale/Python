#5. Write a program to check whether a input number is palindrome or not.

def palindrome(num):
    res=num
    rem=0
    rev=0
    while(num>0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    if (rev==res):
        print("Number is palindrome")
    else:
        print("Number not palindrome")
        
num=int(input("Enter number:"))
palindrome(num)
