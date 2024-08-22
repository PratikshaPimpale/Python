#2)Write a python program that will show the simplest form of inheritance using info() function.

class Emp:
    def accept(self):
        self.eno=input("Enter emp no:")
        self.ename=input("Enter emp name:")
        self.sal=input("Enter emp sal:")
class Demo(Emp):
    def info(self):
        print("Emp no=",self.eno)
        print("Name=",self.ename)
        print("Salary=",self.sal)

ob=Demo()
ob.accept()
ob.info()
