import queuemodule
s1=queuemodule.getqueue()
n=int(input('enter size'))
while True:
    print('for enqueue type e <value>')
    print('for dequeue type d')
    print('for quit type q')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'e':
        if queuemodule.isfull(s1,n):
            print('Queue is full')
        else:
            queuemodule.enqueue(s1,int(do[1]))
        
    elif operation == 'd':
        if queuemodule.isempty(s1):
            print('queue is empty.')
        else:
            print('dequeued element: ', queuemodule.dequeue(s1))
    elif operation == 'q':
        break
