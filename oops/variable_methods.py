#class->blueprint
#class-->attribute and method


#ttribute --> it represrnt variable
#attribute
#instance variable
#class variable/static variable

#method-->similar to function
#instance method
#class method
#static method

#instance variable-->those variable which single copy is created for every object(make different location for ever variable made from thee object)
#define and initialize using constructor with self parameter

# class Student:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.name=age
        
#     def show(self):
#         print(f"hello sipalaya my name is {self.name} and age is {self.age}")#self.variable_name
    
# a=Student("sujan",90)
# a.name="ashish"
# a.show()
# print(a.name)#acess instance variable outside the class:object_name

# b=Student("ram",40)
# b.show()

#class variable-->those variable  which seperated copy of file is created for every object
#define and initialize using constructor with cls parameter

class Student:
    school="Mangala"#class variable
    def __init__(self,name) -> None:
        self.name=name#instant variable
    def show(self):
        print(f"my name is {self.name}")#self.variable_name
    @classmethod
    def display(cls,hello):#class method -->it is use acess class variable
        cls.hello=hello
        print(f"my name is {cls.school}")#cls.variable_name

a=Student("sujan")
a.display("untitle")
print(Student.school)#class_name.variable_name

b=Student("ram")
b.display()

print(Student.school)

#static Student:

class Student:
    def __init__(self,name) -> None:
        self.name=name
    @staticmethod
    
    def show(a,b):
        print(a+b)
a=Student()
a.show(2,3)
        
        


