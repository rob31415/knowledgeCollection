#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python has nice language features.
# here you find concise examples for a lot of them.
# make shure to know the "zen of python"


# python is strongly typed.
# sometimes you need to explicitly cast, sometimes it's done implicitly 
# for you (duck typing), especially regarding numeric types.
#
# types available:
#
# Numeric types:
#     int: Integers; equivalent to C longs in Python 2.x, non-limited length in Python 3.x (immutable)
#     long: Long integers of non-limited length; exists only in Python 2.x (immutable)
#     float: Floating-Point numbers, equivalent to C doubles (immutable)
#     complex: Complex Numbers (immutable)
# Sequences:
#     str: String; (immutable); represented as a sequence of 8-bit characters in Python 2.x, but as a sequence of Unicode characters (in the range of U+0000 - U+10FFFF) in Python 3.x
#     bytes: (immutable); a sequence of integers in the range of 0-255; only available in Python 3.x
#     byte array: like bytes, but mutable; only available in Python 3.x
#     list (mutable)
#     tuple (immutable)
# Sets:
#     set: (mutable) an unordered collection of unique objects; available as a standard type since Python 2.6
#     frozen set: like set, but immutable; available as a standard type since Python 2.6
# Mappings:
#     dict: (mutable) Python dictionaries, also called hashmaps or associative arrays


# Every object has an identity (address in ram), a type and a value.
# "is" on objects checks equality of identity.
# == checks equality of value.
# id() returns the identity.
someObject = [13]
someObject2 = [13]
print(someObject is someObject2, id(someObject), id(someObject2))    #false
print(someObject == someObject2)    #true

# in integral data types "is" is equal to "=="
someIntegralDatatypeVariable = 13
someIntegralDatatypeVariable2 = 13
print(someIntegralDatatypeVariable is someIntegralDatatypeVariable2, id(someIntegralDatatypeVariable), id(someIntegralDatatypeVariable2))    #true


# collections

# unordered. for expressing relationships, linking, counting, grouping
aDictionary = {"Beer" : "Bofferding", "Schnapps" : "Bärwurz", 4 : "four"}
print(aDictionary)	#{4: 'four', 'Beer': 'Bofferding', 'Schnapps': 'B\xc3\xa4rwurz'}
print(aDictionary["Schnapps"])	#Bärwurz
# keys of different types are possible, but it's problematic
# e.g. when iterating

# iterate dictionary
for drink,brand in aDictionary.items():
	print(drink, brand)

aDictionaryEmpty = {}
aDictionaryEmpty2 = dict()
aDictionaryEmpty["H2O"] = "Vodka"
del aDictionaryEmpty["H2O"]

# defaultdict: acts like dict.getOrElse(key, defaultValue)
# meaning: give me element with key and if it doesn't exist, create it with given defaultValue and return it
from collections import defaultdict
def someDefaultValue():
	return 0
bladd = defaultdict(someDefaultValue)
bladd["one"] = 1
print(bladd["one"])	#1
print(bladd["two"])	#0 returned by someDefaultValue()
print(bladd["avgn"])	#0 returned by someDefaultValue()


aList = ["blabla", 5, 4.2]
print(aList)	#["blabla", 5, 4.2]
aList.append(10) #works, but list elements should all have the same type.
aListEmpty = []
aListEmpty2 = list()


aTuple = ("blabla", 5, 4.2)
print(aTuple)	#('blabla', 5, 4.2)
#so what's the diff to a list then?
#aTuple.append(10)	#AttributeError: 'tuple' object has no attribute 'append'
#plus, tuple is immutable. they say: "Tuples have structure, lists have order"
aTupleEmpty = ()
aTupleEmpty = tuple()


#unordered
aSet = set((1,1,2)) #set([1, 2])
print(aSet)
aSetEmpty = set()	#there isn't a literal for empty set


# don't mutate while iterating. instead do this - .keys() makes a copy
for k in aDictionary.keys():
	if(type(k) == "int"):
		del aDictionary[k]

