# Example Python file with class

# THIS IS REALLY DIFFICULT


class vehicle():
    def __init__(self,bodystyle):
        self.bodystyle = bodystyle

    def drive(self,speed):
        self.mode = "driving"
        self.speed = speed

    def backward(self,reverse):
        self.mode = "reversing"
        self.reverse = reverse

class car(vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self,speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "at a speed of", self.speed)

class motorcycle(vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        
        self.doors = 0
        self.enginetype = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "at a speed of", self.speed)


class truck(vehicle):
    def __init__(self, enginetype, isparked):
        super().__init__("Truck")

        if (isparked):
            self.engine = "stop"
        else:
            self.engine = "move"

        self.enginetype = enginetype


class racecar(vehicle):
    def __init__(self, enginetype):
        super().__init__("Racecar")
        self.enginetype = enginetype
        
    def backward(self, reverse):
        super().backward(reverse)
        if (reverse):
            print("The racecar is reversing")
        else:
            print("You got the wrong code")
        
        
        

carbody = vehicle("BMW")
print(carbody.bodystyle)
car1 = car("gas")
car2 = car("oil")
mc1 = motorcycle("gas",True)
mc2 = motorcycle("oil", False)
car1.drive(49)
mc1.drive(90)
trk1 = truck("natural gas", True)
trk1 = truck("natural gas", False)

rac1 = racecar("natrualgas")
rac1.backward(False)

# print(car1.wheels)
# print(mc1.bodystyle)
# print(mc2.wheels)
# print(trk1.engine)

