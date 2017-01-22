#!node --es_staging --harmony --use_strict jsCheatsheet.js

// feature / compiler table:  https://kangax.github.io/compat-table/es6/


//////////////////////////////////////////////////////////////
// INTRO
//////////////////////////////////////////////////////////////

// jslint ("Use spaces, not tabs") vs jshint ("--show-non-errors")

// "environment" is a browser, a database, any js engine

// 5 primitive types that are not an object: number, string, boolean, null, undefined
// but: number, string, boolean have an "object representation" (wrapper)



//////////////////////////////////////////////////////////////
// SCOPE
//////////////////////////////////////////////////////////////

var aGlobal = "x";
function impliedGlobalF() {
	impliedGlobal = 0;	// not possible in strict mode
	var local;
}
//delete aGlobal;			// works, but only if "var" is omitted, which is only possible in non-strict mode
//delete impliedGlobal;	// works, but only in non-strict


// when it comes to scope, a js-person usually 
// strives for a metaphor called "hoisting":
// vars defined somewhere in a fct behave like they're defined at
// the beginning.
// vars in the same scope are considered declared,
// even when used before their definition.
function hoisting() {
	// uncommenting the next line is equivalent to leaving it commented
	//var someVar;	// equivalent to "var someVar=undefined;"
	console.log(someVar);	// "undefined"
	var someVar = 1;
	console.log(someVar);	// "1"
}
// js does 2 stages:
// stage 1: parsing and entering context. stage 2: runtime code exec. 

// best to always use the "single var pattern"
function singleVarPattern() {
	var a=1,	// put it on top of the function - C style, not at all C++ RAII like.
		b=2,
		c=3;
	// ... some code
};

console.log("this.aGlobal:", this.aGlobal);	// undefined. why?

function globalVar() {
	globallyScoped = "x";	// most likely accidentally. discouraged. not possible in strict mode.
	var locallyScoped = "y";
};


// eval() has access to outer scope
(function () {
	var local = 1;
	eval("local=3; console.log(local)");	// "3"
	console.log(local);	// "3"
}());
// Function() doesn't (it also evaluates string argument)
(function () {
	var local = 1;
	Function("console.log(typeof local);")();	// "undefined"; new is optional
}());

// iife (see below)


//////////////////////////////////////////////////////////////
// OBJECT
//////////////////////////////////////////////////////////////

// object types:
// host (defined, implemented and provided by environment)
// native (defined in user-land)

// activation object?

// in js - for better or worse - everything is always mutable.
// ("everything" = user-defined native objects and most props of built-in native objs)

// start with empty object...
var anEmptyObject = {};	// equivalent to "new Object()"
anEmptyObject.prop1 = "Bla";
anEmptyObject.prop2 = 41;
anEmptyObject.prop3 = function() {}

// ...or better, use object literal notation
var anObjectIsAnAssociativeArray = {
	aProperty : "aValue",
	aFunctionProperty : function () {}
};

anObjectIsAnAssociativeArray.addAnotherFunction = function () {}
delete anObjectIsAnAssociativeArray.addAnotherFunction;	// remove it again

// Object is a built-in. prototype is a member of object.
// built-in prototype can be "augmented".
// changes are immediate/live for all sub-objects.
if(typeof Object.prototype.someFunction === "undefined") {
	Object.prototype.someFunction = function () {};
}
// so now, "man" has someFunction() as well.

// object property enumeration
for (var i in man) {
	// only use what a "man" itself really has; omit super-object's properties.
	// actually, filter away "someFunction()".
	if(man.hasOwnProperty(i)) {
		// ...
	}
	if(Object.prototype.hasOwnProperty.call(man,i)) {	// alternative

	}
}

// alternative object property enumeration
console.dir({a:1, b:"bla"});


var anObjectLiteral = {
	prop1 : 1,
	prop2 : true,
	prop3 : function () {}
}

