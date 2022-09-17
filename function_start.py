# LinkedIn Learning Python course by Joe Marini

# Example file for working with functions
#3/Sep/2022 (Sat)



# TODO : define a basic function
def fun1():
    print("This is function 1")

# fun1()
# print(fun1()) 
#  output: "This is function 1"
#  None
# print(fun1) #<function fun1 at 0x0000017C783C3E20>


# TODO : function that takes arguments
def fun2(arg1,arg2):
    print(arg1," ",arg2)

# fun2(10,20)
# print(fun2(10,20)) # output: 10 20 /n None

# TODO : function that returns a value
def cube(x):
    return x*x* x

# cube(3) # output : no result
#print(cube(3)) # 27

# TODO : function with default value for an argument
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
        print(result)
    return result
    

# print(power(2))
# print(power(2,3))
# print(power(x=3,num=2))

# TODO : function with the variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(3,5,6,2,23))



