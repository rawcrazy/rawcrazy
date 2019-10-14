n=input("enter n value")
sum1=0
count=len(n)
n=int(n)
n2=n
while(n2>0):
    r=n2%10
    sum1=sum1+r
    n2=n2//10
print('no.of digits in',n ,': ',count)
print('sum of digits in ',n ,': ',sum1)