// {} (an object literal) is equivalent to "new Object()"

Number.prototype.addTo = function(value) {
	return this + value;
}
console.log((8).addTo(2))	// 10
//console.log(8.addTo(2))	// doesn't work, for js tokenizer, "." is a decimal pt.
console.log(8['addTo'](3));	// 11


// seal() = prevents adding and/or removing properties
// makes every property non-configurable, and they cannot be converted from data accessors to properties
// freeze() = seal() + prevents changing any existing properties
// Neither one affects children objects
// preventExtensions()

var someObjectWithSubobjects = { b: {c:4} , d: { e: {f:1}} };
//var shallowCopyByRef = Object.assign({}, someObjectWithSubobjects);
var deepCopyByVal = JSON.parse(JSON.stringify(someObjectWithSubobjects));
someObjectWithSubobjects.d.e.f = 2;
console.log("copy", deepCopyByVal.d.e);	// {f: 1}


var o1 = { a: 1, b: 1, c: 1 };
var o2 = { b: 2, c: 2 };
var o3 = { c: 3 };
//var obj = Object.assign({}, o1, o2, o3);
//console.log(obj); // { a: 1, b: 2, c: 3 }


// object attributes (changeable, deletable, enumerable with for-in)
// prototype chain


//////////////////////////////////////////////////////////////
// FUNCTION CALL
//////////////////////////////////////////////////////////////

// it's not by-ref, and not by-val, it's "call by object (sharing)" (barbara liskov):
// the value of the argument is not the direct alias, but the copy of the address.
// how does that behave?
// CBO lets you change existing propertis, but not add/remove new ones (with by ref you could).

var callByObject = { x: 10, y: 20};

function addNewProps(obj) {
	obj = {z: 1, q: 2};
	delete obj.x;
	return callByObject;
};

function change(obj) {
	obj.x = 100
	obj.y = 200
	return callByObject;
};

console.log("addNewProps", addNewProps(callByObject));	// { x: 10, y: 20 } doesn't work that way
console.log("change", change(callByObject));	// { x: 100, y: 200 }


//////////////////////////////////////////////////////////////
// CONSTRUCTORS
//////////////////////////////////////////////////////////////

// constructors always return an object -
// either the "this"-object, when return is omitted or any object you specify.
var Person = function(name) {
	// this is magically there. it's not empty really.
	// it's like: var this = Object.create(Person.prototype)
	this.name = name;
	return new Number(2);
};
var roger = new Person("roger");
console.log(roger.name);	// "undefined"
console.log(roger); "12"

// doesn't work because "Cannot set property 'name' of undefined".
// means: js wants to set name on global object and forgotNew is undefined.
//var forgotNew = Person("bla");	


function Book(name, year) { 
  if (!(this instanceof Book)) { 	// amend forgotten new
    return new Book(name, year);
  }
  this.name = name;
  this.year = year;
}


// constructors: Object(), Array(), Function()



//////////////////////////////////////////////////////////////
// ARRAY
//////////////////////////////////////////////////////////////

// data can be stored at non-contiguous locations in the array,
// JavaScript arrays are not guaranteed to be dense
var fruits = [];
fruits[5] = 'mango';
console.log(fruits[0], fruits.length);	// "undefined 6"
fruits.length = 5;	// deletes elements
console.log(fruits[5]);	// "undefined"
// RegExp.exec, String.match, and String.replace, all return Arrays.

// arrays can do lots of useful things:
// push/pop, shift/unshift, sort, fill, includes, lastIndexOf, concat, Array.isArray
// toSource() returns a literal
// every() ("for all" predicate) and some() ("exists" predicate)
// forEach()
// no "zip" though...

//console.log(Array(3), " is not ", Array.of(3));	// "[,,] is not [3,3,3]"

