#wap to take two list as a input and returns a new list the contains only common value

# def common(a,b):    
#     c=set(a).intersection(set(b))
#     print(list(c))
# a=[1,2,3,4,5,6]
# b=[3,4,6,7,8]

# common(a,b)

#take a list from the  input and the sort it in the decending order in such a way that first only odd number should be added and then the even number

a=input("enter you list with space")
b=a.split()
b=list(map(int,b))


b.sort(reverse=True)
print(b)
odd=(list(filter(lambda x:x%2!=0 ,b)))
even=(list(filter(lambda x:x%2==0,b)))
    
print(odd+even)
    
    
    
    


 
    
