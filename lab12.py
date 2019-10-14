import math
import sys
def display(l):
        print("elements in list : ",l)

def length(l):
        print('length of list',len(l))

def accessindex(l):
   print('Access an element based on index')
   x=int(input("enter index to access"))
   if x>=len(l):
        print('invalid index')
   else:
        print(l[x])

def accessvalue(l):
        f=0
        print('Access an element based on value')
        x=int(input('enter value'))
        for i in range(len(l)):
            if l[i]==x:
               f=1
               break
            else:
               f=0
        if f==0:
           print(x ,'is not in list')
        else:
                print(x ,'is in index ',i)

def replaceindex(l):
        print('Replace an element based on index')
        index=int(input('enter index to replace'))
        if index>=len(l):
                print('invalid index')
        else:
              x=int(input('enter value to be placed'))
              l[index]=x
              print(l)

def replacevalue(l):
        f=0
        print('Replace an element based on value')
        x=int(input('enter value'))
        y=int(input('enter value to be placed'))
        for i in range(len(l)):
            if l[i]==x:
               print(x ,'is in index ',i)
               l[i]=y
               print(l)
               f=1
               break
            else:
               f=0
        if f==0:
           print(x ,'is not in list')

def insertindex(l):
        print('Insert an element based on index')
        x=int(input('enter index'))
        y=int(input('enter value to be inserted'))
        if x>=len(l):
                print('index out of range')
        else:        
           l.insert(x,y)
           print(l)

def appendvalue(l):
        print('Append element to the list.')
        x=int(input('enter value to append'))
        l.append(x)
        print(l)

def deleteindex(l):
        print('Delete an element based on index.')
        x=int(input('enter index to delete'))
        if x>=len(l):
             print('index out of range')
        else:
              del l[x]
              print(l)

def deletevalue(l):
        print('Delete an element based on value.')
        x=int(input('enter value to remove'))
        f=0
        for i in range(len(l)):
            if l[i]==x:
               f=1
               break
            else:
               f=0
        if f==0:
           print(x ,'is not in list')
        else:
            print(x ,'is in index ',i)
            l.remove(x)
            print(l)

def sortvalues(l):
        print('sort list')
        l.sort()
        print(l)
        
def reverselist(l):
        print('reverse the list')
        l.reverse()
        print(l)

def count(l):
        print('count the occurance in list')
        x=int(input('enter value'))
        c=l.count(x)
        print(c)

def minmax(l):
        print('max and min')
        print('max number is',max(l))
        print('min number is',min(l))
def sum1(l):
        print('sum is ',sum(l))
        

         
l1=list(map(int,input('enter list').split()))
while(1):
    print("1) To display the list elements\n2) To display the length of the list\n3) Access an element based on index \n4) Access an element based on value.")
    print("5) Replace an element based on index \n6) Replace an element based on value\n7) Insert an element based on index.\n8) Append element to the list.")
    print("9) Delete an element based on index\n10) Delete an element based on value\n11) To Sort list elements.\n12) To Reverse List elements\n13) To count the no.of times an element occurs in the list.")
    print("14) To find the Minimum and Maximum value in the list.\n15) To display the sum of list elements\n16)Exit")
    i=int(input("enter ur choice.........."))
    
    if(i==1):
            display(l1)
    elif(i==2):
            length(l1)
    elif(i==3):
            accessindex(l1)
    elif(i==4):
            accessvalue(l1)
    elif(i==5):
            replaceindex(l1)
    elif(i==6):
            replacevalue(l1)
    elif(i==7):
            insertindex(l1)
    elif(i==8):
            appendvalue(l1)
    elif(i==9):
            deleteindex(l1)
    elif(i==10):
            deletevalue(l1)
    elif(i==11):
            sortvalues(l1)
    elif(i==12):
            reverselist(l1)
    elif(i==13):
            count(l1)
    elif(i==14):
            minmax(l1)
    elif(i==15):
            sum1(l1)
    elif(i==16):
            sys.exit()
            
    
    