// copyWithin works like C and C++'s memmove, and is a high-performance method to shift the data of an Array
//console.log(["alpha", "bravo", "charlie", "delta"].copyWithin(2, 0)); // results in ["alpha", "bravo", "alpha", "bravo"]
// it behaves python-slice-esque:
//console.log([1, 2, 3, 4, 5].copyWithin(-2)); // [1, 2, 3, 1, 2]

// slice returns a shallow copy of a portion of an array into a new array object
var myHonda = { color: 'red', wheels: 4, engine: { cylinders: 4, size: 2.2 } };
var myCar = [myHonda, 2, 'cherry condition', 'purchased 1997'];
var newCar = myCar.slice(0, 3);
newCar.color = "green";
console.log(newCar);	// "green", so everything happens byRef / shallow

// splice(start, deleteCount, item1, item2, ...) removes and adds elements IN PLACE
var spliceExample = ["a", "b", "c", "d"];
console.log(spliceExample.splice(2,1,"X"));	// what's deleted ("c")
console.log(spliceExample);	// "a b X d"

// join
console.log(["E", "W", "F"].join(" and ")); // a string "E and W and F"

// map/filter/lfold

console.log([1,2,3,4,5].map(e=>e*2));	// 2, 4, 6, 8, 10
console.log([1,2,3,4,5].filter(e=>e%2===0));	// 2, 4
console.log([1,2,3,4,5].reduce((e1,e2)=>e1+e2));	// 15

// convert array-like object to array
// creates a new Array instance from string, set, map or array-like object.
//console.log(Array.from("abc")); // ['a', 'b', 'c']
// Array.from() is equivalent to:
console.log(Array.prototype.slice.call("abc"));	// ['a', 'b', 'c']


// iterable concept since es6
/*
var arr = ["a", "b", "c"];
var iterator = arr.keys();
console.log(iterator.next()); // { value: 0, done: false }
console.log(iterator.next()); // { value: 1, done: false }
console.log(iterator.next()); // { value: 2, done: false }
console.log(iterator.next()); // { value: undefined, done: true }
*/


// typed arrays

// allow handling of raw, untyped data as js array by splitting concerns into
// buffer (inaccessible for reading)
// and view (giving buffer a js format)

/* consider this c-struct
struct someStruct {
  unsigned long A;	// 4 bytes
  char B[16];	// 16 bytes
  float C;	// 4 bytes
};
*/

// 24 bytes of raw untyped data. filled by some source.
var buffer = new ArrayBuffer(24);	
var viewA = new Uint32Array(buffer, 0, 1);	// use 3 views to access raw data
var viewB = new Uint8Array(buffer, 4, 16);
var viewC = new Float32Array(buffer, 20, 1);
console.log(Array.isArray(viewA));  // false
console.log(viewA[0]);
// create a regular js array from a view:
//console.log(Array.isArray(Array.from(viewB)));	// true


// "array-like object"
// js objects are associative arrays.
// if key is a String, it's an "Object".
// if key is a Number (and it has some array specific methods), it's an "Array".
console.log( Array.isArray(["A", "B", "C"]) );	// true
var anArrayLikeObject = {0:"A", 1:"B", 2:"C", length:3};
console.log( Array.isArray(anArrayLikeObject) );	// false
console.log( typeof(Object.keys(anArrayLikeObject)[0]) );	// string


// creates property
var nonIntegerKey = [];
nonIntegerKey[3.4] = "Oranges";
console.log(nonIntegerKey.length);                // 0
console.log(nonIntegerKey.hasOwnProperty(3.4));   // true



//////////////////////////////////////////////////////////////
// FUNCTIONS
//////////////////////////////////////////////////////////////

//Function.prototype.apply()
//Function.prototype.bind()
//Function.prototype.call()



//////////////////////////////////////////////////////////////
// DOs AND DONTs / BEST PRACTICES
//////////////////////////////////////////////////////////////


