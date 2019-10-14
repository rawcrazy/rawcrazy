n=int(input('enter range'))
a=0
print(a)
b=1
print(b)
count=2
while(count<n):
    c=a+b
    a=b
    b=c
    count=count+1
    print(c)
