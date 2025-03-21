#mainly two types of programming language
#1.procedural progrsmming language
#2.oops

#oop-->objet oriented programming language
#it match all the variable in real worls context
#it mao in the real world scenario


#oops is group of class and object
#class--> blueprint of object,template of creating a object ,group of object
# object-->instance of the class

#class-->attribute  and method
#attribute-->it represent variable which hold data
#method-->similar to function which perform specific task


#syntax 
#class Class_name:

# class Student:
#     def __init__(self,name,age) -> None:#self is not a keyword it is an variable or argument
#         self.name="ashish"
#         self.age=12
#         print("constructor called")
#     def show(self,price):
#         self.price=price
#         print(f"my name is {self.name} and age  is {self.age} and price is {self.price}")
        
# r1=Student("sujan",19)
# r1.show(7000)

# r2=Student("sujina",16)
# r2.show()


# class Shop:
#     def __init__(self,name,price,qty) -> None:
#         assert qty>0,price>0#it make quantity is always +ve as well as price
#         self.name=name
#         self.price=abs(price)#it works as a modulus value
#         self.qty=abs(qty)
#     def total_price(self):
#         print(f"my product name is {self.name} and price is {self.price*self.qty} and quantity is {self.qty}")


# obj=Shop("Book",-2000,-4)
# obj.total_price()

# x,y,z=45,43,41

# if x>y and x>z:
#     max=x
# elif y>z:
#     max=y
# else:
#     max=z
    
# print(max)

def summation(a,b):
    print(a+b)