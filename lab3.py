n=int(input('enter range'))
m=int(input('enter high range'))
print(2)
flag=0
for i in range(3,n+1,2):
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break;
        else:
            flag=0
    if(flag==0):
        print(i)
       
        
