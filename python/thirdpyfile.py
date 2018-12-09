'''
def everyoneVote():
	# Let's create a file 
	thoughts = open("reasons.txt", "w+")
	print(thoughts.read())

	# Let's write some stuff into it
	thoughts.write("Add two paragraphs that you want to, supporting voting. \r\rYou can break lines using the backslash n and make paragraphs using backslash r.")


	# Now let's add more stuff into it
	thoughts = open("reasons.txt", "a")
	thoughts.write("\r\rThe end!\nMeke Brown")

	# ALWAYS CLOSE the file once you're done messing with it
	thoughts.close()

everyoneVote()
'''

'''
def participants():
	# Let's open the file 
	peopleList = open("participants.txt", "r")
	theContents = peopleList.read()
	print("Hello?", theContents)

	# ALWAYS CLOSE the file once you're done messing with it
	peopleList.close()

participants()
'''

'''
with open('meke.txt', "w+") as teacher:
	data = "I am done teaching at the end of January"
	teacher.write(data)

print (data)
'''

'''
import json

with open('stats.txt') as info:
	uhhuh = json.dumps(info.read())

print (uhhuh)  
'''
