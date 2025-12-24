class Vehicle:
    def acc(self):
        print("Vehicle moves")
class Bike(Vehicle):
    def acc(self):
        print("Bike moves")
class Car(Vehicle):
    # def acc(self):
    #     print("Car moves")
    pass

C = Car()
C.acc()