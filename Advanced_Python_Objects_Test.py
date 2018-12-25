Advanced Numbers
Problem 1: Convert 1024 to binary and hexadecimal representation:

In [6]:
print bin(1024)
print hex(1024)
0b10000000000
0x400

Problem 2: Round 5.23222 to two decimal places

In [5]:
round(5.23222,2)
Out[5]:
5.23

Advanced Strings
Problem 3: Check if every letter in the string s is lower case

In [7]:
s = 'hello how are you Mary, are you feeling okay?'

s.islower()
Out[7]:
False


Problem 4: How many times does the letter 'w' show up in the string below?

In [8]:
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
s.count('w')
Out[8]:
12


Advanced Sets
Problem 5: Find the elements in set1 that are not in set2:

In [12]:
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

set1.difference(set2)
Out[12]:
{2}