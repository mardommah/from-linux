class Dog:
	species = "Canis familiaris"

	def __init__(self, name, age, breed):
		self.name = name
		self.age = age
		self.breed = breed

	def __str__(self):
		return f"{self.name} is {self.age} years old and the breed is {self.breed}"
	
	def speak(self, sound):
		return f"{self.name} says {sound}"

#inheritance goes here
#inheritance the breed as the child class and the Dog as the parent class

class JackRussellTerrier(Dog):
	#override speak method
	def speak(self, sound="Arf"):
		return f"{self.name} says {sound}"

class Dachshund(Dog):
	pass

class Bulldog(Dog):
	pass

#initiates the breed values
miles = JackRussellTerrier("Miles", 4)
miles.speak()
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


#intancenances value
miles = Dog("Miles", 4, "Jack Russel Terrier")
buddy = Dog("Buddy", 4, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")


print(miles)
