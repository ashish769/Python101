#exception handling---the process responding unexecpted event occur when program is run
#it help to reduce data crash or data loss

# try:
#     def show(a):
#         print(a)
        
#     show("sujan") 

# except:
#     print("some error occur in your code")
    
# print("some imp code ")

#error
#mainly three error
# syntax error
#run time error
# def show(a):
#         print(a+3)
        
# show("sujan") 


#logical error
# def show():
#     print(2*3)#hamlai ans chai chaiyeko 5 xa tarw logic bigarerw rakheko xa 
        
# show() 


#run time error
#type error
#ZeroDivisionError
#NameError
#IndexError
# def show(a):
#     # print(a/0)
#     b="sujan"
#     print(b[9])
        
# show(2) 



# try:
#     def show(a):
#         # print(3/0)
#         print(a+2)
        
#     show("sujan") 
    
# except ZeroDivisionError:
#     print("you shouldnot divide same value by zero")
# except TypeError:
#     print("you data should be in same type")
# except:
#     print("some error occur in your code")
    
# print("some imp code ")




# finally:  always excuted
# try:
#     def show(a):
#         print(a)
        
#     show("sujan") 

# except:
#     print("some error occur in your code")
    
# finally:
#     print("some imp code ")


def show():
    try:
        print("my name is sujan")
        print("sujan"[9])
        
    except:
        print("error ayo hai")
        return 
    finally:
        print("hello sipalaya")
    
show()
    