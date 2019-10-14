def length(l):
    return len(l)
def avg(l):
    su=sum(l)
    n=len(l)
    return su/n
def bsearch(i,j,el,l):
    mid=i+j
    mid=mid//2
    if(i<j):
        if(l[mid]==el):
            return mid
        if(l[mid]>el):
            bsearch(mid+1,j,el,l)
        if(l[mid]<el):
            bsearch(i,mid-1,el,l)
    else:
        return -1
    
l=list(map(int,input().split()))
n=length(l)
n1=avg(l)
print(n,n1)
i=int(input())
l=sorted(l)
el=bsearch(0,n-1,i,l)
if(el==-1):
    print("element not found")
else:
    print("element found in location ",el)
