"""
1.2) Input Function: input()
accepts data as input at runtime using standard input (stdin) (default input device = keyboard)
gets prompt string as argument (optional) - statement / message to the user, to know what input can be given
Syntax:
variable_1_name = variable_2_name = ... = variable_n_name = input(prompt)
"""

#i) value is not stored in any variable
input("Prompt String:") #With Prompt String (optional)
input() #Without Prompt String

#ii) value is stored in some variable
a=input("Getting input from user: ") #Prints Prompt String and gets input from user and stores it in variable a
b=input() #Does Not Print Any Prompt String But Gets Input From User and and stores it in variable b
c=input(None) #Prints None In Screen and Gets Input From User and and stores it in variable c
d=input("Enter any string: ")
e=[input("Enter 1st Number:"),input("Enter 2nd Number:")]
print(a,b,c,d) #Printing the values stored in a, b, c, d using print()function

#iii) To get user input only from command line (terminal) (Ex: command prompt, windows powershell)
import sys

a=int(sys.argv[1])
b=int(sys.argv[2])
print(a+b)

#iv) To Get Multiple Inputs

#a) Method 1: Using split() Function Alone
"""split()
Syntax:
input().split(sep="whitespace", maxsplit=-1)
where,
sep parameter has default value = whitespace (" ","\n")
maxsplit parameter has default value = -1 which means all occurrences of separator will be splitted
"""
#Example 1: Getting space spearated 2 inputs
a,b = input("Enter Space Separated 2 Numbers").split()
print(a,b)

#Example 2: Getting comma spearated 2 inputs
a,b = input("Enter Comma Separated 2 Numbers").split(',')
print(a,b)

#b) Method 2: Using map() And split() Functions Together
"""map()
Gets multiple inputs at a time and splitted using input()and split() functions, maps datatype to all multiple inputs and gives an iterable output
This output is type casted using list() function
Syntax:
list(map(function_name, input().split()))
"""
#Example 1: Getting 2 inputs at a time (comma separated)
a,b = list(map(int, input("Enter Comma Separated 2 Numbers: ").split(",")))
print(a,b)

#Example 2: Getting mutiple inputs at a time (space separated)
mutiple_input = input().split()
print(mutiple_input)
a = list(map(int, mutiple_input))
print(a)
b = list(map(float, mutiple_input))
print(b)
c = list(map(bool, mutiple_input))
print(c)

#Example 3: Getting mutiple inputs at a time, then fetching and displaying them 
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
for i in x:
    print(i,end=' ')

#c) Method 3: Using List comprehension, input() and split() functions altogether

#Example 1: Getting 2 inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)

#Example 2: Getting 3 inputs at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)
