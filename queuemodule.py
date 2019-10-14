def getqueue():
    return []
def isempty(s):
    if s==[]:
        return True
    else:
        return False
def isfull(s,n):
    if(len(s)>n-1):
       return True
    else:
        return False
def enqueue(s,item):
        s.append(item)
        print('queue Elements after enqueue operation are')
        print(s);
    
def dequeue(s):
    if isempty(s):
        return None
    else:
        item=s[0]
        del s[0]
        print('queue Elements after dequeue operation are')
        print(s);
        return item
