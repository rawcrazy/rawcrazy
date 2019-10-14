import sys
def display():
    print(" program to convert C->F and F->C")
    print(" press 'C' for converting C to F ")
    print(" press 'F' for converting F to C")
def convertFtoC(t):
    con_temp=(t-32)*5//9
    print('',format(t,'4.1f'),'',format(con_temp,'4.1f'))
def convertCtoF(t):
    ct=(t*9//5)+32
    print('',format(t,'4.1f'),'',format(ct,'4.1f'))
display();
choice=input('enter your choice')
if(choice!='C' and choice!='F'):
    print('enter valid choice')
    sys.exit()
if(choice=='C'):
    print("conversion from celsius to farenhit")
elif(choice=='F'):
    print("conversion from  farenhit to celsius")
start=int(input("enter starting range"))
end=int(input("enter ending range"))
for temp in range(start,end+1):
    if(choice=='F'):
        convertFtoC(temp);
    elif(choice=='C'):
        convertCtoF(temp);
