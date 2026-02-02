# ################################################################################################# #
#                                                                                                   #
#  1. Getting Started                                                                               #
#                                                                                                   #
# ################################################################################################# #

# Welcome to the ShwaTech Python Primer!
# We will start with the basic syntax of the language and work our way up
# You will notice these lines that start with a hashtag
# These are comments in Python, they will be ignored by the interpreter
# Comments allow you to explain what your code is doing

# ###################################################### #
#   Syntax & Scope                                       #
# ###################################################### #

hello_world = 'Hello, world!'   # Python is a script language
print(hello_world)              # Each line is an instruction to the interpreter

# Python allows you to combine instructions onto a single line using the ; operator

hello_world = 'Hello again, world!'; print(hello_world)

# Python allows you to carry instructions onto subsequent lines with the \ operator

hello_world = \
'Hello again there, world!'
print(hello_world)

# Scope in Python is defined by indentation

the_number_seven = 7        # This is at the top scope
if the_number_seven != 7:   # Conditional scopes like ifs...
  print('Oops!')            # Get indented with tab or spaces

# Variables declared at lower scopes persist at higher scopes

the_number_eight = 8                          # Variables declared at lower scopes
if the_number_eight == 8:                     #
  the_number_nine = 9                         #
print('The number nine is:',the_number_nine)  # Persist at higher scopes

# Function variables do not persist outside of the function scope

def do_math(*a):
  math_result = sum(a)    # math_result goes out of scope after the function call
  return math_result      # You cannot use unless you return it to the caller

# ###################################################### #
#   Namespaces & External References                     #
# ###################################################### #

# Python defines everything you do in your base script as the local namespace

i_like_bacon = True
print(i_like_bacon)

# In Python when you import a module it gets assigned a namespace name

import math         # Here we import the math module
math.sqrt(654.23)   # Then we use the math namespace to call the sqrt function

# You can also alias the import of a module to avoid collisions

import statistics as stat_man
stat_man.mean([1,2,3,4,4,4,5,6,7,7,7,7,8,8])

# Importing with the from keyword imports functions into the local namespace
# Importing using from can be limited or unlimited

from os import *         # This imports everything from the os module
from json import dumps   # This only imports the dumps function from the json module
dumps([1,2,3,4,5])       # When you import a single function from a module it
                         # gets loaded into the local namespace

from json import dumps as convert_to_json   # As such, individual functions imported into the local
convert_to_json([1,2,3,4,5])                # namespace can be aliased to avoid conflicts

# Python scripts in the same, current directory can be imported using their filename

from python_primer_refs import three_blind_mice   # This is python_primer_ref.py in the current directory
three_blind_mice()                                # We can import this function into the local namespace

# ###################################################### #
#   Variables, Primitives & Literals                     #
# ###################################################### #

# Python variables are simple tokens assigned with the assignment (=) operator

my_name = 'Christian Holslin' # String
my_company = "ShwaTech LLC"   # Also String
my_age = 43                   # Integer
my_favorite_number = 7.0      # Float
am_i_awesome = True           # Boolean
this_is_null = None           # Null (Unassigned)
                              # String (multiline), below
my_life_story = """
A long, long time ago...
In an In'N'Out Burger far far away...
"""

# Python supports escape sequences in Strings

'\n'  # Newline
'\t'  # Tab
'\"'  # Double Quotation Mark

# Python supports collection literals

my_parents = ['Mom','Dad']            # List
my_hobbies = ('Golf','Motorcycles')   # Tuple
my_friends = {'Alice':29,'Bob':41}    # Dictionary
my_skills = {'Python','C','C++','C#'} # Set

# Variables can be assigned and reassigned to any value at run-time

some_thing = 12
some_thing = 'Twelve'
some_thing = 7.5
some_thing = [1,1,2,2,3,4,5]
some_thing = range(9)

# ###################################################### #
#   Arithmetic                                           #
# ###################################################### #

# Common arithmetic operators include

x = 1 + 1   # Addition
x = 1 - 1   # Subtraction
x = 1 * 1   # Multiplication
x = 1 / 1   # Division
x = 1 % 1   # Modulo
x = 1 ** 1  # Exponentiation
x = 1 // 1  # Division with Floor

