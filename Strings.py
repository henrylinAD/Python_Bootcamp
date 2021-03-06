Strings
Strings are used in Python to record text information, such as name. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the 
string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab 
particular letters (like the first letter, or the last letter).

This idea of a sequence is an important one in Python and we will touch upon it later on in the future.

In this lecture we'll learn about the following:

1.) Creating Strings
2.) Printing Strings
3.) Differences in Printing in Python 2 vs 3
4.) String Indexing and Slicing
5.) String Properties
6.) String Methods
7.) Print Formatting

Creating a String
To create a string in Python you need to use either single quotes or double quotes. For example:

In [1]:
# Single word
'hello'
Out[1]:
'hello

In [2]:
# Entire phrase 
'This is also a string'
Out[2]:
'This is also a string'
In [3]:
# We can also use double quote
"String built with double quotes"
Out[3]:
'String built with double quotes'

In [4]:
# Be careful with quotes!
' I'm using single quotes, but will create an error'
  File "<ipython-input-4-6565b0b7b5e3>", line 2
    ' I'm using single quotes, but will create an error'
        ^
SyntaxError: invalid syntax
The reason for the error above is because the single quote in I'm stopped the string. You can use combinations of double and single quotes to get the complete statement.

In [10]:
"Now I'm ready to use the single quotes inside a string!"
Out[10]:
"Now I'm ready to use the single quotes inside a string!"
Now let's learn about printing strings!



Printing a String
Using Jupyter notebook with just a string in a cell will automatically output strings, but the correct way to display strings in your output is by using a print function.

In [11]:
# We can simply declare a string
'Hello World'
Out[11]:
'Hello World'
In [12]:
# note that we can't output multiple strings this way
'Hello World 1'
'Hello World 2'
Out[12]:
'Hello World 2'

We can use a print statement to print a string.

In [13]:
print 'Hello World 1'
print 'Hello World 2'
print 'Use \n to print a new line'
print '\n'
print 'See what I mean?'
Hello World 1
Hello World 2
Use 
 to print a new line


See what I mean?

Something to note. In Python 3, print is a function, not a statement. So you would print statements like this: print('Hello World')

If you want to use this functionality in Python2, you can import form the future module.

A word of caution, after importing this you won't be able to choose the print statement method anymore. So pick whichever one you prefer depending on your Python installation and continue on with it.

In [32]:
# To use print function from Python 3 in Python 2
from __future__ import print_function

print('Hello World')
Hello World

String Basics
We can also use a function called len() to check the length of a string!

In [33]:
len('Hello World')
Out[33]:
11

String Indexing
We know strings are a sequence, which means Python can use indexes to call parts of the sequence. Let's learn how this works.

In Python, we use brackets [] after an object to call its index. We should also note that indexing starts at 0 for Python. Let's create a new object called s and the walk through a few examples of indexing.

In [1]:
# Assign s as a string
s = 'Hello World'
In [35]:
#Check
s
Out[35]:
'Hello World'

In [36]:
# Print the object
print(s)
Hello World
Let's start indexing!

In [21]:
# Show first element (in this case a letter)
s[0]
Out[21]:
'H'
In [22]:
s[1]
Out[22]:
'e'
In [23]:
s[2]
Out[23]:
'l'
We can use a : to perform slicing which grabs everything up to a designated point. For example:

In [24]:
# Grab everything past the first term all the way to the length of s which is len(s)
s[1:]
Out[24]:
'ello World'

In [25]:
# Note that there is no change to the original s
s
Out[25]:
'Hello World'
In [26]:
# Grab everything UP TO the 3rd index
s[:3]
Out[26]:
'Hel'
