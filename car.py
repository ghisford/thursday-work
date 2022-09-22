# create a class called Vehicle. The class should have the following attributes: make, model,
#  and year. The class should have the following methods: start, stop, and drive. The start 
# method should print out the make, model, and year of the vehicle and the word "is starting".
#  The stop method should print out the make, model, and year of the vehicle and the word "is
#  stopping". The drive method should print out the make, model, and year of the vehicle and 
# the word "is driving". Create a subclass of Vehicle called Car. The Car class should have 
# the following attributes: make, model, year, and color. The Car class should have the 
# following methods: start, stop, drive, and park. The park method should print out the make, 
# model, year, and color of the car and the word "is parking". Create an instance of the Car 
# class and call all the methods.

from operator import mod


class Vehicle:
    def __init__(self,make,model,year):
        self.make = make 
        self.model  = model 
        self.year = year

    def start(self):
        print(f'{self.make} {self.model} {self.year} is starting ')

    def stop(self):
        print(f'{self.make} {self.model} {self.year} is stopping ')

    def drive(self):
        print(f'{self.make} {self.model} {self.year} is driving ')



class Car(Vehicle) :
    def __init__(self,make,model,year,color) :
        super().__init__(make,model,year)
        self.color = color
    def park(self):
        print(f'{self.make} {self.model} {self.year} {self.color} is parking ')



tesla =  Car('tesla','model_s','2010','black')

tesla.start()
tesla.drive()
tesla.park()
tesla.stop()