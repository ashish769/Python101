#nested looop
# a=["sujan",'ram','syam','hari']
# for i in a:
#     print(i)
#     for j in i:
#         print(j)
        
#find the second largest value in the list  withoutusing a inbuild function    
# a=[3,4,5,6,1,2,3]

# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]


# print(a)          
# print("second largest number is",a[-2])
    

# a=[13,15,45,34,45]
# b=[]
# for i in a:
#     b.append(i+2)
# print(b)

a=[1,2,3,4,4,5]
b=[2,4,6,8]
c=[]
# for i in range(len(a)):
#         c.append((a[i]+b[i]))
# print(c)

# for i,j in zip(a,b):#it didnot throw an error if index is not same
#     print(i+j)