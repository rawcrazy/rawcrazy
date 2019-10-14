def binary(n):
    if(n>1):
        binary(n//2)
    print(n%2,end='')
n=int(input('enter value'))
print('binary value for ',n,' is' )
binary(n)
