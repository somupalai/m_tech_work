Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 4+15
19
>>> 8/2
4
>>> 8/2*7
28
>>> x=12
>>> x**2
144
>>> y

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> y=9+7*x
>>> y
93
>>> ^d
SyntaxError: invalid syntax
>>> 
>>> 
>>> ^D
SyntaxError: invalid syntax
>>> y=9+7
>>> y
16
>>> 4>0
True
>>> apple == bear

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    apple == bear
NameError: name 'apple' is not defined
>>> "apple" == "bear"
False
>>> "apple" < "bear" "candy cane" < "dill"
True
>>> x = y=7
>>> x<= y
True
>>> y <= x
True
>>> x>= y
True
>>> not x>= y
False
>>> 1* -2 * 3 * -4 * 5 * -6
-720
>>> factorial (6)

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    factorial (6)
NameError: name 'factorial' is not defined
>>> factorial(6)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    factorial(6)
NameError: name 'factorial' is not defined
>>> fact(6)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fact(6)
NameError: name 'fact' is not defined
>>> 1
1
>>> 1 * -2 * 3 * -4 * 5 * -6
-720
>>> factorial(6)

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    factorial(6)
NameError: name 'factorial' is not defined
>>> interjection = "ohplease"
>>> interjection[2:6]
'plea'
>>> interjection [4:1]
''
>>> inetrjection[4:1]

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    inetrjection[4:1]
NameError: name 'inetrjection' is not defined
>>> interjection [4:1]
''
>>> interjection [:2]
'oh'
>>> interjection [:]
'ohplease'
>>> interjection *4
'ohpleaseohpleaseohpleaseohplease'
>>> oldmaidsays = "pickme"+ interjection * 3
>>> oldmidsays

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    oldmidsays
NameError: name 'oldmidsays' is not defined
>>> oldmaidsays = "pickme" + interjection * 3
>>> oldmaidsays
'pickmeohpleaseohpleaseohplease'
>>> 'abcdefghijklmnop' [-5:] # negetives indices from trhe end!
'lmnop'
>>> 'abcdefghij' .find('ef')
4
>>> 'abcdefghij' .find('ijk')
-1
>>> 'yodelady-yodelo' .count('y')
3
>>> 'google'.endswitch('ggle')

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    'google'.endswitch('ggle')
AttributeError: 'str' object has no attribute 'endswitch'
>>> 'google' .endswith('ggle')
False
>>> 'litTle ThIrTeEn YeAr OlD gIrl' .captilize()

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    'litTle ThIrTeEn YeAr OlD gIrl' .captilize()
AttributeError: 'str' object has no attribute 'captilize'
>>> 'litTle ThIrTeEn YeAr OlD gIrl' .captitalize()

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    'litTle ThIrTeEn YeAr OlD gIrl' .captitalize()
AttributeError: 'str' object has no attribute 'captitalize'
>>> 'litTle thIrteEn YeAr Old gIrl' .capitalize()
'Little thirteen year old girl'
>>> 'spiderman 3' .istitle()
False
>>> '1234567890' .isdigit()
True
>>> '12345aeiuo' .isdigit()
False
>>> '12345abcde' .isalnum()
True
>>> 'sad' .replace('s', 'gl')
'glad'
>>> 'This is a test.' .split(' ')
['This', 'is', 'a', 'test.']
>>> '-' .join(['ee', 'eye', 'ee', 'eye', 'oh'])
'ee-eye-ee-eye-oh'
>>>streets = ["Castro", "Noe", "Sanchez", "Church",
"Dolores", "Van Ness", "Folsom"]
>>> streets[0]
'Castro'
>>> streets[5]
'Van Ness'
>>> len(streets)
7
>>> streets[len(streets) - 1]
'Folsom'
>>> streets[1:6]
['Noe', 'Sanchez', 'Church', 'Dolores', 'Van Ness']
>>> streets[:2]
['Castro', 'Noe']
>>> streets[5:5]
[]
>>> streets
['Castro', 'Noe', 'Sanchez', 'Church', 'Dolores', 'Van Ness', 'Folsom']
>>> streets[5:5] = ["Guerrero", "Valencia", "Mission"]
>>> streets
['Castro', 'Noe', 'Sanchez', 'Church', 'Dolores', 'Guerrero',
'Valencia', 'Mission', 'Van Ness', 'Folsom']
>>> streets[0:1] = ["Eureka", "Collingswood", "Castro"]
>>> streets
['Eureka', 'Collingswood', 'Castro', 'Noe', 'Sanchez', 'Church',
'Dolores', 'Guerrero', 'Valencia', 'Mission', 'Van Ness', 'Folsom']
>>> streets.append("Harrison")
>>> streets
['Eureka', 'Collingswood', 'Castro', 'Noe', 'Sanchez', 'Church',
'Dolores', 'Guerrero', 'Valencia', 'Mission', 'Van Ness', 'Folsom', 'Harrison']
>>> prop = ["355 Noe Street", 3, 1.5, 2460,
[[1988, 385000],[2004, 1380000]]]
>>> print("The house at %s was built in %d." % (prop[0], prop[4][0][0])
The house at 355 Noe Street was built in 1988.
>>> cto = ("Will Shulman", 154000, "BSCS Stanford, 1997")
>>> cto[0]
'Will Shulman'
>>> cto[2]
'BSCS Stanford, 1997'
>>> cto[1:2]
(154000,)
>>> cto[0:2]
('Will Shulman', 154000)
>>> cto[1:2] = 158000
>>> import divisors
>>> divisors.gatherDivisors(54)
[1, 2, 3, 6, 9, 18, 27]
>>> gatherDivisors(216)
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'gatherDivisors' is not defined
>>> from divisors import gatherDivisors
>>> gatherDivisors(216)
[1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 27, 36, 54, 72, 108]
>>> "neat"
'neat'
>>> from quicksort import quicksort
>>> quicksort([5, 3, 6, 1, 2, 9])
[1, 2, 3, 5, 6, 9]
>>> quicksort(["g", "b", "z", "k", "e", "a", "y", "s"])
['a', 'b', 'e', 'g', 'k', 's', 'y', 'z']
