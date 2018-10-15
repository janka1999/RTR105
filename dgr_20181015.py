Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print("Hello world")
Hello world
>>> x = 12.2
>>> x
12.2
>>> y = 14
>>> y
14
>>> x = 100
>>> x
100
>>> a = 35.0
>>> b = 12.50
>>> c = a * b
>>> print(c)
437.5
>>> x = 2
>>> x = x +2
>>> print(x)
4
>>> xx = 2
>>> xx = xx + 2
>>> print(xx)
4
>>> yy = 440 *12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print(zz)
5
>>> jj = 23
>>> kk = jj % 5
>>> print(kk)
3
>>> print(4 ** 3)
64
>>> x = 1 + 2 * 3 - 4 / 5 ** 6
>>> print(x)
7
>>> x = 1 + 2 ** 3 / 4 * 5
>>> print(x)
11
>>> ddd = 1 + 4
>>> print(ddd)
5
>>> eee = "hello" + "there"
>>> print(eee)
hellothere
>>> eee = "hello" + "there"
>>> eee = eee + 1

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    eee = eee + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type("hello")
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type(xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10 / 2)
5
>>> print(9 / 2)
4
>>> print(10.0 / 2.0)
5.0
>>> print(99.0 / 100.0)
0.99
>>> sval = "123"
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> nsv = "hello bob"
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam = input("Who are you?")
Who are you?

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    nam = input("Who are you?")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print("Welcome", nam)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print("Welcome", nam)
NameError: name 'nam' is not defined
>>> inp = input("Europe floor?")
Europe floor?

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    inp = input("Europe floor?")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> usf = int(inp) + 1

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    usf = int(inp) + 1
NameError: name 'inp' is not defined
>>> print("US flor", usf)

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print("US flor", usf)
NameError: name 'usf' is not defined
>>> 
