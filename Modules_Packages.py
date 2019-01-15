Modules and Packages
There's no code here because it didn't really make sense for the section. Check out the video lectures for more info and the resources for this.

Here is the best source the official docs! https://docs.python.org/2/tutorial/modules.html#packages

But I really like the info here: https://python4astronomers.github.io/installation/packages.html

Here's some extra info to help:

Modules in Python are simply Python files with the .py extension, which implement a set of functions. Modules are imported from other modules using the import command.

To import a module, we use the import command. Check out the full list of built-in modules in the Python standard library here.

The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. If another module in your code imports the same module again, it will not be loaded twice but once only - so local variables inside the module act as a "singleton" - they are initialized only once.

If we want to import module math, we simply import the module:

In [5]:
# import the library
import math
In [6]:
# use it (ceiling rounding)
math.ceil(2.4)
Out[6]:
3


Exploring built-in modules
Two very important functions come in handy when exploring modules in Python - the dir and help functions.

We can look for which functions are implemented in each module by using the dir function: