The StringIO module implements an in-memory file like object. This object can then be used as input or output to most functions that would expect a standard file object.

The best way to show this is by example:

In [1]:
import StringIO

In [16]:
# Arbitrary String
message = 'This is just a normal string.'

In [25]:
# Use StringIO method to set as file object
f = StringIO.StringIO(message)