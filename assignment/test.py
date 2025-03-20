# def function(str):
#     lower=0
#     upper=0
#     for i in str:
#         if i.islower():
#             lower+=1
#         else:
#             upper+=1
#     print(f"no of lower case letter is :{lower}")
#     print(f"no of upper case letter is :{upper}")
        
            


# str=input("enter the string ")
# function(str)


#_________________________________________________
# def Multiplication(num):
#     for i in range(1,11):
#         print(f"{num}*{i}={num*i}")
# num=int(input("enter any number"))
# Multiplication(num)


#______________________________________________________
# def prime(num):
#     if num<=1:
#         print("neither prime nor non prime",num)
        
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num,end=" ")
    

# start=int(input("enter the starting point"))   
# end=int(input("enter the end point"))   

# for i in range(start,end):
#     prime(i)

# ____________________________
dict1={}
dict2={}
num=int(input("Enter the no of entries you want to add=>"))

for i in range(num):
    k=input("enter the key value=>")
    v=int(input("enter the value of the above key=> "))
    dict1['k']=v
    print(dict1)
    
    for i in dict.keys():
        a= i.sorted()
    for i in dict.values():
        b=i.sort()
        
for i,j in zip(a,b):
    dict2['i']=j
    print(dict2)
    




