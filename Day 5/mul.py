def multiplication(array):
    if n>0:
        if len(array)<0:
            print("Invalid Input")
        else:
            mul=1
            for i in array:
                mul=mul*i
            return mul
    else:
        print("invalid input")
        exit()
n= int(input())
array=list(map(int,input().split()))
print(multiplication(array))
