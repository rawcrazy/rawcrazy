st=input()
for i in st:
    print(i,end=' ')
    for j in st:
        if j!=i: 
            print(j,end=' ')
        else:
            continue
    print()
        
