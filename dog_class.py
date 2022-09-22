
# create Animal class and Dog class. Make the Dog class inherit from the Animal class. 
# Add a bark method to the Dog class. Create an instance of the Dog class and call the 
# bark method.


class Animal:
    
        type = 'domestic'

class Dog(Animal):
    def __init__(self,name) :
        self.name = name

    def bark(self):
        print(f'{self.name} is a {self.type} animal and he goes WOOF WOOF')


rockie = Dog('rockie')
rockie.bark()
