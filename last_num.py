
# create a class of your choice. It should have at least 3 attributes and 3 methods 
# where one of the methods is a static method. Implement polymorphism, encapsulation, 
# and inheritance.


class Boy:
    __age = 0
    def __init__(self,sport,name,age) -> None:
        self.sport = sport
        self.name = name

# static method
    def shout():
        print('woooooo')

    def getSport(self):
        print(f'{self.name} plays {self.sport} ')

    def getAge(self):
        print(f'{self.name} is  {self.__age} years old ')

class Black_boy(Boy):
# polymorphism
    def getSport(self):
        print('we all hate sports')




bo= Boy('ball','tom',7)
Boy.shout()

bobo = Black_boy('volley','james',8)

bo.getSport()
bobo.getSport()









