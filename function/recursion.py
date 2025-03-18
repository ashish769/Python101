#recursion->those kind of function which call itself again and again to compute a value

# def show(n):
#     if n==10:#base case stop condition
#         return#it stop the looop here
#     print("hello",n)
#     show(n+1)
# show(0)

# import sys
# sys.setrecursionlimit(200)
# print(sys.getrecursionlimit())



#factorial of the given number
# def fact(num):
#     if num==0 or num==1:
#         return 1;
#     return num*fact(num-1)

# print(fact(5))



def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
    
print(fact(5))