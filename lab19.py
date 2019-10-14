x=input('enter a sentence')
count=0
count1=0
count2=0
for i in x:
      if i in('a','e','i','o','u','A','E','I','O','U'):
            count=count+1
      elif(i!=' ' and i not in('0','1','2','3','4','5','6','7','8','9')):
            count1=count1+1
      elif(i==' '):
            count2=count2+1
print('no of vowels:',count)
print('no of consonants',count1)
print('no of characters',len(x))
print('no of words:',count2+1)
