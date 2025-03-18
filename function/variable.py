#variable: reserved memory location which store value
#type of variable:
# local variable 
# global variable

# a=20
# a=40 #reassign
# print(a)

# course="python" #global variable ___used to declare outside function
# def show():
#     course="django" #local variable ---variable which is declare inside the function
#     print(course)

# show()
# print(course)


# a=30
# def show():
#     b=20
#     print(b,"local variable")
#     print(a,"global variable")

# show()
# print(a,"global variable")
# #print(b)


# a=20
# b=50
# def show():
    # global a
    # x=globals()['b']
    # print(x)
    # a=a+3
    # print(a)

# show()


a=12
b=13
def fun():
    global a
    print(f'value of a is {a}')
    
    print(f"the vlaue of b is {b}")
    
fun()