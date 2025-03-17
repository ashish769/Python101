#looop---->it is used to repeat again and again to complete a specific condition to match
#for loop->performance fast
#while loop->

#for loop->it is used for the predetermine number
#it is used for traversal sequence i.e list tuple set dict

# a=['sujan','ram','shyam','hari']

# for name in a:
#     print(name ) #for single line
    
# for i in range(start,end,step)

# for i in range(2,10,2):#:is called the indentation to notify the block of code
#     print(i)
    
# #find the multiplication 
# num=int(input("enter the number you want to print the multiplication table"))
# for i in range(10):
#     print(f"{num} X {i+1}={num*(i+1)}")
    
    
#find the palindrom word from the list given


a=['sujan','mom','madam','ram','crac',141,222,343]
b=[]

# for i in a:
    
#     if str(i) == str(i)[::-1]:
#         b.append(i)
        
# print(b)

#alternative

# for i in range(len(a)):
#     if str(a[i])==str(a[i])[::-1]:
#         b.append(a[i])
        
# print(b)


#string="aabbssae"
#print this in dict like{"a":3,"b":2,"s":2,"e":1}

str="aaabbsse"
di={}
for i in str:
    if i  in di:
        di[i]+=1
    else:
        di[i]=1
  
print(di)      