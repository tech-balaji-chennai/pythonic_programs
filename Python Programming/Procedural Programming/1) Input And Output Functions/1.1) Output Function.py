"""
Input And Output Functions:
An interface between a user and a program (system)
Program interacts with user to accomplish the desired task

1.1) Output Function: print()
displays constants or variable values on the screen using standard output (stdout) (default output device = monitor)
Syntax:
print(value_1, value_2, ..., value_n, sep=" ", end="\n")
"""

"""
Parameters in print() function
i) value (constant)
ii) sep
iii) end
iv) file
v) flush
"""

#i) value (constant) - prints value on the screen
print("hello")
print(1)

#Types of values (constnts): 4

#a) Integer Constants - any integer value

#Example 1: Normal integer value
print(5)

#Example 2: Binary value to integer value
print(0b1011)

#Example 3: Fetching stored value from variable x
#value stored in variable x
x=2
#fetches the value stored in memory of variable x and displays it on the screen
print(x)

#Example 4: evaluation of expression
#expression of values is evaluated according to pemdas rule (ordeer of precedence) and then printed in the screen
print(5+10*15-20/25)

#b) String Constants - any character or value within quotes are considered as strings

#Example 1: value within single quotes
print('Single Quote')

#Example 2: value within double quotes
print("Double Quotes") #value within double quotes

#Example 3: value within single triple quotes
print('''Single Triple Quotes''') #value within  quotes

#Example 4: value within double triple quotes
print("""Double Triple Quotes""")

#c) Boolean Constants - True, False
print(True)
print(False)

#d) None Constant - None
print(None)

#single value
print("hello")
print(1)

#More than 1 value (ir) arguments are separated by commas (,)

#Example 1:
print(5,10)

#Example 2:
print(2,"Hello") #displays 2 values with default space between them on the screen

#Example 3:
#stores value 5 in variable y
y=5
print("""World""",y)

#ii) sep - how to separate the objects when there are more than 1 value is given (Default = ' ')
print("Welcome","To","The","World","Of","Python") #by default, sep = ' '
print("Welcome","To","The","World","Of","Java", sep = '\n')
print("Welcome","To","The","World","Of","C++", sep = ',')
print("Welcome","To","The","World","Of","C", sep = ':')

#iii) end - what to print at the end of value in  the current line (Default = '\n')
print("Welcome","To","The","World","Of","Python") #by default, end = '\n'
print("Welcome","To","The","World","Of","Java", end = ' ')
print("Welcome","To","The","World","Of","C++", end = ',')
print("Welcome","To","The","World","Of","C", end = 'Bye')

#To print an empty line
print()

#To print 2 empty lines
print('\n')

#iv) file - an object with a write method (Default = sys.stdout)

#v) flush - a boolean specifying if the output is flushed (True) or buffered (False) (Default = False)

#return value of print() function - None value (NoneType Object)
r = print()
print(r)
print(type(r))
