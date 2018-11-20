class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, first_person, second_person):
        print 'Hey %s how are you, I am %s!, meet my friend %s' % (first_person.name, self.name, second_person.name )
        print 'Nice meeting you %s' % (first_person.name)
    




# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', 
Sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
print Sonny.name
# store it in the variable sonny.
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456',
jordan = Person('Jordan', 'jordan@aol.com','495-586-3456')
print jordan.name, jordan.email, jordan.phone
#  store it in the variable 'jordan'.
# Instantiate another person with the name of 'Frank', email of 'frank@aol.com', and phone of '495-586-9999',
Frank = Person('Frank', 'frank@aol.com', '495-586-9999')
Ron = Person('Ron', 'Ron@aol.com', '495-586-9449')
print Frank.name, Ron.name
# Have sonny greet jordan using the greet method.
Sonny.greet(jordan, Frank)
# Have jordan greet sonny using the greet method.
# Write a print statement to print the contact info (email and phone) of Sonny.
# Write another print statement to print the contact info of Jordan.
jordan.greet(Sonny, Frank)