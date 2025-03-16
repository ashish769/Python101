#conditional statement:making decision based on a variable hold or result
#if statement

#syntax
#if condition:
    #statement;
#else:
    #expresiion
    
# a=23;
# if a<25:
#     print(" if statement executed");
# else:
#     print("else statement executed");
    
#one line statement

# age=20

# if age>=18:
#     print("you can vote")
# else:
#     print("you are not eligeable for vote ");

#shorthanded if statement

# print("you can vote now") if age>=18 else print("you cannot vote");


# age=int(input("enter your age:"))
# if age<12:
#     print("fare=24");
# elif age>12 and age<18:
#     if age==15:
#         print("fare is free for this age")
#     else:
#         print("fare=34")
# else:
#     print("fare=56")


#find the data type of the variable

a=" "
# b=type(a)


# if  b == str:
#     print("data type is str")
# elif b == int:
#     print("data type is int")
# elif b == list:
#     print("data type is list")
# else:
#     print("not found")

#alternative

# if isinstance(a,int):
#     print("this is integer")
# elif isinstance(a,float):
#     print("this is float")
# elif isinstance(a,list):
#     print("this is list")
# else:
#     print("other")
    
    

#find the user enter string or digit in the input field
# a=input("enter your input:")

# if a.isdigit() :
#     print("input is digit or base 10")
# else:
#     print("input is string")


#find the last digit of the number
a=int(input("enter your input=>"))
print(a%10)