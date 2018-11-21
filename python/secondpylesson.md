Diving into the data types!

... but

rrr......ewind to us talking about operators. Check these out:
	|= 	means if the value on the left exists store THAT into the variable; if not store what's on the right; Performs bitwise OR and assigns value to the left operand.
	^= 	means the left value will be brought to the power of the thing on the right; Performs bitwise XOR and assigns value to the left operand.
	>> 	Shifts the bits of the first operand right by the specified number of bits.
	<< 	Shifts the bits of the first operand left by the specified number of bits.
	>>= means Performs bitwise right shift and assigns value to the left operand.
	<<= means Performs bitwise left shift and assigns value to the left operand.
	//= means Floor divides the variable by a value and assigns the result to that variable.
	&	AND	Sets each bit to 1 if both bits are 1
	| =	OR	Sets each bit to 1 if one of two bits is 1
	^ = XOR	Sets each bit to 1 if only one of two bits is 1
	~ =	NOT	Inverts all the bits
	<< = Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
	>> = Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

---
range(), __init__(), .update(), __iter__(), .remove(), __next__(), .add(), .pop(), .clear(), .dumps()

---
Up to now, we've been programming procedurally; Writing statements that work in the order that they are written, "following a procedural flow"

Python let's you do this AND also in with an OOP focus. 

Note: What's the difference between print() and return anyway?! Well, the print function sends out standard output and functions use return to give a value. Functions ALWAYS return a value, even if you don't explicitly create a return statement. 

---
Classes

Base class

Respect your SELF keyword

	What's cool about OOP is how an object can be used to refer to its instance of self; In JavaScript you may have seen the keyword this used. It plays the same role.

Methods and properties

Objectifying the classes - Copies of classes

Inheritance

Super Classes

Class variables

---
Objects

Initialization of an object 

Instance variables

---
Modules using import

A module is a library you can use great computations from. You can use your own created .py module or one already made; Just import it into the file you need elements from it in.
	
	import yourmoduleeesss.  # Leads to the file YOU make with stuff in it

	youNeedThisInfo = yourmoduleeesss.employer.name
	print(youNeedThisInfo)


	import platform

	x = platform.system()
	print(x)
	y = dir(platform)
	print(y)

Examples of modules: platform, os, datetime, json, timedelta

---
The Date and Time classes

	We're going to import various methods and properties of the Date and Time classes from their packages (aka libraries, modules, gems, or its equivalent depending on the language you are programming in)

	import datetime

	whatIsNow = datetime.datetime.Now()
	print(whatIsNow.year)	
	print(whatIsNow.strftime("%A"))			# Returns datetime info as a readable string, using one parameter. Cool huh?






