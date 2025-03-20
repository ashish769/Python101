#1.leap year or not

# def is_leap_year(year):
#     if year%400==0 and year%100==0:
#         return True
#     elif year%4==0 and year %100!=0:
#         return True
#     else:
#         return False

# year=int(input("enter the year you want to check=>"))
# print(is_leap_year(year))

"""2.Write a Python function that takes two lists of integers 
as input and returns a new list containing only the numbers 
that are present in both lists, but with each number 
appearing only once in the final list.
"""
# #function decleration
# def check(lst1,lst2):
#    a= list(set(lst1).intersection(set(lst2)))
   
#    print(a)
# #input for first list
# user1=input("enter the number entering space=>")
# b=user1.split(" ")
# c=[]
# for i in b:
#    c.append(int(i))
# #input for second list
# user2=input("enter the number entering space=>")
# d=user2.split(" ")
# e=[]
# for j in d:
#    e.append(int(j))
# #function call
# check(c,e)

"""3.Write a Python program that takes a string
 as input and returns a dictionary where each key
   is a unique word in the string and the value is
     a list of the indices where that word appears in the string.
"""
# #function definition
# def string_to_dictionary(str):
#    dict={}
#    lst=[]
#    for i in range(len(str)):
#       if str[i] not in dict.keys():
#          dict[str[i]]=1
#       else:
#          dict[str[i]]+=1
#    print(dict)
# #input and function call   
# str =input("enter any string you want to insert=>")
# string_to_dictionary(str)


"""4.Write a Python function that takes a list of integers as input and returns a new list with
 the elements sorted in descending order, but with all odd numbers appearing before all even numbers.
"""

# def Test(lst):
#     l=sorted(lst,reverse=True)
#     j=[]
#     k=[]
#     for i in l:
#         if i%2!=0:
#             j.append(i)
#         else:
#             k.append(i)
#     return j+k



# str=input("enter the number entering the space=>")
# lst=str.split(" ")
# b=[]
# for i in lst:
#     b.append(int(i))

# print(Test(b))

"""5.Write a Python program that takes two sets as input and returns a new set containing
 the elements that are in the first set but not in the second set, and the elements that are
   in the second set but not in the first set.
"""
# def set_difference(set1,set2):
#     return set1.symmetric_difference(set2)


# str=input("enter the number entering the space=>")
# lst1=str.split(" ")
# b=[]
# for i in lst1:
#     b.append(int(i))
# b=set(b)

# str1=input("enter the number entering the space=>")
# lst1=str1.split(" ")
# c=[]
# for i in lst1:
#     c.append(int(i))
# c=set(c)

# print(set_difference(b,c))

"""6.Write a Python function that takes a list of strings as input and returns a new list
 containing only the strings that are palindromes.
"""

# def Palindrome(lst):
#     palin=[]
#     for i in lst:
#         if str(i)==str(i)[::-1]:
#             palin.append(i)
#     print(palin)


# user=input("enter the word seperating by space=> ")
# lst=user.split(" ")
# Palindrome(lst)

"""7.Write a Python program that takes a list of tuples, where each tuple contains a
 string and an integer, and returns a new list containing the tuples sorted by the
   length of the string, with ties broken by the value of the integer.
"""

"""8.Write a Python function that takes a dictionary as input and returns a new
 dictionary where the keys are sorted alphabetically and the values are sorted in
   descending order.
"""
# #function definition
# def Ordering(dict):
#     a=dict.keys()
#     b=dict.values()
#     s=sorted(a)
#     t=sorted(b)
#     dict1={}
#     for i,j in zip(s,t):
#         dict1[i]=j
#     print(dict1)

# #user input for the dictionary
# user=input("enter the key and value pair seperating by single space")
# lst=user.split(" ")
# key=[]
# value=[]
# dict={}
# for i in range(len(lst)):
#     if i%2==0:
#         key.append(lst[i])

#     else:
#         value.append(int(lst[i]))
# for i in range(len(value)):
#     dict[key[i]]=value[i]
# #function call
# Ordering(dict)

"""9.Write a Python program that takes a list of tuples, where each tuple contains
 a string and a set of integers, and returns a new list containing the tuples sorted
   by the sum of the integers in the set, with ties broken by the length of the string.
"""
""" 10.Write a Python function that takes a string as input and returns a new string
 where each word in the string is replaced with the word that appears most frequently
   in the string.
"""
# def Replace_string(str):
#     lst=str.split(" ")
#     for i in range(len(lst)):







# user=input("enter the string =>")
# Replace_string(str)

"""12.Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
For example nums = [1,2,3,4,5,6,7], k=3 should output [5,6,7,1,2,3,4] Do it with the least possible space. I.e O(1) space complexity.
Make your code as “pythonic” as you possibly can use shortcuts that may not be available i"""


def shifting(lst,n):
    lst1=lst[n+1::1]+lst[:n+1:]
    print(lst1)

str=input("enter the number entering the space=>")
lst1=str.split(" ")
b=[]
for i in lst1:
    b.append(int(i))

n=int(input("enter the number you want to shift the array"))
shifting(b,n)