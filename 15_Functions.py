#defining a function
'''
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
'''

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

#calling a function

printme("This is first call to the user defined function!")
printme("Again second call to the same function")



#pass by reference Vs pass by value
def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function before change: ", mylist)
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

#Types of arguments
'''
Required arguments
Keyword arguments
Default arguments
Variable-length arguments
'''

#Range - Range of values
#Lambda - Single line expression functions
#lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda arg1, arg2: arg1 + arg2


# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

#map function

'''
items = [1, 2, 3, 4, 5]
squared = []
for x in items:
	squared.append(x ** 2)
'''

items = [1, 2, 3, 4, 5]
def sqr(x): return x ** 2
list(map(sqr, items))

#lambda and map together

def square(x):
    return (x ** 2)


def cube(x):
    return (x ** 3)


funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print(value)


#Filter - cuts down the range according to condition

list( filter((lambda x: x < 0), range(-5,5))) #prints only negative numbers

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(filter(lambda x: x in a, b))  # prints out [2, 3, 5, 7]

''' List Comprehension
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print[x for x in a if x in b]
'''