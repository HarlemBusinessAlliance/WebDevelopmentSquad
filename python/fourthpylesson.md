# Review ALL previous Python lessons on your own outside of class


## Python Input/Output

---
## A review of the Date and Time classes

We're going to import various methods and properties of the Date and Time classes from the datetime package (aka library, module, gem, or its equivalent depending on the language you are programming in)

	import datetime

	whatIsNow = datetime.datetime.now()

	currentCohortYear = whatIsNow.year
	prevCohortYear = currentCohortYear - 1

	currentCohort = {
		"student1" : currentCohortYear, 
		"student2" : currentCohortYear, 
		"student3" : prevCohortYear
	}
	print(currentCohort["student1"], currentCohort["student3"])

---
## Lambda functions

Lambda functions are just functions without a name. They can be very useful inside of functions, returning calculations for unknown inputs. Abstraction when done right can be useful, and lambdas can only work on one calculation.


---
References

https://docs.python.org/3/tutorial/controlflow.html#lambda-forms

https://www.w3schools.com/python/python_lambda.asp

https://www.udacity.com/course/machine-learning-for-trading--ud501

https://www.geeksforgeeks.org/python-programming-language/

https://www.digitalocean.com/community/tutorial_series/how-to-code-in-python-3