# .iteritems() is faster than .items() because uses iterators
for k,v in aDictionary.items():
	print(k,v)


# comprehensions (for lists, maps, sets)
def doSomething(x):
	return x

for e in aList:		#iteration can be...
	doSomething(e)

[doSomething(e) for e in aList] #...equivalent to comprehension (if doSomething returns value of fitting type)

# but comprehensions really are for creating a new collection from a given collection
x = [doSomething(e) for e in aList]


# tip:
# you have: list of tuples 
# you want: list of 1st element of every tuple
# this is done with list comprehension:
# [element[0] for element in listOfTuples]



# btw: pythons for is like foreach in javascript/C#. it loops over collections using the iterator protocol.


#range(100000) #in pyton2, creates a datastructure with 100000 elements
# in python2, xrange uses iterators instead, so only one value getting iterated. lots of ram saved.
#for i in xrange(100000):
#	print i**2
# in python3, xrange is renamed to range, the old style range is gone

#loop backwards
for i in reversed(range(10)):
	print(i)
# 9 8 7 ... 0



# enumerate() adds an index to for loops
anotherList = ["c", "a", "b"]
for i, element in enumerate(anotherList):
	print(i, anotherList[i])


#iterate over two collections at once with zip (which is ages old)
for el1,el2 in zip(aList, anotherList):
	print(el1,el2)
#	blabla a
#	5 b
#	4.2 c


for i in sorted(anotherList, reverse=True):
	print(i)
#c b a


# construct dict from 2 lists 
# (izip  reuses tuple, saves space and speed)
print( dict(zip(["key1", "key2", "key3"], ["val1", "val2", "val3"])) )



# when sorting, instead of compare-functions you can use "key" parameter.
# it specifies a function to be called on each list element prior to making comparisons
# it's like sql's "order by"

persons = [
	("andrea","girl",10),
	("rob","boy",11),
	("clare","girl",7)
]
for i in sorted(persons, key=lambda person: person[2]):
	print(i)
# sorts by age
# ('clare', 'girl', 7)
# ('andrea', 'girl', 10)
# ('robert', 'boy', 11)
#
# e.g. key=len would sort ["abc", "a", "ab"] to: a ab abc.

# iterate unless a sentinel value appears

i=0
def blablabla():
	global i
	i += 1
	return i

blocks = []
for block in iter(blablabla,5):
	blocks.append(block)
print(blocks)


# multipleLoopExitPoints; 2 possible outcomes (idea by knuth)

def containsACertainValue():
	for val in [1,2,3,4,5]:
		if(val==777):
			break
	else:	#ran to the end; didn't break; could've be called "nobreak" or "didn't break"
		return False
	return True

print(containsACertainValue())

# conditional expression (instead of ternary operator)

b = 1
a = "yes" if b == 1 else "no"
print(a) #yes


# val vs ref

aValue = 1
anotherValue = aValue
aValue = 2
print(anotherValue)	 # 1

aRef = [1]
anotherRef = aRef
aRef[0] = 2
print(anotherRef[0])	# 2


# lambda (anonymous fct) and the three seminal functional built ins

lst = range(1, 7)
print(lst)	#[1, 2, 3, 4, 5, 6]

val = 0
for x in lst:
	val += x
print(val)	#21

# lambda can only be a single expression - no sequece, no repetition, no branching statements
# guido says: lambda is syntactic sugar, it's technically redundant and controversial
bla = lambda x,y: x+y

# fct. definition
def bla2(x,y):
	return x+y

# python goes functional

import functools
# all equivalent, all give 21
print(functools.reduce(lambda x,y: x+y, lst))	# reduce does this: (((((1+2)+3)+4)+5)+6) thus aka "left-fold"
print(functools.reduce(bla, lst))
print(functools.reduce(bla2, lst))
# guido says: "the only purpose of reduce is to write really obfuscated code that shows how cool you are"


# map/reduce one liner

