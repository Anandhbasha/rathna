class Engine:
    def start(self):
        print("Engine Starts")
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print("Car is Moving")

C = Car()
C.drive()


# Operator overloading

class Box:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def __mul__(self,other):
        peri = self.length+self.breadth
        return(self.length*self.breadth)
    
b1 =Box(2,5)
print(b1*None)