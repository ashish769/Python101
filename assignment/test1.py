
def fun(show):
    def display():
        print("this is an display function")
        return show()
    return display
@fun
def sum():
    print("this is an sum function")

sum()

# class Car:
#     grade=9#class variable
#     def __init__(self,n,age) -> None:
#         self.name=n
#         self.age=age
#     def display(self):
#         print("my name is {self.n} and {self.age}")
#     @classmethod
#     def show(cls):
        
#         print(f"grage is {cls.grade}")
        
# Car('ashish',2020)
# Car.display()
# Car.show()
