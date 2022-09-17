# LinkedIn Learning Python course by Joe Marini

# Basic data types in Python: Numbers, String, Booleans, Sequences, Tuple, Dictionaries
myint = 5
myfloat = 13.2
# mystr = "This is a string"
mybool = True
mylist = [0,1,"two",3.2,False]
mytuple = (0,1,2)
mydict = {"one" : 1, "two":2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works
# myint = "abc"
# print(myint)

# to access a memeber of a sequence type, use []
# print(mylist[2])
# print(mytuple[1])

# use slices to get parts of a sequence
# print(mylist[2:5]) # [start index : end index -1 : steps(step to skip)]
# print(mylist[0::2])

# you can use slices to reverse a sequence
# print(mylist[::-1]) # [::] means default value

# dictionaries are accessed via keys
# print(mydict["one"])

# ERROR : variables of different types cannot be combined
# print("string type " + 123) # in python different datatype does not work
# TypeError: can only concatenate str (not "int") to str
# print("string type " + str(123))

# Global vs Local variables in functions

# def someFunction():
#     # Local var
#     mystr = "definition"
#     print(mystr)

# someFunction()
# mystr = "This is a string"
# # Global var
# print(mystr)

# If I want to affect the value of local variable to global variable

mystr = "This is a string"
def someFunction():
    # Local var
    global mystr # This affects datatype-var in global which is mentioned above
    mystr = "definition"
    print(mystr)

someFunction()
# Global var
print(mystr)

# NameError: name 'mystr' is not defined 
# del mystr
# print(mystr)