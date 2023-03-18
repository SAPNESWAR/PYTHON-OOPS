'''
class Example:
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        self.num=num

    def get_num(self):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())


#o/p
#10
#15
'''
#------------------
'''
class Example:
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        num=num

    def get_num(self):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

#o/p
#10
#10
'''
#--------------------
'''
class Customer:
    def __init__(self):
        self.cust_id=100  #cust_id=100  (error)
c1=Customer()
print(c1.cust_id)
'''
#---------------------
'''
class Customer:
    def __init__(self,id):
        self.id=100  #id=100
c1=Customer(200)
print(c1.id)
'''
#----------------------
'''
class Book:
    def __init__ (self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"

my_fav.title="Learning Python"

print("My favourite is",my_fav.title)
print("Your's is",your_fav.title)
'''
#---------------------
'''
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=Shoe(1000,"Canvas")
print(s1)
print(s1.price,s1.material)
'''
#-------------------
'''
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=Shoe(1000,"Canvas")
print("the unique id of the object",id(s1))
'''
#------------------
'''
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material

    def __str__ (self):
        return "Shoe with price: "+ str(self.price) + " and material:"+ self.material
s1=Shoe(1000,"Canvas")
print(s1)
'''
#--------------------
'''
class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("Calculating Price")
Mobile().purchase()
Mobile().purchase()
'''
#-----------------------
'''
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*(discount/100)
        print("Total price of",self.brand,"mobile is",self.total_price)
    def amount_returned(self):
        return (self.price-self.total_price)
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())
'''
#------------------------
'''
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount<1000 and amount>0:
            self.__wallet_balance+=amount
    def show_balance(self):
        print("The balance is ",self.__wallet_balance)
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Gopal",24,1000)
c1.update_balance(500)
c1.show_balance()
print(c1.get_wallet_balance())
'''
#---------------------------------
'''
class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name",dam1.name)
print("Dam Length:",dam1.get_length())
'''
# ------------------------------------------------------------------------------------------
'''
class table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top):
            rate=30000
        else:
            rate=0
        return rate
dining_table=table()
rate=dining_table.identify_rate(False,True)
print(rate)
'''
#---------------------------

class table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
dining_table=table()
back_table=table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)

#-----------------------------