print( functools.reduce(lambda x, y: x+y, map(lambda x:len(x), [ [1,2], [1,4,9], [4,4,4,4] ])) )
# the map-part gives [2,3,4] and eventually this prints "9"

# in a full-blown map/reduce framework, the map-part is being parallellized.
# as a result there's intermediate results (here e.g. 2, 3 and 4 - the length of the three arrays).
# a map/reduce framework will do the work of maintaining those intermediate results.
# also, partitioning of the data to be mapped and 
# a user of a map/reduce framework typically provides the map and the reduce function.


# iterate over lst, apply lamda to each single element, create new list from lamda retval
print(map(lambda x: x*2, lst))	#[2, 4, 6, 8, 10, 12]
# guido says: map(F, S) becomes [F(x) for x in S]
# so, instead of map, using list comprehension is more pythonesque

# iterate over lst, apply lamda to each single element, create new list where lamda evals to true
print(filter(lambda x: x%2!=0, lst))	#[1, 3, 5]
# guido says: filter(P, S) is almost always written clearer as [x for x in S if P(x)]
# so, instead of filter, better use list comprehension with a conditional expression

# filter a map
for a in filter( lambda e: e[0]=="Beer", aDictionary.items()):
	print(a[1], type(a))	# 'Bofferding' <class 'tuple'>


# ifilter/imap/izip etc


# slices

name = "Robert"
print(name[3:4] + "=" + name[-3])	#e=e
print(name[-3:])					#ert
print(name[:-3] + "=" + name[:3])	#Rob=Rob



# chained comparisons

print(10 <= 50 < 100 > 5)


# positional args vs. keyword args
# *args **kwds


# type built in

x = type([])
print(x)
print(type(x))	#'type'. so type is also a type
print(type(()))	#tuple
print(type({})) #dict
print(type([]))	#list


# ordererd / unordered collections


# name mangling: "__" prefix makes python interpreter rename the attribute

class NameMangle(object):
	__secret=1
nameMangeExample=NameMangle()
#print(nameMangeExample.__secret)	# AttributeError: 'NameMangle' object has no attribute '__secret'


# descriptor protocol

# A descriptor defines (lets you override) the default behavior when an attribute of an object is looked up.

# __get__(self, instance, owner)
# __set__(self, instance, value)
# __delete__(self, instance)
# If any of those methods are defined for an object, it is said to be a descriptor.

# properties (provide a built-in descriptor type that knows how to link an attribue to *a set of methods*)

class Properties(object):
	def __init__(self):		#constructor
		self._my_secret = 1111
	def _iGet(self):
		return self._my_secret
	def _iSet(self, value):
		self._my_secret = value
	def _iDelete(self):
		print("nah")
	myThing = property(_iGet, _iSet, _iDelete, "some docstring")
properties = Properties()
print(properties.myThing)	# 1111
properties.myThing = 2222
print(properties.myThing)   # 2222
del properties.myThing	# nah
#help(properties)  makes shell defined reader show

# property shortcut

class Props(object):
	_x = 0
	@property
	def x(self):
		return self._x
	@x.setter
	def x(self, x):
		self._x = x
props = Props()
print(props.x)	#0

# named tuples (attention! they're immutable)

from collections import namedtuple
Person = namedtuple("Person", "name age gender")
print('Type of Person:', type(Person))
he = Person(name="Bob", age=30, gender="male")
she = Person("Drea", 28, "female")
print("her name is {0}".format(she.name))

# use named tuples to clarify return values (pendant to keyword args)!
print(he, she)
# Person(name='Bob', age=30, gender='male')
# Person(name='Drea', age=28, gender='female')

# named and optional function args

def someArgs(first, second=10, third=1):
	print(third)

someArgs(2) # 1
someArgs(1,10,9) # 9
someArgs(1, third=3) # 3


# varargs (unpacking args with * and **)

def varargF(*args):
	for arg in args:
		print(arg)

varargF(1,"two")	# 1 two


def namedVarargF(**args):
	for key in args:
		print(key)
		print(args[key])

namedVarargF(argone=1, another="two")	# prints "another two argone 1"



