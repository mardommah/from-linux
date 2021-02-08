class Dog:
	#class attributes
	species = "Canis familiaris"

	#instance attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	#instance method
	#use f-strings format
	#replace description with __str__
	def __str__(self):
		return f"{self.name} is {self.age} years old"

	#another instance methods
	def speak(self, sound):
		return f"{self.name} says {sound}"	

dog1 = Dog("Coeg", 5)
dog2 = Dog("Mardoket", 10)
	
#print(dog1.name)
#print(dog1.description())
#print(dog1.speak("woof woof"))

print(dog1)
