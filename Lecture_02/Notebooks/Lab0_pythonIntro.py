# this is a comment
# We start with numbers
# define and assign variables a and b
a = 17
b = 3
# a and b are defined as int values
c = a / b # c is now a float
d = a // b # floor division
print(d)
e = a % b # remainder of the division
print(e)
# floored quotient * divisor + remainder
print( d * b + e )

# simple power format
a = 8**2
print(a)
# strings are arrays of characters
s = "Python"
print(s[2])
print(s[-4])
# Strings can be concatenated
s = "hello " + s
print(s)
# Portions of scrings may be selected
print(s[5:])

# Python list is an array of values, like strings
myList = range(10)
print(myList)
# now we define a list of cube values through a for cycle
cubes = [] # empty list
for i in myList: # loop through myList
    cubes.append(i**2) # append cube values to cubes

print(cubes)
# the same result can be achieved simply by
cubes = [i**2 for i in myList]
print(cubes)
# this one line python list definition
# makes code run faster an easier to read

# definition of a function that returns a python list
# of cube values in a range Xmin to Xmax
# by defaul Xmin = 0
def CubesList(Xmax, Xmin=0):
    # check if Xmax > Xmin
    if Xmax < Xmin:
        # if Xmax < Xmin we return an error message
        # and exit the function
        print("Error Xmax < Xmin")
        return 1

    # check if values are integers
    if not isinstance(Xmax,int) or not isinstance(Xmax,int):
        # if not int we return an error message
        # and exit the function
        print("Error Xmax or Xmin are not integers")
        return 2 

    # now we define the list
    return [ i**2 for i in range(Xmin, Xmax)]

# Use the function
print(CubesList(-2))
print(CubesList(2.4))
print(CubesList(4,12))
print(CubesList(12,4))
print(CubesList(12))
