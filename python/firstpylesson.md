Installing Python on our laptops

Open up the terminal and type python. What do you see?
Open up the terminal and type python3. What do you see?
If neither command returns a version of the Python language installed on your computer [download the latest version](https://www.python.org/downloads/)
---
First Hello World Python program in the command prompt:

- Type python
- Write print("Hello World!")
- When the class is done, altogether, give yourselves a hand
- Type Ctrl-D or exit() to exit the terminal

Note: Type python --help for a summary of the main Python commands
---
Second program in the command prompt:

def factorial(n):
	if n == 0:
     	return 1
    else:
        return n * factorial(n-1)

factorial(n-1)
---
Let's use the [Visual Studio Code IDE for our Python development](https://code.visualstudio.com/Download)  

We're now downloading and opening firstpyfile.py in the Code IDE and talk about the similarities and differences of this interpretation method and the program interpreted from the command line.
---
CBS Story Break
Python was made in the early 90's by [Guido van Rossum](https://gvanrossum.github.io//), the ["Benevolent Dictator for Life"](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life) until this past July. He now resides in CA and works for Dropbox.
--- 
Python data types: Numbers, boolean, strings, lists, dictionaries
---
We're going to use a nifty module called *Turtle*. All we have to do is before our Python program's code, we type import turtle. And we can then use all of that module's capabilities. It's similar in nature to the HTML5 canvas element, a drawing board for visuals. This tool and more is in the language itself.

The "turtle" is the arrow that we will move around as we wish. Let's do some now.

- Type python
- type import turtle
- Type Turtle.forward(0) to see the drawing board pop up!
- Type turtle.forward(25)
- Type turtle.forward(5)
- Type turtle.forward() and in the parenthesis another number
- When the class is done, altogether, give yourselves a hand. You just wrote your first Turtle!

Mess around with more turtle moves by using the .backward(), .left(), and .right() functions. The forward and backward moves the turtle by pixels. The left and right turns the turtle by degrees.

Try the following program, now.

- Type import turtle
- Type turtle.shape("turtle") 
- Type turtle.forward(0) 
- Type turtle.left(45)
- Type turtle.forward(5)
- Type turtle.left(65)
- Type turtle.forward(15)

Want to start over? No problem. Just type turtle.reset()

This module or feature gives us a good way to practice using functions, navigating visual landscapes using pixels and degrees, and importing a helpful tool.

