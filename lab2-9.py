def getphone():
    valid_num=False
    empty_str=''
    while not valid_num:
        ph_num=input("enter phone number")
        if len(ph_num)<11 or ph_num[5]!='-':
           print("invalid number")
        else:
           k=0
           valid_num=True
           ph_num_digits=ph_num.replace('-',empty_str)
           while valid_num and k<len(ph_num_digits):
               if not ph_num_digits[k].isdigit():
                   print('non-digit',ph_num_digits[k])
               else:
                   k=k+1
           return ph_num
def displayallwords(ph_num):
    translate={'0':('a','b','c'),'1':('d','e','f'),'2':('g','h','i'),'3':('j','k','l'),'4':('m','n','o'),'5':('p','q','r'),'6':('s','t'),'7':('u','v'),'8':('w','x','y','z'),'9':('*')}
    count=0
    for let1 in translate[ph_num[6]]:
        for let2 in translate[ph_num[7]]:
            for let3 in translate[ph_num[8]]:
                for let4 in translate[ph_num[9]]:
                    for let5 in translate[ph_num[10]]:
                        print(ph_num[0:5]+let1+let2+let3+let4+let5)
                        count=count+1
    print(count)
#main program
print(' to display all possible words for last 4 digits')
terminate=False
while not terminate:
      ph_num=getphone()
      displayallwords(ph_num)
      response=input('enter do u want to continue..')
      if response=='n':
           terminate=True
              
