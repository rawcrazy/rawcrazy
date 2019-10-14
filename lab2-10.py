import sys
class Calculator:
    a=0
    b=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum1(self):
        return a+b
    def sub(self):
        return a-b
    def mul(self):
        return a*b
    def divide(self,a,b):
        if b==0:
            raise "division cant be performed"
        return a/b
#main
print("Program for performing calculator operations")
print("1-Addition\n2-subtraction\n3-multiplication\n4-division\n5-exit\n")
while(1):
    
    
    n=int(input("enter your choice!!"))
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    p=Calculator(a,b)
    if n==1:
        print("addition of given sequence of numbers is: ",p.sum1())
    elif n==2:
        print("difference between given two numbers is ",p.sub())
    elif n==3:
        print("result after multiplying given sequence of numbers ",p.mul())
    elif n==4:
        print("result after performing division on given numbers is",p.divide(a,b))
    elif n==5:
        break
    else:
        print("enter valid choice")
        
