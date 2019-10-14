def getFile():
    file_open=False
    while not file_open:
        try:
            filename=input('enter filename with extension')
            input_file=open(filename,'r')
            line=input_file.read()
            words=line.split()
            file_open=True
        except IOError:
            print('entered file does not exist(re-enter)')
    return (filename,input_file,line,words)
def uniquewords(words):
    space=''
    l1=[]
    delimeter=(space,',','.','"',':',';','\n')
    for i in words:
        if words.count(i)==1 and i not in delimeter:
            l1.append(i)
    return l1
print('This program prints unique words in file')
file_name,input_file,line,words=getFile()

l1=uniquewords(words)
l1=sorted(l1)
print("Unique occured word(s) is as follows")
for i in l1:
    print(i)
