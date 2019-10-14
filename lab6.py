l=int(input("l"))
u=int(input("u"))
n=int(input("n"))
for i in range(l,u+1):
    if(i%n==0):
        print(i)
