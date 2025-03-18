# iterator-object that contain countable number value (iterate over the collection of the items)
#eg:list,tuple,set,dict
# def show(a):
#     c=[]
#     for i  in a:
#         c.append(i+2)
#     print(c)
    
# a=[1,2,3,4,5,6]
# print(show(a))


# high order inbuild function are map(),filter(),reduce()

#map()-->build in function which execute specific function in all item 

# def show(n):
#     return n*n

# a=[1,2,3,4,5]
# var=map(show,a)
# print(list(var))

#filter

# b=list(filter(lambda a:a%2==0,a))
# print(b)

#reduce
# from functools import reduce

# var=reduce((lambda x,y:x+y),a)#it takes x as a 1 and y as a 2 and sum this two value and take in the x value and so on to sum the all value of the list
# print(var)



# var=set(map(lambda x:x+2 ,s))
# print(var)

a=[1,2,3,4,5,67]
# b=[]
# for item in a:
#     var=item+2
#     b.append(var)
    
# print(b)

# print(list(map(lambda x:x+2 ,a)))
print(list(filter(lambda x:x%2==0 ,a)))