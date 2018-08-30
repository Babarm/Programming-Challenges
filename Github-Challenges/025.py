print('Question 25')
print('Level 1\n')
print('Define a class, which have a class parameter and a same instance parameter\n\n')

class Person:
	name = 'Person'

	def __init__(self, name = None):
		self.name = name
		return None

kevin = Person('Kevin Conte')

print('{0}: {1}'.format(Person.name, kevin.name))
