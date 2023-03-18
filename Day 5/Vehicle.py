'''
class Vehicle:
    def __init__(self, id, type, cost):
        self.id = id
        self.type = type
        self.cost = cost
        if self.type == "2 wheeler":
            self.premium = self.cost * 0.02
        elif self.type == "4 wheeler":
            self.premium = self.cost * 0.06

    def display_details(self):
        print(f"Vehicle ID: {self.id}")
        print(f"Type: {self.type}")
        print(f"Cost: {self.cost}")
        print(f"Premium Amount: {self.premium}")

# example usage
v1 = Vehicle("V001", "2 wheeler", 50000)
v1.display_details()

v2 = Vehicle("V002", "4 wheeler", 100000)
v2.display_details()
'''

class vehicle:
    def __init__(self,id,type,cost):
        self.__id=id
        self.__type=type
        self.__cost=cost
        self.__premium_amount=0

    def set_id(self,id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_type(self,type):
        if type =="Four Wheeler" or type=="Two wheeler":
            self.__type=type
        else:
            print("Invalid Input")
    def get_type(self):
        return self.__type

    def set_cost(self,cost):
        self.__cost = cost
    def get_cost(self):
        return self.__cost

    def premium_amount(self):
        if self.__type=="Two Wheeler":
            self.__premium_amount=0.02*self.__cost
        elif self.__type=="Four Wheeler":
            self.__premium_amount=0.06*self.__cost
        return self.__premium_amount

    def display(self):
        print(self.__id,self.__type,self.__cost,self.__premium_amount)

v=vehicle(101,"Two Wheeler",90000)
# v.set_id(200)
v.premium_amount()
v.display()


