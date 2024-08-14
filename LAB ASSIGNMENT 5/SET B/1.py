'''1) Define a class named Rectangle which can be constructed by a length and 
width. The Rectangle class has a method which can compute the area and 
volume. '''

class Rectangle:
    def accept(self):
        self.l=float(input("Enter length:"))
        self.w=float(input("Enter width:"))
        self.h=float(input("Enter height:"))
    def compute(self):
        a=self.l*self.w
        v=self.l*self.w*self.h
        print("Area of rectangle=",a)
        print("Volune of rectangle=",v)

ob=Rectangle()
ob.accept()
ob.compute()
