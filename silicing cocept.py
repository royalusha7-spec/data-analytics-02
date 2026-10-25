Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a="codegnan"
>>> a[0]+a[1]+a[2}]+a[3]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[0]+a[1]+a[2]+a[3]
'code'
>>> #slicing
>>> a[0:3]
'cod'
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[:4]
'code'
>>> a="work until you succeed"
>>> a[0]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]+a[21]
'wsucceed'
>>> a=[15:10]
SyntaxError: invalid syntax
>>> a=[15:22]
SyntaxError: invalid syntax
>>> a=[15:22]
SyntaxError: invalid syntax
a[15:22]
'succeed'
a[11:14]
'you'
a[5:11]
'until '
a[0:4]
'work'
a="simple is better than complex"
b[10:16]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b[10:16]
NameError: name 'b' is not defined
b[11:17]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b[11:17]
NameError: name 'b' is not defined
a[11:17]
'etter '
a[10:16]
'better'
a[0:4]
'simp'
a[0:6]
'simple'
a[22:29]
'complex'
b[7:9]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b[7:9]
NameError: name 'b' is not defined
a[7:9]
'is'
a="python is easy to learn"
a[-13:-9]
'easy'
a[-23:-17]
'python'
a[-5:-1)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a[-5:-1]
'lear'
a[-5:]
'learn'
a= "god is great"
b[-5:]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b[-5:]
NameError: name 'b' is not defined
a[-5:]
'great'
a[-12:-9]
'god'
a[-8:-6]
'is'