# old style classes vs. new style classes
#
# <= python 2.1 has only old style classes
# in between it's "class X()" for old style, "class X(object)" for new style
# python3 has only new style classes (no matter if you subclass from object or not; although you should do that.)
#
# python3:
# old style: type(X) is always <type 'instance'>, X.__class__ designates the class (type is classobj)
# new style: type(X) == X.__class__
#
# new style classes:
# - unify the concepts of class and type
# - provide a unified object model with a full meta-model
# - bring the ability, to change classes and objects definitions at run time via __new__ and __metaclass__
# - introduce super(), which doesn't work when old-style is involved


# meta programming


# __new__ vs __init__

# https://www.python.org/download/releases/2.3/mro/

# diamond inheritance and super != parent

# method resolution order (C3 algo)



# __call__ able objects

class aCallable:
	def __call__(self):
		print("aCallable.__call__()")

aCallableObject = aCallable()
aCallableObject()	# aCallable.__call__()


# function decorator
# modifies functions by passing them as argument to another function

class aDecorator:
	def __init__(self, f):
		# do something before and/or after f()
		f()

@aDecorator		# "bla"
def someDecoratedFunction():
	print("bla")


# class decorator



# decorators can be used to seperate administrative logic from business logic.
# e.g.: looking up an url (business log.) and memoizing/caching it with a dict (administrative logic).

# instantiating descriptors and using class decorators as an alternate to mixins


# closure

def aClosure(msg):
	def anInnerFct():
		print(msg)		#inner fct has access to vars scoped in the outer fct
	return anInnerFct

printer = aClosure("glorb")
printer()


# generators and yield

def yielding():		# the first call exits at the first yield (9). the next call continues from there - and so on.
	print("this prints only the 1st call")
	yield 9
	yield 31
	yield 42
	yield "hello"

yielding()				# doesn't do anything because it's not a funtion
print(type(yielding()))	# <class 'generator'>

y = yielding()
print(y.__next__(), y.__next__())	# 9 31
print(next(y), next(y))				# 42 hello
#print(y.__next__()) 	this would error, because there's only 4 values generated
#generators can only be iterated over one time

print(yielding().__next__(), yielding().__next__())		#prints out:
#this prints only the 1st call
#this prints only the 1st call
#9 9

# generator expressions

def double(x):
	return x*2

genexp = (double(i) for i in range( 3 ))	 # writing "i*2" here instad of "double(i)" is equivalent
for b in genexp:
	print(b)	# calls next implicitly; prints 0 2 4

# Use generator expressions where the range is large/infinite and only one iteration suffices.
# Use list comprehensions when the result needs to be iterated over multiple times. maybe it's also faster.


# coroutines

# they're different from subroutines (ordinary fct. calls), in that there is no 
# coordinating instance (a superfunction calling many subroutines).
# evaluation is lazy - similar to generators, they contain a loop and every single iteration is triggered from the outside.
# coroutines are composed together to form a pipeline.

def coroutineMatch(pattern):	# a consumer
	try:
		while True:
			s = (yield)
			if pattern in s:
				print(s)
	except GeneratorExit:
		print("coroutineMatch closing")

matcher = coroutineMatch("a")
matcher.__next__()		# let execution reach (yield). quasi inits the coroutine.
matcher.send("abc")		# "abc"
matcher.send("def")		# no output
matcher.close()			# "coroutineMatch closing"

# compose coroutines

def coroutineRead(text, nextCoroutine):	# a producer
	nextCoroutine.__next__()
	for line in text.split():
		nextCoroutine.send(line)
	nextCoroutine.close()

# give the consumer to the producer
reader = coroutineRead("a b c aa b c dea", coroutineMatch("a"))	# "a" "aa" "dea"

# producer: has a send() call only.
# filter: has both, (yield) and a send() call. can delete/modify data that's passing through.
# consumer: has a (yield) call only.


# grouping
# create a dict from a list, where the key is what's being grouped by and the value is a list of elements from the source.

