#decorator:it is a type of function which takes another function as argument and add more functionality and return another function

#first step
# def fun():
#     print("hello sipalaya")
#     return "tmt"
    
# fun()
# print(fun())#this gives the the nonw value if return is not present in the function

#second step

# def show():
#     print("hello sipalayaa")

# a=show#making a object of the show function

# a()

#nested function
# def show():
#     print("this is an outer function")

# def outer():
#     def inner():
#         print("this is inner function")
#     print("this is outer function")
#     inner()
    
#     return show()


# a=outer
# a()


#a function that can take another function as an argument


# def show(fun):
#     print("this is show function")
#     fun()
    
# def fun():
#     print('this is an fun function')
    
# a=show
# a(fun)

#decorator in python 


# def outer(func):
#     def inner():
#         print("this is an inner function")
#     print("this is an outer function")
#     func()
#     return inner#it is an inner function

# @outer
# def show():
#     print("this is an argument function")

# show()
#another example-->mainly decorator is a special kind of function which takes our original function as an argument and the make our function more decorative or adds the some feature in the function
#in above case outer function takes  an argument function func() or show() beacause we define the function outer as a decorator so the our original function i.e show() is decorated with the features of the outer function 
def greet(fun):
    def sayNamaskar():
        print("Namskar! all of you")
    print("this is an greet function")
    fun()
    return sayNamaskar#saynamskar is also an function so prenthesis is not required for the return function
    
@greet
def show():
    print("this is an argument function")

show()