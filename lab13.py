l=list(map(int,input("enter list").split()))
l1=list(map(int,input("enter list").split()))
print("enter u for union")
print("enter c for concat")
print("enter i for intersect")
l=sorted(l)
l1=sorted(l1)
print(l1)
print(l)
i=0
j=0
c=[]
c1=[]
while(i<len(l) and j<len(l1)):
    if(l[i]<l1[j]):
        c.append(l[i])
        i=i+1
    elif(l[i]>l1[j]):
        c.append(l1[j])
        j=j+1
    else:
        c.append(l[i])
        c1.append(l[i])
        i=i+1
        j=j+1
while(i<len(l)):
    c.append(l[i])
    i=i+1
while(j<len(l1)):
    c.append(l1[j])
    j=j+1
print("union of the two given lists is:",c)
print("intersection of the given lists",c1)
i=0
j=0
c2=[]
while(i<len(l) and j<len(l1)):
    if(l[i]<l1[j]):
        c2.append(l[i])
        i=i+1
    elif(l[i]>l1[j]):
        c2.append(l1[j])
        j=j+1
    else:
        c2.append(l[i])
        i=i+1
while(i<len(l)):
    c2.append(l[i])
    i=i+1
while(j<len(l1)):
    c2.append(l1[j])
    j=j+1
print("concatination of 2 given lists",c2)
