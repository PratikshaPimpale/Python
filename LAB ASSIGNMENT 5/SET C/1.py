#1) Python Program to Create a Class which Performs Basic Calculator Operations.

class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        print("Division=",a/b)

ob=Calculator()
a=int(input("Enter no1:"))
b=int(input("ENter no2:"))
print("Addition=",ob.add(a,b))
print("Substraction=",ob.sub(a,b))
print("Multiplication=",ob.mul(a,b))
ob.div(a,b)
