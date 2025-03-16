# dictionary->it is the collection of the data item in the key value pair,mutable,order,do not aloow duplicate
# a={
#     "name":"sujan",
#     "age":88,
#     45:99
# }

# print(a.get("name","data not found"))
# print(a["name"])
# # print(a["nam"])#throw an error
# print(a.get("nam","data not found"))


# a=dict(name='sujan',age=23)#another way of defining dictionary

# print(len(a))
# print(a)
# print(type(a))

# print(a.values())
# print(a.keys())
# print(a.items())


#nested dictionay

# student={
#     "roll no 1":{
#         "name":'sujan',
#         "age":22
#     },
#     "roll no 2":{
#         "name":'dipak',
#         'age':12
#     }
# }
# print(student["roll no 2"]["name"])
# print(student.get("roll no 2").get("name"))


a={
    "name":'sujan',
    "age":88
}

# b={
#     "age":89,
#     "email":"ram@gmail.com"
# }


# a["email"]="sujan@gmail.com"
# a.update(b)#it add the value of b to the a in this scenario age is overwrite and update a
# print(a)
# a.update["age"]
# a.pop("age")
# del a["age"]

# a.popitem()
# print(a)
# a.popitem()
# print(a)
# print(a)
var=a.setdefault("email",'sujan@gmail.com')
print(var)
print(a)
# var=a.copy()


# a=[1,2,3,4,5,6]
# print(dict.fromkeys(a,"sujan"))



#wap that creates a dictionary representing a student's grade in different subjects and then calculate the students average grade or percentage

# percentage={
#     "math":77,
#     "science":74,
#     "english":43,
#     "nepali":55,
#     "account":88,
# }

# num=len(percentage)
# var1=percentage.values()
# print(var1)

# total=sum(var1)
# result=(total/num)
# print(" obtained percentage is",result,"%")


# #make a nepali dictionary where user can search the nepali meaning of the items

# Nepali={
#     "name":"नाम",
#     "love":"माया",
#     "leaf":"पात",
#     "mother":"आमा",
#     "father":"पिता",
#     "brother":"दाजु",
# }
# str=input("enter your key:=>")

# print(Nepali.get(str,"value not found"))

