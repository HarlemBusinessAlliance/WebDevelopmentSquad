def everyoneVote():
	# Let's create a file and write some stuff into it
	thoughts = open("reasons.txt", "w+")
	thoughts.write("Add two paragraphs that you want to, supporting voting. \r\rYou can break lines using the backslash n and make paragraphs using backslash r.")

	# Open the file and see what it has in it

	# Now let's add more stuff into it
	thoughts = open("reasons.txt", "a")
	thoughts.write("\r\rThe end!\nMeke Brown")

	# ALWAYS CLOSE the file once you're done messing with it
	thoughts.close()

everyoneVote()