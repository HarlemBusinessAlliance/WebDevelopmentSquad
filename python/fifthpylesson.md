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

Exercise
# Ask User for Input
# User Gives Input

# If Input Is Bad, Tell User & Ask again
# Ask no more than 3 times!
# If user fails to give right password, tell user to stop & end program
actual_password = "cohort6"
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
Basics of a website framework:
- Modeling of each data entity or holder that the site will do stuff with 
- Views the user sees
- Controllers or computations holding all of the site functionality

Frameworks are libraries of reusable code: A bunch of pre-configured files, directories, images, configurations, you name it. 

The HTML that a framework comes with forms a template for your site building to be wrapped within. This gives it automatic structure within the browser: Everything needed and wanted is formed in the infrastructure for you to mod out as you please. The HTML files will hold placeholders where the data you want to output to the viewer will be seen.

Python itself can be used to make a template where you just plug in the info and voila, it's outputted!
'''
	template = "<html><body><h1>Hello %s!</h1></body></html>"
	print(template % "Reader")

	from string import Template
	template = Template("<html><body><h1>Hello ${name}</h1></body></html>")
	print(template.substitute(dict(name='Dinsdale')))
'''


Great Python web frameworks to connect your Python app to your HTML/CSS/JS web pages: 
- [Django](https://www.djangoproject.com/) Working with this one. Sites using Django are Disqus, Instagram, MacArthur Foundation, and Pinterest
- [Flask](http://flask.pocoo.org/)
- [Pyramid](https://pylonsproject.org/)
- [Bottle](https://bottlepy.org/docs/dev/)
- [Tornado](https://www.tornadoweb.org/en/stable/)
- [web2py](http://www.web2py.com/)


Django supports 4 databases: MySQL, PostgreSQL, SQLite, and Oracle. We'll be using MySQL.



---
References
https://www.python.org/

https://djangoforbeginners.com/

http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/

http://github.com/M0nica/flask_weather

http://learnyouahaskell.com/chapters