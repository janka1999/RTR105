Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __
NameError: name '__' is not defined
>>> __bu

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    __bu
NameError: name '__bu' is not defined
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> a = 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a = 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 20, '__package__': None}
>>> b = 56
>>> vars()
{'a': 20, 'b': 56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> b = 1.56
>>> vars()
{'a': 20, 'b': 1.56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> c = "W"
>>> vars()
{'a': 20, 'c': 'W', 'b': 1.56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> a * a
400
>>> b * b
2.4336
>>> c * c

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    c * c
TypeError: can't multiply sequence by non-int of type 'str'
>>> type(a)
<type 'int'>
>>> type(b)
<type 'float'>
>>> type(c)
<type 'str'>
>>> 
