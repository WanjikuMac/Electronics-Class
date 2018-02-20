Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x =range(0,50)
>>> for y in range(2,n)
SyntaxError: invalid syntax
>>> for y in range(2,n)
SyntaxError: invalid syntax
>>> x=range(0,50)
>>> for y in range x:
	
SyntaxError: invalid syntax
>>> for y in x:
	for z in y:
		if y%z==0:
			print ("%s is not a prime number"(y))
			break
		else:
			print ("%s is a prime number"(y))

			
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    for z in y:
TypeError: 'int' object is not iterable
>>> for n in range(0,50)
SyntaxError: invalid syntax
>>> for n in range(0,50):
	for x in range (0,n):
		if n%x ==0:
			print("%s is not a prime number"(n))
		else:
			print("%s is a prime number"(n))

			
Traceback (most recent call last):
  File "<pyshell#27>", line 3, in <module>
    if n%x ==0:
ZeroDivisionError: integer division or modulo by zero
>>> for n in range(2,50):
	for x in range (2,n):
		if n%x ==0:
			print("%s is not a prime number"(n))
		else:
			print("%s is a prime number"(n))

			
Traceback (most recent call last):
  File "<pyshell#29>", line 6, in <module>
    print("%s is a prime number"(n))
TypeError: 'str' object is not callable
>>> for n in range(2,50):
	for x in range (2,n):
		if n%x ==0:
			print("%s is not a prime number"(n))
			break
		else:
			print("%s is a prime number"(n))

			
Traceback (most recent call last):
  File "<pyshell#31>", line 7, in <module>
    print("%s is a prime number"(n))
TypeError: 'str' object is not callable
>>> for n in range(2,50):
	for x in range (2,n):
		if n%x ==0:
			print("%s is not a prime number"(%n))
			break
		else:
			print("%s is a prime number"(%n))
			
SyntaxError: invalid syntax
>>> 
>>> for n in range(2,50):
	for x in range (2,n):
		if n%x ==0:
			print("{} is not a prime number".format(n))
			break
		else:
			print("{} is a prime number".format(n))

			
3 is a prime number
4 is not a prime number
5 is a prime number
5 is a prime number
5 is a prime number
6 is not a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 is not a prime number
9 is a prime number
9 is not a prime number
10 is not a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
12 is not a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
14 is not a prime number
15 is a prime number
15 is not a prime number
16 is not a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
18 is not a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
20 is not a prime number
21 is a prime number
21 is not a prime number
22 is not a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
24 is not a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is not a prime number
26 is not a prime number
27 is a prime number
27 is not a prime number
28 is not a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
30 is not a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
32 is not a prime number
33 is a prime number
33 is not a prime number
34 is not a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is not a prime number
36 is not a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
38 is not a prime number
39 is a prime number
39 is not a prime number
40 is not a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
42 is not a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
44 is not a prime number
45 is a prime number
45 is not a prime number
46 is not a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
48 is not a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is not a prime number
>>> for n in range(2,50):
	for x in range (2,n):
		if n%x ==0:
			print("{} is not a prime number".format(n))
			
		else:
			print("{} is a prime number".format(n))

			
