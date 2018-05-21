#List of standard exceptions

'''
1
Exception

Base class for all exceptions

2
StopIteration

Raised when the next() method of an iterator does not point to any object.

3
SystemExit

Raised by the sys.exit() function.

4
StandardError

Base class for all built-in exceptions except StopIteration and SystemExit.

5
ArithmeticError

Base class for all errors that occur for numeric calculation.

6
OverflowError

Raised when a calculation exceeds maximum limit for a numeric type.

7
FloatingPointError

Raised when a floating point calculation fails.

8
ZeroDivisonError

Raised when division or modulo by zero takes place for all numeric types.

9
AssertionError

Raised in case of failure of the Assert statement.

10
AttributeError

Raised in case of failure of attribute reference or assignment.

11
EOFError

Raised when there is no input from either the raw_input() or input() function and the end of file is reached.

12
ImportError

Raised when an import statement fails.

13
KeyboardInterrupt

Raised when the user interrupts program execution, usually by pressing Ctrl+c.

14
LookupError

Base class for all lookup errors.

15
IndexError

Raised when an index is not found in a sequence.

16
KeyError

Raised when the specified key is not found in the dictionary.

17
NameError

Raised when an identifier is not found in the local or global namespace.

18
UnboundLocalError

Raised when trying to access a local variable in a function or method but no value has been assigned to it.

19
EnvironmentError

Base class for all exceptions that occur outside the Python environment.

20
IOError

Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.

21
OSError

Raised for operating system-related errors.

22
SyntaxError

Raised when there is an error in Python syntax.

23
IndentationError

Raised when indentation is not specified properly.

24
SystemError

Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.

25
SystemExit

Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.

26
TypeError

Raised when an operation or function is attempted that is invalid for the specified data type.

27
ValueError

Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.

28
RuntimeError

Raised when a generated error does not fall into any category.

29
NotImplementedError

Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.
'''

#Assertion Exception

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
#print (KelvinToFahrenheit(-5))

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()