# The Python interpreter obeys PEMDAS

x = 2 * (2 + 2) + 2 + 2 - 2 * 2 / 2 ** 2  # This operation
x = 2 * 4 + 2 + 2 - 2 * 2 / 2 ** 2        # Simplfies to this
x = 8 + 2 + 2 - 2 * 2 / 2 ** 2            # Which simplifies to this
x = 12 - 2 * 2 / 2 ** 2                   # Which simplifies to this
x = 12 - 2 * 2 / 4                        # Which simplifies to...
x = 12 - 4 / 4                            # Which simplifies to...
x = 12 - 1                                # Which becomes...
x = 11                                    # x = 11

# Division will cause the expression to become a float

# ###################################################### #
#   RANDOM NUMBERS                                       #
# ###################################################### #

# Python includes a random module with generators for random umbers

import random
random.choice([1,2,3,4,5,6])    # Choice picks a random item from the list
random.randint(0,99)            # Create a random number between a and b

# This List comprehension fills a List with random integers
random_numbers = [random.randint(0,99999) for n in range(1000)]

# ###################################################### #
#   Boolean Logic                                        #
# ###################################################### #

# Python supports standard arithmetic boolean comparion operators

5 == 1   # Equality
5 > 1    # Greater than
5 < 1    # Less than
5 <= 5   # Less than or equal
5 >= 5   # Greater than or equal
5 != 5   # Not equal

# Python supports standard boolean logic operators and, or and not

(2 < 3) and (5 < 4)   # x is False
(2 < 3) or (5 < 4)    # x is True
not (2 < 3)           # x is False

# Comparison operators work on primitives and collections

5 == 5                   # Compare two Ints
'Christian' == 'Peter'   # Compare two Strings
['a','b'] == ['a','b']   # Compare two Lists
('a','b') == ('a','b')   # Compare two Tuples

# String comparisons are case-sensitive

'Christian' == 'cHrisTian'   # This is False
'Christian' == 'Christian'   # This is True

# Boolean expressions are evaluted conditionally

empty_list = []
if len(empty_list) > 0 and empty_list[0] % 2 == 0:   # There are two Boolean expressions here
  print('empty_list should be empty')                # empty_list[0] is illegal, but because
                                                     # the first is False and the condition is
                                                     # 'and' then the right-hand expression is
                                                     # not evaluated, avoiding an IndexError

# ################################################################################################# #
#                                                                                                   #
#  2. Basic Operations                                                                              #
#                                                                                                   #
# ################################################################################################# #

# ###################################################### #
#   String Manipulation                                  #
# ###################################################### #

# Python allows you to combine strings together with concatenation

x = 'Christian' + ' Holslin'        # Concatenante two Strings
x += ' is awesome'                  # Append a String to a String
x = 'Christian'.join(['Holslin'])   # Append a List of Strings

# Python has a syntax called f strings which are formatted string

cash_on_hand = 32.75                              # Using a variable...
print(f'You have {cash_on_hand} cash on hand.')   # embed that variable's value into a string

# Python strings are Lists of characters, they are iterable and can be indexed

my_name = 'Christian'                   # Here is my first name
my_name_len = len(my_name)              # Get the length of my_name
my_first_initial = my_name[0]           # Index the first letter for my first initial
my_nick_name = my_name[0:5]             # Slice the first 5 letters for my nickname
jibberish = my_name[-5:-1]              # Negative indeces also work on strings
for letter in my_name: print(letter)    # Iterate the characters in my name
my_list = []                            # Make an empty List
my_list += my_name                      # Each letter in my name is added as an item in this List
fav_quote = "\"Elementary, my dear.\""  # Escape special characters with '\'
list(map(lambda x: x.upper(), 'test'))  # Strings can be mapped because they are iterable
'Chris' in my_name                      # The in operator will test for a substring

# Python strings are immutable, so changes are illegal
# my_name[0] = 'F'   # This throws a TypeError

# Python has methods for strings which perform actions on the string itself

