Nested Statements and Scope
Now that we have gone over on writing our own functions, its important to understand how Python deals with the variable names you assign. When you create a variable name in Python the name is stored in a name-space. Variable names also have a scope, the scope determines the visibility of that variable name to other parts of your code.

Lets start with a quick thought experiment, imagine the following code:

In [6]:
x = 25

def printer():
    x = 50
    return x

print x
print printer()
What do you imagine the output of printer() is? 25 or 50? What is the output of print x? 25 or 50?

In [3]:
print x
25
In [8]:
print printer()
50
Interesting! But how does Python know which x you're referring to in your code? This is where the idea of scope comes in. Python has a set of rules it follows to decide what variables (such as x in this case) you are referencing in your code. Lets break down the rules:

This idea of scope in your code is very important to understand in order to properly assign and call variable names.

In simple terms, the idea of scope can be described by 3 general rules:

Name assignments will create or change local names by default.
Name references search (at most) four scopes, these are:
local
enclosing functions
global
built-in
Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.
The statement in #2 above can be defined by the LEGB rule.

LEGB Rule.

L: Local — Names assigned in any way within a function (def or lambda)), and not declared global in that function.

E: Enclosing function locals — Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...

Quick examples of LEGB
Local
In [15]:
# x is local here:
f = lambda x:x**2

Enclosing function locals
This occurs when we have a function inside a function (nested functions)

In [19]:
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print 'Hello '+name
    
    hello()

greet()
Hello Sammy
Note how Sammy was used, because the hello() function was enclosed inside of the greet function!



Global
Luckily in Jupyter a quick way to test for global variables is to see if another cell recognizes the variable!

In [20]:
print name
This is a global name
Built-in
These are the built-in function names in Python (don't overwrite these!)

In [22]:
len
Out[22]:
<function len>