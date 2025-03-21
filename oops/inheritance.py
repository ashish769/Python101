#fundamental concept 
#1.inheritance
#2.polymorphism
# 3.encapsulation
#4.abstraction
#inheritance-- a class is inherit all method and attribute from another class

#base classs--parent class
#derived class-->child class
#total five type
#single inheritance

# class A:
#     def feature1(self):
#         print("i have feature1")
# class B(A):#class A features are inherit in the class B
#     def feature2(self):
#         print("i have feature 2")
        
# b=B()
# b.feature2()
# b.feature1()

#single level inheritance(multilevel)

# class A:
#     def feature1(self):
#         print("i have feature1")
# class B(A):#class A features are inherit in the class B#child class
#     def feature2(self):
#         print("i have feature 2")
# class C(B):#grand child
#     def feature3(self):
#         print("i have feature 3")
        
# c=C()
# c.feature2()
# c.feature1()
# c.feature3()

#multiple inheritance
# class A:
#     def feature1(self):
#         print("i have feature1")
# class B:#child class
#     def feature2(self):
#         print("i have feature 2")
# class C(B,A):#grand child
#     def feature3(self):
#         print("i have feature 3")
        
# c=C()
# c.feature2()
# c.feature1()
# c.feature3()

#Hirarchichal inheritance#one parent has the multiple child
# class A:
#     def feature1(self):
#         print("i have feature1")
# class B(A):#child class
#     def feature2(self):
#         print("i have feature 2")
# class C(A):#grand child
#     def feature3(self):
#         print("i have feature 3")
        
# c=C()
# b=B()
# b.feature2()
# b.feature1()
# c.feature1()
# c.feature3()

#hybrid  inheritance :it is the mixture of all type of the inheritance 
class A:
    def feature1(self):
        print("i have feature1")
class B:
    def feature2(self):
        print("i have feature 2")
class C(A):
    def feature3(self):
        print("i have feature 3")
class D(C,B):
    def feature4(self):
        print("i have feature 4")
c=D()
c.feature1()
c.feature2()
c.feature3()
c.feature4()



