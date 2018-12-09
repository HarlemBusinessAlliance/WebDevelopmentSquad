class User: 
    pass 

user1 = User()
user1.first_name = 'Meke'
user1.last_name = 'Brown'

print(user1.last_name)


# ------------------ #
# {key:value}
sample = {'red':'dog','green':'fish','blue':53}
print (sample['red'] )
print ( sample['green'])
print ( sample['blue'])

print ( sample.keys() )
print ( sample.values() )


# ------------------- #
x = input("Test Blurb: ")
print ( x[3] )

test_input = input("test blurb!")


# ------------------- #
#def foo(sample):
#	print(sample)

#foo(93234234)

x = 4

class Car:
	def __init__(self,year,color):
		self.year = year
		self.color = color
		self.x, self.y = 0,0

	def stats(self):
		print("This car is from: ", self.year)
		print("This car's color is: ",self.color)
		print("The car is at this location: ",self.x,self.y)

	def drive(self):
		self.x = int(input("x: "))
		self.y = int(input("y: "))

car1 = Car(2015,"black")
car1.stats()

car1.drive()
car1.stats()