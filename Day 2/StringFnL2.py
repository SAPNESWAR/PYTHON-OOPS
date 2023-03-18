def new(str):
    length=len(str)
    if length<2:
        return(-1)
    else:
       return str[0:2]+str[-2:]
str=input()
print(new(str))
    
