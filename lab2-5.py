import palindromemodule
s1=palindromemodule.getstack()
text=input('enter string')
for i in text:
    palindromemodule.push(s1,i)
reverse_text=''
while not palindromemodule.isempty(s1):
    reverse_text=reverse_text+palindromemodule.pop(s1)
if text == reverse_text:
    print(text ,'is a palindrome')
else:
    print(text ,'is not a palindrome')
