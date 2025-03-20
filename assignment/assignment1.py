#assignment first

#Q1.find the name only from the user gmailaccount
gmail=input("enter the gmail:-")

index=gmail.find("@")
print(gmail[:index])

# remove the double space with the single
str="my  name"
print(str.replace("  "," "))


#Q2.swap the first and last letter of the string


str2=input("enter the string=>")

print(str2[-1]+str2[1:-1]+str2[0])

#Assignment-2

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

#dictionary
#wap that creates a dictionary representing a student's grade in different subjects and then calculate the students average grade or percentage

percentage={
    "math":77,
    "science":74,
    "english":43,
    "nepali":55,
    "account":88,
}

num=len(percentage)
var1=percentage.values()
print(var1)

total=sum(var1)
result=(total/num)
print(" obtained percentage is",result,"%")


#make a nepali dictionary

Nepali={
    "name":"नाम",
    "love":"माया",
    "leaf":"पात",
    "mother":"आमा",
    "father":"पिता",
    "brother":"दाजु",
}
str=input("enter your key:=>")

print(Nepali.get(str,"value not found"))


