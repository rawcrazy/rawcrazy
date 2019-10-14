import math
import sys                  
def indexerror():
    print('accesing an element based on index')
    l=list(map(int,input('enter list').split()))
    x=int(input('enter index value'))
    valid=False
    while not valid:
        try:
            print('value is: ',l[x])
            valid=True
        except IndexError:
            print('index out of bound')
            x=int(input('re-enter index'))
def nameerror():
    print("program to check Name error")
    l=list(map(int,input("enter list l").split()))
    try:
        print("trying to print list l1 which was not present")
        print(l1)
    except NameError:
        print("Name error")
        print("check the name of the variables that you are trying to retrive")
def valueerror():
    n=int(input("enter positive number"))
    valid=False
    while not valid:
        try:
            fact=math.factorial(n)
            print(fact)
            valid=True
        except ValueError:
            print("enter positive value")
            n=int(input("Re-enter value"))
def typeerror():
    valid=False
    while not valid:
        try:
            a=input('enter a value')
            b=input('enter b value')
            c=a+b
            print('after concatenation: ',c)
            d=int(input('enter d value'))
            f=input('enter f value')
            e=f+d
            print('after addition: ',e)
            valid=True
        except TypeError:
            print('invalid value')
            break
def ioerror():
    file=input('enter filename')
    valid=False
    while not valid:
        try:
            input_file=open(file,'r')
            line=input_file.readline()
            while line!='':
                print(line)
                line=input_file.readline()
            valid=True
        except IOError:
            print('file not found')
            file=input('re-enter filename')

#main
print('1)IndexError\n2)NameError\n3)ValueError\n4)TypeError\n5)IOError\n6)Exit\n')
while(1):
    ch=int(input('enter ur choice\n'))
    if ch==1:
        indexerror()
    elif ch==2:
        nameerror()
    elif ch==3:
        valueerror()
    elif ch==4:
        typeerror()
    elif ch==5:
        ioerror()
    elif ch==6:
        sys.exit()
    else:
        print('invalid choice')




