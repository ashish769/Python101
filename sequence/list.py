# # list->collection of data item or data items. which is mutable, ordered,allow duplicate
# a=["sujan",1,2,3.5,True]
# # print(type(a))
# # print(len(a))
# # print(a[0][2])#print the first string and print the second index of the sujan
# # print(a[0:2])

# PI=3.14# const is not define in python but generally const variable define in capital letter

# a[0]="ram"

# a.insert(0,"gita")#inset the value in the 0th index
# a.append("hari")#insert in the last place of the list#it support only one 
# a.extend([2,3,4])#it insert the multiple data at a time
# a.pop()#it pop the value from the last index
# a.remove("sujan")
# a.clear()#it  empty the list
# del a#it destroy the variable also
# print(a)


# a=[1,5,7,6,4,2,3,8]
# print(a.sort())#it change in the original value but sorted() make the new 
# print(a.reverse())

# b=sorted(a,reverse=True)#it make the new list 

# b=a#it does the copyalso

# a=[1,2,3,4,5,6]
# b=a.copy()#while changing on the original data copied data also can be changed

# a=["ashish","ram","hari"]
# b=" +".join(a)#this is not applicable for the integer data type
# print(b)

#it swap the value of a and b
# a,b=40,50
# a,b=b,a


# sent=input("enter the sentence:-")

# b=sent.split(" ")
# print(len(b))


# a="my name is sujan"
# b=a.split(" ")
# b.reverse()
# print(b)
# c=" ".join(b)
# print(c)



#assignment

#input the five fruit name show then in a list
str=input("enter the five fruit name:=>")
print(str.split())
# #exchange the first and last element of the list
arr=["my","name",'is','ashish']
arr[0],arr[-1]=arr[-1],arr[0]
print(arr)

#find the second largest number from the list
arr=[1,5,8,9,3,5,7]
b=sorted(arr,reverse=False)
print(b)
arr.sort()
print(arr[-2])





