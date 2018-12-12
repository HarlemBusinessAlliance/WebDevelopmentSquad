'''
def everyoneVote():
	# Let's create a file 
	thoughts = open("reasons.txt", "r")
	txtHolder = thoughts.read()
	print("First section ", txtHolder)
	thoughts.close()

	# Let's write some stuff into it
	thoughts = open("reasons.txt", "w+")	
	thoughts.write("Add two paragraphs that you want to, supporting voting. \r\rYou can break lines using the backslash n and make paragraphs using backslash r.")
	thoughts.close()

	# Now let's add more stuff into it
	thoughts = open("reasons.txt", "r+")
	txtHolder = thoughts.readlines()
	print("Third section ", txtHolder)
	# ALWAYS CLOSE the file once you're done messing with it
	thoughts.close()

everyoneVote()
'''

'''
import json

def participants():
	# Let's open the file 
	peopleList = open("participants.txt", "r")
	theContents = json.loads(peopleList.read())
	print("Say hello to the next pitchers ", theContents)

	# ALWAYS CLOSE the file once you're done messing with it
	peopleList.close()

participants()
'''

'''
import json

# a Python object (dict):
x = {
	"name": "John",
	"age": 30,
	"city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
'''


'''
with open('meke.txt', "w+") as teacher:
	data = "I am done teaching at the end of January"
	teacher.write(data)
'''

'''
import json
import requests

with open('stats.txt', 'r+') as info:

	# info.write('{"one":1, "two":2}')
	whatIsIt = info.readlines()
	# whatIsIt = json.dumps(whatIsIt)
	print ("The contents: ", whatIsIt)  

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
'''

'''
import json

print(json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':')))
# Result: '[1,2,3,{"4":5,"6":7}]'

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
# Result: {"a": 0, "b": 0, "c": 0}

print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4, separators=(',', ': ')))

# Result: 
# {
#    "4": 5,
#    "6": 7
# }
'''