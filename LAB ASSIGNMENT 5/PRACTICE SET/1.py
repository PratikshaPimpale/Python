#1) Write a python program using simple class having class name as Student.

class Student:
    def accept(self):
        self.rno=input("Enter roll no:")
        self.name=input("Enter name:")
        self.per=input("Enter percentage:")
    def disp(self):
        print("Roll no=",self.rno)
        print("Name=",self.name)
        print("Percentage=",self.per)
        
ob=Student()
ob.accept()
ob.disp()
