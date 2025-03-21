#polymorphism--->one things in different form

# a="sujan"
# b="ram"

# v=len(a)
# print(v)

#duck type

# class A:
#     def show(self):
#         print("my name is ashish")
# class B:
#     def show(self):
#         print("MY NAME IS RAM")
# ashish=A()
# Ram=B()

# # ashish.show()
# # Ram.show()
# #using polymorphism technique
# def display(var):#single function can acess the multiple 
#     var.show()

# display(ashish)
# display(Ram)

# class A:
#     def show(self):
#         print("first show")
#     def show(self,a,b):
#         print(a+b)
#     def show(self,a,b,c):
#         print(a+b+c)
# a=A()
# a.show(1,2,3)#last ma jun function xa tei function call hunxa due to function overwriting
#handling of function overwriting
# class A:
#     def show(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#         elif a!=None and b!=None and c==None:
#             s=a+b
        
#         else:
#             s="nothing"
#             return s
# a=A()
# print(a.show(1,2))


#method overriding

# class A:
#     def show(self):
#         print("this is a parent class")
# class B(A):
#     def show(self):
#         print("this is a child class")
#         super().show()#this is called the super function
        
# b=B()
# b.show()#this shows this is child class because the object of the child class is made and the function name is same in the both class

 #super()-->it acess all the function of the parent class and
 
 
 #operator overloading 
 
# a=[1,2,3,4,5,6]
# b=[1,2,3,4,5]
# print(a+b)
# print(a.__add__(b))   # dunder function 

class A:
    def __init__(self,a):
        self.a=a  
    def __add__(self,other):
        return self.a+other.b
    def __sub__(self,other):
        return self.a-other.b
    
    
class B:
    def __init__(self,b) -> None:
        self.b=b
a=A(3)
b=B(1)
print(a+b)#it calls the __add__
print(a-b)

