Python 3.0.1 (r301:69561, Feb 13 2009, 17:50:10) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for x in range (1,5):
	for y range (1,x):
		if x%y ==0:
			print ("%s is not a prime number"(%x)):
		else:
			print ("%s is a prime number"(%X)):
				
SyntaxError: invalid syntax (<pyshell#0>, line 2)
>>> 
>>> def hello():
	print("Hello Akirachix")
	return
hello()
SyntaxError: invalid syntax (<pyshell#5>, line 4)
>>> def hello():
	print("Hello Akirachix")
	return

>>> 
>>> hello()
Hello Akirachix
>>> def hello(name):
	print("Hello {}".format(name))
	return

>>> hello("Carol")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    hello("Carol")
  File "<pyshell#11>", line 2, in hello
    print("Hello {}".format(name))
ValueError: zero length field name in format
>>> def hello(name):
	print("Hello %s" %name))
	return
SyntaxError: invalid syntax (<pyshell#13>, line 2)
>>> 
>>> 
>>> 
>>> def hello(name):
	print("Hello %s" %(name))
	return

>>> hello("Carol")
Hello Carol
>>> def hello(name):
	print("Hello"+name)
	return

>>> hello("Wendy")
HelloWendy
>>> 
>>> hello("Memory")
HelloMemory
>>> def hello(name):
	print("Hello %s" %(name))
	return

>>> hello("Carol,Memory,Ashley")
Hello Carol,Memory,Ashley
>>> def multiply(a,b):
	answer =(a*b)
	print (answer)
	return

>>> multiply(a,b)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    multiply(a,b)
NameError: name 'a' is not defined
>>> def multiply(a,b):
	answer =(a*b)
	print %(answer)
	return

>>> multiply(4,5)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    multiply(4,5)
  File "<pyshell#35>", line 3, in multiply
    print %(answer)
TypeError: unsupported operand type(s) for %: 'builtin_function_or_method' and 'int'
>>> def multiply(a,b):
	answer =(a*b)
	print (answer)
	return

>>> multiply(4,5)
20
>>> def modulus(a,b):
	answer =(a%b)
	print (answer)
	return

>>> modulus(10,3)
1
>>> def subtraction(a,b):
	print ("Subtraction %s from %s" %(a,b))
	answer =(a-b)
	return answer

>>> subtraction(8,5)
Subtraction 8 from 5
3
>>> def summa(a = 10,b=14):
	return a+b

>>> summa()
24
>>> def summa(a = 10,b=14):
	return a+b

>>> summa()
24
>>> subtract
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    subtract
NameError: name 'subtract' is not defined
)
>>> subtract(b=2,c=8):
	
SyntaxError: invalid syntax (<pyshell#53>, line 1)
>>> def hello (name ="AkiraChix"):
	print("Hello" + name)

	
>>> hello()
HelloAkiraChix
>>> def hello (name ="AkiraChix"):
	print("Hello " + name)

	
>>> hello()
Hello AkiraChix
>>> hello("Caroline")
Hello Caroline
>>> hello(name="Caroline")
Hello Caroline
>>> def array(*args):
	for x in args:
		print(x)
		return

	
>>> array([1,2,3,4])
[1, 2, 3, 4]
>>> def array(*args):
	for x in args:
		print(x)
		return

	
>>> array(range(5,30))
range(5, 30)
>>> def array(*args):
	for x in args:
		print(x)
	return

>>> array(range(5,30))
range(5, 30)
>>> def array(*args):
	for x in args:
	print(x)
	return
SyntaxError: expected an indented block (<pyshell#76>, line 3)
>>> def array(*args):
	for x in args:
		print(x)
	return

>>> array(range(5,30))
range(5, 30)
>>> def array(*args):
	for x in args:
		print(args)
	return

>>> array(range(5,30))
(range(5, 30),)
>>> for x in [1,2,3,4]:
	print(x)

	
1
2
3
4
>>> def array(*args):
	x = args
	for y in x:
		print(y)

		
>>> 
>>> array([1,2,3,4])
[1, 2, 3, 4]
>>> def array(*args):
	x = args
	print(x)
	    
	for y in x:
		print(y)\\
		
SyntaxError: unexpected character after line continuation character (<pyshell#93>, line 6)
>>> def array(*args):
	x = args
	print(x)

	for y in x:
		print(y)

		
>>> array([1,2,3,4])
([1, 2, 3, 4],)
[1, 2, 3, 4]
>>> 
>>> 
>>> 
>>> 
>>> def array(**args):
	x = args
	print(x)

	for y in x:
		print(y)

		
>>> array([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    array([1,2,3,4])
TypeError: array() takes exactly 0 positional arguments (1 given)
>>> def array(args):
	x = args
	print(x)

	for y in x:
		print(y)

		
>>> 
>>> 
>>> array([1,2,3,4])
[1, 2, 3, 4]
1
2
3
4
>>> 
>>> def array(args):
	x = args

	for y in x:
		print(y)

		
>>> array([1,2,3,4])
1
2
3
4
>>> array(range(3,100))
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> 