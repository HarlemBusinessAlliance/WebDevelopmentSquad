# create a variable that holds 100k dice rolls in a two-dimensional array (100k rows, 2 columns) as part of the assignment

# Collecting Input
'''
import random
x = input("My name: ")

rolls = []
for n in range(10):
	rolls.append([random.randint(1, 10), random.randint(1, 10)])

print("Hello,", x, ". You have the following rolls: ", rolls)
'''


# Rock Paper Scissors, but computer always picks Rock.
'''
print ( "1) Rock\n2) Scissors\n3) Paper ")

user_input = int(input("Select a choice:"))
print ( type(user_input) )

if user_input == 1:
	print ( "Draw!")
elif user_input == 2:
	print ( "You lose!")
elif user_input == 3:
	print ( "You win!")
else:
	print ( "You didn't give a proper value")
'''

# ---------------------------- #
# Count the amount of files you have in a folder, in your program

'''
import os, os.path

onlyfiles = next(os.walk("/"))[2] #dir is your directory path as string
print(len(onlyfiles))

print(len([name for name in os.listdir('.') if os.path.isfile(name)]))
'''

# ---------------------------- #
# play a fun FizzBuzz game where the user guesses how many FizzBuzz outputs there will be in n chances

# Looks at an Integer
# If the integer is divisible by 3, Print "Fizz"
# If the integer is divisible by 5, Print "Buzz"
# If the integer is divisible by both, Print "Fizz Buzz"

# Check the Fizz-Buzz for each value between initial ( start ) & 0 -- Count Up

'''
choice = int(input("Where do we begin: "))

start = 0
while start <= choice:
	if start%3 == 0 and start%5 == 0:
		print("Fizz Buzz")
	elif start%3 == 0:
		print("Fizz")
	elif start%5 == 0:
		print("Buzz")
	else:
		print ( start )
		pass

	start += 1 # start = start + 1

print (start)
'''

'''
def make_incrementor(n):
	return lambda x: x + n

f = make_incrementor(42)
print(f(0))

print(f(1))
'''