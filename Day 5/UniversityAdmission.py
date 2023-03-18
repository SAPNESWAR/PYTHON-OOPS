'''
class Student:
    def init(self):
        self.__s_id=None
        self.__s_age=None
        self.__s_marks=None
    def validate_marks(self):
        if(self.__s_marks>0 and self.__s_marks<100):
            return True
        else:
            return False
    def validate_age(self):
        if(self.__s_age>20):
            return True
        else:
            return False
    def check_qualification(self):
        if(self.validate_marks() and self.validate_age() and self.__s_marks>65):
            return True
        else:
            return False
        
        
    def choose(self,c_id):
        if self.check_qualification():
            if(c_id == 1001):
                f = 25575.0
                if(self.__s_marks>85):
                    fees_to_paid = f - f*0.25
                    print("fees to be paid is ",fees_to_paid)
                else:
                    print("fees to be paid is ",f)
            elif(c_id == 1002):
                f = 15500.0
                if(self.__s_marks>85):
                    fees_to_paid = f - f*0.25
                    print("fees to be paid is ",fees_to_paid)
                else:
                    print("fees to be paid is ",f)
            else:
                print("Invalid couse id")  
        else:
            print("not eligible")
    def set_id(self,x):
        self.__s_id = x
    def get_id(self):
        return self.__s_id
    def set_age(self,x):
        self.__s_age = x
    def get_age(self):
        return self.__s_age
    def set_marks(self,x):
        self.__s_marks = x
    def get_marks(self):
        return self.__s_marks

     
s1=Student()
s1.set_id(1010)
s1.set_age(98)
s1.set_marks(66)
s1.choose(1009)

s2=Student()
s2.set_id(1011)
s2.set_age(36)
s2.set_marks(99)
s2.choose(1001)
                         
'''

class student:
    def _init_(self):
        self.__id=None
        self.__marks=None
        self.__age=None
        self.__course=None
        self.__discount_price=0

    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id

    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks

    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

    def set_course(self,course):
        self.__course=course
    def get_course(self):
        return self.__course

    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False

    def validate_age(self,):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if (self.validate_marks()==True and self.validate_age()==True and self.__marks>=65):
            return True
        else:
            return False

    def course_selection(self,):
        if self.check_qualification()==True:
            if self.__marks>85:
                if self.__course==1001:
                    self.__discount_price=25575-25575*0.25
                elif self.__course==1002:
                    self.__discount_price = 15500 - 15500 * 0.25
            else:
                if self.__course == 1001:
                    self.__discount_price = 25575
                elif self.__course == 1002:
                    self.__discount_price = 15500
        return self.__discount_price

    def display(self):
        if self.check_qualification()==False:
            print("Student having id: ",self.__id," is not eligible for admission")
        else:
            print("Student having id: ",self.__id," is qualified and the course price is",self.__discount_price)

s1=student()
s1.set_id(101)
s1.set_age(22)
s1.set_marks(87)
s1.set_course(1001)

s1.validate_age()
s1.validate_marks()
s1.course_selection()
s1.display()
