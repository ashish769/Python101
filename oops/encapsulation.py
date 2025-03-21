#encapsulation-->wrapping a data(variable ) and methods(functions) that operate the datawith in single unit
#main advantage of the encapsulation
#data hiding and encapsulation
#data protection
#

#to achieve encapsulation we use access modifier and property decorator

#access modifiers: it restrics methods and attributes to acess globally by using private protected 

#public:methods and attribute can be acessible from outside the class
#private: only within the class
#protected: Acess only within class and subclass(child class)


# class A:
#     def __init__(self):
#         self.__name="sujan"#private variable
#     def __show(self):
#         print(f"my name is {self.__name}")

# 
        
# a=A()
# # print(a.__show())#this didnot access because the show function is private
# print(a.__dict)
# print(a._A__show())

# class A:
#     def __init__(self):
#         self._name="sujan"#private variable
#     def _show(self):
#         print(f"my name is {self._name}")
# class B(A):
#     def __init__(self):
#         print(f"my name is {self._name}")
  
      
# b=B()



#property decorator 
#inbuild decorator are three types
#static method 
#classmethod
#getter:access the value(get)
#setter:set or change the value 
#deleter:delete value

# class A:
#     def __init__(self):
#         self.__name="sujan"
#     @property
#     def show(self):
#         print(f"my name is {self.__name}")
#     @show.setter
#     def show(self,new):
#         self.__name=new
#     @show.deleter
#     def show(self):
#         self.__name="No data"
    
# a=A()
# a.show="ram"
# del a.show
# a.show






