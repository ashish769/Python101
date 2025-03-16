#tuple-> coolection of item which is immutable order and allow duplicate value
# a=("sujan",23,44,7.8,6,6)
# print(type(a))
# print(a[0])
# print(a[0:2])

# #it is different from the list because list use the more memory than the tuple.so we can change list to the tuple for the increase in the performance
# print(a.count(6))
# print(a.index("sujan"))


#to show the facebook only from www.facebook.com

# a="www.facebook.com"
# b=a.lstrip("w.")#all the value i.e(w.)coming at the begging is striped
# c=b.find(".")
# print(b[:c])

# #alternative
# print(a.removeprefix("www.").removesuffix(".com"))


a=""
print(bool(a))