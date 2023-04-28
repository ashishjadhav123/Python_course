class Dog():

    def __init__(self, my_breed):
        self.breed = my_breed


my_dog = Dog(my_breed='Lab')

print('My Dog')
print(my_dog.breed)

print('\n--------------------------------\n')

print('My Cat')
class Cat():

    def __init__(self,breed, name):
        self.breed = breed
        self.name = name

    def it_name(self):
        print('Her name is {}.'.format(self.name))


my_cat = Cat(breed='India', name='Rani')

print(my_cat.breed)
print(my_cat.name)
print(my_cat.it_name())
