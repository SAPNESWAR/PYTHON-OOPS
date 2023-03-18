num1=int(input())
num2=int(input())
num3=int(input())
print("magic_number")
num4=int(input())
if num1==num4:
    print(num2*num3)
elif num2==num4:
    print(num3)
elif num3==num4:
    print(-1)
else:
    print(num1*num2*num3)
    
