import sys
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
#main
print('1}Factorial\n2)Fibonacci sequence\n3)Exit\n')
while(1):
    ch=int(input('enter ur choice\n'))
    if ch==1:
        n=int(input('enter n value to find factorial\n'))
        while(n<0):
            n=int(input('enter positive value\n'))
        f=fact(n)
        print(n ,'factorial is: ',f)
    elif ch==2:
        n=int(input('enter n value to find Fibonacci sequence\n'))
        while(n<0):
            n=int(input('enter positive value\n'))
        print('fibonacci series\n')
        for i in range(1,n+1):
            f=fib(i)
            print(f)
    elif ch==3:
        sys.exit()
    else:
        print('invalid choice\n')
            
        
    
