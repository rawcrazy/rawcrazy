def gross(basic):
    da=float(basic*75/100)
    hra=float(basic*20/100)
    g=basic+da+hra
    income=float(basic*5/100)
    n=g-income
    return (g,n,da,hra,income)
n=int(input("enter no of employees"))
i=1
name=[]
g=[]
n2=[]
da=[]
hr=[]
inctx=[]
while n>0:
    print("enter details of emp",i)
    name.append(input("enter employee name"))
    basic=int(input('enter basic salary'))
    g1,n1,d,h,it=gross(basic)
    g.append(g1)
    n2.append(n1)
    da.append(d)
    hr.append(h)
    inctx.append(it)
    i=i+1
    n=n-1
print(format("empname",">10")+format("gross sal",">10")+format("net sal",">10")+format("da",">10")+format("hra",">10")+format("tax",">10"))
for i in range(len(n2)):
    print(format(name[i],">10")+format(g[i],">10")+format(n2[i],">10")+format(da[i],">10")+format(hr[i],">10")+format(inctx[i],">10"))

