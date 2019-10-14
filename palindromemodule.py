def getstack():
    return []
def isempty(s):
    if s==[]:
        return True
    else:
        return False
def isfull(s,n):
    if len(s)>=n:
        return True
    else:
        return True
def push(s,item):
        s.append(item)
    
def pop(s):
    if isempty(s):
        return None
    else:
        item=s[len(s)-1]
        del s[len(s)-1]
        return item
