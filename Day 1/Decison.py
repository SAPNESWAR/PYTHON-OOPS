#Decision making Statement
#read a number--
#multiple 3--
#multiple 5--
#multiple both 3 5 --
#invalid


num=int(input(""))
#print(num,type(num))
if num%3==0 and num%5 ==0:
    print("multiple of both")
elif num%5==0:
    print("multiple of 5")
elif num%3==0:
    print("multiple of 3")
else:
    print("Invalid")