toBeProcessed = ["Hans", "Liz", "Rob", "Frankly", "Bubbele", "Hans"]
grouped = {}
for el in toBeProcessed:
	key = len(el)
	if(key in grouped):			# can of course be simplified, but readability counts
		grouped[key].append(el)
	else:
		grouped[key] = []
		grouped[key].append(el)
print(grouped)

# grouping II

grouped = defaultdict(list)
for el in toBeProcessed:
	key = len(el)
	grouped[key].append(el)	# if its not there, create&return an empty list
print(grouped)
# if grouped were a normal dict, this is equivalent:
# grouped.setdefault(key, []).append(el)

# iterator protocol

# itertools groupby

# counting is similar to grouping - instead of append, a counter is increased

# counting I

count = {}
for el in toBeProcessed:
	count[el] = count.get(el,0) + 1
print(count)

# counting II

count = defaultdict(int)	# "int" evaluates to 0
for el in toBeProcessed:
	count[el] += 1
print(count)

while grouped:
	key, value = grouped.popitem()	# popitem is atomic (threadsafe)
	print(key, value)
print(grouped)	#empty

# linking dicts

# I: using dict.copy(first) and dict.update(second)

# II

first =  {"key1":"val1", "key2":"val2"}
second = {"key1":"bla", "key3":"val3"}
# print(ChainMap(first,second)) # python > 3.3


# keyword args > positional args, use them whenever you can!

def someFunction(arg1, arg2, arg3):
	print(arg2)
someFunction(arg3="a", arg1=False, arg2="cool")

# sequence unpacking

p = "A", "Hello", 0x10, 4.5
a, b, c, d = p 		# forget about []

# update multiple vars at once
# no dangerous out-of-order updates

a, b, c = 3, "hello", 4.3

# concatenate strings
print("A" + "B") 	 # is slow.
print("A".join("B")) # is fast. (python > 3.2)


# doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one)
# don't do:
# del l[0]
# l.pop(0)
# l.insert(0, "bla")
#
# instead use the far more efficient:
import collections
deq = collections.deque([2, "hi", 5, "bueno"])
del deq[0]
deq.popleft()
deq.appendleft("bla")

# c struct packing
# this creates a requested c datatype
from struct import pack, unpack
data = pack('IIf', 2, 4, 20.3)
a,b,c = unpack('IIf', data)
print(a, b, c)

# itertools combi/permu


# metaprogramming, metaclasses and type 


# classes, scope, constructor, polymorphism, inheritance


# large scale structuring: namespaces, packages, pip, virtual environments 
# TODO: explain that very concise


# threading, GIL and multiprocessing

# alternative to visitor pattern of OO-strong langs, with python you can
# - pull out loop body as a function (trivial)
# - pull out the loop iteration logic with generators
# - pull out setup and teardown with context managers


# context managers

class SomeContexto(object):
	someAttrib = 1

	def __init__(self):
		print("is called once, when obj is initialized")
		pass

	def __enter__(self):	# called each time, when entering context with "with"
		self.anotherAttrib = 2
		print("entering da zone")
		return self 	# don't forget to do this! can't be done in __init__

	def __exit__(self, exception_type, exception_value, exception_traceback):
		print("leaving da zone")

someContexto = SomeContexto()

with someContexto as contexto:
	print("in da zone!", contexto.someAttrib, contexto.anotherAttrib)

with someContexto as contexto:
	print("in da zone again, no __init__ this time!")


# python versions and ecosystem/packagemanager

# import looks:
# 1st) in the same directory than the file that does "import ..."
# 2nd) in an evironment variable named "PYTHONPATH" if it exists
# 3rd) in the "installation-dependent default"

# finding out "installation-dependent default":
#import os, inspect
#print(inspect.getfile(os))  # e.g. /usr/lib/python3.4/

# libs and frameworks exploiting lang' features
# http://python-3-patterns-idioms-test.readthedocs.org/en/latest/
# webtamplating https://wiki.python.org/moin/Templating
