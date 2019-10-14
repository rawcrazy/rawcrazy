def getFile():
    input_file_opened=False
    while not input_file_opened:
        try:
            filename=input('enter filename with extension')
            input_file=open(filename,'r')
            input_file_opened=True
        except IOError:
            print('entered file does not exist(re-enter)')
    return (filename,input_file)
def countwords(input_file,search_word):
    space=''
    delimeter=(space,',','.','"',':',';','\n')
    num_occurences=0
    search_word_len=len(search_word)
    for line in input_file:
        end_of_file=False
        line=line.lower()
        while not end_of_file:
            try:
                index=line.index(search_word)
                if index==0 and line[search_word_len] in delimeter:
                    Found=True
                elif line[index-1] in delimeter and line[index+search_word_len] in delimeter:
                    Found=True
                else:
                    Found=False
                if Found==True:
                    num_occurences=num_occurences+1
                    line=line[index+search_word_len:len(line)]
            except ValueError:
                    end_of_file=True
    return num_occurences
print('This program counts the user entered word in file')
file_name,input_file=getFile()
search_word=input('enter a word to check and count occurences')
search_word=search_word.lower()
num_occurences=countwords(input_file,search_word)
print('entered word',search_word,'occurs',num_occurences,'times')
