#categories of functions
#based on arguments


#1:Positional arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(100,200,300,400)


#2:Keyword arguments
def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=20,num2=30,num3=40)
function2(num4=10,num1=10,num2=30,num3=40)


#3:Default arguments
def function3(name,rollno,branch,collegename):
    print(name,rollno,branch,collegename)
function3("Sapneswar",270,"CSE","GIET")
function3("Atul",37,"ECE","GIET")


def function3(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("Sapneswar",270,"CSE")
function3("Atul",37,"ECE")


#4:Variable no. of arguments
def function4(*var):#tuple=
    for i in var:
        print(i,end=' ')
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)
print()


def add(*var):#tuple=
    sum1=0
    for i in var:
       sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))





