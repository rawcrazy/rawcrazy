a=[]
n=int(input("enter no. of students"))
n1=int(input("enter no. of subjects"))
for i in range(n):
    print("marks obtained for student",i+1)
    a.append([])
    c=0
    while(c<n1):
        b=int(input('enter marks'))
        c=c+1
        a[i].append(b)
print("nested list elements are ")
print(a)
l=len(a)
print("number of elements in the list are ")
print(l)
li=[]
for i in range(n1):
    v=0
    for j in range(n):
        v=v+a[j][i]
    v=round(v/n)
    li.append(v)
print("average of each subject marks")
print(li)
s=0
for i in range(n1):
    s=s+li[i]
s=round(s/n1)
print("average marks obtained by class is ")
print(s)
