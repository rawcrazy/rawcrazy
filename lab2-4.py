import stackmodule
n=int(input('enter the size of a stack(Number of elements:)'))
s1=stackmodule.getstack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        if stackmodule.isfull(s1,n):
            print('PUSH is avoided beause stack is full and the current elements in a stack are');
            print(s1);
        else:
            stackmodule.push(s1,int(do[1]))
        
    elif operation == 'pop':
        if stackmodule.isempty(s1):
            print('Stack is empty.')
        else:
            print('Popped element: ', stackmodule.pop(s1))
    elif operation == 'quit':
        break
