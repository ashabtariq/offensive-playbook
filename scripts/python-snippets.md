## Strings
Shebang for python: #!/bin/python3
Use triple quotes “”" for multiline string
+ Sign is used to concat

~~~Python
#PRINT STRING

print ("Helllo World")
print ('Hello World')

print (""" THIS STRING RUNS MULTIPLE 
LINES""")

print ("This String is " + "Awesome")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Maths

Use ** to make exponente e.g.  5 ** 5 = S raised to power of 5 

~~~python
#!/bin/python3

print (50 + 50)
print (50 * 50)
print (50 - 50)
print (50 / 50)
print(50 ** 2) # 50 RAISED TO POWER OF 2
print (50 % 6) #MOD
pint (50 / 6)
print (50 //6) # NO LEFTOVER (ROUIND OFF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Variables & Methods

Cannot concat int + Sting, so we have to convert it to str or int, making same data types

~~~python
#!/bin/python3

#Variable and Methods
quote = "All is fair in love and war."
print (quote.upper()) # ALl text in Upper case
print (quote.lower()) # ALl text in Lower case
print (quote.title()) # ALl text in Title case

print(len(quote)) #length of variable

name = "Ashab" #STRING
age = 28 #Integer
gpa = 2.86 # Float

print(int(age))     #Print integer part of age variable
print (int(30.1))   #Print Integer part of given number
print("My name is " + name + " and i am " + str(age) + " Years old")

age += 1
print(age)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Functions and Methods

~~~python
FUNCTIONS
print("Here is an example function: ")

#FUNCTION DEFINITION
def who_am_I():
    name = "Ashab"
    age = 30
    gpa = 2.86
    print("My name is " + name + " and i am " + str(age) + " Years old")

#FUNCTION CALL
who_am_I()

#ADDING PARAMETERS
def add_one_hundered(num):
    print(num + 100)

add_one_hundered(100)

#MLTIPLE PARAMETERS
def add(x,y):
    print (x + y)

add(7,7)

def multiply(x,y):
    return x*y
res = multiply(7,7)
print(multiply(7,8))
print (res)

def sqrt(x):
    print(x ** .5)

sqrt(64)

def newLine():
    print('\n')

newLine()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Relational & Boolean Operators

~~~python
#BOOLEAN EXPRESSIONS
print ("Boolean Expressions: ")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))


#RELATIONAL AND BOOLEAN OPERATORS
print("BOOLEAN AND RELATIONAL OPERATORS")
print('\n')

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equalto = 7 >= 7
less_than_equal = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) # True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Conditional Statements

~~~python
#CONDITIONAL STATEMENTS
print("Conditional Statements")
print("\n")

def drink(money):
    if money >=2:
        return "You've got yourself a drink"
    else:
        return "NO DRINK FOR YOU"

print(drink(3))
print(drink(1))

#FUNCTION DEFINATION
def alcohol(money,age):
    if (money >= 5) and (age >= 21):
        return "You can buy Alcohol"
    elif (age >= 21) and (money < 5):
        return "Come back with money"
    elif (age <= 21) and (money >= 5):
        return "Nice try Kid"
    else:
        return "Your are too poor and young"

#FUNCTION CALLS
print(alcohol(5,21))
print(alcohol(4,21))
print(alcohol(4,20))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lists - Have Brackets []
Lists are mutable - They can be changed

~~~python
#LISTS - Have Brackets []

movies = ['Harry met sallt','Hangover','Perks of Waliflower','Exorcist']
print (movies[0])
print(movies[1:3]) # Print from 1st element to 3rd
print(movies[1:])
print(movies[:1]) #print everything before 1
print (movies[-1]) #Prints last item of list
print(len(movies)) #Number of Items in LISTS
movies.append("JAWS") # Appended to end always
print(movies)
movies.pop() #Deletes last element
print(movies)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tuples - Have Paratenses ()
Immuatable - They cannot be changed

~~~python
#TUPLES DO NOT CHANGE ()

grades = ("a","b","c","d")
print (grades[1]) #PRINT SECOND ELEMENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Looping

~~~python
#LOOPING

#FOR LOOPS - Start to finsih of an iterate
vegetables = ["Cucumber","Tomato","Potato"]

for x in vegetables:
    print (x)

#WHILE LOOPS - Execute as long as True
i = 1

while i < 10:
    print (i)
    i += 1

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Importing Modules

~~~python
#!/bin/python3

import sys #Sys is a ystem function and parameters
import os
from datetime import datetime as dt #Importing with alias

print(dt.now())

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Advanced Strings

~~~python
#ADVANCE STRINGS
my_name = "Ashab"
print(my_name[0]) # FIRST LETTER
print(my_name[-1]) #LAST LETTER

sentence = "This is a Sentence. "
print(sentence[0:4]) #Number of bytes of "THIS"

print(sentence.split()) #Spliting a sentence/string with space as delimiter

sentence_split = sentence.split()
sentence_join = '-'.join(sentence_split) #Joining sentences with space(any can be in brackets) as delimiter
print(sentence_join)

quote = "He said \"give me all your money\"" # To add quotes we can use backslash as shown in code
print(quote)

too_much_space = "              Hello         World"
print(too_much_space.strip()) ##REMOVING EXTRA SPACES

print("A" in "Apple") #DOES A EXIST IN APPLE, this is case sensitive and will return true if correct

letter = "A"
word = "Apple"

print(letter.lower() in word.lower())#improved

movie =  "Hangover"

print("My Favourite movie is {}.".format(movie)) #Python will substitute var value instead of curly brackets


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Dictionaries

~~~python
#DICTONARIES - Key value pairs {}
drink = {"White Russian": 7, "Lemon Drop": 8} #Drink Name is Key and price is value
print (drink)

employees = {"Finance": ["Bob","Linda","Tina"], "IT": ["Gene","Louis","Teddy"], "HR":["Jimmy","Mart"]} #multi value DICTONARIES
print(employees)

employees['Legal'] = ["Mt Frond"] # Adding new key/value pair to employees dict
print(employees)

employees.update({"Sales":["Andy","Olive"]}) # ADD NEW KEY VALLE PAIR
print(employees)

drink['White Russian'] = 8
print(drink.get("White Russian"))

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Sockets

use “nc -nvlp” to setup a listening port (same as in script)

~~~python
#!/bin/python3
import socket

HOST = '127.0.0.1'
PORT = 7777
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#AF_INET = IPV4 IP ADDRESS
#SOCK_STREAM = PORT

s.connect((HOST,PORT)) #CONNECT TO HOST/PORT PAIR
~~~