'Hello, world!'.find('world')      # Locate the index of a substring in a string
'{}, {}!'.format('Hello','world')  # Creates a 'formatted' string => 'Hello, world!'
':'.join(['hello','world'])        # Joins a List with a delimiter into a String => 'hello:world'
'Hello World'.lower()              # Converts all letters to lowercase
'Hello, world!'.replace('l','f')   # Replaces part of a string with another string
'sauce cheese pesto'.split()       # Splits a string into a List using spaces as the delimeter
'sauce:cheese:pesto'.split(':')    # Splits a string into a List using a specified delimeter
' Hello, world! '.strip()          # Removes whitespace at the beginning and end of a string
'*Hello, world!*'.strip('*')       # Removes leading and trailing '*'s from the string
'enterprise architect'.title()     # Creates a Title Case string => 'Enterprise Architect'
'Hello World'.upper()              # Converts all letters to UPPERCASE

# Python string formatting supports keyword parameters

def email_signature(n,t,pn):
  return '{name}, {title} ({phone_number})'.format(name=n,title=t,phone_number=pn)

# ###################################################### #
#   List Operations                                      #
# ###################################################### #

# Python Lists are dynamic collections of any item

backpack = ['laptop','charger',23.50,['gum','mints']]   # Make a list of stuff in my backpack
backpack = backpack + ['pen']                           # Add a pen to my backpack
backpack += ['paper','phone']                           # Add two more things
backpack += ('earbuds','cashews')                       # Add two more things from a Tuple
backpack += {"breakfast":"eggs","lunch":"noodles"}      # Add the lunch menu, NOTE: Only the keys are added (not the values)
backpack += {'glasses','sweater','watch'}               # Add three more things from a Set
# backpack += 5                                         # Illegal: append operator only works with collections

# Python Lists use the index operator to fetch items or Lists of items

backpack[0]        # Get the first item in the List
backpack[3][0]     # Get the first item of the fourth item in the List
backpack[0:3]      # Get a new List with the first three items at indexes 0, 1, and 2
backpack[:3]       # Note the leading 0 is optional
backpack[:]        # Gets every item in the List
backpack[4:]       # Get the fifth item and all items after it in the List
backpack[-1]       # Get the last item in the List
backpack[-2]       # Get the second to last item in the List
backpack[-4:-2]    # Get the fourth-to-last and third-to-last items in the List
backpack[-3:]      # Get the third-to-last item and all subsequent items in the List

# Python Lists use methods to add, remove and find items

backpack.append(5)                                # Add 5 bucks into the backpack
how_many_pens = backpack.count('pen')             # Count how many pens are in the backpack
where_is_my_paper = backpack.index('paper')       # Find the paper in the backpack
find_my_watch = backpack.index('watch',4)         # Find the watch but skip the first 4 items
find_my_earbuds = backpack.index('earbuds',5,8)   # Look for the earbuds but skip the first 5 items and only check the next 3 items
backpack.insert(4,'pen')                          # Add another pen next to the current pen
backpack.insert(-2,'glasses')                     # Add glasses next to the other glasses
five_bucks = backpack.pop()                       # Take the 5 bucks back out of the backpack
laptop = backpack.pop(0)                          # Take the laptop out of the backpack
backpack.remove('sweater')                        # Take the sweater out of the backpack and toss it

# Python Lists can be sorted forwards or backwards

primes = [11,7,13,2,5,3]         # Create an unsorted List of prime numbers
primes.sort()                    # Sort the List in ascending order
primes.sort(reverse = True)      # Sort the List in descending order
sorted(primes)                   # Use the built-in function sorted to sort the List instead
sorted(primes, reverse = True)   # Use the built-in function sorted to sort the List in reverse order

# Python has built-in functions for List arithmetic

digits = [2,5,8,3,7,2,4,5,5,6,7]   # Make a List of some numbers
sum(digits)                        # Calculate the sum of the List of numbers
max(digits)                        # Find the largest (max) number in the List
min(digits)                        # Find the smallest (min) number is the List

# Python allows you to combine Lists and Tuples together with concatenantion

x = ['a','b','c'] + ['d','e','f']   # Concatenante two Lists
x = ('a','b','c') + ('d','e','f')   # Concatenante two Tuples

# ###################################################### #
#   List Comprehensions & Generators                     #
# ###################################################### #

