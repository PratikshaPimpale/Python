#1)Write a python program to demonstrate single inheritance using findArea() function.

class Circle:
    def accept(self):
        self.r=float(input("Enter radius:"))
class Area(Circle):
    def findArea(self):
        a=3.14*self.r*self.r
        print("Area of circle=",a)

ob=Area()
ob.accept()
ob.findArea()
