n=input('enter string/number ')
flag=0
l=len(n)
for i in range(0,int(l/2+1)):
    if n[i]!=n[l-i-1]:
        flag=0
        break
    else:
        flag=1
if flag==0:
    print(n ,'is not palindrome')
else:
    print(n ,'is palindrome')