# Python has a unique way to create a List of items from another List called comprehensions

positive_integers = list(range(100))                               # Make a List of positive integers from a range
odd_numbers = [num for num in positive_integers if num % 2 == 1]   # Use a List comprehension to extract the odd numbers

# You can also manipulate the value that is extracted with a comprehension

double_evens = [num * 2 for num in positive_integers if num % 2 == 0]   # Find all the even numbers and multiple them by 2
print('Double Evens list:',double_evens)

# Generators are useful for creating an iterator over a List especially in cases where the List is very large

double_evens_generator = (num * 2 for num in positive_integers if num % 2 == 0)
print('Double Evens generator:',double_evens_generator)

# ################################################################################################# #
#                                                                                                   #
#  3. Control Flow                                                                                  #
#                                                                                                   #
# ################################################################################################# #

# ###################################################### #
#   If Statements                                        #
# ###################################################### #

# Python conditional control flow uses the if, elif, and else keywords

my_name = 'Bob'
if my_name == 'Christian':
  print('My name is Christian')

if my_name == 'Christian':
  print('My name is Christian')
else:
  print('My name is not Christian')

if my_name == 'Christian':
  print('My name is Christian')
elif my_name == 'Bob':
  print('My name is Bob')
else:
  print('Who am I?')

# ###################################################### #
#   Loops                                                #
# ###################################################### #

# Python loop control include for loops and while loops

for item in backpack:
  print('Backpack item:',item)

x = 0
while x < len(backpack):
  print(f'Backpack item {x}:',backpack[x])
  x += 1

# ###################################################### #
#   Branching/Switching                                  #
# ###################################################### #

# Python uses the match statement to create a switch case branch

letter = 'q'
match letter:
  case 'a':
    print('a is for aardvark')
  case 'b':
    print('b is for boysenberry')
  case default:
    print(letter)

# ################################################################################################# #
#                                                                                                   #
#  4. Functions                                                                                     #
#                                                                                                   #
# ################################################################################################# #

# ###################################################### #
#   User-Defined Functions                               #
# ###################################################### #

# Python allows you to define your own functions which are blocks of reusable code

def my_function():
  print('Hello, world!')

# Python user-defined functions can return zero, one or more values

def returns_nothing(): print('Hello, world!')
def returns_something(): return 'Hello, world!'
def returns_three_values(): return 'Hello', 'world', '!'

# Return values are assigned to one or more variables using the assignment (=) operator

returns_nothing()
hello_world = returns_something()
hello, world, exclaim = returns_three_values()

# Function arguments and their parameters can be passed in positional or keyword format

def calc_product(a, b, c): return a * b * c
calc_product(1,2,3)
calc_product(b = 2, c = 3, a = 1)

# Function definitions can have default argument values

def say_my_name(name = 'Christian'): print(name)
say_my_name()
say_my_name('Alice')
say_my_name(name = 'Bob')

# Functions also support arbitrary positional arguments

def add_numbers(*nums):
  result = 0
  for i in nums:
    result += i
  return result
add_numbers(3,7,4,2,8,3,4,5,6)

# Functions also support abritrary keyword arguments

def print_brochure(**tags):
  for key, value in tags.items():
    print(f"{key} = {value}")
print_brochure( breakfast = 'eggs', lunch = 'salad', dinner = 'pasta')

# ###################################################### #
#   Anonymous Functions (Lambda)                         #
# ###################################################### #

# Python supports anonymous functions called lambda functions

positive_integers = list(range(100))
odd_numbers = [num for num in positive_integers if num % 2 == 1]
odd_numbers = list(filter(lambda x: x % 2 == 1, positive_integers))

# Lambda functions can have multiple arguments that can map into the caller parameters
# In the example below we are passing two iterables to the map function thus our
# Lambda function will be defined with two arguments, in order, one for the first
# And one for the second iterable

products = list(map(lambda x, y: x * y, odd_numbers, odd_numbers))

# Here is another examples with two different lists

menu_items = ['Eggs','Sausage','Toast','Coffee']
menu_prices = ['2.99','3.99','1.99','2.00']

menu = list(map(lambda x, y: f'{x}: ${y}', menu_items, menu_prices))
print(menu)