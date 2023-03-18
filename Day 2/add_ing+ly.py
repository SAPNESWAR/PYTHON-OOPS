def add(str):
    length=len(str)
    if length>2:
        if(str[-3:]=="ing"):
            str+="ly"
        else:
            str+="ing"
    return str
str=input()
print(add(str))
        
