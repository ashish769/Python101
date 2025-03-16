#set->collection of the similar type of item.which is mutable ,unordered,donot allow the duplicate value
# a={'sujan',1,2,'ram','shyam',"shyam"}#it didnot allow the duplicate value i.e shyam
# print(a)
#index and slicing is not allow in set


# set-{1,2,3,4,5,6,7}
# set.add(9)
# set.update({10,11,12,13})
# set.pop()#it is not a convinent waay to remove the data
# set.remove(4)#if the value not find it throw an error both are used to remove the data from the set
# set.discard(4)#if the value doesnot exist it didnot throw an error
# set.copy()#same 

#update add the value in the original location but union make a difference set

a={1,2,3,4,5}
b={2,4}
# b=a.copy()
# print(b)
# var=a.intersection(b)
# print(var)
# var=a.union(b)

# print(b)
# print(a.difference(b))

# print(a.symmetric_difference(b))#comlement of a intersection b

# print(a.issuperset(b))

# a.difference_update(b)#it update on the original a
# a.intersection_update(b)
# print(a)



# frozenset(a)#it frozen the set 

a={2,3,4,5,6,7,8}
b=frozenset(a)
print(b)#now this set b cannot be update because it is frozen
b.add(45)#throw an error





