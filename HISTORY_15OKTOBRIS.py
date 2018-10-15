Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x1q3z90cd = 35.0
>>> x1q3z9ocd = 35.0
>>> x = 2
>>> x = x+2
>>> print(x)
4
>>> x=3.9*x*(1-x)
>>> xx=2
>>> xx=xx+2
>>> print(xx)
4
>>> yy=440*12
>>> print(yy)
5280
>>> zz=yy/1000
>>> print(zz)
5
>>> jj=23
>>> kk=jj%5
>>> print(kk)
3
>>> print(4**3)
64
>>> x=1+2**3/4*5
>>> print(x)
11
>>> ddd=1+4
>>> print(ddd)
5
>>> eee='hello '+ 'there'
>>> print(eee)
hello there
>>> eee= 'hello'+ 'there'
>>> eee= eee+1

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    eee= eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type('hello')
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx=1
>>> type(xx)
<type 'int'>
>>> temp=98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> temp = type (xx)
>>> temp=98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99)+100)
199.0
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> 5./4
1.25
>>> print(5./4)
1.25
>>> 5%4
1
>>> print(9.0/2.0)
4.5
>>> sval ='123'
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival =int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv='hello bob'
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam input('Who are you?')
SyntaxError: invalid syntax
>>> nam= input('who are you?')
who are you?

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    nam= input('who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print(Welcome'nam)
      
SyntaxError: EOL while scanning string literal
>>> print('welcome',nam)

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print('welcome',nam)
NameError: name 'nam' is not defined
>>> nam= input('who are you?')
who are you?Me

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    nam= input('who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Me' is not defined
>>> nam= raw_input('who are you?')
who are you?Me
>>> print('welcome',nam)
('welcome', 'Me')
>>> print('welcome %s'%nam)
welcome Me
>>> inp=input('Europe floor?')
Europe floor? 0
>>> usf=int(inp)+1
>>> print('US floor',usf)
('US floor', 1)
>>> inp= raw_input('Europe floor?')
Europe floor? 0
>>> usf=int(inp)+1
>>> print('US floor',usf)
('US floor', 1)
>>> usf=raw_input('US floor %s',usf)

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    usf=raw_input('US floor %s',usf)
TypeError: [raw_]input expected at most 1 arguments, got 2
>>> inp= raw_input('Europe floor?')
Europe floor? 0
>>> usf=int(inp)+1
>>> print('US floor %s,usf)
      
SyntaxError: EOL while scanning string literal
>>> print('US floor %s,'usf)
SyntaxError: invalid syntax
>>> 
