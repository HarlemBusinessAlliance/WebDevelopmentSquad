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
import HTMLParser
#or
#from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def __init__(self, name):
    	self._name = name

	def handle_starttag(self, tag, attrs):
		print ("Encountered a start tag:", tag)

	def handle_endtag(self, tag):   
		print ("Encountered an end tag :", tag)

	def handle_data(self, data):
		print ("Encountered some data  :", data)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
'<body><h1>Parse me!</h1></body></html>')
'''