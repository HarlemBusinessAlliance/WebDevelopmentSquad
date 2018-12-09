## Storing data

Example

'''
class User: 
    pass 

user1 = user()
user1.first_name = 'Meke'
user1.last_name = 'Brown'

print(user1.last_name)
'''

# Ask User for Input
# User Gives Input

# If Input Is Bad, Tell User & Ask again
# Ask no more than 3 times!
# If user fails to give right password, tell user to stop & end program
actual_password = "Hello"
input_password = input("Put in password: ")

counter = 3
while counter >= 1:
	counter = counter - 1

	if actual_password == input_password:
		print ( "Thank you. This is correct!" )
		break
	else:
		print ( "Password Incorrect, Try again! ")
		input_password = input("Put in password: ")


---
## Project: User research survey

---
## Connection to HTML/CSS/JS

---
References
http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/

http://github.com/M0nica/flask_weather

http://learnyouahaskell.com/chapters