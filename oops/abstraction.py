#abstraction-->hidding unnecessary data or innformation from user to reduce complexity

# print("hello")

# import basic
# basic.summation(3,4)


# from basic import summation#there is a function summation in the file basic.py which is imported towardss this file 
# summation(5,6)

# print(sum([1,2,3,4,5,6]))#we only know the function of sum 



#to acheive the abstraction  we use the abstract method and the abstract class


#interface -->only the abstract Method(one or many) in this class
#concrete Method --->this is the normal function within the class

# from abc import abstractmethod,ABC

# class Student(ABC):#abstract class
#     @abstractmethod
#     def show():#abstract method
#         pass
#     def display(self):
#         print("this is display method")
# class A(Student):
#     def show(self):
#         print("this is good")
#     def checkout(self):
#         print("this is checkout")
        
# a=A()
# a.display()
# a.show()
# a.checkout()