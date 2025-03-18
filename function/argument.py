#argument-

#four types
#positional ,keyword,default,arbitary argument

#positional argument

# def user(name,age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
    
# user('ashish',12)#position affects

# #keyword argument

# def user(name,age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
    
# user(age=12 ,name='ashish')#positon doesnot matter while keyword is defined 

#default argument
# def user(name,age,address="syangja"):#default value is always at the last
#     print(f"my name is {name}")
#     print(f"my age is {age}")
#     print(f"my address is {address}")

# user('ashish',66)#if we pass the default value it overwrite the content of the default paramenter


#arbitary argument
# types
# 1.positional arnitary argument-
# 2.keyword arbitary argument


#1.positional argument-it has the prefix with asterisk(*)

# def show(a,*b):
#     print(a)
#     print(b)
#     c=0;
#     for i in b:
#         c+=i;
#     print(c)

# show(1,2,3,4,5,6)

#2.keyword arbitary argument

# def show(*a,**b):#* hold in the form of tuples and ** holds data i the form of dictionary
#     print(a)
#     print(b)
    
#     for i,j in b.items():
#         print(f"key:{i} value:{j}")
        
        
# show(1,2,3,4,5,name="sujan",age=22,address="ktm")
    

def number(*x,**y):
    print(x)
    print(y)
number(1,2,3,4,5,6,7,name='ashish',age=23,profession='student')

