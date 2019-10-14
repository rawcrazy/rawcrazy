n=input("enter n value")
sum1=0
count=len(n)
n=int(n)
n2=n
while(n2>0):
    r=n2%10
    sum1=sum1+pow(r,count)
    n2=n2//10
if n==sum1:
    print("Amstrong number")
    
else:
    print("not amstrong number") 
