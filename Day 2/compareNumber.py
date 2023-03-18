def check_double(number):
    double=int(number)*2
    length=len(number)
    d_length=len(str(double))
    if(length==d_length):
        for i in number:
            if i in str(double):
                return True
            else:
                return False
number=input()
print(check_double(number))
    
