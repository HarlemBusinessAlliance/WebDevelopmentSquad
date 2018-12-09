# create a variable that holds 100k dice rolls in a two-dimensional array (100k rows, 2 columns) as part of the assignment

# Collecting Input
'''
x = raw_input("My name: ")

print ("Hello," )
print (x)


rolls = []
for n in range(100000):
	rolls.append([random.randint(1, 10), random.randint(1, 10)])
'''

# Rock Paper Scissors, but computer always picks Rock.
'''
print ( "1) Rock\n2) Scissors\n3) Paper ")

user_input = raw_input("Select a choice:")
#print ( type(user_input) )

if user_input == '1':
	print ( "Draw!")
elif user_input == "2":
	print ( "You lose!")
elif user_input == "3":
	print ( "You win!")
else:
	print ( "You didn't give a proper value")
'''

# ---------------------------- #
# Count the amount of files you have in a folder, in your program
'''
counter = 10
while counter >= 0:
	print ( counter )
	counter = counter - 1

# Or 
counter = 0
while True:
	print ( counter )
	counter = counter + 1
	if counter > 10:
		break
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

	start += 1 # start = strart + 1

print (start)
'''