// opening curly brace - better in same line, because of js's "semicolon insertion mechanism"
function semicolonFail() {
	return	{
		some: "thing"
	};
};
console.log("eigentlich we want true. but:", semicolonFail() === Object);	// false

var dummy = "use strict;";	// ignored by emascript3, use strict lang subset in es5; once per scope

// better always avoid implicit and opaque typecasting by using
// identity operators: === and !===
// instead of equality operators == and !=

console.log(parseInt("10", 16));	// always specify base with parseint

// for loops are for arrays.
// cache array length, because not doing so can get expensive.
for(var i=0, max=[1, 2, 4].length; i<max; i++) {
}

// for-in is for enumeration of objects.
var man = {
	hands: 2,
	legs: 2,
	head: 1
};



//////////////////////////////////////////////////////////////
// ECMASCRIPT 6 FEATURES
//////////////////////////////////////////////////////////////

// Constants
const someConst = 10;

// in ES5 only through the help of object properties
// and only in global context and not in a block scope
Object.defineProperty(
	global,
	"someConst2", 
	{value: 3.141593, 
	enumerable: true, 
	writable: false, 
	configurable: false });

//Scoping

{
	let onlyHere = 1;
	console.log(onlyHere);
}
// console.log(onlyHere);  // doesn't work

// pre ES6:
// block-scope emulating function with
// iife idiom ("immediately invoked function expression")
(function() {
    var onlyHere = 10;
    console.log(onlyHere);
})();

(function() {}());	// alternative

// console.log(onlyHere);  // doesn't work


//Arrow Functions (aka nice anonymous function syntax, like in scala or c#)

console.log( [1,2,3,4].map(v => v * 2) );

// Object context / Lexical this

//var self = this;
//this.nums.forEach(function(v) {console.log();});
//this.nums.forEach((v) => { if (v % 5 === 0) this.fives.push(v) })
//this.nums.forEach(function (v) { if (v % 5 === 0) this.fives.push(v); }.bind(this));

function defaultArgsOld(x, y) { if (y === undefined) y = 7;  };
//function defaultArgs(x, y=7) {  };


function f (x, y) {
    var a = Array.prototype.slice.call(arguments, 2);
    return (x + y) * a.length;
};
f(1, 2, "hello", true, 7) === 9;


/*
Extended Parameter Handling

    Default Parameter Values
    Rest Parameter
    Spread Operator

Template Literals

    String Interpolation
    Custom Interpolation
    Raw String Access

Extended Literals

    Binary & Octal Literal
    Unicode String & RegExp Literal

Enhanced Regular Expression

    Regular Expression Sticky Matching

Enhanced Object Properties

    Property Shorthand
    Computed Property Names
    Method Properties

Destructuring Assignment

    Array Matching
    Object Matching, Shorthand Notation
    Object Matching, Deep Matching
    Parameter Context Matching
    Fail-Soft Destructuring

Modules

    Value Export/Import
    Default & Wildcard

Classes

    Class Definition
    Class Inheritance
    Class Inheritance, From Expressions
    Base Class Access
    Static Members
    Getter/Setter

Symbol Type

    Symbol Type
    Global Symbols

Iterators

    Iterator & For-Of Operator

Generators

    Generator Function, Iterator Protocol
    Generator Function, Direct Use
    Generator Matching
    Generator Control-Flow
    Generator Methods

Map/Set & WeakMap/WeakSet

    Set Data-Structure
    Map Data-Structure
    Weak-Link Data-Structures

Typed Arrays

    Typed Arrays

New Built-In Methods

    Object Property Assignment
    Array Element Finding
    String Repeating
    String Searching
    Number Type Checking
    Number Safety Checking
    Number Comparison
    Number Truncation
    Number Sign Determination

Promises

    Promise Usage
    Promise Combination

Meta-Programming

    Proxying
    Reflection

Internationalization & Localization

    Collation
    Number Formatting
    Currency Formatting
    Date/Time Formatting
*/

