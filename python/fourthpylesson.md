## Review ALL previous Python lessons on your own outside of class

The Date and Time classes

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
## File navigation

---
References
https://www.udacity.com/course/machine-learning-for-trading--ud501

https://www.geeksforgeeks.org/python-programming-language/

https://www.digitalocean.com/community/tutorial_series/how-to-code-in-python-3