3 is a prime number
4 is not a prime number
4 is a prime number
5 is a prime number
5 is a prime number
5 is a prime number
6 is not a prime number
6 is not a prime number
6 is a prime number
6 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 is not a prime number
8 is a prime number
8 is not a prime number
8 is a prime number
8 is a prime number
8 is a prime number
9 is a prime number
9 is not a prime number
9 is a prime number
9 is a prime number
9 is a prime number
9 is a prime number
9 is a prime number
10 is not a prime number
10 is a prime number
10 is a prime number
10 is not a prime number
10 is a prime number
10 is a prime number
10 is a prime number
10 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
11 is a prime number
12 is not a prime number
12 is not a prime number
12 is not a prime number
12 is a prime number
12 is not a prime number
12 is a prime number
12 is a prime number
12 is a prime number
12 is a prime number
12 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
13 is a prime number
14 is not a prime number
14 is a prime number
14 is a prime number
14 is a prime number
14 is a prime number
14 is not a prime number
14 is a prime number
14 is a prime number
14 is a prime number
14 is a prime number
14 is a prime number
14 is a prime number
15 is a prime number
15 is not a prime number
15 is a prime number
15 is not a prime number
15 is a prime number
15 is a prime number
15 is a prime number
15 is a prime number
15 is a prime number
15 is a prime number
15 is a prime number
15 is a prime number
15 is a prime number
16 is not a prime number
16 is a prime number
16 is not a prime number
16 is a prime number
16 is a prime number
16 is a prime number
16 is not a prime number
16 is a prime number
16 is a prime number
16 is a prime number
16 is a prime number
16 is a prime number
16 is a prime number
16 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
17 is a prime number
18 is not a prime number
18 is not a prime number
18 is a prime number
18 is a prime number
18 is not a prime number
18 is a prime number
18 is a prime number
18 is not a prime number
18 is a prime number
18 is a prime number
18 is a prime number
18 is a prime number
18 is a prime number
18 is a prime number
18 is a prime number
18 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
19 is a prime number
20 is not a prime number
20 is a prime number
20 is not a prime number
20 is not a prime number
20 is a prime number
20 is a prime number
20 is a prime number
20 is a prime number
20 is not a prime number
20 is a prime number
20 is a prime number
20 is a prime number
20 is a prime number
20 is a prime number
20 is a prime number
20 is a prime number
20 is a prime number
20 is a prime number
21 is a prime number
21 is not a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is not a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
21 is a prime number
22 is not a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is not a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
22 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
23 is a prime number
24 is not a prime number
24 is not a prime number
24 is not a prime number
24 is a prime number
24 is not a prime number
24 is a prime number
24 is not a prime number
24 is a prime number
24 is a prime number
24 is a prime number
24 is not a prime number
24 is a prime number
24 is a prime number
24 is a prime number
24 is a prime number
24 is a prime number
24 is a prime number
24 is a prime number
24 is a prime number
24 is a prime number
24 is a prime number
24 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is not a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
25 is a prime number
26 is not a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is not a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
26 is a prime number
27 is a prime number
27 is not a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is not a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
27 is a prime number
28 is not a prime number
28 is a prime number
28 is not a prime number
28 is a prime number
28 is a prime number
28 is not a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is not a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
28 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
29 is a prime number
30 is not a prime number
30 is not a prime number
30 is a prime number
30 is not a prime number
30 is not a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is not a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is not a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
30 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
31 is a prime number
32 is not a prime number
32 is a prime number
32 is not a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is not a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is not a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
32 is a prime number
33 is a prime number
33 is not a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is not a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
33 is a prime number
34 is not a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is not a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
34 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is not a prime number
35 is a prime number
35 is not a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
35 is a prime number
36 is not a prime number
36 is not a prime number
36 is not a prime number
36 is a prime number
36 is not a prime number
36 is a prime number
36 is a prime number
36 is not a prime number
36 is a prime number
36 is a prime number
36 is not a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is not a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
36 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
37 is a prime number
38 is not a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is not a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
38 is a prime number
39 is a prime number
39 is not a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is not a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
39 is a prime number
40 is not a prime number
40 is a prime number
40 is not a prime number
40 is not a prime number
40 is a prime number
40 is a prime number
40 is not a prime number
40 is a prime number
40 is not a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is not a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
40 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
41 is a prime number
42 is not a prime number
42 is not a prime number
42 is a prime number
42 is a prime number
42 is not a prime number
42 is not a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is not a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is not a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
42 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
43 is a prime number
44 is not a prime number
44 is a prime number
44 is not a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is not a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is not a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
44 is a prime number
45 is a prime number
45 is not a prime number
45 is a prime number
45 is not a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is not a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is not a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
45 is a prime number
46 is not a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is not a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
46 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
47 is a prime number
48 is not a prime number
48 is not a prime number
48 is not a prime number
48 is a prime number
48 is not a prime number
48 is a prime number
48 is not a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is not a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is not a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is not a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
48 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is not a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
49 is a prime number
>>> 
