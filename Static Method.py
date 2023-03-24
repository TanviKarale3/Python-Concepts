#In this program, we define a class MyClass that has a static method my_static_method(). 
#We use the @staticmethod decorator to indicate that this method is a static method.
class MyClass:
    @staticmethod
    def my_static_method(x, y):
        return x + y
# Calling the static method without creating an object of the class
result = MyClass.my_static_method(3, 5)
print("Result:", result)


#This method can be call without creating an object
#create a class mylib

class Mylib:
    @staticmethod
    def fact(n):
        f=1
        for i in range (1,n+1):
            f=f*i
        return f
    @staticmethod
    def sum(n):
        s=0
        for i in range(1,n+1):
            s=s+i
        return s
    
print("factorial is", Mylib.fact(5))
print("sum is",Mylib.sum(5))


#Design a class mydata using static method

class Mydata:
    @staticmethod
    def max(n,m):
        if(n>m):
            return(1) #n is greater
        else:
            return(0)  #n is smallar
    def min(n,m):
        if(n<m):
            return(1)  #m is greater
        else:
            return(0)  #m is smallar
print("Max no is",Mydata.max(5,3))
print("Min no is",Mydata.min(3,5))    
    
