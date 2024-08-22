#3) Write a python program for parameterized constructor has multiple parameters along 
#with the self Keyword.

class Product:
    def __init__(self,pno,pname,price):
        self.pno=pno
        self.pname=pname
        self.price=price
    def disp(self):
        print("Product no=",self.pno)
        print("Product Name=",self.pname)
        print("Price=",self.price)

print("Enter product no, name, price:")
pno=int(input())
pname=input()
price=float(input())
ob=Product(pno,pname,price)
ob.disp()
