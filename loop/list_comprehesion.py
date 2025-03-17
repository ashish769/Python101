#list comprehension-->it is used to clean program in a error free in one line code

a=["sujan",'ram','shyam',"ashish"]


# for i in a:
#     print(len(i))

#syntax:[expression for item in iteratable(loop)]

# b=[len(i) for i in a]
# print(b)


a=[1,2,3,4,5,6]
# b=[2,4,5,6,7,8]
b=[i+2 for i in a]
print(b)

# c=[a[i]+b[i] for i in range(len(a))]
# print(c)

# a=["sujan",'ram','shyam',"ashish"]
# b=[f"{i}={len(i)}" for i in a]
# print(b)


#print the even number in the list
# a=[1,2,3,4,5,6,7,8,9]
#for if statement
# b=[i for i in a 
# if i%2==0]

#print(b)
#syntax:[Expression if condition else expression for i in iterator]
# b=["even" if i%2==0 else "odd" for i in a]

# print(b)

#for nested loop

# syntax:[[expression for j in range(3)] for i in range(5)]

# var=[[i+j for j in range(3)] for i in range(5)]
# print(var)


# a=["ashish","bishal","name","sujan","hello"]


# b=[len(i) for i in a]
# print(b)

# a=[1,2,3,4,5,6,7,8]
# b=[i for i in a if i%2==0]
# print(b)



a=[1,2,3,4,5,6,7,8]
print(a)
b=["even" if i%2==0 else "odd" for i in a]
print(b)