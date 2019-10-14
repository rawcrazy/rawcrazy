import sys
print('program for password encryption/decryption')
ch=input('enter e for encrypt d for decrypt')
j=''
if(ch!='e' and ch!='d'):
      print('enter valid choice')
      sys.exit()
if(ch=='e'):
      m=input('enter string to encrypt')
      for i in m:
            if(i=='y'):
                  j=j+'a'
            elif(i=='z'):
                  j=j+'b'
            else:
               j=j+chr(ord(i)+2)
if(ch=='d'):
      m=input('enter string to decrypt')
      for i in m:
            if(i=='a'):
                  j=j+'y'
            elif(i=='b'):
                  j=j+'z'
            else:
                j=j+chr(ord(i)-2)
print(j)
      
