def getstack():
    return []
def isempty(s):
    if s==[]:
        return True
    else:
        return False
def isfull(s,m):
    if len(s)==m:
        return True
    else:
        return False
def top(s):
    if isempty(s):
        return None
    else:
        return s[len(s)-1]
def push(s,item):
        s=s.append(item)
        print('Stack Elements after PUSH operation are')
        print(s);
    
def pop(s):
    if isempty(s):
        return None
    else:
        item=s[len(s)-1]
        del s[len(s)-1]
        print('Stack Elements after Pop operation are')
        print(s);
        return item
