import sys
def merge(l,l1):
    l2=[]
    i=0
    j=0
    while(i<len(l) and j<len(l1)):
        if(l[i]<l1[j]):
            l2.append(l[i])
            i=i+1
        elif(l[i]>l1[j]):
            l2.append(l1[j])
            j=j+1
        else:
            l2.append(l[i])
            i=i+1
    while(i<len(l)):
        l2.append(l[i])
        i=i+1
    while(j<len(l1)):
        l2.append(l1[j])
        j=j+1
    return l2

def mergesort(l):
    if(len(l)==1):
        return l
    mid=len(l)//2
    l2=mergesort(l[:mid])
    l3=mergesort(l[mid:])
    l1=merge(l2,l3)
    return l1



def quicksort(a , l , h):
    if h-l>1:
        j = partition(a,l,h)
        quicksort(a,l,j)
        quicksort(a, j+1, h)
 
 
def partition(a,l,h):
    pivot = a[l]
    i = l + 1
    j = h - 1
 
    while True:
        while (i <= j and a[i] <= pivot):
            i = i + 1
        while (i <= j and a[j] >= pivot):
            j = j - 1
 
        if i <= j:
            a[i], a[j] = a[j], a[i]
        else:
            a[l], a[j] = a[j], a[l]
            return j
  
 

print('1)Quick sort\n2)Merge sort\n3)exit\n')
while(True):
    print('enter ur choice')
    ch=int(input())
    if ch==1 or ch==2 :
        n=int(input('enter n value'))
        a=[]
        print('enter list values')
        for i in range(0,n):
            b=int(input())
            a.append(b)
    if(ch==1):
        print('list before sort is:',a)
        quicksort(a,0,len(a))
        print('Sorted list:')
        print(a)
    elif(ch==2):
        print('list before sort is:',a)
        l=mergesort(a)
        print('Sorted list:')
        print(l)
    elif ch==3:
        sys.exit()
    else:
        print('invalid choice')
        
        


































