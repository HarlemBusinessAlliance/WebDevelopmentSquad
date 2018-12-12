# -*- coding: utf-8 -*-

""" int 			
			x = 666			
			y = 12345678987654321
			z = -y
"""

"""float			
			x = 3.1415927	
			y = 12E4 			# A scientific number
"""

"""long
			x = 229493995929919499969499299597993919979899929939797994929497999999991929969799096999929993934997979901899999288586868775848488322949399592991949996949929959799391997989992993979799492949799999999192996979909699992999
"""

"""complex			
			x = 1j 			# The j stands for an imaginary value
"""

"""boolean 
			x = True
			y = "True"

"""

"""str 			
			x = "Cohort"	
			y = "Complex type?"		
			z = y[10]
"""

"""lists
			x = ["Philomena", "Meke", "Moe"]
			y = len(x)			<- len() is Python’s .length
			z = "Meke" in x 	<- True or false?
"""

"""tuples
			x = ("SSD", "Non-SSD")	# Unchangeable!
			w = 0
			while w < len(x):
				print(type(x[w]))
				w += 1

			del x
"""

"""set
			x = {"Why", "are", 3.4, "sets", "unordered", "?", 275}
			y = {"sets", "don't", "have", "indices", 9012832914} 		# You can add/remove values, check if a value exists, find out the length of, and loop through sets
			z = frozenset(y)	# You can make a set Unchangeable
"""

"""dictionaries
			x = {"muse" : "The Purple One", "theme": "purple", "genre": "music"}
			y = x.get("muse")
			z = x["fan"] = "Meke"
"""

"""None
			x = None
"""




# Classes  
"""
class theDivision:
	def __init__(self, player, age, loc):
		self.player = player	# Doesn't have to use the word self
		self.age = age
		self.loc = loc

	def tagLine():
		print("My name is " + self.player + ", your God")


p1 = theDivision("The Dudette", 37, "NYC")		# An object made from the BASE CLASS theDivision

print(p1.player)
"""






# Try except finally error checking
"""
x = "Everything is now in the cloud, folks"

try:
	prin(x)
except:
	print("An exception occurred")







try:
	prnt(x)
except IndentationError:
	print("Watch your indents people!")	
except:
	print("Oopsy, did you spell something wrong?")
else:
	print("I don't know. I just don't know")






try:
	print("Hi " + 1 + 2)
except:
	print("Watch your data types people!")	
finally:
	print("Great effort either way!")
"""