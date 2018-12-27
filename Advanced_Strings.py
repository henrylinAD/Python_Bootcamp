String objects have a variety of methods we can use to save time and add functionality. Lets explore some of them in this lecture:

In [75]:
s = 'hello world'


Changing case
We can use methods to capitalize the first word of a string, change cases to upper and lower case strings.

In [76]:
# Capitalize first word in string
s.capitalize()
Out[76]:
'Hello world'
In [77]:
s.upper()
Out[77]:
'HELLO WORLD'
In [78]:
s.lower()
Out[78]:
'hello world'



Location and Counting
In [80]:
s.count('o')
Out[80]:
2
In [81]:
s.find('o')
Out[81]:
4



Formatting
The center() method allows you to place your string 'centered' between a provided string with a certain length. Personally, I've never actually used this in code as it seems pretty esoteric...

In [83]:
s.center(20,'z')
Out[83]:
'zzzzhello worldzzzzz'
expandtabs() will expand tab notations \t into spaces:

In [84]:
'hello\thi'.expandtabs()
Out[84]:
'hello   hi'



is check methods
These various methods below check it the string is some case. Lets explore them:

In [40]:
s = 'hello'
isalnum() will return True if all characters in S are alphanumeric

In [41]:
s.isalnum()
Out[41]:
True
isalpha() wil return True if all characters in S are alphabetic

In [43]:
s.isalpha()
Out[43]:
True