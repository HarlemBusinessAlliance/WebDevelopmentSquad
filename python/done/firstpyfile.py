# A simple string output, similar to console.log("Hello World"); in JavaScript
# print("Hello World")

# ---

# A simple function, similar to function factorial(num); in JavaScript
# def factorial(n):
#     if n == 0:
#     	return 1
#     else:
#         return n * factorial(n-1)
 

# ... but a function call is the same
# print(factorial(5))

# In some ways JavaScript is stricter when it comes to the usage of keywords, in other ways Python is stricter because 
# of the use of indentation (each tab is around 4 spaces). There are many rules to remember so don't try to memorize them all. Just remember to find 
# references you can find helpful info from.

# ---

# Try this on for size:
# print("An example of a number is " + 321)
# What does this return? -> TypeError: cannot concatenate 'str' and 'int' objects
# Python is a strongly typed language! This WILL work by matching the types of the output data:
# print("An example of a number is " + str(321))

# ---

# Remember scope?! Remember ordering of program statements?
# dance = "Electric slide"

# def someFunkyFunction():
# 	dance = "Flossing"
# 	print(dance)

# someFunkyFunction()
# print(dance)
# print(someFunkyFunction) <- We can actually see how functions themselves are objects!

# ---

# Setting default values for your parameter(s)


# def downANum(y = 3):
# 	return y - 1

# downANum()
# downANum(55)

# ---

# checking_acct = [1000000, 1000000000, 1]
# for balances in checking_acct:
# 	print(balances)

# ---

# dareDevil = [("one", "Foggy"), ("two","Karen"), ("three","Fisk"), ("four","Matthew")]

# for num, characters in daredevil: 
#     print num, characters

# ---

# def sevenEightNine(num = 10):
# 	result = 1
# 	for x in range(num):
# 		result = result * num

# 	return result

# print(sevenEightNine())

# Note: If Code is acting wonky, just close out and restart the program

# ---

# stuff, do_stuff, do_other_stuff = "Sup?", "What's up?", "Hey"
# a, b, elemeno = 11, 22, None

# if a or b:
# 	print(do_stuff)


# if a and b:
# 	print(do_stuff)
# else:
# 	print(do_other_stuff)


# if not elemeno:
# 	print(stuff)
# elif a or b:
# 	print(do_stuff)
# else:
# 	print(do_other_stuff)

# ---

# i, aMiNaLs = -1, ["rats", "cats", "turtles", "dogs", "more dogs", "circus monkeys"]

# for pet in aMiNaLs:
# 	i += 1
# 	if pet == "dogs":
# 		print "It's a doggy dog world!", i
# 		break 


# for i in range(1,6):
# 	if i <= 4:
# 		continue                        
# 	print "Greater than 4:", i


# Note: The break and continue keywords are usable in while loops too! 
