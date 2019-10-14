def convertgrade(grade):
    if grade=='F':
        return 0
    if grade=='S':
        return 10
    else:
        return 9-(ord(grade)-ord('A'))
print('To calculate SGPA,CGPA')
grade=[]
credit=[]
c=0.0
prev_cgpa=float(input('enter previous cGPA'))
prev_credits=float(input('enter credits earned upto prevoius sem'))
no_of_sub=int(input('enter no of subjects b/w 8 &9'))
while(no_of_sub<8 and no_of_sub>9):
    no_of_sub=int(input('enter no of subjects b/w 8&9'))
for i in range(no_of_sub):
    a=input('enter grade')
    if a not in ('S','A','B','C','D','E','F'):
        a=input('Re-enter the grade')
        i=i-1
    b=int(input('enter no of credits'))
    c=c+convertgrade(a)*b
    credit.append(b)
cre=sum(credit)
d=c/cre
print('present SGPA',d)
new_CGPA=(d*cre+prev_cgpa*prev_credits)/(cre+prev_credits)
print('Total CGPA',new_CGPA)
    
    
